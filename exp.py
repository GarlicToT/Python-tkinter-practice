import tkinter as tk
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class MCSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("My Experiment")
        
        self.menu = tk.Menu(self.master, font=("黑体",12))
        self.master.config(menu=self.menu)

        self.canvas = tk.Canvas(self.master, width=500, height=500, bg="white")
        self.canvas.pack()
        self.pi_label = tk.Label(self.master, text=" π = ", font=("", 20))
        self.pi_label.pack()
        self.pi_label.pack_forget()

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
        # 接受用户输入随机点的个数n
        n = simpledialog.askinteger("输入", "请输入随机点的个数n：", initialvalue=30000)
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
        ax1.plot(x, y, 'ro', color= "orange", markersize=1, alpha=0.5)
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
        legend_text = f'生成随机点数目 n= {n}\n落在圆内的随机点数目 m= {count}'
        plt.legend([legend_text], loc="upper right", fontsize=8)
        plt.xlim(-1.5,2.5)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().place(x=0, y=0)
        canvas.draw()

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