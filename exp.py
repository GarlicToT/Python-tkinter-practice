'''实验任务
(1)采用可视化设计，有菜单界面。

(2)利用蒙特卡洛方法计算圆周率并展示结果。

(3)验证泊松定理并展示，对于泊松分布固定的，随着二项分布n的增加，二项分布逐渐收敛于泊松分布。

(4)给定参数μ和σ，展示对应的正态分布概率密度图；通过动态调整参数μ或σ，展示图像的变化。

(5)生成正态分布的样本，验证大数定律。画图展示随着样本容量的增加，随机变量的算术平均依概率收敛到数学期望。


3. 实验设备及环境
开发环境：Python 3.10(tkinter)  + Numpy + Scipy + matlibplot'''

import tkinter as tk
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt

class MCSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("My Experiment")

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()
        
        self.menu = tk.Menu(self.menu_frame, font=("黑体",12))
        self.master.config(menu=self.menu)

        self.canvas = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack()
        # self.pi_label = tk.Label(self.master, text=" π = ", font=("", 20))
        # self.pi_label.pack()
        
        self.create_menu()

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
        num = simpledialog.askinteger("Input", "Enter the number of points:")
        points_in_circle = 0

        for _ in range(num):
            x,y = np.random.uniform(0,1,2)
            distance = np.sqrt((x-0.5)**2 + (y-0.5)**2)

            if distance <= 0.5:
                points_in_circle += 1
                self.canvas.create_oval(x*500-1, y*500-1, x*500+1, y*500+1, fill="red")

            else:
                self.canvas.create_oval(x*500-1, y*500-1, x*500+1, y*500+1, fill="blue")

        pi = 4*points_in_circle / num
        self.pi_label.config(text="Pi = {:.4f}".format(pi))

    def poisson(self):
        pass

    def normal(self):
        pass

    def law_of_large_numbers(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MCSimulation(root)
    root.mainloop()
