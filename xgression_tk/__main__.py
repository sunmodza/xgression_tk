from __future__ import annotations
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import secrets
import random as rd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import numpy as np

from xgression.xgression_lib import Xgression

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False) 
        self.variables = [Variable(self),Variable(self)]
        self.model_trainer = TrainerBox(self)
        self.process = None
        # configure the root window
        self.title('XGression')
        #self.geometry('300x300')

        # label
        self.add_variable = ttk.Button(self, text='Add')
        self.add_variable.grid(row = 0, column=0, sticky="news")
        self.add_variable.bind("<Button-1>",self.add_variable_box)

        self.execute_variable = ttk.Button(self, text='Execute')
        self.execute_variable.bind("<Button>",self.execute_model)
        self.execute_variable.grid(row = 0, column=1, sticky="news")

        self.showing_variable = True

        self.render_variable_box()

    def render_variable_box(self,*args):
        current_row = 1
        for i,widget in enumerate(self.variables):
            if (i+1) % 2 == 0:
                widget.grid(padx=2,pady=6,columnspan=1,row = current_row, column=1)
                current_row += 1
            else:
                widget.grid(padx=2,pady=6,columnspan=1,row = current_row, column=0)

        #self.vb = Variable(self)
        #self.vb.grid(padx=2,pady=6,columnspan=2)

        #self.vb2 = Variable(self)
        #self.vb2.grid(padx=2,pady=6,columnspan=2)

    def add_variable_box(self,*args):
        self.variables.append(Variable(self))
        self.render_variable_box()

    def execute_model(self,*args):
        if self.showing_variable:
            self.execute_variable["text"] = "Stop"
            for v in self.variables:
                v.grid_forget()
            
            self.model_trainer.stop_process = False
            # begin trainer box
            self.model_trainer.grid(columnspan=2, sticky="news")
            self.model_trainer.setup_model(self.variables)
        else:
            self.execute_variable["text"] = "Execute"
            self.model_trainer.grid_forget()
            self.model_trainer.stop_process = True
            self.render_variable_box()

        self.showing_variable = not self.showing_variable

class TrainerBox(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.stop_process = True
        
        self.equation_label = ttk.Entry(self,text="Noob SADISAJDAS)ODOJIEAFI")
        self.equation_label.pack(expand=True, fill=tk.BOTH)
        """
        self.error_label = ttk.Label(self,text = f"Error = {3.0}",width=54)
        self.error_label.pack()
        
        self.canvas = FigureCanvasTkAgg(None, master=self)
        """
        self.canvas = FigureCanvasTkAgg(None, master=self)

    def setup_model(self,variables : Variable):
        y = None
        x = {}
        y_name = None
        for i,v in enumerate(variables):
            if i == 0:
                y_name,y = v.get_variable()
            else:
                x_name,x_value = v.get_variable()

                x[x_name] = x_value

        self.process = threading.Thread(target=lambda *args :self.handle_model(x,y,y_name))
        self.process.start()

    def handle_model(self,x,y,y_name):
        plt.switch_backend('agg')
        self.model = Xgression(x,y,y_name)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        best_dist = 999999999999999
        while not self.stop_process:
            try:
                dist = self.model.iteration()
                if dist < best_dist:
                    best_dist = dist
                    #print(dist,self.model.get_equation())
                    self.model.show_unpause()
                    self.canvas.figure = self.model.fig
                    self.equation_label.delete(0, tk.END)
                    self.equation_label.insert(0, self.model.get_equation())
                    self.canvas.draw()
            except Exception as e:
                print(e)
                pass


class Variable(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.id = secrets.randbits(8)
        self.parent = master

        self.variable_name_label = ttk.Label(self, text="Name")
        self.variable_name_label.grid(row=0,column=0)

        self.variable_name_entry = ttk.Entry(self)
        self.variable_name_entry.grid(row=0,column=1)



        self.text_area = scrolledtext.ScrolledText(self, width=15, height=10, wrap=tk.WORD)

        self.text_area.grid(row=1,column=0,columnspan=2,padx=1,pady=3)

        self.del_button = ttk.Button(self,text="Delete")
        self.del_button.grid(row=2,column=0,columnspan=2)

        def del_this(x):
            for i,v in enumerate(self.parent.variables):
                if v == self:
                    #print(v)
                    v.destroy()
                    self.parent.variables.pop(i)
            self.parent.render_variable_box()

        self.del_button.bind(f"<Button>",del_this)

    def get_variable(self):
        text = self.text_area.get('1.0', 'end-1c')
        lines = [float(i) for i in re.split(r'[\n,; , ]', text)]
        return self.variable_name_entry.get(), np.array(lines)

app = App()
app.mainloop()