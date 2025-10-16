
def main_program():
    import argparse
    from .my_module import do_something
    from .another_module import do_something_else

    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=float, help="This is better help")

    args = parser.parse_args()

    do_something(args.number)
    do_something_else(args.number)

