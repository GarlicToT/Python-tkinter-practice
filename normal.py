# 绘制正态分布图像的函数
import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from scipy.stats import norm


def normal(self):
    master = self.master

    # 接受用户输入的均值和方差
    mean_var = tk.StringVar()
    mean_var.set("0")  # Set the initial value to 0
    label1 = tk.Label(master, text="均值μ=")
    label1.place(relx=0.1, rely=0.9, anchor="center")
    mean_inp = tk.Entry(master, textvariable=mean_var)
    mean_inp.place(relx=0.28, rely=0.9, anchor="center")
    sq_var = tk.StringVar()
    sq_var.set("1")  # Set the initial value to 1
    label2 = tk.Label(master, text="方差σ²=")
    label2.place(relx=0.5, rely=0.9, anchor="center")
    sq_inp = tk.Entry(master, textvariable=sq_var)
    sq_inp.place(relx=0.68, rely=0.9, anchor="center")
    # 点击提交按钮后，获取输入框的值
    global c1
    def submit():
        mean = mean_var.get()
        sq = sq_var.get()
        print("μ =", mean, "σ² =", sq)
        c1 = draw(float(mean), float(sq))
        
    but = tk.Button(master, text="开始演示", command=submit)
    but.place(relx=0.8, rely=0.9, anchor="center")

    def draw(mean,sq):
        x = np.arange(mean-sq*3.8, mean+sq*4, 0.01)
        y = norm.pdf(x, mean, sq)
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.set_title(f'正态分布概率密度图')
        # 更改标题字体为SimHei
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax1.plot(x, y, color="orange", alpha=0.5)
        plt.vlines(mean, 0, norm.pdf(mean, mean, sq), colors='red', linestyle='dashed', alpha=0.3, linewidth=2.0)
        plt.vlines(mean+sq, 0, norm.pdf(mean+sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        plt.vlines(mean-sq, 0, norm.pdf(mean-sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        plt.vlines(mean+2*sq, 0, norm.pdf(mean+2*sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        plt.vlines(mean-2*sq, 0, norm.pdf(mean-2*sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        plt.vlines(mean+3*sq, 0, norm.pdf(mean+3*sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        plt.vlines(mean-3*sq, 0, norm.pdf(mean-3*sq, mean, sq), colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        
        legend_icon1 = Line2D([0], [0], color='orange', label='正态分布')
        legend_text1 = f'正态分布 μ={mean} $\sigma^2$={sq}'
        plt.legend(handles=[legend_icon1], labels=[legend_text1], loc='upper right')    
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.465, rely=0.3, anchor="center")  # 调整相对位置
        canvas_widget.config(height=300, width=500)
        canvas.draw()
        return canvas

    c1 = draw(0,1)
    return c1, mean_inp, sq_inp, but, label1, label2