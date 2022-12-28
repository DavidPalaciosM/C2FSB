# test y analisis de dependencias

- buscar en el codigo apariciones del modulo, ej
```
C2FSB$ grep -R -n tqdm --include=*py
```
- Hacer un virtual environment con menos modulos para pruebas

# matplotlib
Bien! no hay uso de plt.show() luego no abre ventanas interactivamente. solo uso de plt.savefig para guardar .png

Dependera de un backend para mostrarlas

# seaborn
creo que depende solo de matplotlib 

# imread
reemplazo de cv2.imread

# tqdm
_candidato a quitarse_

Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!
Si no hubiese output de la consola en el gui, quitarlo (un macro de vim se me ocurre para matchear el parentesis)

# opencv 
_candidato a quitarse_
Es cacho empacarlo, se pueden reemplazar sus 2 usos con un unico de imread, paquete especifico
```
fdo@p51:~/source/C2FSB$ grep -R cv2 --include=*py
	Cell2Fire/Stats.py:import cv2
	Cell2Fire/Stats.py:        p1 = cv2.imread(ForestFile)
	Cell2Fire/Stats.py:        p2 = cv2.imread(PathFile)
	Cell2Fire/Stats.py:        p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2RGBA)
	Cell2Fire/Stats.py:        p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2RGBA)
```
- cv2.cvtColor(p2, cv2.COLOR_BGR2RGBA) : cambiar de lugar el b y r, agregarle un 0 del alpha

```
In [16]: import imread

In [20]: imgA = imread.imread('test.png')#por default lee rgba

In [21]: import cv2 as cv

In [22]: imgB = cv.imread('test.png') #por default lee bgr

In [27]: imgA[ 242:244, 318:320 ]
Out[27]:
array([[[183, 195, 220, 255],
        [216, 220, 234, 255]],

       [[187, 198, 221, 255],
        [202, 209, 228, 255]]], dtype=uint8)

In [28]: imgB[ 242:244, 318:320 ]
Out[28]:
array([[[220, 195, 183],
        [234, 220, 216]],

       [[221, 198, 187],
        [228, 209, 202]]], dtype=uint8)
```

como se aprecia 220 y 183 estan invertidos, luego es posible evitar opencv completamente

# networkx
```
C2FSB$ grep -R -n "networkx\|nx\." --include=*py
```
depende de matplotlib para dibujar
nx.draw...

# rasterio
reads and writes geospatial raster data.
Unofficial binary packages for Windows are available through other channels.
Usado para los tifs mapas con capas y metadata

# deap
platforms : win, linux, macos

# scipy
platforms : win, linux, macos
ok Heuristics
 


