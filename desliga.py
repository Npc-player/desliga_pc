#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.1
#  in conjunction with Tcl version 8.6
#    Jun 02, 2020 12:48:42 AM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import subprocess
import webbrowser

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.update()
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def bt_30s(self, tempo=''):
        subprocess.call('shutdown -a')
        subprocess.call('shutdown -s -t 1800')
        self.cancel()
        bt = 30
        self.Label2.configure(text='DESLIGANDO EM\n'+str(bt)+' MINUTOS')
        self.Label2.configure(background='red')
        self.setarlabel(bt)

    def bt_1hora(self, tempo=''):
        subprocess.call('shutdown -a')
        subprocess.call('shutdown -s -t 3600')
        self.cancel()
        bt = 60
        self.Label2.configure(text='DESLIGANDO EM\n'+str(bt)+' MINUTOS')
        self.Label2.configure(background='red')
        self.setarlabel(bt)

    def bt_2horas(self, tempo=''):
        subprocess.call('shutdown -a')
        subprocess.call('shutdown -s -t 7200')
        self.cancel()
        bt = 120
        self.Label2.configure(text='DESLIGANDO EM\n' + str(bt)+' MINUTOS')
        self.Label2.configure(background='red')
        self.setarlabel(bt)

    def setarlabel(self, value=''):
        self.Label2.configure(text='DESLIGANDO EM\n' + str(value)+' MINUTOS')
        self.Label2.configure(background='red')
        value = value - 1
        self.para_after = self.Label2.after(60000, self.setarlabel, value)

    def cancel(self):
        if self.para_after is not None:
            self.Label2.after_cancel(self.para_after)
            self.para_after = None

    def bt_cancela(self):
        subprocess.call('shutdown -a')
        self.cancel()
        self.Label2.after_cancel(self.Label2)
        self.Label2.configure(text='CANCELADO')
        self.Label2.configure(background='red')

    def doar(self):
        webbrowser.open('https://www.paypal.com/donate?hosted_button_id=Y4WAV3LSWMVMU')

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 13 -weight bold"
        font9 = "-family {Segoe UI} -size 22 -weight bold"

        top.geometry("353x450")
        top.minsize(120, 1)
        top.maxsize(1370, 1517)
        top.resizable(1, 1)
        top.title("Desliga PC")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.184, rely=0.018, height=21, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''DESLIGAR COMPUTADOR''')

        self.Button_30S = tk.Button(top)
        self.Button_30S.place(relx=0.034, rely=0.111, height=64, width=328)
        self.Button_30S.configure(activebackground="#ececec")
        self.Button_30S.configure(activeforeground="#000000")
        self.Button_30S.configure(background="#00ff80")
        self.Button_30S.configure(disabledforeground="#a3a3a3")
        self.Button_30S.configure(font=font9)
        self.Button_30S.configure(foreground="#000000")
        self.Button_30S.configure(highlightbackground="#d9d9d9")
        self.Button_30S.configure(highlightcolor="black")
        self.Button_30S.configure(command=self.bt_30s)
        self.Button_30S.configure(pady="0")
        self.Button_30S.configure(text='''30 MINUTOS''')

        self.Button_1_HORA = tk.Button(top)
        self.Button_1_HORA.place(relx=0.034, rely=0.267, height=64, width=328)
        self.Button_1_HORA.configure(activebackground="#ececec")
        self.Button_1_HORA.configure(activeforeground="#000000")
        self.Button_1_HORA.configure(background="#ff0080")
        self.Button_1_HORA.configure(disabledforeground="#a3a3a3")
        self.Button_1_HORA.configure(font=font9)
        self.Button_1_HORA.configure(foreground="#000000")
        self.Button_1_HORA.configure(highlightbackground="#d9d9d9")
        self.Button_1_HORA.configure(highlightcolor="black")
        self.Button_1_HORA.configure(pady="0")
        self.Button_1_HORA.configure(text='''1 HORA''')
        self.Button_1_HORA.configure(command=self.bt_1hora)

        self.Button_2_horas = tk.Button(top)
        self.Button_2_horas.place(relx=0.034, rely=0.422, height=64, width=328)
        self.Button_2_horas.configure(activebackground="#ececec")
        self.Button_2_horas.configure(activeforeground="#000000")
        self.Button_2_horas.configure(background="#0080c0")
        self.Button_2_horas.configure(disabledforeground="#a3a3a3")
        self.Button_2_horas.configure(font=font9)
        self.Button_2_horas.configure(foreground="#000000")
        self.Button_2_horas.configure(highlightbackground="#d9d9d9")
        self.Button_2_horas.configure(highlightcolor="black")
        self.Button_2_horas.configure(pady="0")
        self.Button_2_horas.configure(text='''2 HORAS''')
        self.Button_2_horas.configure(command=self.bt_2horas)

        self.Button_cancela = tk.Button(top)
        self.Button_cancela.place(relx=0.283, rely=0.822, height=34, width=138)
        self.Button_cancela.configure(activebackground="#ececec")
        self.Button_cancela.configure(activeforeground="#000000")
        self.Button_cancela.configure(background="#f5010a")
        self.Button_cancela.configure(disabledforeground="#a3a3a3")
        self.Button_cancela.configure(font=font9)
        self.Button_cancela.configure(foreground="#000000")
        self.Button_cancela.configure(highlightbackground="#d9d9d9")
        self.Button_cancela.configure(highlightcolor="black")
        self.Button_cancela.configure(pady="0")
        self.Button_cancela.configure(text='''cancela''')
        self.Button_cancela.configure(command=self.bt_cancela)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.034, rely=0.6, height=71, width=328)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")

# instancia para cancelamento do loop .after
        self.para_after = tk.Label(top)

        self.bt_doar = tk.Button(top)
        self.bt_doar.place(relx=0.623, rely=0.962, height=14, width=47)
        self.bt_doar.configure(activebackground="#ececec")
        self.bt_doar.configure(activeforeground="#000000")
        self.bt_doar.configure(background="#d9d9d9")
        self.bt_doar.configure(disabledforeground="#a3a3a3")
        self.bt_doar.configure(foreground="#000000")
        self.bt_doar.configure(highlightbackground="#d9d9d9")
        self.bt_doar.configure(highlightcolor="black")
        self.bt_doar.configure(pady="0")
        self.bt_doar.configure(text='''Doar''')
        self.bt_doar.configure(command=self.doar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0, rely=0.956, height=21, width=144)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Curtiu? Considere doar!''')

if __name__ == '__main__':
    vp_start_gui()
