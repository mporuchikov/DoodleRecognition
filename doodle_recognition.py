import numpy as np
import cv2
import tkinter
from tkinter import *

img = np.ones((480,640,3), dtype=np.uint8)*255

print(img.shape)

window = tkinter.Tk()
window.title('Doodle Recognition')

x_new = -1
y_new = -1
x_old = -1
y_old = -1

strokes = []
curve = []
stroke_idx = 0

def clear_canvas():
    canvas.create_rectangle(0, 0, 640, 480, outline="#FFFFFF", fill="#FFFFFF")
    

def ms_release(event):
    global strokes, stroke_idx, curve

    strokes.append(curve)
    curve = []
    stroke_idx += 1


def ms_right_dbl_click(event):
    global strokes, stroke_idx, curve, img
    
    strokes = []
    curve = []
    stroke_idx = 0
    cv2.imwrite('image.png', img)

    img = np.ones((480,640,3), dtype=np.uint8)*255
    clear_canvas()
    

def ms_move(event):
    global x_old, y_old, x_new, y_new, curve, img
    
    x_new = np.clip(event.x,0,639)
    y_new = np.clip(event.y,0,479)

    if len(curve) == 0:
        x_old = x_new
        y_old = y_new

    canvas.create_line(x_old, y_old, x_new, y_new, fill='black', width=10)
    cv2.line(img,(x_old,y_old),(x_new,y_new),(0,0,0),10)

    curve.append([x_old,y_old,x_new,y_new])

    x_old = x_new
    y_old = y_new


### main

canvas = Canvas(window, width=640, height=480)

clear_canvas()

canvas.bind("<B1-Motion>", ms_move)
canvas.bind("<ButtonRelease-1>", ms_release)
canvas.bind("<Double-Button-3>", ms_right_dbl_click)

canvas.pack(fill=BOTH, expand=0)


window.mainloop()
