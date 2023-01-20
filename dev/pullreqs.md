# pull request

## remove trailing whitespace
In vim: `:%s/\s\+$//e`  

## replace opencv-python with imread
En Cell2Fire/Stats.py : 924   
```
import imread
        p1 = cv2.imread(ForestFile) --> p1 = imread.imread(ForestFile)
        p2 = cv2.imread(PathFile) --> p2 = imread.imread(PathFile)
-       p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2RGBA)
-       p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2RGBA)
```
No veo por que el png cargado podria no tener el canal transparente si lo genera el mismo codigo.  
En todo caso se podria implementar con arreglos numpy la funcion `cv2.COLOR_BGR2RGBA`:    
Para cada pixel, cambiar el primero por el tercero y adicionar un cuarto...

En requirements.txt, quite opencv-python

## dummy messages missing folder
Cell2FireC.py : 215 , 238, 499; en funcion DummyMsg, DummyMsg_Heur, heur
```
# similar a esto
        MPath = os.path.join(self.args.OutFolder, "Messages")
+       if not os.path.exists(MPath):
+           os.makedirs(MPath)
```
Segun entiendo se deberia resolver en 
```
Cell2FireC/Cell2Fire.cpp:481:   // Messages Folder
Cell2FireC/Cell2Fire.cpp:482:   if(this->args.OutMessages){
Cell2FireC/Cell2Fire.cpp:484:           this->messagesFolder = "mkdir -p " + this->args.OutFolder + "/Messages/";
```
pero tal vez llegue al bug por una combinacion de cmd options ilogica asi que juan segura checkea 3 veces

## matplotlib figsize deprecation in plt.savefig
- [current docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
```
    plt.savefig(..., figsize=(200, 200)...)
    ->
    plt.figure(1,figsize=(200, 200))
    plt.savefig(...
```
Ahora se puede quitar el ==3.5.1 en matplotlib requirements.txt  

## matplotlib efficency
- https://stackoverflow.com/questions/28757348/how-to-clear-memory-completely-of-all-matplotlib-plots  
- https://github.com/matplotlib/matplotlib/issues/20300  
- https://pypi.org/project/memory-profiler/  
Cell2Fire/Stats.py : Usar una sola figura para todo!  (lo revise con pypi memory_profiler porque se caia un ejemplo con mi compu de 8GB ram)
```
matplotlib.use('Agg')
class Statistics(object):
    def __init__(self,...
+       # recicle just one figure
+       self.fig = plt.figure(1)

# cada vez que comienza un grafico 
        plt.figure(1,figsize = (15, 9))
# es equivalente tambien llamar
        self.plt_style()

```
### duda con figsize=(200,200) y dpi=200
En GlobalFireSpreadEvo, SimFireSpreadEvo, SimFireSpreadEvoV2, 
creo que es excesivo ese tamaño = 200*200*200 pixeles en principio, siendo que el png resultante es mucho menor. ? Por que? Reduzcamoslo
