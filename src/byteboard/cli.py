import argparse

from .inspect import inspect_function
from .loader import load_function
from .report import render


def main():
    parser = argparse.ArgumentParser(description="Inspect Python function bytecode.")
    parser.add_argument("path")
    parser.add_argument("function")
    args = parser.parse_args()
    print(render(inspect_function(load_function(args.path, args.function))))


if __name__ == "__main__":
    main()
