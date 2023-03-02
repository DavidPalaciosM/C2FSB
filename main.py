# coding: utf-8
__version__ = "1.0"
__author__ = "Cristobal Pais"

# Importations
#from tqdm import tqdm

# No Warnings
import warnings
warnings.filterwarnings("ignore")

# Inputs and environment generator
from Cell2Fire.ParseInputs import ParseInputs
from Cell2FireC import *
from Cell2Fire.Stats import *
from Cell2Fire.Heuristics import *

def main():
    # Parse inputs (args)
    args = ParseInputs()

    # C++ init and run
    env = Cell2FireC(args)
    
    # Postprocessing: Plots Stats
    if args.stats:
        print("------ Generating Statistics --------",flush=True)
        env.stats()
        
    if args.heuristic != -1:
        print("------ Generating outputs for heuristics --------",flush=True)
        env.heur() 

if __name__ == "__main__":
    main()    
