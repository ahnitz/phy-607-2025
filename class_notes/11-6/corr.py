import numpy as np
import matplotlib.pyplot as plt
import emcee.autocorr

# Generate a chain with a known correlation length as an example
# This works by adding a relative amont of noise between each sample.
def generate_simulated_chain(n_samples, phi):
    """  Generates an Autoregressive AR(1) chain.
    Theoretical autocorrelation length ~ (1 + phi) / (1 - phi).
    
    This is one of the simplest models where the autocorrelation time can be
    worked out analytically. 
    The model is described here (https://en.wikipedia.org/wiki/Autoregressive_model)
    """
    chain = np.zeros(n_samples)
    # Initialize with random noise scaled to stationary distribution
    chain[0] = np.random.randn() / np.sqrt(1 - phi**2)
    noise = np.random.randn(n_samples)
    for i in range(1, n_samples):
        chain[i] = phi * chain[i-1] + noise[i]
    return chain

def direct_autocorr(chain, max_lag=None):
    """ This directly calculates the autocorrelation time / length
    using numpy functions. Note there are some heuristic steps.
    """
    # We'll assume that the first half of the chain is "burn-in"
    chain = chain[len(chain)//2:]
    
    n = len(chain)
    if max_lag is None:
        max_lag = n // 10 # practical limit for estimation


    # Calculate the autocorrelation of the chain's single parameter value
    # as function of lag/shift/offset in the number of samples. 
    # If the function is correlated, small shifts will give a large correlation
    y = chain - np.mean(chain)
    # mode='full' gives 2*n-1 points. The second half (starting at n-1) is positive lags.
    c = np.correlate(y, y, mode='full')
    c = c[n-1 : n-1+max_lag] # Take positive lags up to max_lag
    rho = c / c[0] # Normalize so rho[0] is 1.0

    # To get the correlation time, we integrate over the autocorrelation
    # function. This gives us the effective decay rate of the correlation
    # or the number of samples between required before the value of the chain
    # has become independent.
    
    # In practice, summing the noisy tail can introduce a large variance
    # A simple heuristic method is to sum until the ACF first goes negative.
    negative_indices = np.where(rho < 0)[0]
    if len(negative_indices) > 0:
        cutoff = negative_indices[0]
    else:
        cutoff = len(rho)

    tau_estimate = 1.0 + 2.0 * np.sum(rho[1:cutoff])
    return tau_estimate, rho

N = 500000

# 1. Independent Chain (White Noise)
# Theoretical ACL should be 1.0
chain_indep = np.random.randn(N)

# 2. Correlated Chain (AR(1) process with phi=0.9)
# Theoretical ACL = (1 + 0.9) / (1 - 0.9) = 1.9 / 0.1 = 19.0
PHI = 0.9
THEORY_ACL = (1 + PHI) / (1 - PHI)
chain_corr = generate_simulated_chain(N, PHI)

print(f"Theoretical Correlated ACL: {THEORY_ACL:.2f}\n")


print("--- A) Library Implementation (emcee) ---")
# emcee's integrated_time is robust and uses automated windowing
#
# See https://emcee.readthedocs.io/en/stable/user/autocorr/#emcee.autocorr.integrated_time
tau_emcee_indep = emcee.autocorr.integrated_time(chain_indep, quiet=True)[0]
tau_emcee_corr = emcee.autocorr.integrated_time(chain_corr, quiet=True)[0]
print(f"Independent ACL: {tau_emcee_indep:.2f}")
print(f"Correlated ACL:  {tau_emcee_corr:.2f}")

print("\n--- B) Direct Implementation (numpy) ---")
# =========================================
# B) Direct Implementation
# =========================================
tau_direct_indep, _ = direct_autocorr(chain_indep)
tau_direct_corr, rho_corr = direct_autocorr(chain_corr)

print(f"Independent ACL: {tau_direct_indep:.2f}")
print(f"Correlated ACL:  {tau_direct_corr:.2f}")

# Optional: Visualizing the convergence for the correlated chain
# This shows why we don't just sum the whole thing (the tail is noisy)
# You can see how this changes if you modify the number of samples in the chain
# more samples will mean that larger lags will have a smaller 'noise', but
# eventually once it is decorrelated, it will just be mixing in random variance.
print("\n(Generating visualization of cumulative sum...)")
max_window = 500
rho_short = rho_corr[:max_window]
cumulative_tau = 1.0 + 2.0 * np.cumsum(rho_short[1:])

plt.figure(figsize=(8, 4))
plt.plot(np.arange(1, max_window), cumulative_tau, label="Cumulative Sum (Direct)")
plt.axhline(THEORY_ACL, color='r', linestyle='--', label=f"Theoretical ({THEORY_ACL:.1f})")
plt.axhline(tau_emcee_corr, color='g', linestyle=':', label=f"emcee estimate ({tau_emcee_corr:.1f})")
plt.xlabel("Window Size (Lags)")
plt.ylabel("Estimated ACL")
plt.title("Convergence of Autocorrelation Length")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
