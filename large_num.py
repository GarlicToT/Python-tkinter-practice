import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from scipy.stats import norm


def law_of_large_numbers(self):
    master = self.master
    
    peoplenum_var = tk.StringVar()
    peoplenum_var.set("200")  # Set the initial value to 100
    label1 = tk.Label(master, text="样本容量n=")
    label1.place(relx=0.1, rely=0.9, anchor="center")
    peoplenum_inp = tk.Entry(master, textvariable=peoplenum_var)
    peoplenum_inp.place(relx=0.28, rely=0.9, anchor="center")
    expect_var = tk.StringVar()
    expect_var.set("85")  # Set the initial value to 0
    label2 = tk.Label(master, text="数学期望μ=")
    label2.place(relx=0.38, rely=0.9, anchor="center")
    expect_inp = tk.Entry(master, textvariable=expect_var)
    expect_inp.place(relx=0.56, rely=0.9, anchor="center")
    sq_var = tk.StringVar()
    sq_var.set("4")  # Set the initial value to 1
    label3 = tk.Label(master, text="方差σ²=")
    label3.place(relx=0.6, rely=0.9, anchor="center")
    sq_inp = tk.Entry(master, textvariable=sq_var)
    sq_inp.place(relx=0.76, rely=0.9, anchor="center")
    # 点击提交按钮后，获取输入框的值
    global c1
    def submit():
        peoplenum = peoplenum_var.get()
        expect = expect_var.get()
        sq = sq_var.get()
        print("n =", peoplenum, "μ =", expect, "σ² =", sq)
        c1 = draw(int(peoplenum), float(expect), float(sq))
    but = tk.Button(master, text="开始演示", command=submit)
    but.place(relx=0.83, rely=0.9, anchor="center")


    def draw(sampSize, exp, sq):
        sampY = np.random.normal(exp, sq, sampSize)
        x = np.arange(0, sampSize, 1)
        y = np.cumsum(sampY) / (x + 1)
        
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.set_title(f'大数定律验证')
        # 更改标题字体为SimHei
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax1.plot(x, y, color="orange", linewidth=1.6, alpha=1)
        ax1.plot(x, sampY, 'o', color="blue", markersize=1.2, alpha=0.5)
        plt.hlines(exp, 0, sampSize, colors='red', linestyle='dashed', alpha=0.8, linewidth=2)
        for i, xi in enumerate(x):
            plt.vlines(xi, 0, sampY[i], colors='blue', linestyle='solid', alpha=0.2, linewidth=0.8)
        
        legend_icon1 = Line2D([0], [0], color='orange', linewidth=1, label='前n项均值')
        legend_icon2 = Line2D([0], [0], marker='o', color='blue', markersize=2, linestyle='', label='评委打分')
        legend_icon3 = Line2D([0], [0], color='red', linestyle='dashed', linewidth=1, label='数学期望')

        plt.legend(handles=[legend_icon1, legend_icon2, legend_icon3], loc='upper right')

        plt.ylim(exp-1.2*sq, exp+1.4*sq)
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.465, rely=0.3, anchor="center")  # 调整相对位置
        canvas_widget.config(height=300, width=500)
        canvas.draw()
        return canvas
    c1 = draw(200, 85, 4)
    return c1, label1, peoplenum_inp, label2, expect_inp, label3, sq_inp, but