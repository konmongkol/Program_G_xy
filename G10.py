from tkinter import *
import tkinter as tk
import matplotlib
import numpy as np #! 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from G_xy import *
from PIL import Image, ImageTk
win = Tk()
global VT

win.title('G10')
win.minsize(width=1000, height=700) #setขนาด
win.geometry("1000x700")
win.option_add("*Font"," TkTooltipFont 15")
w1 = 10
matplotlib.use("TkAgg")

menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ='menu', menu = filemenu)

#! เเก้รูปเเปะ  setขนาดรูปภาพ ขนาดหน้าจอ
def some():
    root1 = Toplevel()    
    root1.wm_title("member")
    root1.geometry("1000x550")
    load = Image.open("team.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root1,image=render)
    img.image = render
    img.place(x=0, y=0)
    print("img")
# some()

fileanother = Menu(menubar, tearoff=0) 
fileanother.add_command(label="member", command=some)
menubar.add_cascade(label ='another', menu = fileanother)

read_file = open("save.txt", "r")
i_file = read_file.read()
global o_file
o_file = i_file.split(',')
read_file.close()

def i_value(x,value):
    for i,j in enumerate(o_file):
        if j == x:
            o_file[i+1] = value
def o_value(x):
    for i,j in enumerate(o_file):
        if j == x:      
            return float(o_file[i+1])

def save(x):
    f = open("save.txt", "w")
    f.write(x)
    f.close()


def list_to_str(x):
    STR = []
    _STR = ""
    for i in x:
        STR.append(str(i))
    _STR = ','.join(STR)
    return _STR


def setting():
    def set():
        if (input_g.get() != ""):  
            i_value("g",input_g.get())
            g.config(text="g"+ " " + str(o_value("g")))
            save(list_to_str(o_file))
            input_g.delete(0, END)
        if (input_x.get() != ""):
            i_value("x",input_x.get())
            x.config(text="x"+ " " + str(o_value("x")))
            save(list_to_str(o_file))
            input_x.delete(0, END)
        if (input_y.get() != ""):
            i_value("y",input_y.get())
            y.config(text="y"+ " " + str(o_value("y")))
            save(list_to_str(o_file))
            input_y.delete(0, END)
        if(input_k.get() != ""):
            i_value("k",input_k.get())
            k.config(text="k"+ " " + str(o_value("k")))
            save(list_to_str(o_file))
            input_k.delete(0, END)
            spring_constant.config(text="ค่านิจสปริง : " + str(o_value("k")) +" N*m")
        if(input_m.get() != ""):
            i_value("m",input_m.get())
            m.config(text="m"+ " " + str(o_value("m")))
            save(list_to_str(o_file))
            input_m.delete(0, END)
        if(input_p.get() != ""):
            i_value("p",input_p.get())
            p.config(text="p"+ " " + str(o_value("p")))
            save(list_to_str(o_file))
            input_p.delete(0, END)
    root = Tk()
    root.title('Setting')
    root.geometry("400x200")
    g = Label(root,text = "g"+ " " + str(o_value("g")))
    g.place(x = 4,y = 6)  
    input_g = Entry(root, width=20)
    input_g.place(x = 50,y = 6)
    x = Label(root,text = "x"+ " " + str(o_value("x")))
    x.place(x = 4,y = 35)  
    input_x = Entry(root, width=20)
    input_x.place(x = 50,y = 35)
    y = Label(root,text = "y"+ " " + str(o_value("y")))
    y.place(x = 4,y = 64)  
    input_y = Entry(root, width=20)
    input_y.place(x = 50,y = 64)
    k = Label(root,text = "k"+ " " + str(o_value("k")))
    k.place(x = 4,y = 93)
    input_k = Entry(root, width=20)
    input_k.place(x = 50,y = 93)
    #!สร้างใหม่
    m = Label(root,text = "m"+ " " + str(o_value("m")))
    m.place(x = 204,y = 6)
    input_m = Entry(root, width=20)
    input_m.place(x = 250,y = 6)
    p = Label(root,text = "p"+ " " + str(o_value("p")))
    p.place(x = 204,y = 35)
    input_p = Entry(root, width=20)
    input_p.place(x = 250,y = 35)
    Button(root, text="setting",fg="blue",command=set).place(x = 50,y = 122)
#!---------เเก้

if(o_value("k") == 0.0 and o_value("x") == 0.0 and o_value("y") == 0.0):
    print("No........")
    setting()
    
def simulator():
    global value_i
    k = float(o_value("k"))
    VT = (((k/2)*(value_i**2))-1.29*value_i)**0.5
    xy = G_xy(VT,float(o_value("g")))
    xy.graph_g_xy()
    
def savevalue():
    print("save")
    data = []
    data.append("--------------------------------------------------------------")
    data.append("x = "+str(X))
    data.append("y = "+str(Y))
    data.append("k = "+str(o_value("k")))
    data.append("g = "+str(o_value("g")))
    data.append("x_spring = "+str(value_i))
    data.append("D or ND = "+D_ND)
    print(data)
    with open('data.txt', 'a') as f:
        f.writelines('\n'.join(data))

#!-------------------------------------
def reset():
    gxy(0,0)
    NDgraph(0,0)
    Dgraph(0,0,0,0,0,0)
#!-------------------------------------
#!----------------
filemenu.add_command(label="setting", command=setting)
filemenu.add_command(label="simulator", command=simulator) #!------------
filemenu.add_command(label="reset", command=reset)
filemenu.add_command(label="save", command=savevalue)
filemenu.add_separator()
win.config(menu = menubar)

def NDgraph(v=0,G = 9.8):
    #!-----xt
    figure = Figure(figsize=(w1, 2), dpi=100)
    plot = figure.add_subplot(1, 4, 1) #,xlim=(0, 1), ylim=(-1, 1) ใส่เพื่อset x,y
    lr_x = []
    lr_y = []
    g_xt = graphxt(v,G)
    plot.set_title('xt')
    # plot.set_xlabel('Popularity')
    # plot.set_ylabel('Popularity')
    lr_x,lr_y = g_xt.list_graph_xt()
    plot.plot(lr_x, lr_y)
    canvas = FigureCanvasTkAgg(figure, win)
    canvas.get_tk_widget().grid(row=0, column=0)
    
    figure1 = Figure(figsize=(w1, 2), dpi=100)
    plot1 = figure1.add_subplot(1, 4, 2)
    lr_x1 = []
    lr_y1 = []
    g_yt = graphyt(v,G)
    plot1.set_title('yt')
    lr_x1,lr_y1 = g_yt.list_graph_yt()
    plot1.plot(lr_x1, lr_y1)
    canvas1 = FigureCanvasTkAgg(figure1, win)
    canvas1.get_tk_widget().grid(row=0, column=1)
    
    figure2 = Figure(figsize=(w1, 2), dpi=100)
    plot2 = figure2.add_subplot(1, 4, 3)
    lr_x2 = []
    lr_y2 = []
    g_vxt = graphvxt(v,G)
    plot2.set_title('vxt')
    lr_x2,lr_y2 = g_vxt.list_graph_vxt()
    plot2.plot(lr_x2, lr_y2)
    canvas2 = FigureCanvasTkAgg(figure2, win)
    canvas2.get_tk_widget().grid(row=0, column=2)

    figure3 = Figure(figsize=(w1, 2), dpi=100)
    plot3 = figure3.add_subplot(1, 4, 4)
    lr_x3 = []
    lr_y3 = []
    g_vyt = graphvyt(v,G)
    plot3.set_title('vyt')
    lr_x3,lr_y3,lr_z3 = g_vyt.list_graph_vyt()
    plot3.plot(lr_x3, lr_y3)
    canvas3 = FigureCanvasTkAgg(figure3, win)
    canvas3.get_tk_widget().grid(row=0, column=3)
    
    # todo ---------------- 2
    figure4 = Figure(figsize=(10, 5), dpi=100)
    plot4 = figure4.add_subplot(111)
    lr_x4 = []
    lr_y4 = []
    lr_x4,lr_y4  = gxy(v,G)
    plot4.set_title('xy')
    plot4.set_xlabel('x')
    plot4.set_ylabel('y')
    plot4.plot(lr_x4, lr_y4)
    canvas4 = FigureCanvasTkAgg(figure4, win)
    canvas4.get_tk_widget().grid(row=1,column=0,columnspan=3,rowspan=2,stick= "nsew")
    #!---------------------------------
    figure5 = Figure(figsize=(2, 2), dpi=100)
    plot5 = figure5.add_subplot(111)
    lr_x5 = []
    lr_y5 = []
    lr_x5,lr_y5 = g_xt.list_graph_xt()
    lr_x5 = []
    plot5.set_title('x')
    for lr_5 in range(len(lr_y5)):
        lr_x5.append(0)
    #! graph_xt ใช้
    #! r_x appendใน y
    #! r_x = self.v_x * t #!--------------เเปะในกราฟ x
    plot5.plot(lr_y5, lr_x5)
    canvas5 = FigureCanvasTkAgg(figure5, win)
    canvas5.get_tk_widget().grid(row=1, column=3,stick= "nsew")
    
    figure6 = Figure(figsize=(2, 2), dpi=100)
    plot6 = figure6.add_subplot(111)
    lr_x6 = []
    lr_y6 = []
    #! set x ,y = 0
    lr_x6,lr_y6,lr_z6 = g_vyt.list_graph_vyt()
    lr_x6 = []
    plot6.set_title('y')
    for lr_6 in range(len(lr_z6)):
        lr_x6.append(0)
    plot6.plot(lr_x6, lr_z6)
    canvas6 = FigureCanvasTkAgg(figure6, win)
    canvas6.get_tk_widget().grid(row=2, column=3,stick= "nsew")
    #!---------------------------------
def gxy(v=0,G=9.8):
    g = G
    V_initial4 = int(v)
    theta4 = (np.pi)/4
    v_x4 = V_initial4 * np.cos(theta4)
    v_y4 = V_initial4 * np.sin(theta4)
    time4 = np.linspace(0,100,10000)
    lr_x4 = []
    lr_y4 = []
    for t in time4:
        r_x = v_x4 * t
        r_y = (v_y4 * t) - 1/2 * g * (t ** 2)
        if r_y >= 0:
            lr_x4.append(r_x)
            lr_y4.append(r_y)
        else:
            break
    return lr_x4, lr_y4
#!!!!!!!!!!!!!!!!!!!!!!!!!
def Dgraph(k=0,x=0,m=0.025,g=9.8,p=1.25,v=0):
    #!-----xt
    figure = Figure(figsize=(w1, 2), dpi=100)
    plot = figure.add_subplot(1, 4, 1) #,xlim=(0, 1), ylim=(-1, 1) ใส่เพื่อset x,y
    lr_x = []
    lr_y = []
    g_xt = D_xVelocity(k,x,m,g,p)
    plot.set_title('xt')
    # plot.set_xlabel('Popularity')
    # plot.set_ylabel('Popularity')
    lr_x,lr_y = g_xt.list_xVelocity()
    plot.plot(lr_x, lr_y)
    canvas = FigureCanvasTkAgg(figure, win)
    canvas.get_tk_widget().grid(row=0, column=0)
    
    figure1 = Figure(figsize=(w1, 2), dpi=100)
    plot1 = figure1.add_subplot(1, 4, 2)
    lr_x1 = []
    lr_y1 = []
    g_yt = D_yVelocity(k,x,m,g,p)
    plot1.set_title('yt')
    lr_x1,lr_y1 = g_yt.list_yVelocity()
    plot1.plot(lr_x1, lr_y1)
    canvas1 = FigureCanvasTkAgg(figure1, win)
    canvas1.get_tk_widget().grid(row=0, column=1)
    
    figure2 = Figure(figsize=(w1, 2), dpi=100)
    plot2 = figure2.add_subplot(1, 4, 3)
    lr_x2 = []
    lr_y2 = []
    g_vxt = D_X_trajectory(k,x,m,g,p)
    plot2.set_title('vxt')
    lr_x2,lr_y2 = g_vxt.list_X_trajectory()
    plot2.plot(lr_x2, lr_y2)
    canvas2 = FigureCanvasTkAgg(figure2, win)
    canvas2.get_tk_widget().grid(row=0, column=2)

    figure3 = Figure(figsize=(w1, 2), dpi=100)
    plot3 = figure3.add_subplot(1, 4, 4)
    lr_x3 = []
    lr_y3 = []
    g_vyt = D_Y_trajectory(k,x,m,g,p)
    plot3.set_title('vyt')
    lr_x3,lr_y3 = g_vyt.list_Y_trajectory()
    plot3.plot(lr_x3, lr_y3)
    canvas3 = FigureCanvasTkAgg(figure3, win)
    canvas3.get_tk_widget().grid(row=0, column=3)
    
    # todo ---------------- 2
    figure4 = Figure(figsize=(10, 5), dpi=100)
    plot4 = figure4.add_subplot(111)
    lr_x4 = []
    lr_y4 = []
    lr_x4,lr_y4  = gxy(v,g)
    plot4.set_title('xy')
    plot4.set_xlabel('x')
    plot4.set_ylabel('y')
    plot4.plot(lr_x4, lr_y4)
    canvas4 = FigureCanvasTkAgg(figure4, win)
    canvas4.get_tk_widget().grid(row=1,column=0,columnspan=3,rowspan=2,stick= "nsew")
    #!--------------------------------- ออก
    figure5 = Figure(figsize=(2, 2), dpi=100)
    plot5 = figure5.add_subplot(111)
    lr_x5 = []
    lr_y5 = []
    lr_x5,lr_y5 = g_vyt.list_Y_trajectory()
    plot5.set_title('x')
    #! graph_xt ใช้
    #! r_x appendใน y
    #! r_x = self.v_x * t #!--------------เเปะในกราฟ x
    plot5.plot(lr_x5, lr_y5)
    canvas5 = FigureCanvasTkAgg(figure5, win)
    canvas5.get_tk_widget().grid(row=1, column=3,stick= "nsew")
    
    figure6 = Figure(figsize=(2, 2), dpi=100)
    plot6 = figure6.add_subplot(111)
    lr_x6 = []
    lr_y6 = []
    #! set x ,y = 0
    lr_x6,lr_y6 = g_vyt.list_Y_trajectory()
    plot6.set_title('y')
    plot6.plot(lr_x6, lr_y6)
    canvas6 = FigureCanvasTkAgg(figure6, win)
    canvas6.get_tk_widget().grid(row=2, column=3,stick= "nsew")
    #!---------------------------------ออก
def gxy(v=0,G=9.8):
    g = G
    V_initial4 = int(v)
    theta4 = (np.pi)/4
    v_x4 = V_initial4 * np.cos(theta4)
    v_y4 = V_initial4 * np.sin(theta4)
    time4 = np.linspace(0,100,10000)
    lr_x4 = []
    lr_y4 = []
    for t in time4:
        r_x = v_x4 * t
        r_y = (v_y4 * t) - 1/2 * g * (t ** 2)
        if r_y >= 0:
            lr_x4.append(r_x)
            lr_y4.append(r_y)
        else:
            break
    return lr_x4, lr_y4
#!----------------------------------------------
Dgraph(350,0.1,0.025,9.78,1.225)
# todo ---------------- 3
spring_distance = tk.Label(win,
    text="ระยะสปริง",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'center',
    height = 4,
    # bg="black",
)
spring_distance.grid(row=3, column=3,stick= "nsew")

Speed = tk.Label(win,
    text="ความเร็วต้น : 0 m/s",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'w',
    # bg="black",
)
Speed.grid(row=3, column=1)

Spring_recoil = tk.Label(win,
    text="ระยะหดสปริง : 0 cm",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'w',
    # bg="black",
)
Spring_recoil.grid(row=4, column=1)

spring_constant = tk.Label(win,
    text="ค่านิจสปริง : " + str(o_value("k")) +" N*m",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'w',
    # bg="black",
)
spring_constant.grid(row=5, column=1)

x_max = tk.Label(win,
    text="x สูงสุด : 0 m",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'w',
    # bg="black",
)
x_max.grid(row=3, column=2)

#!------------------------------
# def something():
#     text1 = input("text = ")
#     y_max.config(text=text1)

y_max = tk.Label(win,
    text="y สูงสุด : 0 m",
    fg="black",
    font = ("Helvetica",20),
    anchor= 'w',
    # bg="black",
)
y_max.grid(row=4, column=2)
#!------------------------------
def button_command():
    value_input = input_value.get()
    Spring_recoil.config(text="ระยะหดสปริง : "+str(abs(float(value_input)))+" cm")
    value_input = abs(float(value_input))
    value_input = value_input/100
    print(value_input)
    global value_i
    value_i = value_input
    k = float(o_value("k"))
    global D_ND
    D_ND = var1.get()
    # VT = (((k/2)*(value_input**2))-1.29*value_input)**0.5
    VT = (5.59*(k*(value_input**2)-2.48*value_input))**0.5
    if var1.get() == "ND":
        NDgraph(VT,float(o_value("g")))
        x,y = gxy(VT,float(o_value("g")))
        global X
        X = max(x)
        global Y
        Y = max(y)
        # print(max(x),max(y))
        # print(x,y)
        if(max(x) > int(o_value("x"))):
            x_max.config(fg="red")
        if(max(y) > int(o_value("y"))):
            y_max.config(fg="red")
        if(max(x) <= int(o_value("x")) ):
            x_max.config(fg="green")
        if(max(y) <= int(o_value("y"))):
            y_max.config(fg="green")
        Speed.config(text = "ความเร็วต้น : " + str(str('%.2f' %(VT))) +" m/s")
        y_max.config(text="y สูงสุด :" + str('%.2f' %(max(y))) + "m") #!เปลี่ยนเป็น cm
        x_max.config(text="x สูงสุด :" + str('%.2f' %(max(x))) + "m") #!เปลี่ยนเป็น cm
        input_value.delete(0, END)
    elif(var1.get() == "D"): #!---เเรงต้านอากาศ
        Dgraph(k,value_input,o_value("m"),o_value("g"),o_value("p"),VT)
        x,y = gxy(VT,float(o_value("g")))
        # print(max(x),max(y))
        # print(x,y)
        if(max(x) > int(o_value("x"))):
            x_max.config(fg="red")
        if(max(y) > int(o_value("y"))):
            y_max.config(fg="red")
        if(max(x) <= int(o_value("x")) ):
            x_max.config(fg="green")
        if(max(y) <= int(o_value("y"))):
            y_max.config(fg="green")
        Speed.config(text = "ความเร็วต้น : " + str(str('%.2f' %(VT))) +" m/s")
        y_max.config(text="y สูงสุด :" + str('%.2f' %(max(y))) + "m") #!เปลี่ยนเป็น cm
        x_max.config(text="x สูงสุด :" + str('%.2f' %(max(x))) + "m") #!เปลี่ยนเป็น cm
        input_value.delete(0, END)
    return None

def clicked(value):
    print(value)

var1 = StringVar()
var1.set("D")
rdt = True; #เลือกว่าเป็นปุ่มหรือไม่เอาปุ่ม True ไม่ปุ่ม False ปุ่ม
# Radiobutton(win,text="เเรงต้านอากาศ",variable=var1,value=1,command=lambda :print(var1.get())).grid(row=3, column=0)
Radiobutton(win,text="เเรงต้านอากาศ",indicatoron=rdt,variable=var1,value="D",command=lambda :clicked(var1.get())).grid(row=3, column=0)
Radiobutton(win,text="ไม่มีเเรงต้านอากาศ",indicatoron=rdt,variable=var1,value="ND",command=lambda :print(var1.get())).grid(row=4, column=0)

input_value = Entry(win, width=20)
input_value.grid(row=4, column=3)

photo = Image.open("start.png")
photo = photo.resize((80, 30))
photo = ImageTk.PhotoImage(photo)


Button(win, text="run",fg="blue",image=photo ,command=button_command).grid(row=5, column=3)

tk.Grid.columnconfigure(win, 0, weight=1)
tk.Grid.columnconfigure(win, 1, weight=1)
tk.Grid.columnconfigure(win, 2, weight=1)
tk.Grid.columnconfigure(win, 3, weight=1)
tk.Grid.rowconfigure(win, 1, weight=1)
tk.Grid.rowconfigure(win, 2, weight=2)
tk.Grid.rowconfigure(win, 3, weight=2)
tk.Grid.rowconfigure(win, 4, weight=0)
tk.Grid.rowconfigure(win, 5, weight=0)
tk.Grid.rowconfigure(win, 6, weight=0)
win.mainloop()