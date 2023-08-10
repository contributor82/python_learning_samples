"""Module for argparse is for building command line interface"""

import argparse


class ArgParseSample:
    """ Class for Argument Parser Sample from Python doc """

    parser: argparse.ArgumentParser
    args: argparse.Namespace

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Calculate X to the power of Y when X and Y are provided.")

    def add_new_argument(self) -> None:
        """ Function to add new argument to module """
        try:
            self.parser.add_argument(
                "-v", "--verbose", help="increase output verbosity", action="store_true")
            self.args = self.parser.parse_args()
            if self.args.verbose:
                print("verbosity turned on")
        except ValueError as new_arg_value_error:
            print(new_arg_value_error)

    def add_positional_argument(self) -> None:
        """ Function to add positional argument to module """
        try:
            self.parser.add_argument(
                "echo", help="echo the string you use here.. ")
            self.args = self.parser.parse_args()
            print("echo")
        except ValueError as positional_arg_value_error:
            print(positional_arg_value_error)

    def add_optional_argument(self) -> None:
        """ Function to add new argument to module """
        try:
            self.parser.add_argument(
                "--verbosity", help="increase output verbosity")
            self.args = self.parser.parse_args()
            if self.args.verbose:
                print("verbosity turned on")
        except Exception as optional_arg_value_error:
            print(optional_arg_value_error)

    def add_combine_positional_optional_argument(self) -> None:
        """ Function to combine positional and optional argument """
        try:
            self.parser.add_argument(
                "square", type=int, help="display square of a given number")
            # self.parser.add_argument("-v", "--verbose",
            #                           help="increase output verbosity", action="store_true")
            self.parser.add_argument(
                "-v", "--verbosity", help="increase output verbosity", action="count")
            self.args = self.parser.parse_args()
            result = self.args.square ** 2
            if self.args.verbosity == 2:
                print(f"the square of {self.args.square} equals {result}")
            elif self.args.verbosity == 1:
                print(f"{self.args.square}^2 == {result}")
            else:
                print(result)
        except Exception as ex:
            print(ex)

    def add_adv_combine_positional_option_argument(self) -> None:
        """ Function to combine positional and optional argument """
        try:
            self.parser.add_argument("x", type=int, help="the base")
            self.parser.add_argument("y", type=int, help="the component")
            self.parser.add_argument(
                "-v", "--verbosity", action="count", default=0)

            self.args = self.parser.parse_args()
            result = self.args.x ** self.args.y
            if self.args.verbosity >= 2:
                print(f"Running '{__file__}'")
            elif self.args.verbosity >= 1:
                print(f"{self.args.x}^{self.args.y} == ", end="")
            print(result)
        except Exception as ex:
            print(ex)

    def add_mutually_exclusive_group_argument(self) -> None:
        """ Function to add arguments for mutually exclusive group """
        try:
            mutually_exclusive_group = self.parser.add_mutually_exclusive_group()
            mutually_exclusive_group.add_argument(
                "-v", "--verbose", help="increase output verbosity", action="count")
            mutually_exclusive_group.add_argument(
                "-q", "--quiet", help="quiet", action="count")

            self.parser.add_argument("x", type=int, help="the base")
            self.parser.add_argument("y", type=int, help="the component")

            self.args = self.parser.parse_args()
            result = self.args.x ** self.args.y

            if self.args.quiet:
                print(result)
            elif self.args.verbose:
                print(f"{self.args.x} to the power {self.args.y} equals {result}")
            else:
                print(f"{self.args.x}^{self.args.y} == {result}")
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    arg_parse_sample_instance = ArgParseSample()
    # arg_parse_sample_instance.add_new_argument()
    # OR following line for optional argument
    # arg_parse_sample_instance.add_optional_argument()
    # OR following line for positional argument
    # arg_parse_sample_instance.add_positional_argument()
    # OR following line since combining arguments
    # arg_parse_sample_instance.add_combine_positional_optional_argument()
    # OR following line with more advance argument combination
    # arg_parse_sample_instance.add_adv_combine_positional_option_argument()
    # OR following line with mutually exclusive group argument
    arg_parse_sample_instance.add_mutually_exclusive_group_argument()
   # Use command line to get the output
   # python arg_parse_sample.py --v
   # python arg_parse_sample.py --help
   # python arg_parse_sample.py --verbosity 1
   # python arg_parse_sample.py -h
   # python arg_parse_sample.py
   # python arg_parse_sample.py [number]
   # python arg_parse_sample.py [number]  --v
   # python arg_parse_sample.py [number]  --verbosity --verbosity
   # python arg_parse_sample.py [number] -h
   # python arg_parse_sample.py [number1] [number2] --v
   # python arg_parse_sample.py [number1] [number2] --v --v
   # python arg_parse_sample.py [number1] [number2] --q
   # python arg_parse_sample.py [number1] [number2] --vq
   # python arg_parse_sample.py [number1] [number2] --quiet
