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
import threading
import socket
import json
import single
import function_
#--------------------------------数据定义------------------------------
class city:
    def __init__(self, name, location,地价):
        self.name = name
        self.state = 0
        self.next = None  # next指向下一个结点
        self.number = 0
        self.location = location
        self.地价=地价
class data:
    def __init__(self):
        self.location=[None,1,1,1,1,1,1]
        self.money=[0,1200,1200,0,0]
        self.破产=[0,0,0,0,0]
        self.id=1

        self.ai=[]
        self.开始页面state=0
        self.角色图片文件路径= [None, "游戏图片/李凯尔.png", "游戏图片/喜羊羊.jpeg", "游戏图片/汤姆猫.jpeg", "游戏图片/马里奥.jpg"]
        self.主页面状态=1
        self.几人游戏=None
        self.轮到谁=0
        self.主按钮开关=False
        self.展示文字=""
        self.citylst=[]
        self.结束=0
        self.citylst.append(city("广州", 2, 500))
        self.citylst.append(city("香港", 4, 400))
        self.citylst.append(city("上海", 13, 450))
        self.citylst.append(city("纽约", 15, 300))
        self.citylst.append(city("北京", 20, 350))
        self.citylst.append(city("伦敦", 26, 600))
        self.newmessage=""
data=data()
#-------------------------------tkinter控件封装-----------------------
class 图片按钮:
    def __init__(开始页面, 路径, 位置, 大小, 方法,*arg):
        开始页面.路径 = 路径
        开始页面.位置 = 位置
        开始页面.大小 = 大小
        开始页面.lst = []
        开始页面.方格1a = Image.open(路径)  # 括号里为需要显示在图形化界面里的图片
        开始页面.方格1a = 开始页面.方格1a.resize((大小[0], 大小[1]))  # 规定图片大小
        开始页面.方格1b = ImageTk.PhotoImage(开始页面.方格1a)
        开始页面.方格1c = tk.Button(image=开始页面.方格1b, command=lambda: 方法(arg))
        开始页面.lst.append(开始页面.方格1c)
        开始页面.lst[-1].place(x=位置[0], y=位置[1])
import tkinter as tk
from tkinter import scrolledtext

class SimpleChatRoom:
    def __init__(self, root):
        self.root = root
        # self.root.title("简单聊天室")
        # self.root.geometry("400x300")  # 设置窗口大小

        # 聊天区域
        self.chat_area = scrolledtext.ScrolledText(root, state="disabled", height=10, width=30)
        self.chat_area.place(x=1220, y=400, width=380, height=200)  # 使用绝对坐标

        # 输入框
        self.input_field = tk.Entry(root, width=30)
        self.input_field.place(x=1220, y=600, width=280, height=30)  # 使用绝对坐标
        self.input_field.bind("<Return>", self.send_message)  # 绑定回车键发送消息

        # 发送按钮
        self.send_button = tk.Button(root, text="发送", command=self.send_message)
        self.send_button.place(x=1220, y=640, width=90, height=30)  # 使用绝对坐标

    def send_message(self, event=None):
        message = self.input_field.get()

        if message:
            # self.display_message(message)
            # self.input_field.delete(0, tk.END)  # 清空输入框
            print('message')
            #服务器端，广播
            if data.id==1:
                print('message send1')
                app.update(message, data.id)
                message={"0":"1","1":message,"2":data.id}
                message=json.dumps(message)
                broadcast(message,None)

            if data.id!=1:
                print('message send2')
                message = {"0": "1", "1": message, "2": data.id}
                message = json.dumps(message)
                client_socket.send(message.encode('utf-8'))  # 这个是对应发送数据的
        self.input_field.delete(0, tk.END)  # 清空输入框
    def display_message(self, message,用户i):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"用户{用户i}: {message}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)  # 自动滚动到最底部
    def update(self,message,用户i):
        if message:
            self.display_message(message,用户i)
# -------------------------------进入页面-------------------
def 开始游戏(aistete):
    aistete=aistete[0]
    print('aistate',aistete)
    开始页面.destroy()
    data.开始页面state = 1
    if aistete==0:                     #单人游戏，打3个AI
        data.ai=[0,0,1,1,1]
        data.几人游戏=1
        single._main()   #单人游戏的脚本
        exit()

    elif aistete==1:
        data.几人游戏=2

def 退出(arg):
    quit()

开始页面 = tk.Tk()
开始页面.geometry("500x600")

开始页面state = 0
开始页面.方格1a = Image.open("游戏图片/大富翁封面.png")  # 括号里为需要显示在图形化界面里的图片
开始页面.方格1a = 开始页面.方格1a.resize((500, 600))  # 规定图片大小
开始页面.方格1b = ImageTk.PhotoImage(开始页面.方格1a)
开始页面.方格1c = ttk.Label(image=开始页面.方格1b)
开始页面.方格1c.place(x=0, y=0)
开始游戏按钮1 = 图片按钮("游戏图片/单人游戏.png", (50, 200), (120, 60), 开始游戏,0)
开始游戏按钮2 = 图片按钮("游戏图片/双人游戏.png", (50, 275), (120, 60), 开始游戏,1)
# 开始游戏按钮3 = 图片按钮("游戏图片/四人游戏.png", (50, 350), (120, 60), 开始游戏,2)
退出游戏按钮 = 图片按钮("游戏图片/退出游戏.png", (330, 350), (120, 60), 退出)
开始页面.mainloop()
#---------------------------------------------------------------------------------
#----------------------------------线程函数定义------------------------------------
#---------------------------------  服务器端--------------------------------------
def handle_client(client_socket):
    print('start')
    while data.主页面状态==1 and data.结束==0:
        print(11)
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"Received: {msg}")

                #------------------这里可以进行收到信息后的处理---------------------------


                #-----------------------------------------------------------
                #-----------------下面这里则是将最新信息广播到各个服务器
                # broadcast(str(data.location), client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue
        #------------------------------------------
        data_decode(msg)
        broadcast(msg, client_socket)
        动态刷新()
    print('sercice_main_stop')
def broadcast(message, client_socket):
    for client in clients:
        # if client != client_socket:
            try:
                client.send(message.encode('utf-8'))         #这里是回显信息
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def TCP_service_main():
    while data.主页面状态==1 and data.结束==0:
        print(22)
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} has been established!")
        文字1.更新("玩家已加入！请点击按钮，从你开始！")
        data.轮到谁=1
        threading.Thread(target=handle_client, args=(client_socket,)).start()
    print('sercice_main_stop')
#---------------------------------  服务器端--------------------------------------
#--------------------------------客户端------------------------
def receive_messages(sock):
    print("receive_start")
    while data.结束==0:
        # print(33)
        try:
            msg = sock.recv(2048).decode('utf-8')
            if msg:
                print(f"Broadcast Received: {msg}")

        except:
            print("Error receiving messages")
            break
        # ---------------------这里是对接收到的信息进行处理---------------------
        data_decode(msg)
        动态刷新()
        # -----------------------------------------------------------------

#-----------------------------------上面是客户端-----------------------------


def 计时():
    count=10
    while count>0:
        文字1.更新(f"轮到你了,还剩{count}秒")
        time.sleep(1)
        count-=1
        if data.轮到谁!=data.id:
            return

#------------------------------------------主页面部分----------------------------------
def 动态刷新():
    if data.轮到谁==0:
        return
    def 箭头刷新(i):
        箭头.replace(x=区域[i][0] + 25, y=区域[i][1] + 120)
    角色[1].replace(x=区域[data.location[1]][0],y=区域[data.location[1]][1])
    角色[2].replace(x=区域[data.location[2]][0]+50,y=区域[data.location[2]][1])
    # 角色[3].replace(x=区域[data.location[3]][0],y=区域[data.location[3]][1]+50)
    # 角色[4].replace(x=区域[data.location[4]][0]+50,y=区域[data.location[4]][1]+50)
    print("data.轮到谁",data.轮到谁)
    print("data.location",data.location)

    箭头刷新(data.location[data.轮到谁])
    if data.money[1]>=data.money[2]:
        富豪榜文字清单[0].更新(f"NO.1：玩家1\n 资金：{data.money[1]}")
        富豪榜文字清单[1].更新(f"NO.2：玩家2\n 资金：{data.money[2]}")
        富豪榜图片清单[0].换图片(1)
        富豪榜图片清单[1].换图片(2)
    else:
        富豪榜文字清单[0].更新(f"NO.1：玩家2\n 资金：{data.money[2]}")
        富豪榜文字清单[1].更新(f"NO.2：玩家1\n 资金：{data.money[1]}")
        富豪榜图片清单[0].换图片(2)
        富豪榜图片清单[1].换图片(1)
    if data.轮到谁==data.id:
        文字1.更新(f"轮到你了！")
    else:
        文字1.更新(f"轮到玩家{data.轮到谁}")
    地产信息1.更新(data.展示文字)
    if data.轮到谁==6:
        提示图片1.换图片(1)
    else:
        提示图片1.换图片(data.轮到谁)
def data_encode():
    dic={0:0,1:data.location[1],2:data.location[2],3:data.location[3],4:data.location[4],
         5:data.money[1],6:data.money[2],7:data.money[3],8:data.money[4],9:data.轮到谁,
         10:data.citylst[0].state,11:data.citylst[1].state,
         12:data.citylst[2].state,13:data.citylst[3].state,
         14:data.citylst[4].state,15:data.citylst[5].state,16:data.展示文字}
    return  json.dumps(dic)   #转为字符串
def data_decode(dic_str):
    dic_from_str = json.loads(dic_str)
    if int(dic_from_str["0"])==0:                        #0表示传data
        for i in range(1,5):
            data.location[i]=dic_from_str[str(i)]
        for i in range(5,9):
            data.money[i-4]=dic_from_str[str(i)]
        data.轮到谁=int(dic_from_str["9"])
        for i in range(10,16):
            data.citylst[i-10].state=dic_from_str[str(i)]
        data.展示文字=dic_from_str["16"]
    if int(dic_from_str["0"])==1:                 #用于聊天框的通信
        app.update(dic_from_str["1"],dic_from_str["2"])

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
    def replace(root, x,y):
        root.lst[-1].place(x=x, y=y)
    def 换图片(root, 序号):
        root.lst[-1].destroy()
        root.lst.pop()
        root.方格1a = Image.open(data.角色图片文件路径[序号])  # 括号里为需要显示在图形化界面里的图片
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
        # root.文字.destroy()
        # root.文字 = tk.Label(text=内容, font=root.字号)
        # root.文字.place(x=root.位置[0], y=root.位置[1])
        root.文字.config(text=内容)

def 破产判断():
    for x in range(1, 5):  # 看看有没有人钱是负数的
        if data.money[x] < 0:  # x记录的是玩家数
            messagebox.showinfo("提示", f"玩家{x}已破产")
            data.展示文字=f"玩家{x}已破产"
            data.money[x] = 0  # 钱财清零，不然下一次会重复判断
            data.破产[x] = 1

            for ci in data.citylst:
                if ci.state == x:
                    ci.state = 0
                    messagebox.showinfo("提示", f"{ci.name}的房产充公")

            # 角色[x].销毁()
            print("lendata(pochan)",len(data.破产))
            if sum(data.破产) == 1:
                for _ in range(1,3):
                    if data.破产[_] == 0:
                        messagebox.showinfo("提示", )
                        data.展示文字=f"玩家{_}获胜"
                        data.轮到谁=5
                        # root.destroy()

def 判断(i,data,ai=None):  # 这里i是玩家几的意思,索引，判断判断
    def 城市方格判断(方格编号, i, city):
        if data.location[i]==方格编号:
            print('city.state=',city.state,"   i=",i)
            if i != city.state and city.state != 0:     #交租
                过路费=city.地价//3
                messagebox.showinfo("提示", f"玩家{i}需要向玩家{city.state}交{过路费}元作为过路费")
                data.money[i] -= 过路费
                data.money[city.state] += 过路费
                data.展示文字=f"玩家{i}需要向玩家{city.state}交{过路费}元作为过路费"
            if city.state == 0:  # 买地
                if ai==None:
                    ans = askokcancel("提示", f"你要花{city.地价}元买地吗？")
                else:
                    ans=random.randint(0,1)
                if ans:
                    if data.money[i] >= city.地价:
                        messagebox.showinfo("提示", "成功购买")
                        data.money[i] -= city.地价
                        city.state = i
                        data.展示文字=f"玩家{i}购买了土地{city.name}"
                    else:
                        messagebox.showinfo("提示", "钱不够")


    def 方格判断(方格编号, i, 方格效果, 附加文字=None, 参数=None):  # i是人物编号

        if 方格效果 == "增减钱":
            if 参数 > 0:
                符号 = '+'
            else:
                符号 = ''
            if data.location[i]==方格编号:
                messagebox.showinfo("提示", f"{附加文字},{符号}{参数}元")
                data.money[i] = data.money[i] +参数
                data.展示文字 = f"玩家{i}{附加文字},{符号}{参数}元"
        if 方格效果 == "除以":
            if data.location[i]==方格编号:
                messagebox.showinfo("提示", 附加文字)
                data.money[i] = data.money[i] // 2
                data.展示文字=f"玩家{i}{附加文字}"

        if 方格效果 == "无事发生":
            if data.location[i]==方格编号:
                   data.展示文字=f"玩家{i}无事发生"
        if 方格效果=="聚财":
            if data.location[i]==方格编号:
                t = 1
                messagebox.showinfo("提示", "其它玩家都要给你100元")
                data.money[i] = data.money[i] + 100 * (4 - len(data.破产))
                for _ in data.money[1:3]:
                    if data.money[t] >= 0 and data.破产[t] == 0:
                        data.money[t] -= 100
                    t += 1
                data.展示文字=f"其它玩家都要给玩家{i}  100元"

        if 方格效果=="法院":
            strr=[]
            if data.location[i]==方格编号:
                t = 0
                if ai==None:
                    ans = askokcancel("法院提示", "要抵押卖掉房产换现金吗？")
                else:
                    ans=random.randint(0,1)
                if ans:
                    for ci in data.citylst:
                        if ci.state == i:
                            t += 1
                            if ai==None:
                                ans1 = askokcancel("法院提示", f"要把{ci.name}的房产卖了吗？")
                            else:
                                ans1 = random.randint(0, 1)
                            if ans1:
                                data.money[i] += ci.地价
                                ci.state = 0
                                strr.append(ci.name)
                    if t == 0:
                        messagebox.showinfo("提示", "你没有房产")
                    if len(strr)==0:
                        data.展示文字=f"玩家{i}经过法院，没有变卖土地"
                    else:
                        data.展示文字 = f"玩家{i}经过法院，变卖了{[name for name in strr]}"
                if not ans:
                    data.展示文字 = f"玩家{i}经过法院，没有变卖土地"
        if 方格效果=="前进":
            if data.location[i]==方格编号:
                y = np.random.randint(1, 参数)
                messagebox.showinfo("提示", f"再前进{y}个格子")
                data.location[i]+=y
                if data.location[i]>26:
                    data.location[i]-=26

        if 方格效果=="交换钱财":
            max = 0
            t = 0
            t0 = 0
            temp = 0
            for _ in data.money[:3]:
                if data.money[t] > max:
                    max = data.money[t]
                    t0 = t
                t += 1
            if data.location[i]==方格编号:
                messagebox.showinfo("恭喜", "你一夜暴富")
                messagebox.showinfo("提示", f"你将和玩家{t0}交换钱财")
                data.展示文字 = f"玩家{i}和玩家{t0}交换钱财"
                temp = data.money[i]
                data.money[i] = data.money[t0]
                data.money[t0] = temp


    方格判断(3, i, "增减钱", 附加文字="听演唱会", 参数=-100)
    方格判断(5, i, "增减钱", 附加文字="得到红包", 参数=100)
    方格判断(6, i, "除以", 附加文字="参与赌博，身家只剩一半")
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
    方格判断(25, i, "增减钱", 附加文字="见义勇为，奖励", 参数=300)
    城市方格判断(2, i, data.citylst[0])
    城市方格判断(4, i,data.citylst[1])
    # 10有
    # 方格13判断(i)
    城市方格判断(13, i, data.citylst[2])
    # 14有
    城市方格判断(15, i, data.citylst[3])
    # 19是公园
    城市方格判断(20, i, data.citylst[4])
    城市方格判断(26, i, data.citylst[5])
    破产判断()
    # end=time.time()
    # print(f'主判断函数执行用了{end-start}秒')

def main(arg):
    print("data.id=",data.id)

    if data.轮到谁==6:
        messagebox.showinfo("提示",f"游戏已经结束！现在退出")
        root.destroy()
        socket.close()
        return
    if data.轮到谁!=data.id:
        messagebox.showinfo("提示","现在还不是你的回合哦！")
        return
    # threading.Thread(target=计时, args=(client_socket,)).start()
    step=function_.骰子()
    data.location[data.id]+=step


    if data.location[data.id]>26:
        data.location[data.id]=data.location[data.id]-26  #循环回到初始点

    if data.id==1:                  #服务器端
        broadcast(data_encode(), None)
        动态刷新()
        判断(data.id, data)

        data.轮到谁 += 1
        if data.轮到谁 == 3:
            data.轮到谁 = 1

        broadcast(data_encode(), None)
        动态刷新()
    elif data.id==2:                #客户端，
        msg = data_encode()
        client_socket.send(msg.encode('utf-8'))  # 这个是对应发送数据的
        判断(data.id, data)

        data.轮到谁 += 1
        if data.轮到谁 == 3:
            data.轮到谁 = 1
        msg = data_encode()
        client_socket.send(msg.encode('utf-8'))  # 这个是对应发送数据的

    # print("data.money=",data.money)


# 1200x600,每行10个格，每列5个格，每个格120*120
root = tk.Tk()
root.geometry("1600x750")  # 长乘宽
w1 = Canvas(root, width=1200, height=650, background='blue')
w1.place(x=0, y=0)
棋盘x = 0;棋盘y = 50;区域 = [None]  # 左上坐标的位置
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
提示图片1 = 图片(data.角色图片文件路径[1], (区域[3][0], 区域[3][1] + 240), (125, 125))
文字1 = 文字((区域[3][0], 区域[3][1] + 160), 32, "现在轮到玩家1")
引导图片1 = 图片(r"游戏图片\引导图片1.png", (区域[6][0], 区域[6][1] + 120),(125, 230))
操作规则图片 = 图片(r"游戏图片\引导文字.png",(区域[7][0] + 10, 区域[7][1] + 120), (300, 230))
金钱信息1 = 文字((区域[4][0] + 10, 区域[4][1] + 260), 32, "刚刚发生的事件：")
地产信息1 = 文字((区域[4][0] + 10, 区域[4][1] + 290), 32, "\n")
地产信息2 = 文字((区域[4][0] + 10, 区域[4][1] + 330), 32, "")
富豪榜文字 = 文字((区域[13][0] + 120, 0), 32, "实时富豪榜")

富豪榜文字清单 = []
富豪榜图片清单 = []
富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 75), 32, "NO.1：玩家1\n 资金：1200"))
富豪榜图片清单.append(图片(data.角色图片文件路径[1], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 75), (50, 50)))
富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 200), 32, "NO.2：玩家2\n 资金: 1200"))
富豪榜图片清单.append(图片(data.角色图片文件路径[2], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 200), (50, 50)))

# 富豪榜文字清单.append(文字((富豪榜文字.位置[0], 富豪榜文字.位置[1] + 325), 32, "NO.3:玩家3\n 资金:1200"))
# 富豪榜图片清单.append(图片(data.角色图片文件路径[3], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 325), (50, 50)))
#
富豪榜文字清单.append(文字((富豪榜文字.位置[0]+10, 富豪榜文字.位置[1] + 350), 32, "聊天框"))
# 富豪榜图片清单.append(图片(data.角色图片文件路径[4], (富豪榜文字.位置[0] + 180, 富豪榜文字.位置[1] + 450), (50, 50)))

角色 = [None]
角色.append(图片(data.角色图片文件路径[1], (区域[1][0], 区域[1][1]), (47, 47)));
角色.append(图片(data.角色图片文件路径[2], (区域[1][0]+50, 区域[1][1]), (47, 47)));
# 角色.append(图片(data.角色图片文件路径[3], (区域[1][0], 区域[1][1]+50), (47, 47)));
# 角色.append(图片(data.角色图片文件路径[4], (区域[1][0]+50, 区域[1][1]+50), (47, 47)))

继续按钮 = 图片按钮("游戏图片/继续按钮.png", (区域[18][0], 区域[18][1] - 100), (120, 100), main)

if data.几人游戏==1:         #单人游戏
    pass

if data.几人游戏==2:         #多人游戏，初始化服务器或加入
    ans = askokcancel("提示", f"已有房间？（点击确定加入房间，点击取消创建房间）")
    if ans:                    #加入房间的逻辑（客户端）
        SERVER_IP=askstring("提示","请输入目标IP")
        # SERVER_IP = '127.0.0.1'
        SERVER_PORT = askinteger("提示","请输入目标port")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            data.id=2                          #id=2对应2号玩家
            threading.Thread(target=receive_messages, args=(client_socket,)).start()
        except:
            tk.messagebox.showinfo("提示","无法连接到该地址")

    else:                     #创建服务器
        SERVER_IP=function_.get_local_ip()
        if not askokcancel("提示", f"您的IP是{SERVER_IP},点击确定使用该IP，点击取消使用本地回路"):
            SERVER_IP = '127.0.0.1'


        SERVER_PORT = 9999
        clients = []
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER_IP, SERVER_PORT))
        server.listen(5)
        print(f"Server started on {SERVER_IP}:{SERVER_PORT}")
        data.id=1                      #id=1对应1号玩家，也就是服务器端
        文字1.更新(f"等待玩家加入,ip:{SERVER_IP}\nport:{SERVER_PORT}")
        threading.Thread(target=TCP_service_main, args=()).start()


app=SimpleChatRoom(root)
root.mainloop()

#避免线程继续占用资源,所以要让等待的线程结束
print('over')
data.结束=1
def stop_client():
    client_socket.close()
def stop_service():
    print("Stopping service...")

    for client in clients:
        client.close()
    server.close()
    print("Service stopped.")
if data.id==1:
    stop_service()
if data.id==2:
    stop_client()


