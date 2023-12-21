import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from scipy.stats import binom
from scipy.stats import poisson as poisson_stats

# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def poisson(self):
    master = self.master
    lambda_var = tk.StringVar()
    lambda_var.set("5")  # Set the initial value to 5
    n = 20

    label=tk.Label(master, text="参数（请输入4~15之间的数）λ=")
    label.place(relx=0.3, rely=0.9, anchor="center")
    inp = tk.Entry(master, textvariable=lambda_var)
    inp.place(relx=0.6, rely=0.9, anchor="center")
    global c1
    # 点击提交按钮后，获取输入框的值
    def submit():
        lambd = lambda_var.get()
        print("λ =", lambd)
        c1 = draw(int(lambd), n)

    but = tk.Button(master, text="开始演示", command=submit)
    but.place(relx=0.75, rely=0.9, anchor="center")

    # initial_lambda = 5
    # lambda_var.set(str(initial_lambda))  # Set the initial value

    def draw(lambd, n):
        x = np.arange(0, n, 1)
        y = poisson_stats.pmf(x, lambd)
        # 生成二项分布的随机数
        p = lambd/n
        y1 = binom.pmf(x, n, p)
        # 画图
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.set_title(f'泊松分布和二项分布的对比')
        # 更改标题字体为SimHei
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax1.plot(x, y, 'o', color="orange", markersize=2.4, alpha=0.5)
        ax1.plot(x, y1, 'o', color="blue", markersize=2.4, alpha=0.5)
    
        for i, xi in enumerate(x):
            plt.vlines(xi, 0, y1[i], colors='blue', linestyle='solid', alpha=0.3, linewidth=1.6)
        for i, xi in enumerate(x):
            plt.vlines(xi, 0, y[i], colors='orange', linestyle='solid', alpha=0.3, linewidth=1.6)

        legend_icon1 = Line2D([0], [0], marker='o', color='orange', label='泊松分布')
        legend_icon2 = Line2D([0], [0], marker='o', color='blue', label='二项分布')
        legend_text1 = f'泊松分布 λ={lambd}'
        legend_text2 = f'二项分布 n={n} p={p}'
        plt.legend(handles=[legend_icon1, legend_icon2], labels=[legend_text1, legend_text2])

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.465, rely=0.3, anchor="center")  # 调整相对位置
        canvas_widget.config(height=300, width=500)
        canvas.draw()
        return canvas

    c1 = draw(5, 20)
    return c1, label, inp, but