from pathlib import Path
from os import system
import os
from tkinter import Tk, Canvas,Label, Button, PhotoImage,Frame
from tkinter.font import Font
import pandas as pd
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

video=None
page=None
label=None
image_add=None
image_lable=None
data=None
machine_soccer_text=f"{data}"
play_mode='play1.png'
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
if os.path.isfile('data.csv'):
    data=pd.read_csv('data.csv',index_col=False)

window = Tk()
window.attributes("-fullscreen", True)
window.configure(bg = "#FFFFFF")
window.update_idletasks()
window.title("Mositto")
screen_size={'w':window.winfo_width(),'h':window.winfo_height()}
print(screen_size)
custom_font=Font(family='Sheed',size=24)
frame_start=Frame(window)
frame_play=Frame(window)

def resizer(num,mode):
    if mode=='w':
        return num*(screen_size["w"]/1440)
    else:
        return num*(screen_size["h"]/850)

canvas = Canvas(
    frame_start,
    bg = "#FFFFFF",
    height = 850*(screen_size["h"]/850),
    width = 1440*(screen_size["w"]/1440),
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# Example usage
def play_video():
    if video!=None:
        system(video)
        switch_to_start()
    else:
        switch_to_start()

def switch_to_play():
    frame_start.pack_forget()
    canvas.pack_forget()
    frame_play.pack()
    canvas2.pack()
    
def update_image(IM,BG=None):
    global image_add
    global image_lable
    if IM!=None and BG!=None:
        image_add=PhotoImage(master=frame_play,file=relative_to_assets(IM)).subsample(int(resizer(420,'w')/420),int(resizer(370,'h')/370))
        image_lable.config(image=image_add,bg=BG)
    elif BG!=None:
        image_lable.configure(image='',bg=BG,text='در حال بروز رسانی',font=custom_font)
    else:
        image_lable.configure(image='',bg='#FFFFFF',text='در حالی بروز رسانی',font=custom_font)
def switch_to_start():
    frame_start.pack()
    canvas.pack()
    frame_play.pack_forget()
    canvas2.pack_forget()

def play_1():
   global label
   global video
   video='Machin_soccer.mp4'
   canvas2.configure(bg='#BEE6ce')
   if label==None:
        label = Label(canvas2, text=f"نام بازی : فوتبالیست ماشینی\nقیمت بلیط برای هر نفر:  {int(data.loc[data['game_name']=='Machine_soccer']['price'].loc[0])} هزار تومان \nمدت زمان بازی : {int(data.loc[data['game_name']=='Machine_soccer']['time'].loc[0])} دقیقه", bg="#BEE6ce", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : فوتبالیست ماشینی\nقیمت بلیط برای هر نفر:  {int(data.loc[data['game_name']=='Machine_soccer']['price'].loc[0])} هزار تومان \nمدت زمان بازی : {int(data.loc[data['game_name']=='Machine_soccer']['time'].loc[0])} دقیقه",bg='#BEE6ce')
   update_image(None,'#BEE6ce')
   switch_to_play()
   
def play_2():
   global label
   global video
   video='Robo_war.mp4'
   price = int(data.loc[data['game_name']=='Robo_war', 'price'].iloc[0])
   time = int(data.loc[data['game_name']=='Robo_war', 'time'].iloc[0])
   if label==None:
        label = Label(canvas2, text=f"نام بازی : جنگ ربات ها \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه", bg="#FE5F55", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : جنگ ربات ها \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه",bg='#FE5F55')
   canvas2.configure(bg='#FE5F55')
   update_image("Robo_war.png",'#FE5F55')
   switch_to_play()
def play_3():
   global label
   global video
   video='RC_climber.mp4'
   price = int(data.loc[data['game_name']=='RC', 'price'].iloc[0])
   time = int(data.loc[data['game_name']=='RC', 'time'].iloc[0])
   if label==None:
        label = Label(canvas2, text=f"نام بازی : صخره نورد \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه", bg="#319a08", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : صخره نورد \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه",bg='#319a08')
   canvas2.configure(bg='#319a08')
   update_image('RC_climber.png','#319a08')
   switch_to_play()
def play_4():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()
def play_5():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()
def play_6():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()
def play_7():
   global label
   global video
   video=None
   price = int(data.loc[data['game_name']=='Human_soccer', 'price'].iloc[0])
   time = int(data.loc[data['game_name']=='Human_soccer', 'time'].iloc[0])
   if label==None:
        label = Label(canvas2, text=f"نام بازی : فوتبالیست انسان نما \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه", bg="#15887d", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : فوتبالیست انسان نما \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه",bg='#15887d')
   canvas2.configure(bg='#15887d')
   update_image(None,'#15887d')
   switch_to_play()
def play_8():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()
def play_9():
   global label
   global video
   video=None
   price = int(data.loc[data['game_name']=='little_road', 'price'].iloc[0])
   time = int(data.loc[data['game_name']=='little_road', 'time'].iloc[0])
   if label==None:
        label = Label(canvas2, text=f"نام بازی : مسیر چوبی کودکان \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه", bg="#309a08", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : مسیر چوبی کودکان \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه",bg='#309a08')
   canvas2.configure(bg='#309a08')
   update_image(None,'#309a08')
   switch_to_play()
def play_10():
   global label
   global video
   video=None
   price = int(data.loc[data['game_name']=='VR', 'price'].iloc[0])
   time = int(data.loc[data['game_name']=='VR', 'time'].iloc[0])
   if label==None:
        label = Label(canvas2, text=f"نام بازی : واقعیت مجازی \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه", bg="#dd89ff", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text=f"نام بازی : واقعیت مجازی \nقیمت بلیط برای هر نفر:  {price} هزار تومان \nمدت زمان بازی : {time} دقیقه",bg='#dd89ff')
   canvas2.configure(bg='#dd89ff')
   update_image(None,'#dd89ff')
   switch_to_play()
def play_11():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()
def play_12():
   global label
   global video
   video=None
   if label==None:
        label = Label(canvas2, text="درحال بروز رسانی", bg="#FFFFFF", fg="#000000", font=custom_font,justify='right')
        label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+resizer(100,'h'))
   else:
        label.config(text="درحال بروز رسانی",bg='#FFFFFF')
   canvas2.configure(bg='#FFFFFF')
   update_image(None)
   switch_to_play()

button_image_1 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_1.png"))
button_1 = Button(frame_start,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=play_1,
    relief="flat",
)
button_1.place(
    x=resizer(0.0,'w'),
    y=resizer(126.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(114.0,'w'),
)

button_image_2 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_2.png"))
button_2 = Button(frame_start,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=play_2,
    relief="flat",
)
button_2.place(
    x=resizer(0.0,'w'),
    y=resizer(248.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(113.0,'w')
)

button_image_3 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_3.png"))
button_3 = Button(frame_start,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=play_3,
    relief="flat"
)
button_3.place(
    x=resizer(0.0,'w'),
    y=resizer(369.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(116.0,'w')
)

button_image_4 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_4.png"))
button_4 = Button(frame_start,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=play_4,
    relief="flat"
)
button_4.place(
    x=resizer(0.0,'w'),
    y=resizer(491.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(116.0,'w')
)

button_image_5 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_5.png"))
button_5 = Button(frame_start,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=play_5,
    relief="flat"
)
button_5.place(
    x=resizer(0.0,'w'),
    y=resizer(615.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(113.0,'w')
)

button_image_6 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_6.png"))
button_6 = Button(frame_start,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=play_6,
    relief="flat"
)
button_6.place(
    x=resizer(0.0,'w'),
    y=resizer(736.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(114.0,'w')
)

button_image_7 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_7.png"))
button_7 = Button(frame_start,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=play_7,
    relief="flat"
)
button_7.place(
    x=resizer(723.0,'w'),
    y=resizer(126.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(114.0,'w')
)

button_image_8 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_8.png"))
button_8 = Button(frame_start,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=play_8,
    relief="flat"
)
button_8.place(
    x=resizer(723.0,'w'),
    y=resizer(248.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(113.0,'w')
)

button_image_9 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_9.png"))
button_9 = Button(frame_start,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=play_9,
    relief="flat"
)
button_9.place(
    x=resizer(723.0,'w'),
    y=resizer(369.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(116.0,'w')
)

button_image_10 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_10.png"))
button_10 = Button(frame_start,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=play_10,
    relief="flat"
)
button_10.place(
    x=resizer(723.0,'w'),
    y=resizer(491.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(116.0,'w')
)

button_image_11 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_11.png"))
button_11 = Button(frame_start,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=play_11,
    relief="flat"
)
button_11.place(
    x=resizer(723.0,'w'),
    y=resizer(615.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(113.0,'w')
)

button_image_12 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_12.png"))
button_12 = Button(frame_start,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=play_12,
    relief="flat"
)
button_12.place(
    x=resizer(723.0,'w'),
    y=resizer(736.0,'h'),
    width=resizer(717.0,'h'),
    height=resizer(114.0,'w')
)

image_image_1 = PhotoImage(master=frame_start,
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    resizer(720.0,'w'),
    resizer(62.0,'h'),
    image=image_image_1
)
#frame start is finished
canvas2 = Canvas(
    frame_play,
    bg = "#FFFFFF",
    height = 850*(screen_size["h"]/850),
    width = 1440*(screen_size["w"]/1440),
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas2.place(x = 0, y = 0)
button_image_20 = PhotoImage(master=frame_play,
    file=relative_to_assets(play_mode))
button_20 = Button(frame_play,
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=play_video,
    relief="flat",
)
print(button_image_20)
button_20.place(
    x=screen_size['h']+resizer(330,'h'),
    y=resizer(490.0,'h'),
    width=resizer(244.0,'h'),
    height=resizer(221.0,'w')
)
image_add=PhotoImage(master=frame_play,file=relative_to_assets("button_12.png")).subsample(int(resizer(420,'w')/420),int(resizer(370,'h')/370))
image_lable=Label(canvas2,image=image_add)
image_lable.place(x=resizer(18,'w') ,y=(resizer(62.0,'h')+resizer(100,'h'))/2)
if page==None:
    switch_to_start()
    page='start'
window.resizable(False, False)
window.mainloop()
