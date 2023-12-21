import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from cal_pi import calculate_pi
from large_num import law_of_large_numbers
from normal import normal
from poisson import poisson


class Experiment:
    def __init__(self, master):
        self.components = []
        self.master = master
        self.master.title("My Experiment")
        self.master.geometry("600x700")
        self.master.configure(bg="white")
        
        self.menu = tk.Menu(self.master, font=("黑体",12))
        self.master.config(menu=self.menu)

        self.pi_frame = tk.Frame(self.master)  # 创建 Frame 用于显示π的图表
        self.pi_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        self.canvas = tk.Canvas(self.master, width=500, height=800, bg="white")
        self.canvas.pack()
        self.pi_label = tk.Label(self.master, text=" π = ", font=("", 20))
        self.pi_label.pack()
        self.pi_label.pack_forget()

        self.create_menu()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self):
        # Create a menu
        mc_menu = tk.Menu(self.menu, font=("黑体",10))
        self.menu.add_cascade(label="蒙特卡洛算法", menu=mc_menu)
        p_menu = tk.Menu(self.menu, font=("黑体",10))
        self.menu.add_cascade(label="泊松分布", menu=p_menu)
        n_menu = tk.Menu(self.menu, font=("黑体",10))
        self.menu.add_cascade(label="正态分布", menu=n_menu)
        c_menu = tk.Menu(self.menu, font=("黑体",10))
        self.menu.add_cascade(label="大数定律", menu=c_menu)

        # Add menu items
        mc_menu.add_command(label="计算圆周率", command=self.calculate_pi)
        p_menu.add_command(label="验证泊松定理", command=self.poisson)
        n_menu.add_command(label="正态分布概率密度图", command=self.normal)
        c_menu.add_command(label="验证大数定律", command=self.law_of_large_numbers)

    # 用蒙特卡洛方法计算圆周率
    
    def calculate_pi(self):
        for component in self.components:
            if isinstance(component, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
                component.get_tk_widget().destroy()
                self.components.remove(component)
            else:
                component.destroy()
                self.components.remove(component)
        comp_list = list(calculate_pi(self))
        
        self.components.extend(comp_list)

    def poisson(self):
        for component in self.components:
            if isinstance(component, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
                component.get_tk_widget().destroy()
                self.components.remove(component)
            else:
                component.destroy()
                self.components.remove(component)
        comp_list = list(poisson(self))
        self.components.extend(comp_list)

    def normal(self):
        for component in self.components:
            if isinstance(component, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
                component.get_tk_widget().destroy()
                self.components.remove(component)
            else:
                component.destroy()
                self.components.remove(component)
        comp_list = list(normal(self))
        self.components.extend(comp_list)

    def law_of_large_numbers(self):
        for component in self.components:
            if isinstance(component, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
                component.get_tk_widget().destroy()
                self.components.remove(component)
            else:
                component.destroy()
                self.components.remove(component)
        comp_list = list(law_of_large_numbers(self))
        self.components.extend(comp_list)

    def on_closing(self):
        plt.close('all')
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Experiment(root)
    root.mainloop()