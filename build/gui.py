from pathlib import Path
from os import system
from tkinter import Tk, Canvas,Label, Button, PhotoImage,Frame
from threading import Thread

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

video=None
page=None
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.attributes("-fullscreen", True)
window.configure(bg = "#FFFFFF")
window.update_idletasks()
screen_size={'w':window.winfo_width(),'h':window.winfo_height()}
print(screen_size)
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
    system(video)
    switch_to_start()
def switch_to_play():
    frame_start.pack_forget()
    canvas.pack_forget()
    frame_play.pack()
    canvas2.pack()
def switch_to_start():
    frame_start.pack()
    canvas.pack()
    frame_play.pack_forget()
    canvas2.pack_forget()

def play_1():
   global video
   video='1.mp4'
   label = Label(canvas2, text='''نام بازی: فوتبالیست ماشینی 
قیمت بلیط بای هر نفر: 100 هزار تومان
زمان بازی: 10 دقیقه''', bg="#FFFFFF", fg="#000000", font=("Arial", 24),justify='right')
   label.place(x=screen_size['h']+resizer(230,'h'), y=resizer(62.0,'h')+100)
   switch_to_play()


button_image_1 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_1.png"))
button_1 = Button(frame_start,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=play_1,
    relief="flat"
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
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
    command=lambda: print("button_3 clicked"),
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
    command=lambda: print("button_4 clicked"),
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
    command=lambda: print("button_5 clicked"),
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
    command=lambda: print("button_6 clicked"),
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
    command=lambda: print("button_7 clicked"),
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
    command=lambda: print("button_8 clicked"),
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
    command=lambda: print("button_9 clicked"),
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
    command=lambda: print("button_10 clicked"),
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
    command=lambda: print("button_11 clicked"),
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
    command=lambda: print("button_12 clicked"),
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
image_image_2 = PhotoImage(master=frame_play,
    file=relative_to_assets("image_1.png"))
image_2 = canvas.create_image(
    resizer(num=720,mode='w'),
    resizer(num=57.0,mode='h'),
    image=image_image_2
)
button_image_20 = PhotoImage(master=frame_play,
    file=relative_to_assets("play.png"))
button_20 = Button(frame_play,
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=play_video,
    relief="flat"
)
button_20.place(
    x=resizer(555,'w'),
    y=resizer(405.0,'h'),
    width=resizer(340.0,'h'),
    height=resizer(340.0,'w')
)
if page==None:
    switch_to_start()
    page='start'
window.resizable(False, False)
window.mainloop()
