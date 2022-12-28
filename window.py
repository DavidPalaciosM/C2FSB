# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:43:54 2022

@author: david
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfile
import os
def cell2Fire_call():
    call="python3 main.py --input-instance-folder "
    call+=os.path.join(os.path.normpath(fuels_box.get()),"")
    call+=os.path.join(" --output-folder results","")
    call+=os.path.normpath(results_box.get())
    call=call.replace(os.sep,"/")
    call+=" --sim-years 1 "
    call+=" --nsims "+ Nsims.get()
    call+=" --Fire-Period-Length "+FPlength.get()
    call+=" --ROS-CV "+ROSCV.get()
    call+=" --seed "+Seed.get()
    call+= " --nthreads "+threads.get()
    
    if grid_option.get()==0:
        grids_op=" --grids"
    if grid_option.get()==1:
        grids_op=" --final-grid"
    call+=grids_op
    
    if messages_option.get()==0:
        messages=""
    if messages_option.get()==1:
        messages=" --output-messages"

    call+=messages
    
    if behavior_option.get()==0:
        behavior=""
    if behavior_option.get()==1:
        behavior=" --out-behavior"

    call+=behavior
    
    if crown_option.get()==0:
        crown=""
    if crown_option.get()==1:
        crown=" --cros"
        
    call+=crown
    
    
    call+=" --weather "+weather_box.get()
    if weather_box.get()=="random":
        call+=" --nweathers "+ nweathers.get()
    
    if ignition_box.get()=="selected point":
        ignitionMode=" --ignitions "
        ignitionRadius="--IgnitionRad "+ignitionRad.get()
        call+=ignitionMode+ignitionRadius

    if stats_option.get()==0:
        grids_op=""
    if stats_option.get()==1:
        grids_op=" --stats"
    if stats_option.get()==2:
        grids_op=" --stats --allPlots"
        
    call+=grids_op
    #results=fuels_box.get()
    l1 = ttk.Label(text=call, font=('Georgia 6'))
    l1.place(x=20, y=620)
    #call command prompt
    #main_call="ubuntu run time "+call
    main_call=call
    print(main_call)
    os.system(main_call)
    
 
def open_file():
   file = filedialog.askdirectory()
   file="data"+file.split("data")[1]
   #file=file.name
   fuels_box.delete(0, tk.END)
   fuels_box.insert(0, file)
      
ventana = tk.Tk()


ventana.title("Cell2Fire")
ventana.config(width=1200, height=620)
#Data Folder
fuels_label = ttk.Label(text="Data Folder", font=('Georgia 10'))
fuels_label.place(x=20, y=20)
fuels_button= ttk.Button(text="Browse", command=open_file)
fuels_button.place(x=600, y=20)
fuels_box = ttk.Entry()
fuels_box.place(x=180, y=20, width=400)

#Results Folder
results_label = ttk.Label(text="Results Folder", font=('Georgia 10'))
results_label.place(x=20, y=60)
results_box = ttk.Entry()
results_box.place(x=180, y=60, width=400)

#Nsims
ttk.Label(ventana,text="Number of Simulations", font=('Georgia 10')).place(x=20, y=100)
Nsims = ttk.Entry()
Nsims.place(x=250, y=100, width=100)

#Fire Period Length
ttk.Label(ventana,text="Fire Period Length", font=('Georgia 10')).place(x=20, y=140)
FPlength = ttk.Entry()
FPlength.insert(tk.END, "1.0")
FPlength.place(x=250, y=140, width=100)

#ROS C.V.
ttk.Label(ventana,text="ROS CV", font=('Georgia 10')).place(x=20, y=180)
ROSCV = ttk.Entry()
ROSCV.insert(tk.END, "0.0")
ROSCV.place(x=250, y=180, width=100)

#Seed
ttk.Label(ventana,text="Seed", font=('Georgia 10')).place(x=20, y=220)
Seed = ttk.Entry()
Seed.insert(tk.END, "123")
Seed.place(x=250, y=220, width=100)

#Grids
grid_option = tk.IntVar()

rdioOne = tk.Radiobutton(ventana, text='All Grids',
                             variable=grid_option, value=0) 
rdioTwo = tk.Radiobutton(ventana, text='Only Final Grid',
                             variable=grid_option, value=1) 

ttk.Label(ventana,text="Grids Option", font=('Georgia 10')).place(x=20, y=260)
rdioOne.place(x=20,y=290)
rdioTwo.place(x=120, y=290)

#Messages
messages_option = tk.IntVar()
ttk.Label(ventana,text="Messages Option", font=('Georgia 10')).place(x=20, y=330)
c1 = tk.Checkbutton(ventana, text='Messages results',variable=messages_option, onvalue=1, offvalue=0)
c1.place(x=20,y=360)

#Behavior
behavior_option = tk.IntVar()
ttk.Label(ventana,text="Fire Behavior Option", font=('Georgia 10')).place(x=20, y=400)
c2 = tk.Checkbutton(ventana, text='Fire Behavior Results',variable=behavior_option, onvalue=1, offvalue=0)
c2.place(x=20,y=440)

#CrownFire
crown_option = tk.IntVar()
ttk.Label(ventana,text="Crown Fire Option", font=('Georgia 10')).place(x=20, y=480)
c3 = tk.Checkbutton(ventana, text='Allow Crown Fire',variable=crown_option, onvalue=1, offvalue=0)
c3.place(x=20,y=520)




#Weather
#weather_option = tk.StringVar()
#number_of_weathers=""
def pick_weather(e):
    global nweathers
    nweathers = tk.StringVar()
    #number_of_weathers=""
    if weather_box.get()=="random":
        ttk.Label(ventana,text="Number of Weathers", font=('Georgia 10')).place(x=700, y=200)
        weathers = ttk.Entry(textvariable=nweathers)
        weathers.insert(tk.END, "")
        weathers.place(x=900, y=200, width=100)
        #number_of_weathers=" -- "+str(nweathers.get())
    #return number_of_weathers
    
ttk.Label(ventana,text="Weather Options", font=('Georgia 10')).place(x=730, y=150)
options=["distribution","random","rows"]
weather_box=ttk.Combobox(ventana,value=options)
weather_box.current(2)
weather_box.place(x=900,y=150)
weather_box.bind("<<ComboboxSelected>>",pick_weather)


#ignitions
#ignitions_option = tk.StringVar()
def pick_ignition(e):
    global ignitionRad
    ignitionRad =tk.StringVar()
    if ignition_box.get()=="selected point":
        ttk.Label(ventana,text="Ignition Radius", font=('Georgia 10')).place(x=730, y=350)
        ignrad = ttk.Entry(textvariable=ignitionRad)
        ignrad.insert(tk.END, "0")
        ignrad.place(x=900, y=350, width=100)
        #ignitionRad=str(ignrad.get())

    
ttk.Label(ventana,text="Ignition Options", font=('Georgia 10')).place(x=730, y=300)
options_ign=["random","selected point"]
ignition_box=ttk.Combobox(ventana,value=options_ign)
ignition_box.current(0)
ignition_box.place(x=900,y=300)
ignition_box.bind("<<ComboboxSelected>>",pick_ignition)
ignitionMode=""



#nthreads
ttk.Label(ventana,text="Parallel threads", font=('Georgia 10')).place(x=730, y=480)
threads = ttk.Entry()
threads.insert(tk.END, "1")
threads.place(x=900, y=480, width=100)

#PostProcessing

ttk.Label(ventana,text="PostProcessing", font=('Georgia 10')).place(x=20, y=570)
#Stats
stats_option = tk.IntVar()

not_button = tk.Radiobutton(ventana, text='Not PostProcessing',
                             variable=stats_option, value=0) 
stats_button = tk.Radiobutton(ventana, text='Obtain Only Stats',
                             variable=stats_option, value=1) 
plots_button = tk.Radiobutton(ventana, text='Obtain Plots and Stats',
                             variable=stats_option, value=2) 
not_button.place(x=20,y=600)
stats_button.place(x=250,y=600)
plots_button.place(x=450, y=600)



#close_button=ttk.Button(text= "Close the Window", command=close).place(x=180, y=60, width=400)
#print(a)
Execute_button = ttk.Button(text="Execute", command=cell2Fire_call)
Execute_button.place(x=800, y=600)

ventana.mainloop()
