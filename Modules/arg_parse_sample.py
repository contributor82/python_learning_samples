import argparse

class ArgParseSample: 
    ### Argument Parser Sample from Python doc ### 

    parser : argparse.ArgumentParser
    args: argparse.Namespace

    def __init__(self) -> None:
     self.parser = argparse.ArgumentParser() 
     
    def add_new_argument(self): 
        ### Function to add new argument to module ###

        self.parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
        self.args = self.parser.parse_args()
        if self.args.verbose: 
            print("verbosity turned on")

    def add_combine_positional_optional_argument(self): 
        ### Function to combine positional and optional argument ### 

        self.parser.add_argument("square", type=int, help="display square of a given number")
        # self.parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
        self.parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count")
        self.args = self.parser.parse_args()
        result = self.args.square ** 2
        if self.args.verbosity == 2: 
            print(f"the square of {self.args.square} equals {result}")
        elif self.args.verbosity == 1: 
            print(f"{self.args.square}^2 == {result}")        else: 
            print(result)

if __name__ == '__main__': 
    arg_parse_sample_instance = ArgParseSample()
    # arg_parse_sample_instance.add_new_argument() OR following line since combining arguments 
    arg_parse_sample_instance.add_combine_positional_optional_argument()
        
   # Use command line to get the output 
   # python arg_parse_sample.py -v 
   # python arg_parse_sample.py --help
   # python arg_parse_sample.py
   # python arg_parse_sample.py [number]
   # python arg_parse_sample.py [number]  -v
   # python arg_parse_sample.py [number]  --verbosity --verbosity
   # python arg_parse_sample.py [number] -h