# C2F+S&B
## Cristobal Pais, Jaime Carrasco, David Martell, David L. Woodruff, Andres Weintraub
C2F+S&B is an open-source wildfire simulator based on Cell2Fire and the Scott And Burgan Fuel Model

# Requirements
- Boost (C++)
- Eigen (C++)
- Python 3.6
- numpy
- pandas
- matplotlib
- seaborn
- tqdm
- rasterio
- networkx (for stats module)

# Usage
In order to run the simulator and process the results, the following command can be used:
```
$ python main.py --input-instance-folder /data/Hom_Fuel_101_40x40/ --output-folder results/Hom_Fuel --ignitions --sim-years 1 --nsims 100 --grids --finalGrid --weather rows --nweathers 1 --Fire-Period-Length 1.0 --output-messages --ROS-CV 0.8 --seed 123 --stats --allPlots --IgnitionRad 1
```
For the full list of arguments and their explanation use:
```
$ python main.py -h
```


# Console usage (on development)
To use the simulator with a console (via python), the following command can be used:
```
$ python window.py
```
Importante: not all arguments are implemented on the console
