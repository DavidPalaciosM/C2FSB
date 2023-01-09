
from Cell2Fire.ParseInputs import ParseInputs
def main():
    args = ParseInputs()

if __name__ == "__main__":
    main()    

DataFolders
'InFolder' : "The path to the folder contains all the files for the simulation =?"
'OutFolder' : "The path to the folder for simulation output files =?"

Viento
'nweathers' : "Max index of weather files to sample for the random version (inside the Weathers Folder) = 1"

Combustible

Fuego
'IgRadius' : "Adjacents degree for defining an ignition area (around ignition point) = 0"

AjustesAlgoritmo
'seed' : "seed random number generator = 42"
'nthreads' : "cpu threads to run the simulation" = 1!->2"
'nsims' : "number of simulations (replications)"
'heuristic' : "Heuristic version to run (-1 default no heuristic, 0 all)"

AjustesResultados
'gridsStep' : "Grids are generated every n time steps = 60"
'gridsFreq' : "Grids are generated every n episodes/sims = -1"
'messages_path' : "Path with the .txt messages generated for simulators = False"

NOPE
'sim_years' = 1
'max_fire_periods' = 1000

'OutBehavior',
'BBO',
'BFactor',
'BurningLen',
'CBDFactor',
'CCFFactor',
'EFactor',
'FFactor',
'GASelection',
'GPTree',
'Geotiffs',
'HCells',
'HFI_Threshold',
'HFactor',
'OutMessages',
'PromTuning',
'ROS10Factor',
'ROS_CV',
'ROS_Threshold',
'TFraction',
'WeatherOpt',
'allPlots',
'combine',
'cros',
'cxpb',
'fdemand',
'finalGrid',
'grids',
'ignitions',
'indpb',
'input_PeriodLen',
'input_gendata',
'input_trajectories',
'msgHeur',
'mutpb',
'ngen',
'noEvaluation',
'no_output',
'npop',
'onlyProcessing',
'pdfOutputs',
'planPath',
'plots',
'spreadPlots',
'stats',
'tCorrected',
'tSize',
'valueFile',
'verbose',
'weather_period_len'

