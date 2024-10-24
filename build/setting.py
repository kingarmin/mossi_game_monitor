import tkinter as tk 
from tkinter import ttk 
import os
import pandas as pd
value=None
data=None
# Creating tkinter window 
if not(os.path.isfile('game.csv')):
    data=pd.DataFrame({'game_name':['Machine_soccer',
                          'Human_soccer',
                          'RC',
                          'VR',
                          'Hovercraft',
                          'Escape_wall',
                          'Ofroad',
                          'Board_game',
                          'Mossi_one',
                          'little_war',
                          'little_road',
                          'Robo_war',],'price':[100,150,200,100,None,None,None,None,None,None,100,150],'time':[10,10,10,10,10,10,10,10,10,10,10,10]})
    data.to_csv('data.csv',index=False)
else:
    data=pd.read_csv(index_col=False)
window = tk.Tk() 
window.title('Setting') 
window.geometry('300x200')
def get_entry_value(event):
    global data
    game_name=monthchoosen.get()
    game_fucher=monthchoosen2.get()
    value=entry.get()
    data.loc[data['game_name']==game_name,game_fucher]=value
    print(data)

def get_n():
    print(monthchoosen.get())
# label text for title 
  
# label 
ttk.Label(window, text = "game_name :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
# Adding combobox drop down list 
monthchoosen['values'] = ('Machine_soccer',
                          'Human_soccer',
                          'RC',
                          'VR',
                          'Hovercraft',
                          'Escape_wall',
                          'Ofroad',
                          'Board_game',
                          'Mossi_one',
                          'little_war',
                          'little_road',
                          'Robo_war',) 
entry=tk.Entry( window,bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    )
entry.place(x=125,y=100,)
entry.bind("<Return>",get_entry_value)

lable=tk.Label(window,text='game feature : ',font=("Times New Roman", 10))
lable.place(x=9,y=70)
  
# Combobox creation 
n2 = tk.StringVar() 
monthchoosen2 = ttk.Combobox(window, width = 27, textvariable = n2) 
# Adding combobox drop down list 
monthchoosen2['values'] = ('price','time') 
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
monthchoosen2.grid(column = 1, row = 6) 
monthchoosen2.current() 
window.mainloop()
data.to_csv('data.csv',index=False)