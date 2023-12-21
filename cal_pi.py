# 从同一文件夹中导入exp.py
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


def calculate_pi(self):
    master = self.master
    n = tk.StringVar()
    n.set("30000")

    label = tk.Label(master, text="随机点的数目n:")
    label.place(relx=0.3, rely=0.9, anchor="center")
    inp = tk.Entry(master, textvariable=n)
    inp.place(relx=0.5, rely=0.9, anchor="center")
    global c1, c2
    # 点击提交按钮后，获取输入框的值
    def submit():
        nVal = n.get()
        print("n =", nVal)
        c1,c2 = draw(int(nVal))


    but = tk.Button(master, text="开始演示", command=submit)
    but.place(relx=0.7, rely=0.9, anchor="center")


    def draw(n):
        radius = 1.0
        a,b = (0.,0.)
        # 设置正方形的边长
        x_left, x_right = (a-radius, a+radius)
        y_down, y_up = (b-radius, b+radius)
        # 在正方形区域内随机投点
        x = np.random.uniform(x_left, x_right, n)
        y = np.random.uniform(y_down, y_up, n)
        # 求平方根运算，计算点到圆心的距离，返回距离数组dis
        dis = np.sqrt((x-a)**2 + (y-b)**2)
        # 统计落在圆内的点的个数
        # count = sum(np.where(dis <= radius))
        count = np.sum(dis <= radius)
        # 计算圆周率的近似值
        pi = 4*count/n
        print("π = ", pi)
        c1=graph1(radius, a, b, x, y, x_left, x_right, y_down, y_up, n, count, pi)
        c2=graph2(np.pi, n, dis, radius)
        return c1, c2

    def graph1(radius, a, b, x, y, x_left, x_right, y_down, y_up, n, count, pi):
        # 用pyplot进行可视化
        fig = plt.figure()
        ax1=fig.add_subplot(111)
        ax1.set_title(f'蒙特卡洛算法估计的圆周率数值为：{pi:.4f}')
        # 更改标题字体为SimHei
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax1.plot(x, y, 'o', color= "orange", markersize=1, alpha=0.5)
        # 保持作图时正方形的边长相等
        plt.axis("equal")
        circle = Circle(xy=(a,b), radius=radius, alpha=0.5, color="blue")
        ax1.add_patch(circle)
        # 画出正方形的边界
        plt.plot([x_left, x_right], [y_up, y_up], color="orange")
        plt.plot([x_left, x_right], [y_down, y_down], color="orange")
        plt.plot([x_left, x_left], [y_up, y_down], color="orange")
        plt.plot([x_right, x_right], [y_up, y_down], color="orange")
        # 画出圆的边界
        theta = np.arange(0, 2*np.pi, 0.01)
        x1 = a + radius*np.cos(theta)
        y1 = b + radius*np.sin(theta)
        plt.plot(x1, y1, color="blue")

        legend_icon1 = Line2D([0], [0], marker='o', color='orange', label='生成随机点数目')
        legend_icon2 = Line2D([0], [0], marker='o', color='blue', label='落在圆内的随机点数目')
        legend_text1 = f'生成随机点数目 n={n}'
        legend_text2 = f'落在圆内的随机点数目 m={count}'
        plt.legend([legend_icon1, legend_icon2], [legend_text1, legend_text2], loc="upper right", fontsize=8, handlelength=0, borderpad=1, labelspacing=0.5)
        plt.xlim(-1,2)
        plt.ylim(-1,1)

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.465, rely=0.3, anchor="center")  # 调整相对位置
        canvas_widget.config(height=300, width=500)
        canvas.draw()
        return canvas

    def graph2(pi_theoretical, n, dis, radius):
        # 计算不同n值下对应的pi模拟值
        n_values = np.arange(1, n+1)
        pi_simulated_values = 4 * np.cumsum(dis <= radius) / n_values

        # 创建图表
        fig, ax2 = plt.subplots()
        # 设置字体为Simhei
        plt.rcParams['font.sans-serif']=['SimHei']
        ax2.set_title("蒙特卡洛算法估计的圆周率收敛性")
        ax2.set_xlabel("随机点数目 n")
        ax2.set_ylabel("估计的圆周率 π")

        # 绘制理论值的水平线
        ax2.axhline(y=pi_theoretical, color="green", label=f"π的理论值: 3.1415926", alpha=0.8)
        # 绘制模拟值的蓝色线
        ax2.plot(n_values, pi_simulated_values, color="blue", label=f"π的模拟计算值: {pi_simulated_values[-1]:.7f}", alpha=0.8)

        # 设置图例
        ax2.legend(loc="lower right", fontsize=8, handlelength=1, borderpad=1, labelspacing=0.5)

        plt.xlim(0, n)
        plt.ylim(2.9, 3.2)
        fig.tight_layout(pad=3)  # 调整布局，pad 可以根据需要调整

        # 显示图表
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.465, rely=0.7, anchor="center")  # 调整相对位置
        canvas_widget.config(height=250 , width=500)
        canvas.draw()
        return canvas

    c1,c2 = draw(30000)
    
    return c1, c2, label, inp, but