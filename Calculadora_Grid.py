import tkinter as tk

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Prueba posicionamiento con PLACE")
ventanaPrincipal.geometry('300x300')



btn1 = tk.Button(ventanaPrincipal, text= "+/-",width=5,height=2)
btn1.grid(row=9,column=0)

btn2 = tk.Button(ventanaPrincipal, text= "0",width=5,height=2)
btn2.grid(row=9,column=1)

btn3 = tk.Button(ventanaPrincipal, text= ".",width=5,height=2)
btn3.grid(row=9,column=2)

btn4 = tk.Button(ventanaPrincipal, text= "=",width=5,height=2)
btn4.grid(row=9,column=3)
#================
btn5 = tk.Button(ventanaPrincipal, text= "1",width=5,height=2)
btn5.grid(row=8,column=0)

btn6 = tk.Button(ventanaPrincipal, text= "2",width=5,height=2)
btn6.grid(row=8,column=1)

btn7 = tk.Button(ventanaPrincipal, text= "3",width=5,height=2)
btn7.grid(row=8,column=2)

btn8 = tk.Button(ventanaPrincipal, text= "+",width=5,height=2)
btn8.grid(row=8,column=3)

#=============================

btn9 = tk.Button(ventanaPrincipal, text= "4",width=5,height=2)
btn9.grid(row=7,column=0)

btn10 = tk.Button(ventanaPrincipal, text= "5",width=5,height=2)
btn10.grid(row=7,column=1)

btn11 = tk.Button(ventanaPrincipal, text= "6",width=5,height=2)
btn11.grid(row=7,column=2)

btn12 = tk.Button(ventanaPrincipal, text= "-",width=5,height=2)
btn12.grid(row=7,column=3)
#==============
btn13 = tk.Button(ventanaPrincipal, text= "7",width=5,height=2)
btn13.grid(row=6,column=0)

btn14 = tk.Button(ventanaPrincipal, text= "8",width=5,height=2)
btn14.grid(row=6,column=1)

btn15 = tk.Button(ventanaPrincipal, text= "9",width=5,height=2)
btn15.grid(row=6,column=2)

btn16 = tk.Button(ventanaPrincipal, text= "X",width=5,height=2)
btn16.grid(row=6,column=3)

##?=============
btn17 = tk.Button(ventanaPrincipal, text= "1/x",width=5,height=2)
btn17.grid(row=5,column=0)

btn18 = tk.Button(ventanaPrincipal, text= "x^2",width=5,height=2)
btn18.grid(row=5,column=1)

btn19 = tk.Button(ventanaPrincipal, text= "SQRT",width=5,height=2)
btn19.grid(row=5,column=2)

btn20 = tk.Button(ventanaPrincipal, text= "/",width=5,height=2)
btn20.grid(row=5,column=3)

#========================
btn21 = tk.Button(ventanaPrincipal, text= "%",width=5,height=2)
btn21.grid(row=4,column=0)

btn22 = tk.Button(ventanaPrincipal, text= "CE",width=5,height=2)
btn22.grid(row=4,column=1)

btn23 = tk.Button(ventanaPrincipal, text= "C",width=5,height=2)
btn23.grid(row=4,column=2)

btn24 = tk.Button(ventanaPrincipal, text= "<x|",width=5,height=2)
btn24.grid(row=4,column=3)
#=========================

panel= tk.Frame(ventanaPrincipal, bg='grey',width=200)
panel.grid(row=3,column=0,columnspan=5)
btn21 = tk.Button(panel, text= "MC",width=2,height=1)
btn21.grid(row=0,column=0)

btn22 = tk.Button(panel, text= "MR",width=2,height=1)
btn22.grid(row=0,column=1)

btn23 = tk.Button(panel, text= "M+",width=2,height=1)
btn23.grid(row=0,column=2)

btn24 = tk.Button(panel, text= "M-",width=2,height=1)
btn24.grid(row=0,column=3)

btn24 = tk.Button(panel, text= "M^",width=2,height=1)
btn24.grid(row=0,column=4)
#=============

cajaMantisa = tk.Entry(ventanaPrincipal)
cajaMantisa.grid(row=1,column=0,rowspan=2,columnspan=5)

ventanaPrincipal.mainloop()