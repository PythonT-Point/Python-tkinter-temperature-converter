from tkinter import *
import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)



def converttemperature():
    if labelleft['text']=='\N{DEGREE FAHRENHEIT}':
        tempf = entrytemp.get()
        tempc= (float(tempf)-32)*5/9
        labeltemp['text']=f"{round(tempc, 2)}"
    else:
        tempc = entrytemp.get()
        tempf= (float(tempc)*9/5)+32
        labeltemp['text']=f"{round(tempf, 2)}"        

def reverse():
    if labelleft['text']=='\N{DEGREE FAHRENHEIT}':
        labelleft['text']="\N{DEGREE CELSIUS}"
        labelright['text']='\N{DEGREE FAHRENHEIT}'
    else:
        labelleft['text']='\N{DEGREE FAHRENHEIT}'
        labelright['text']='\N{DEGREE CELSIUS}'
        


wd = tk.Tk()
wd.title('Pythontpoint')

entrytemp = tk.Entry(master = wd)
entrytemp.pack(side=tk.LEFT)
entrytemp.insert(0,'0')



labelleft = tk.Label(text='\N{DEGREE FAHRENHEIT}', width=5)
labelleft.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

button = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=converttemperature)
button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

labeltemp = tk.Label(text='', width=10)
labeltemp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

labelright = tk.Label(text="\N{DEGREE CELSIUS}")
labelright.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

button_reverse = tk.Button(text='\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}', command=reverse)
button_reverse.pack(side=tk.LEFT,fill=tk.BOTH, padx=6, expand=True)

wd.mainloop()