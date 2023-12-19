# 从同一文件夹中导入exp.py
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


def calculate_pi(master):
        # 接受用户输入随机点的个数n
        n = simpledialog.askinteger("输入", "请输入随机点的个数n：", initialvalue=30000)
        # tk.Entry(self.master, textvariable="123").pack()
        # 设置圆的半径和圆心
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

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0.5, rely=0.5, anchor="center")  # 让图居中显示
        canvas_widget.config(height=400, width=600)
        canvas.draw()   

def graph1():
    pass