# 27 dic:
 - Cambio para ejecutar window.py en debian

# 28 dic: 
 - Add .gitignore python y compilados
 - Quitar dependencia opencv-python: Solo se usa para abrir imagen y despues intercambiar canales, se reemplaza por imread que es dependencia menos compleja
```
fdo@fdair:~/source/C2FSB$ grep -R -n cv2 --include='*py' --exclude-dir='pyenv/'
Cell2Fire/Stats.py:25:import cv2
Cell2Fire/Stats.py:924:        p1 = cv2.imread(ForestFile)
Cell2Fire/Stats.py:929:        p2 = cv2.imread(PathFile)
Cell2Fire/Stats.py:932:        p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2RGBA)
Cell2Fire/Stats.py:933:        p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2RGBA)
```

