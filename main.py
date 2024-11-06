# coding=gbk
# 2024/8/13将城市的判断方法统一封装，省了几百行
# 2024/11/6将判断方法封装，又省了几百行
import random
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image, ImageFile
from tkinter import ttk
from tkinter.messagebox import *
import numpy as np
from tkinter.simpledialog import askfloat, askinteger, askstring
import matplotlib.pyplot as plt
import time

# 第一部分：进入页面的设计
开始页面 = tk.Tk()
开始页面.geometry("500x600")

开始页面state = 0
开始页面.方格1a = Image.open("游戏图片/大富翁封面.png")  # 括号里为需要显示在图形化界面里的图片
开始页面.方格1a = 开始页面.方格1a.resize((500, 600))  # 规定图片大小
开始页面.方格1b = ImageTk.PhotoImage(开始页面.方格1a)
开始页面.方格1c = ttk.Label(image=开始页面.方格1b)
开始页面.方格1c.place(x=0, y=0)


def 退出():
    quit()


class 图片按钮:
    def __init__(开始页面, 路径, 位置, 大小, 方法):
        开始页面.路径 = 路径
        开始页面.位置 = 位置
        开始页面.大小 = 大小
        开始页面.lst = []
        开始页面.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        开始页面.方格1a = 开始页面.方格1a.resize((大小[0], 大小[1]))  # 规定图片大小
        开始页面.方格1b = ImageTk.PhotoImage(开始页面.方格1a)
        开始页面.方格1c = tk.Button(image=开始页面.方格1b, command=方法)
        开始页面.lst.append(开始页面.方格1c)
        开始页面.lst[-1].place(x=位置[0], y=位置[1])
global ai_
ai_=[]
def 开始游戏1():
    global 开始页面state,ai_
    开始页面.destroy()
    开始页面state = 1
    ai_=[0,0,1,1,1]
def 开始游戏2():
    global 开始页面state,ai_
    开始页面.destroy()
    开始页面state = 1
    ai_ = [0, 0, 0, 1, 1]
def 开始游戏3():
    global 开始页面state,ai_
    开始页面.destroy()
    开始页面state = 1
    ai_ = [0, 0, 0, 0, 0]
开始游戏按钮1 = 图片按钮("游戏图片/单人游戏.png", (50, 200), (120, 60), 开始游戏1)
开始游戏按钮2 = 图片按钮("游戏图片/双人游戏.png", (50, 275), (120, 60), 开始游戏2)
开始游戏按钮3 = 图片按钮("游戏图片/四人游戏.png", (50, 350), (120, 60), 开始游戏3)
退出游戏按钮 = 图片按钮("游戏图片/退出游戏.png", (330, 350), (120, 60), 退出)
开始页面.mainloop()
if 开始页面state == 0:
    quit()

# 1200x600,每行10个格，每列5个格，每个格120*120
root = tk.Tk()
root.geometry("1600x750")  # 长乘宽
w1 = Canvas(root, width=1200, height=650, background='blue')
w1.place(x=0, y=0)

# 初始化金钱
global money
money = [0, 1200, 1200, 1200, 1200]  # 还是用列表来存储吧
玩家1金钱记录 = [money[1]]
玩家2金钱记录 = [money[2]]
玩家3金钱记录 = [money[3]]
玩家4金钱记录 = [money[4]]
global 破产, 破产人数
破产人数 = 0
破产 = [1, 0, 0, 0, 0]  # 定义破产状态
global 玩家事件
玩家事件 = []
for _ in range(5):
    玩家事件.append([])
玩家事件[1] = []
玩家事件[2] = []
玩家事件[3] = []
玩家事件[4] = []


class 根按钮:
    def __init__(root, x, y, 文本):
        root.文本 = 文本
        root.x = x
        root.y = y
        root.子结点 = []
        root.state = 0
        global y0
        y0 = y

        def 展示子按钮():
            global bt, 按钮序号
            if len(bt) == 0:  # bt是按钮的栈，当栈为空，说明没有按钮被展开
                root.state = 0  # 按钮的state表示的是按钮是否已经被按下过（state=0时，点击按钮会展开，state=1时会折叠）
            else:
                按钮序号 = 0  # 按钮序号用来标记按钮，方便入栈出栈
            if root.state == 0:
                if len(bt) > 0:  # 当有别的根按钮处于展开状态，清空，这样保证界面整洁
                    for _ in range(len(bt)):
                        bt[_][1].destroy()
                bt.clear()
                for _ in range(len(root.子结点)):  # 遍历展开自己的子节点
                    按钮序号 += 1
                    root.子结点[_].x = x
                    root.子结点[_].y = 27 * _ + 30  # 给子节点好的位置，方便查看
                    root.子结点[_].序号 = 按钮序号
                    if len(root.子结点[_].子结点) > 0:
                        root.子结点[_].文字 += ">"
                    root.子结点[_].文字 = root.子结点[_].文字.ljust(20, " ")  # 设置子节点
                    b = tk.Button(text=root.子结点[_].文字, command=root.子结点[_].方法)  # 为子节点传参
                    bt.append((按钮序号, b))  # 入栈，并放置子节点
                    bt[-1][1].place(x=root.x, y=27 * _ + 30)
                root.state += 1
                # print(root.x)
            elif root.state == 1:  # state=1意思是再点击就折叠
                按钮序号 = 0  # 重置按钮序号参数，这样可以重复展开
                for _ in root.子结点:  # 让子节点都重置为没被点击的状态
                    _.state = 0
                for _ in range(len(bt)):  # 读栈，从栈中移除子按钮，达到折叠的效果
                    bt[-1 - _][1].destroy()
                root.state = 0

                bt.clear()  # 清空栈，为下次展开准备
                # print(bt)

        root.按钮 = tk.Button(text=文本 + ">", command=展示子按钮, height=1)
        root.按钮.place(x=x, y=y)


class 子按钮:
    def __init__(root, 文字, 根按钮, 方法):
        root.文字 = 文字
        root.方法 = 方法
        root.子结点 = []
        root.state = 0
        root.x = 0
        root.y = 0
        root.序号 = 0

        def 展示子按钮():
            global bt, 按钮序号
            if root.序号 == 0:
                按钮序号 += 1  # 用序号来标记自身，方便管理栈
                root.序号 = 按钮序号
            if root.序号 == len(bt):
                root.state = 0  # 重置子按钮
            if root.state == 0:
                for _ in range(len(root.子结点)):
                    root.子结点[_].x = root.x + 80  # 子按钮位置，让子按钮和父按钮错开
                    root.子结点[_].y = root.y + _ * 27  # 子按钮位置，让子按钮和父按钮错开
                    b = tk.Button(text=root.子结点[_].文字, command=root.子结点[_].方法)  # 传入子按钮方法
                    bt.append((按钮序号, b))  # 用栈存储子按钮方便管理
                    bt[-1][1].place(x=root.x + 100, y=root.y + _ * 27)
                root.state += 1  # 展开后，再点击就变成折叠状态
            elif root.state == 1:
                for _ in root.子结点:
                    _.state = 0
                要减去的按钮数量 = len(bt) - root.序号  # 意思是把自己的子按钮都折叠了，但自身和自身的父按钮都不折叠
                for _ in range(要减去的按钮数量):
                    bt[-1][1].destroy()  # 读栈，去掉子按钮
                    bt.pop()  # 出栈
                root.state = 0  # 重置按钮

        if root.方法 == None:
            root.方法 = 展示子按钮
        根按钮.子结点.append(root)


class 图片按钮:
    def __init__(root, 路径, 位置, 大小, 方法):
        root.路径 = 路径
        root.位置 = 位置
        root.大小 = 大小
        root.lst = []
        root.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        root.方格1a = root.方格1a.resize((大小[0], 大小[1]))  # 规定图片大小
        root.方格1b = ImageTk.PhotoImage(root.方格1a)
        root.方格1c = tk.Button(image=root.方格1b, command=方法)
        root.lst.append(root.方格1c)
        root.lst[-1].place(x=位置[0], y=位置[1])

global bt, 按钮序号
bt = []
按钮序号 = 0

def 清空控件():
    global bt
    for i in bt:
        i[1].destroy()
    bt.clear()

def 跳转到结算页面():
    root.destroy()

def 修改玩家1金钱():
    if 破产[1] == 1:
        messagebox.showinfo("提示", f"玩家{1}已破产")
    if 破产[1] != 1:
        y = askinteger("", "多少钱")
        if y != None:
            money[1] = y
            玩家事件[1].append(f"金钱被修改到{money[1]}元")
        if stateall == 0:
            文字刷新(1)
        富豪榜更新()
        清空控件()


def 修改玩家2金钱():
    if 破产[2] == 1:
        messagebox.showinfo("提示", f"玩家{2}已破产")
    if 破产[2] != 1:
        y = askinteger("", "多少钱？")
        if y != None:
            money[2] = y
        if stateall == 1:
            文字刷新(2)
        富豪榜更新()
        清空控件()


def 修改玩家3金钱():
    if 破产[3] == 1:
        messagebox.showinfo("提示", f"玩家{3}已破产")
    if 破产[3] != 1:
        y = askinteger("", "多少钱？")
        if y != None:
            money[3] = y
        if stateall == 2:
            文字刷新(3)
        富豪榜更新()
        清空控件()


def 修改玩家4金钱():
    if 破产[4] == 1:
        messagebox.showinfo("提示", f"玩家{4}已破产")
    if 破产[4] != 1:
        y = askinteger("", "多少钱？")
        if y != None:
            money[4] = y
        if stateall == 3:
            文字刷新(4)
        富豪榜更新()
        清空控件()


def 修改玩家1头像方法():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("提示", "您打开的不是图片")
    else:
        角色图片文件路径[1] = file_path
        角色[0].传入新路径(file_path, 1)
    清空控件()


def 修改玩家2头像方法():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("提示", "您打开的不是图片")
    else:
        角色图片文件路径[2] = file_path
        角色[1].传入新路径(file_path, 2)
    清空控件()


def 修改玩家3头像方法():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("提示", "您打开的不是图片")
    else:
        角色图片文件路径[3] = file_path
        角色[2].传入新路径(file_path, 3)
    清空控件()


def 修改玩家4头像方法():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("提示", "您打开的不是图片")
    else:
        角色图片文件路径[4] = file_path
        角色[3].传入新路径(file_path, 4)
    清空控件()


def 玩家1信息查询方法():
    print(玩家事件[1])
    a = 滚动控件(玩家事件[1])

    try:
        清空控件()
    except:
        pass


def 玩家2信息查询方法():
    a = 滚动控件(玩家事件[2])
    清空控件()


def 玩家3信息查询方法():
    a = 滚动控件(玩家事件[3])
    清空控件()


def 玩家4信息查询方法():
    a = 滚动控件(玩家事件[4])
    清空控件()


def 修改土地价格方法():
    global 地价
    y = askinteger("", '多少钱？')
    if y != None:
        地价 = y
    清空控件()


def 修改过路费方法():
    global 过路费
    y = askinteger("", '多少钱？')
    if y != None:
        过路费 = y
    清空控件()


def 城市信息查询方法1():
    if 广州.state == 0:
        tk.messagebox.showinfo("提示", "广州目前公有")
    else:
        tk.messagebox.showinfo("提示", f"广州目前归玩家{广州.state}所有")
    清空控件()


def 城市信息查询方法2():
    if 香港.state == 0:
        tk.messagebox.showinfo("提示", "香港目前公有")
    else:
        tk.messagebox.showinfo("提示", f"香港目前归玩家{香港.state}所有")
    清空控件()


def 城市信息查询方法3():
    if 上海.state == 0:
        tk.messagebox.showinfo("提示", "上海目前公有")
    else:
        tk.messagebox.showinfo("提示", f"上海目前归玩家{上海.state}所有")
    清空控件()


def 城市信息查询方法4():
    if 纽约.state == 0:
        tk.messagebox.showinfo("提示", "纽约目前公有")
    else:
        tk.messagebox.showinfo("提示", f"纽约目前归玩家{纽约.state}所有")
    清空控件()


def 城市信息查询方法5():
    if 北京.state == 0:
        tk.messagebox.showinfo("提示", "北京目前公有")
    else:
        tk.messagebox.showinfo("提示", f"北京目前归玩家{北京.state}所有")
    清空控件()


def 城市信息查询方法6():
    if 伦敦.state == 0:
        tk.messagebox.showinfo("提示", "伦敦目前公有")
    else:
        tk.messagebox.showinfo("提示", f"伦敦目前归玩家{伦敦.state}所有")
    清空控件()


def 开发者信息显示方法():
    messagebox.showinfo("提示", "2022210993刘倬诚")
    清空控件()


def 显示图例():

    a = Image.open("游戏图片/图例.png")
    a.show()
    清空控件()

文件 = 根按钮(0, 0, "文件                   ")
编辑 = 根按钮(120, 0, "编辑                   ")
退出按钮 = 子按钮("退出游戏   ", 文件, 退出)
打开结算页面按钮 = 子按钮("跳转到结算页面  ", 文件, 跳转到结算页面)

修改土地价格 = 子按钮("修改土地价格", 编辑, 修改土地价格方法)
修改过路费 = 子按钮("修改过路费", 编辑, 修改过路费方法)
修改玩家金钱按钮 = 子按钮("修改玩家金钱", 编辑, None)
修改玩家1金钱按钮 = 子按钮("玩家1", 修改玩家金钱按钮, 修改玩家1金钱)
修改玩家2金钱按钮 = 子按钮("玩家2", 修改玩家金钱按钮, 修改玩家2金钱)
修改玩家3金钱按钮 = 子按钮("玩家3", 修改玩家金钱按钮, 修改玩家3金钱)
修改玩家4金钱按钮 = 子按钮("玩家4", 修改玩家金钱按钮, 修改玩家4金钱)

修改玩家头像按钮 = 子按钮("修改玩家头像", 编辑, None)
修改玩家1头像按钮 = 子按钮("玩家1", 修改玩家头像按钮, 修改玩家1头像方法)
修改玩家2头像按钮 = 子按钮("玩家2", 修改玩家头像按钮, 修改玩家2头像方法)
修改玩家3头像按钮 = 子按钮("玩家3", 修改玩家头像按钮, 修改玩家3头像方法)
修改玩家4头像按钮 = 子按钮("玩家4", 修改玩家头像按钮, 修改玩家4头像方法)

玩家信息查询 = 根按钮(240, 0, "玩家信息查询       ")
玩家1信息查询按钮 = 子按钮("玩家1", 玩家信息查询, 玩家1信息查询方法)
玩家2信息查询按钮 = 子按钮("玩家2", 玩家信息查询, 玩家2信息查询方法)
玩家3信息查询按钮 = 子按钮("玩家3", 玩家信息查询, 玩家3信息查询方法)
玩家4信息查询按钮 = 子按钮("玩家4", 玩家信息查询, 玩家4信息查询方法)

地产信息查询 = 根按钮(360, 0, "地产信息查询       ")
查询广州 = 子按钮("广州", 地产信息查询, 城市信息查询方法1)
查询香港 = 子按钮("香港", 地产信息查询, 城市信息查询方法2)
查询上海 = 子按钮("上海", 地产信息查询, 城市信息查询方法3)
查询纽约 = 子按钮("纽约", 地产信息查询, 城市信息查询方法4)
查询北京 = 子按钮("北京", 地产信息查询, 城市信息查询方法5)
查询伦敦 = 子按钮("伦敦", 地产信息查询, 城市信息查询方法6)

帮助 = 根按钮(480, 0, "帮助                  ")
图例按钮 = 子按钮("图例", 帮助, 显示图例)
更多操作细节按钮 = 子按钮("更多操作细节", 帮助, None)

更多按钮 = 根按钮(600, 0, "更多              ")
开发者信息按钮 = 子按钮("开发者信息", 更多按钮, 开发者信息显示方法)
地价 = 500
过路费 = 400
global 区域
棋盘x = 0  # 左上坐标的位置
棋盘y = 50
区域 = [None]

def 区域初始化():  # 用for循环快速完成26个区域的划分
    for _ in range(10):
        区域.append((棋盘x + _ * 120, 棋盘y))
    for _ in range(3):
        区域.append((棋盘x + 1080, 棋盘y + _ * 120 + 120))
    for _ in range(10):
        区域.append((棋盘x + 1080 - _ * 120, 棋盘y + 480))
    for _ in range(3):
        区域.append((棋盘x, 棋盘y + 360 - _ * 120))

区域初始化()

global XX, YY
XX = [0, 0, 0, 0, 0]
YY = [0, 0, 0, 0, 0]
XX[1] = 区域[1][0] + 1  # 之后就可以用下标的形式直接去到相应区域，很方便
YY[1] = 区域[1][1] + 1

XX[2] = 区域[1][0] + 51
YY[2] = 区域[1][1] + 1
XX[3] = 区域[1][0] + 1
YY[3] = 区域[1][1] + 51
XX[4] = 区域[1][0] + 51
YY[4] = 区域[1][1] + 51
global stateall, state1, state2, state3, state4
state1 = 1
state2 = 1
state3 = 1
state4 = 1
stateall = 0

角色图片文件路径 = [None, "游戏图片/李凯尔.png", "游戏图片/喜羊羊.jpeg", "游戏图片/汤姆猫.jpeg", "游戏图片/马里奥.jpg"]


def bubble_sort(arr):
    start = time.time()
    a = []
    排序后的顺序 = []
    for _ in range(len(arr) - 1):
        排序后的顺序.append(_ + 1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    for i in range(len(a) - 1):  # 注意这里是len-1
        for j in range(len(a) - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 互换
                排序后的顺序[j], 排序后的顺序[j + 1] = 排序后的顺序[j + 1], 排序后的顺序[j]  # 这是个对应表，对应每个角色
    end = time.time()
    print(f'进行一次排序需要{end - start}秒')
    return 排序后的顺序


# coding=gbk
def shellSort(arr, k, reverse=False):
    a = []
    排序后的顺序 = []
    for _ in range(len(arr) - 1):
        排序后的顺序.append(_ + 1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    length = len(a)
    dk = k  # 设置一个增量dk
    while dk > 0:
        for i in range(dk, length):
            temp = a[i]
            j = i
            while j >= dk and arr[j - dk] > temp:
                a[j] = a[j - dk]
                j -= dk
            a[j] = temp
        dk = int(dk / 2)
    return a

    if reverse == False:
        print(a)
    else:
        a.reverse()
        print(a)


class city:
    def __init__(self, name, location):
        self.name = name
        self.state = 0
        self.next = None  # next指向下一个结点
        self.number = 0
        self.location = location
        cityList.add(self)  # 初始化时自动添加到列表里


class citylist:
    def __init__(self):
        self.head = None  # 相当于c语言里的头指针和尾指针
        self.tail = None

    def add(self, city):
        if self.head == None:  # 新增操作，当链表为空，头尾指针指向同一结点
            self.head = city
            self.tail = city
        if self.head != None:
            self.tail.next = city  # 当链表已经有元素，头指针不动，尾指针后移指向新元素
            self.tail = city

    def println(self):
        point = self.head
        while point != None:
            print(point.name)
            point = point.next

    def name_search(self, name):  # 基于名称的查找
        point = self.head  # 定义一个指针，先指向头
        t = 0
        while point != None:  # 指针后移，匹配
            if point.name == name:
                break
            t += 1
            point = point.next  # 指向下一个
        if point == None:  # 找不到
            return 0
        else:
            return t

    def location_search(self, location):  # 基于位置的查找
        point = self.head  # 定义一个指针，先指向头
        t = 0
        while point != None:  # 指针后移，匹配
            if point.location == location:
                break
            t += 1
            point = point.next  # 指向下一个
        if point == None:  # 找不到
            return 0
        else:
            return t


cityList = citylist()  # 实例化
广州 = city("广州", 2)
香港 = city("香港", 4)
上海 = city("上海", 13)
纽约 = city("纽约", 15)
北京 = city("北京", 20)
伦敦 = city("伦敦", 26)


def 个人地产显示(i):
    str = ""
    point = cityList.head
    while point != None:
        if point.state == i:
            str += point.name
            str += ","
        point = point.next
    return str


def 破产判断():
    global 破产, 破产人数
    a = 0
    for x in range(1, 5):  # 看看有没有人钱是负数的
        if money[x] < 0:  # x记录的是玩家数
            messagebox.showinfo("提示", f"玩家{x}已破产")
            money[x] = 0  # 钱财清零，不然下一次会重复判断
            破产[x] = 1
            破产人数 += 1
            messagebox.showinfo("提示", f"此时破产{破产人数}人")
            if 广州.state == x:
                广州.state = 0
                messagebox.showinfo("提示", "广州的房产充公")
            if 香港.state == x:
                香港.state = 0
                messagebox.showinfo("提示", "香港的房产充公")
            if 上海.state == x:
                上海.state = 0
                messagebox.showinfo("提示", "上海的房产充公")
            if 上海.state == x:
                上海.state = 0
                messagebox.showinfo("提示", "纽约的房产充公")
            if 纽约.state == x:
                纽约.state = 0
                messagebox.showinfo("提示", "北京的房产充公")
            if 伦敦.state == x:
                伦敦.state = 0
                messagebox.showinfo("提示", "伦敦的房产充公")
            角色[x - 1].销毁()
            玩家事件[x].append(f"玩家{x}已破产")

            if 破产人数 == 3:
                for _ in range(5):
                    if 破产[_] == 0:
                        messagebox.showinfo("提示", f"玩家{_}获胜")
                        root.destroy()

def 判断(i,ai=None):  # 这里i是玩家几的意思,索引，判断判断
    def 城市方格判断(方格编号, i, city):
        x左 = 区域[方格编号][0] + 1
        x右 = x左 + 118
        y上 = 区域[方格编号][1] + 1
        y下 = y上 + 118
        global money
        if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
            if i == city.state:  # 交租
                玩家事件[i].append(f'到达方格13，{city.name}，还剩{money[i]}元')
            if i != city.state and city.state != 0:
                messagebox.showinfo("提示", f"你{i}需要向玩家{city.state}交{过路费}元作为过路费")
                money[i] -= 过路费
                money[city.state] += 过路费
                玩家事件[i].append(
                    f'到达方格{方格编号}，{city.name}，向玩家{city.state}交{过路费}元过路费,还剩{money[i]}元')

            if city.state == 0:  # 买地
                if ai==None:
                    ans = askokcancel("提示", f"你要花{地价}元买地吗？")
                else:
                    ans=random.randint(0,1)
                if ans:
                    if money[i] >= 地价:
                        messagebox.showinfo("提示", "成功购买")
                        money[i] -= 地价

                        city.state = i
                        玩家事件[i].append(f'到达方格13，购买{city.name},还剩{money[i]}元')
                    else:
                        messagebox.showinfo("提示", "钱不够")
                        玩家事件[i].append(f'到达方格{方格编号},还剩{money[i]}元')
    def 方格判断(方格编号, i, 方格效果, 附加文字=None, 参数=None):  # i是人物编号
        global money
        x左 = 区域[方格编号][0] + 1
        x右 = x左 + 118
        y上 = 区域[方格编号][1] + 1
        y下 = y上 + 118

        if 方格效果 == "增减钱":
            if 参数 > 0:
                符号 = '+'
            else:
                符号 = ''
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                messagebox.showinfo("提示", f"{附加文字},{符号}{参数}元")
                money[i] = money[i] +参数
                玩家事件[i].append(f"到方格{方格编号}，{附加文字},{符号}{参数}元，还剩{money[i]}元")
        if 方格效果 == "除以":
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                messagebox.showinfo("提示", 附加文字)
                money[i] = money[i] / 2
                玩家事件[i].append(f"到方格{方格编号}，{附加文字}，还剩{money[i]}元")

        if 方格效果 == "无事发生":
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                玩家事件[i].append(f"到方格{方格编号}，{附加文字}，还剩{money[i]}元")
        if 方格效果=="聚财":
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                t = 1
                messagebox.showinfo("提示", "其它玩家都要给你100元")
                money[i] = money[i] + 100 * (4 - 破产人数)
                for _ in money[1:5]:
                    if money[t] >= 0 and 破产[t] == 0:
                        money[t] -= 100
                    t += 1
                玩家事件[i].append(f"到达{方格编号}，收取其它玩家各100元，还剩{money[i]}元")
                temp_llst=[0,1,2,3,4]
                temp_llst[i]=0
                for ii in temp_llst:
                    if ii !=0:
                        玩家事件[ii].append(f"向玩家{i}给了100元，还剩{money[ii]}元")

        if 方格效果=="法院":
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                玩家事件[i].append(f"到达方格{方格编号}法院")
                t = 0
                if ai==None:
                    ans = askokcancel("法院提示", "要抵押卖掉房产换现金吗？")
                else:
                    ans=random.randint(0,1)
                if ans:
                    if 广州.state == i:
                        t += 1
                        if ai==None:
                            ans1 = askokcancel("法院提示", f"要把广州的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            广州.state = 0
                            玩家事件[i].append(f"卖了广州，还剩{money[i]}元")
                    if 香港.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("法院提示", f"要把香港的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            香港.state = 0
                            玩家事件[i].append(f"卖了香港，还剩{money[i]}元")
                    if 上海.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("法院提示", f"要把上海的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            上海.state = 0
                            玩家事件[i].append(f"卖了上海，还剩{money[i]}元")
                    if 纽约.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("法院提示", f"要把纽约的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            纽约.state = 0
                            玩家事件[i].append(f"卖了纽约，还剩{money[i]}元")
                    if 北京.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("法院提示", f"要把北京的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            北京.state = 0
                            玩家事件[i].append(f"卖了北京，还剩{money[i]}元")
                    if 伦敦.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("法院提示", f"要把伦敦的房产卖了吗？")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += 地价
                            伦敦.state = 0
                            玩家事件[i].append(f"卖了伦敦，还剩{money[i]}元")
                    if t == 0:
                        messagebox.showinfo("提示", "你没有房产")
        if 方格效果=="前进":
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                y = np.random.randint(1, 参数)
                messagebox.showinfo("提示", f"再前进{y}个格子")
                for _ in range(y):
                    if i==1:
                        图片1_next()
                    if i==2:
                        图片2_next()
                    if i==3:
                        图片3_next()
                    if i==4:
                        图片4_next()
                玩家事件[i].append(f"到达{附加文字}，再前进{y}个格子")
        if 方格效果=="交换钱财":
            max = 0
            t = 0
            t0 = 0
            temp = 0
            for _ in money:
                if money[t] > max:
                    max = money[t]
                    t0 = t
                t += 1
            if x左 <= XX[i] <= x右 and y上 <= YY[i] <= y下:
                messagebox.showinfo("恭喜", "你一夜暴富")
                messagebox.showinfo("提示", f"你将和玩家{t0}交换钱财")
                temp = money[i]
                money[i] = money[t0]
                money[t0] = temp
                玩家事件[i].append(f'到达方格{方格编号}，和玩家{t0}交换钱财，还剩{money[i]}元')

    方格判断(3, i, "增减钱", 附加文字="听演唱会", 参数=-100)
    方格判断(5, i, "增减钱", 附加文字="得到红包", 参数=100)
    方格判断(6, i, "除以", 附加文字="你参与赌博，身家只剩一半")
    方格判断(7, i, "无事发生", 附加文字="公园")
    方格判断(8,i,"法院")
    方格判断(9,i,"聚财")
    方格判断(10,i,"前进",参数=3,附加文字="机场")
    方格判断(11, i, "增减钱", 附加文字="得到红包", 参数=200)
    方格判断(12, i, "增减钱", 附加文字="被电信诈骗", 参数=-300)
    方格判断(14,i,"前进",参数=4,附加文字="高铁站")
    方格判断(16, i, "交换钱财")
    方格判断(17, i, "增减钱", 附加文字="得到红包", 参数=200)
    方格判断(18, i, "增减钱", 附加文字="误入缅北，需要交钱脱身", 参数=-300)
    方格判断(21, i, "增减钱", 附加文字="污染环境，交罚款", 参数=-350)
    方格判断(22, i, "法院")
    方格判断(23, i, "前进", 参数=2, 附加文字="码头")
    方格判断(24, i, "增减钱", 附加文字="看球赛", 参数=-150)
    方格判断(25, i, "增减钱", 附加文字="建议勇为，奖励", 参数=300)
    城市方格判断(2, i, 广州)
    城市方格判断(4, i, 香港)
    # 10有
    # 方格13判断(i)
    城市方格判断(13, i, 上海)
    # 14有
    城市方格判断(15, i, 纽约)
    # 19是公园
    城市方格判断(20, i, 北京)
    城市方格判断(26, i, 伦敦)
    破产判断()
    # end=time.time()
    # print(f'主判断函数执行用了{end-start}秒')

class 图片:
    def __init__(root, 路径, 位置, 大小):
        root.路径 = 路径
        root.位置 = 位置
        root.大小 = 大小
        root.lst = []
        root.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        root.方格1a = root.方格1a.resize((大小[0], 大小[1]))  # 规定图片大小
        root.方格1b = ImageTk.PhotoImage(root.方格1a)
        root.方格1c = ttk.Label(image=root.方格1b)
        root.lst.append(root.方格1c)
        root.lst[-1].place(x=位置[0], y=位置[1])

    def replace(root, 新位置):
        root.lst[-1].place(x=新位置[0], y=新位置[1])

    def 换图片(root, 序号):
        root.lst[-1].destroy()
        root.lst.pop()
        root.方格1a = Image.open(角色图片文件路径[序号])  # 括号里为需要显示在图形化界面里的图片
        root.方格1a = root.方格1a.resize((root.大小[0], root.大小[1]))  # 规定图片大小
        root.方格1b = ImageTk.PhotoImage(root.方格1a)
        root.方格1c = ttk.Label(image=root.方格1b)
        root.lst.append(root.方格1c)
        root.lst[-1].place(x=root.位置[0], y=root.位置[1])

    def 传入新路径(root, 路径, i):
        root.lst[-1].destroy()
        root.lst.pop()
        root.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        root.方格1a = root.方格1a.resize((root.大小[0], root.大小[1]))  # 规定图片大小
        root.方格1b = ImageTk.PhotoImage(root.方格1a)
        root.方格1c = ttk.Label(image=root.方格1b)
        root.lst.append(root.方格1c)
        if i == 1:
            root.lst[-1].place(x=XX[1], y=YY[1])
        if i == 2:
            root.lst[-1].place(x=XX[2], y=YY[2])
        if i == 3:
            root.lst[-1].place(x=XX[3], y=YY[3])
        if i == 4:
            root.lst[-1].place(x=XX[4], y=YY[4])

    def 销毁(root):
        root.lst[-1].destroy()


def 箭头刷新(i):
    箭头.replace((区域[i][0] + 25, 区域[i][1] + 120))

class 图片按钮:
    def __init__(root, 路径, 位置, 大小, 方法):
        root.路径 = 路径
        root.位置 = 位置
        root.大小 = 大小
        root.lst = []
        root.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        root.方格1a = root.方格1a.resize((大小[0], 大小[1]))  # 规定图片大小
        root.方格1b = ImageTk.PhotoImage(root.方格1a)
        root.方格1c = tk.Button(image=root.方格1b, command=方法)
        root.lst.append(root.方格1c)
        root.lst[-1].place(x=位置[0], y=位置[1])

class 图片2:
    def __init__(root, 路径, 位置):
        root.路径 = 路径
        root.位置 = 位置
        if 路径 != None:
            root.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
            root.方格1a = root.方格1a.resize((110, 110))  # 规定图片大小
            root.方格1b = ImageTk.PhotoImage(root.方格1a)
            root.方格1c = ttk.Label(image=root.方格1b)
            root.方格1c.place(x=区域[位置][0] + 5, y=区域[位置][1] + 5)  # 此位置就是区域的编号
        if 路径 == None:
            root.文字 = tk.Label(text=位置, font=12)
            root.文字.place(x=区域[位置][0] + 50, y=区域[位置][1] + 50)
        w1.create_line(区域[位置][0], 区域[位置][1], 区域[位置][0] + 120, 区域[位置][1], width=5)
        w1.create_line(区域[位置][0], 区域[位置][1], 区域[位置][0], 区域[位置][1] + 120, width=5)
        w1.create_line(区域[位置][0] + 120, 区域[位置][1], 区域[位置][0] + 120, 区域[位置][1] + 120, width=5)
        w1.create_line(区域[位置][0], 区域[位置][1] + 120, 区域[位置][0] + 120, 区域[位置][1] + 120, width=5)


class 文字:
    def __init__(root, 位置, 字号, 内容):
        root.位置 = 位置
        root.字号 = 字号
        root.内容 = 内容
        root.文字 = tk.Label(text=内容, font=字号)
        root.文字.place(x=位置[0], y=位置[1])

    def 更新(root, 内容):
        root.文字.destroy()
        root.文字 = tk.Label(text=内容, font=root.字号)
        root.文字.place(x=root.位置[0], y=root.位置[1])


class 滚动控件:
    def __init__(self, lst):
        滚动条页面 = tk.Tk()
        # bttrt=tk.Button(滚动条页面)   #模仿这个把滚动条加到里面去
        # bttrt.pack()

        self.scrollbar_v = Scrollbar(滚动条页面)
        self.scrollbar_v.pack(side=RIGHT, fill=Y)  # 右滚动条
        self.scrollbar_h = Scrollbar(滚动条页面, orient=HORIZONTAL)  # 水平滚动条
        self.scrollbar_h.pack(side=BOTTOM, fill=X)
        self.text = Text(滚动条页面, width=40, height=40)
        self.text.config(yscrollcommand=self.scrollbar_v.set)  # text绑定垂直滚动条
        self.text.config(xscrollcommand=self.scrollbar_h.set)  # text绑定水平滚动条
        self.text.pack(expand=YES, fill=BOTH)

        for i in range(len(lst)):
            self.text.insert("end", lst[i] + "\n")

        self.scrollbar_v.config(command=self.text.yview)  # 垂直滚动条绑定text
        self.scrollbar_h.config(command=self.text.xview)  # 水平滚动条绑定text


# 滚动条子=滚动控件()
# 方格25=图片("游戏图片/见义勇为，奖励300元.png",(3,243))
方格1 = 图片2("游戏图片/起点.png", 1)
方格2 = 图片2("游戏图片/广州.png", 2)
方格3 = 图片2("游戏图片/演唱会.png", 3)
方格4 = 图片2("游戏图片/香港.png", 4)
方格5 = 图片2("游戏图片/200红包.png", 5)
方格6 = 图片2("游戏图片/赌博现金减半.png", 6)
方格7 = 图片2("游戏图片/公园1.png", 7)
方格8 = 图片2("游戏图片/法院.png", 8)
方格9 = 图片2("游戏图片/交易所.png", 9)
方格10 = 图片2("游戏图片/飞机.png", 10)
方格11 = 图片2("游戏图片/200红包.png", 11)
方格12 = 图片2("游戏图片/电信诈骗.png", 12)
方格13 = 图片2("游戏图片/上海.png", 13)
方格14 = 图片2("游戏图片/高铁.jpg", 14)
方格15 = 图片2("游戏图片/纽约.png", 15)
方格16 = 图片2("游戏图片/一夜暴富.png", 16)
方格17 = 图片2("游戏图片/200红包.png", 17)
方格18 = 图片2("游戏图片/缅北.png", 18)
方格19 = 图片2("游戏图片/公园2.png", 19)
方格20 = 图片2("游戏图片/北京.png", 20)
方格21 = 图片2("游戏图片/环境污染罚款.png", 21)  # 括号里为需要显示在图形化界面里的图片
方格22 = 图片2("游戏图片/法院.png", 22)
方格23 = 图片2("游戏图片/轮船.jpg", 23)
方格24 = 图片2("游戏图片/2018.png", 24)
方格25 = 图片2("游戏图片/见义勇为，奖励300元.png", 25)
方格26 = 图片2("游戏图片/伦敦.png", 26)

箭头 = 图片("游戏图片/向上箭头.png", (区域[1][0], 区域[1][1] + 120), (35, 35))
提示图片1 = 图片(角色图片文件路径[1], (区域[3][0], 区域[3][1] + 240), (125, 125))
文字1 = 文字((区域[3][0], 区域[3][1] + 160), 32, "现在轮到玩家1")
引导图片1 = 图片(r"游戏图片\引导图片1.png", (区域[6][0], 区域[6][1] + 120),
                 (125, 230))
操作规则图片 = 图片(r"游戏图片\引导文字.png",
                    (区域[7][0] + 10, 区域[7][1] + 120), (300, 230))
金钱信息1 = 文字((区域[4][0] + 10, 区域[4][1] + 260), 32, "玩家1的资金为：1200")
地产信息1 = 文字((区域[4][0] + 10, 区域[4][1] + 290), 32, "玩家1的地产有\n")
地产信息2 = 文字((区域[4][0] + 10, 区域[4][1] + 330), 32, "")
富豪榜文字 = 文字((区域[13][0] + 120, 0), 32, "实时富豪榜")
富豪榜文字清单 = []
富豪榜图片清单 = []
富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 75), 32, "NO.1：玩家1\n 资金：1200"))
富豪榜图片清单.append(图片(角色图片文件路径[1], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 75), (50, 50)))
富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 200), 32, "NO.2：玩家2\n 资金: 1200"))
富豪榜图片清单.append(图片(角色图片文件路径[2], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 200), (50, 50)))

富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 325), 32, "NO.3:玩家3\n 资金:1200"))
富豪榜图片清单.append(图片(角色图片文件路径[3], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 325), (50, 50)))

富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 450), 32, "NO.4:玩家4\n 资金:1200"))
富豪榜图片清单.append(图片(角色图片文件路径[4], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 450), (50, 50)))


def 文字刷新(i):
    文字1.更新(f"现在轮到玩家{i}")
    if 破产[i] == 1:
        文字1.更新(f"现在轮到玩家{i}(已破产）")
    金钱信息1.更新(f"玩家{i}的资金为:{money[i]}")
    地产信息1.更新(f"玩家{i}的地产有:")
    地产信息2.更新(个人地产显示(i))

def 富豪榜更新():
    排行 = bubble_sort(money)
    for _ in range(len(排行)):
        富豪榜文字清单[_].更新(f"No.{_ + 1}:玩家{排行[_]}\n 资金: {money[排行[_]]}")
        富豪榜图片清单[_].换图片(排行[_])


角色 = []
角色.append(图片(角色图片文件路径[1], (XX[1], YY[1]), (47, 47)));
角色.append(图片(角色图片文件路径[2], (XX[2], YY[2]), (47, 47)));
角色.append(图片(角色图片文件路径[3], (XX[3], YY[3]), (47, 47)));
角色.append(图片(角色图片文件路径[4], (XX[4], YY[4]), (47, 47)))

def 添加金钱记录(i):
    global money
    if i == 1 and 破产[1] == 0:
        玩家1金钱记录.append(money[1])
    if i == 2 and 破产[2] == 0:
        玩家2金钱记录.append(money[2])
    if i == 3 and 破产[3] == 0:
        玩家3金钱记录.append(money[3])
    if i == 4 and 破产[4] == 0:
        玩家4金钱记录.append(money[4])

def main():
    global stateall, state1, state2, state3, state4
    global 破产
    if stateall % 4 == 0:  # 玩家1回合
        if 破产[1] == 0:
            移动图片1()
            箭头刷新(state1)
            判断(1)
        箭头刷新(state2)
        提示图片1.换图片(2)
        文字刷新(2)
        富豪榜更新()
        # tk.Label(root, text=f'轮到玩家{stateall % 4 + 2}', font=24).place(x=320, y=150)
    if stateall % 4 == 1:  # 玩家2回合
        if 破产[2] == 0:
            移动图片2()
            箭头刷新(state2)
            判断(2,ai=ai_[2])     #是否ai在这里改
        箭头刷新(state3)
        提示图片1.换图片(3)
        文字刷新(3)
        富豪榜更新()
    if stateall % 4 == 2:  # 玩家3回合
        if 破产[3] == 0:
            移动图片3()
            箭头刷新(state3)
            判断(3,ai=ai_[3])
        箭头刷新(state4)
        提示图片1.换图片(4)
        文字刷新(4)
        富豪榜更新()
    if stateall % 4 == 3:  # 玩家4回合
        if 破产[4] == 0:
            移动图片4()
            箭头刷新(state4)
            判断(4,ai=ai_[4])
        箭头刷新(state1)
        提示图片1.换图片(1)
        文字刷新(1)
        富豪榜更新()
    stateall += 1
    添加金钱记录(stateall % 4 + 1)

def 骰子():
    import numpy as np
    import tkinter
    import tkinter.messagebox  # 弹窗库
    y = np.random.randint(1, 7)  # 范围1-9（不包括10），数量三个
    tkinter.messagebox.showinfo('骰子', f'数字为{y}')  # 前面标头，后面内容
    return y

def 图片1_next():
    global state1, XX,YY

    state1 += 1
    if state1 == 27:
        state1 = 1
    XX[1] = 区域[state1][0] + 1
    YY[1] = 区域[state1][1] + 1
    角色[0].replace((XX[1], YY[1]))

def 移动图片1():
    t = 骰子()
    for x in range(t):
        图片1_next()

def 图片2_next():
    global state2
    global XX
    global YY
    state2 += 1
    if state2 == 27:
        state2 = 1
    XX[2] = 区域[state2][0] + 51
    YY[2] = 区域[state2][1] + 1
    角色[1].replace((XX[2], YY[2]))

def 移动图片2():
    t = 骰子()
    for x in range(t):
        图片2_next()

def 图片3_next():
    global state3
    global XX
    global YY
    state3 += 1
    if state3 == 27:
        state3 = 1
    XX[3] = 区域[state3][0] + 1
    YY[3] = 区域[state3][1] + 51
    角色[2].replace((XX[3], YY[3]))

def 移动图片3():
    t = 骰子()
    for x in range(t):
        图片3_next()

def 图片4_next():
    global state4
    global XX
    global YY
    state4 += 1
    if state4 == 27:
        state4 = 1
    XX[4] = 区域[state4][0] + 51
    YY[4] = 区域[state4][1] + 51
    角色[3].replace((XX[4], YY[4]))

def 移动图片4():
    t = 骰子()
    for x in range(t):
        图片4_next()

继续按钮 = 图片按钮("游戏图片/继续按钮.png", (区域[18][0], 区域[18][1] - 100), (120, 100), main)

root.mainloop()

结算页面 = tk.Tk()
结算页面.geometry("500x600")
结算页面.title = "结算页面"
方格1a = Image.open("游戏图片/结算页面.png")  # 括号里为需要显示在图形化界面里的图片
方格1a = 方格1a.resize((500, 600))  # 规定图片大小
方格1b = ImageTk.PhotoImage(方格1a)
方格1c = ttk.Label(image=方格1b)
方格1c.place(x=0, y=0)

def 生成玩家一金钱图表():
    y = 玩家1金钱记录
    print(y)
    x = list(map(lambda x: x, range(len(玩家1金钱记录))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, 玩家1金钱记录)
    plt.show()

bt1 = tk.Button(text="玩家一事件", command=玩家1信息查询方法).place(x=200, y=300)
bt5 = tk.Button(text="玩家一金钱变化", command=生成玩家一金钱图表).place(x=200, y=350)

def 生成玩家二金钱图表():
    y = 玩家2金钱记录
    print(y)
    x = list(map(lambda x: x, range(len(玩家2金钱记录))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, 玩家2金钱记录)
    plt.show()

bt2 = tk.Button(text="玩家二事件", command=玩家2信息查询方法).place(x=300, y=300)
bt6 = tk.Button(text="玩家二金钱变化", command=生成玩家二金钱图表).place(x=300, y=350)

def 生成玩家三金钱图表():
    y = 玩家3金钱记录
    print(y)
    x = list(map(lambda x: x, range(len(玩家3金钱记录))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, 玩家3金钱记录)
    plt.show()

bt3 = tk.Button(text="玩家三事件", command=玩家3信息查询方法).place(x=200, y=400)
bt7 = tk.Button(text="玩家三金钱变化", command=生成玩家三金钱图表).place(x=200, y=450)

def 生成玩家四金钱图表():
    y = 玩家4金钱记录
    print(y)
    x = list(map(lambda x: x, range(len(玩家4金钱记录))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, 玩家4金钱记录)
    plt.show()

bt4 = tk.Button(text="玩家四事件", command=玩家4信息查询方法).place(x=300, y=400)
bt8 = tk.Button(text="玩家四金钱变化", command=生成玩家四金钱图表).place(x=300, y=450)

结算页面.mainloop()
