#coding=gbk
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image,ImageFile
from tkinter import ttk
from tkinter . messagebox import *
import numpy as np
from tkinter.simpledialog import askfloat,askinteger,askstring
import matplotlib.pyplot as plt
import time
#��һ���֣�����ҳ������
��ʼҳ��=tk.Tk()
��ʼҳ��.geometry("500x600")

��ʼҳ��state=0
��ʼҳ��.����1a = Image.open("��ϷͼƬ/���̷���.png")  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
��ʼҳ��.����1a =��ʼҳ��.����1a.resize((500, 600))  # �涨ͼƬ��С
��ʼҳ��.����1b = ImageTk.PhotoImage(��ʼҳ��.����1a)
��ʼҳ��.����1c = ttk.Label(image=��ʼҳ��.����1b)
��ʼҳ��.����1c.place(x=0,y=0)

def �˳�():
    quit()

class ͼƬ��ť:
    def __init__(��ʼҳ��, ·��, λ��, ��С,����):
        ��ʼҳ��.·�� = ·��
        ��ʼҳ��.λ�� = λ��
        ��ʼҳ��.��С = ��С
        ��ʼҳ��.lst = []
        ��ʼҳ��.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        ��ʼҳ��.����1a = ��ʼҳ��.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        ��ʼҳ��.����1b = ImageTk.PhotoImage(��ʼҳ��.����1a)
        ��ʼҳ��.����1c = tk.Button(image=��ʼҳ��.����1b,command=����)
        ��ʼҳ��.lst.append(��ʼҳ��.����1c)
        ��ʼҳ��.lst[-1].place(x=λ��[0], y=λ��[1])
def ��ʼ��Ϸ():
    global ��ʼҳ��state
    ��ʼҳ��.destroy()
    ��ʼҳ��state=1
��ʼ��Ϸ��ť=ͼƬ��ť("��ϷͼƬ/��ʼ��ϷͼƬ.png",(50,350),(120,60),��ʼ��Ϸ)
�˳���Ϸ��ť=ͼƬ��ť("��ϷͼƬ/�˳���Ϸ.png",(330,350),(120,60),�˳�)
��ʼҳ��.mainloop()
if ��ʼҳ��state==0:
   quit()

#1200x600,ÿ��10����ÿ��5����ÿ����120*120
root = tk.Tk()
root.geometry("1600x750")  #���˿�
w1=Canvas(root,width=1200,height=650,background='blue')
w1.place(x=0,y=0)



#��ʼ����Ǯ
global money
money=[0,1200,1200,1200,1200]   #�������б����洢��
���1��Ǯ��¼=[money[1]]
���2��Ǯ��¼=[money[2]]
���3��Ǯ��¼=[money[3]]
���4��Ǯ��¼=[money[4]]
global �Ʋ�,�Ʋ�����
�Ʋ�����=0
�Ʋ�=[1,0,0,0,0]  #�����Ʋ�״̬
���1�¼�=[]
���2�¼�=[]
���3�¼�=[]
���4�¼�=[]
class ����ť:
    def __init__(root,x,y,�ı�):
        root.�ı�=�ı�
        root.x=x
        root.y=y
        root.�ӽ��=[]
        root.state=0
        global y0
        y0=y
        def չʾ�Ӱ�ť():
            global bt,��ť���
            if len(bt)==0:         #bt�ǰ�ť��ջ����ջΪ�գ�˵��û�а�ť��չ��
                root.state=0      #��ť��state��ʾ���ǰ�ť�Ƿ��Ѿ������¹���state=0ʱ�������ť��չ����state=1ʱ���۵���
            else:
                ��ť���=0          #��ť���������ǰ�ť��������ջ��ջ
            if root.state==0:
                if len(bt)>0:                  #���б�ĸ���ť����չ��״̬����գ�������֤��������
                    for _ in range(len(bt)):
                        bt[_][1].destroy()
                bt.clear()
                for _ in range(len(root.�ӽ��)):   #����չ���Լ����ӽڵ�
                    ��ť���+=1
                    root.�ӽ��[_].x=x
                    root.�ӽ��[_].y=27*_+30       #���ӽڵ�õ�λ�ã�����鿴
                    root.�ӽ��[_].���=��ť���
                    if len(root.�ӽ��[_].�ӽ��)>0:
                        root.�ӽ��[_].����+=">"
                    root.�ӽ��[_].����=root.�ӽ��[_].����.ljust(20," ")    #�����ӽڵ�
                    b=tk.Button(text=root.�ӽ��[_].����,command=root.�ӽ��[_].����) #Ϊ�ӽڵ㴫��
                    bt.append((��ť���,b))                            #��ջ���������ӽڵ�
                    bt[-1][1].place(x=root.x,y=27*_+30)
                root.state+=1
                # print(root.x)
            elif root.state==1:             #state=1��˼���ٵ�����۵�
                ��ť���=0                    #���ð�ť��Ų��������������ظ�չ��
                for _ in root.�ӽ��:         #���ӽڵ㶼����Ϊû�������״̬
                    _.state=0
                for _ in range(len(bt)):    #��ջ����ջ���Ƴ��Ӱ�ť���ﵽ�۵���Ч��
                    bt[-1-_][1].destroy()
                root.state=0

                bt.clear()                 #���ջ��Ϊ�´�չ��׼��
                # print(bt)
        root.��ť = tk.Button(text=�ı�+">",command=չʾ�Ӱ�ť,height=1)
        root.��ť.place(x=x, y=y)
class �Ӱ�ť:
    def __init__(root,����,����ť,����):
        root.����=����
        root.����=����
        root.�ӽ��=[]
        root.state=0
        root.x=0
        root.y=0
        root.���=0
        def չʾ�Ӱ�ť():
            global bt,��ť���
            if root.��� == 0:
                ��ť��� += 1                       #���������������������ջ
                root.��� = ��ť���
            if root.���==len(bt):
                root.state=0                       #�����Ӱ�ť
            if root.state == 0:
                for _ in range(len(root.�ӽ��)):
                    root.�ӽ��[_].x = root.x + 80  #�Ӱ�ťλ�ã����Ӱ�ť�͸���ť��
                    root.�ӽ��[_].y = root.y+_*27    #�Ӱ�ťλ�ã����Ӱ�ť�͸���ť��
                    b = tk.Button(text=root.�ӽ��[_].����, command=root.�ӽ��[_].����)  #�����Ӱ�ť����
                    bt.append((��ť���,b))        #��ջ�洢�Ӱ�ť�������
                    bt[-1][1].place(x=root.x+100, y=root.y+_*27)
                root.state += 1                  #չ�����ٵ���ͱ���۵�״̬
            elif root.state == 1:
                for _ in root.�ӽ��:
                    _.state=0
                Ҫ��ȥ�İ�ť����=len(bt)-root.���  #��˼�ǰ��Լ����Ӱ�ť���۵��ˣ������������ĸ���ť�����۵�
                for _ in range(Ҫ��ȥ�İ�ť����):
                    bt[-1][1].destroy()      #��ջ��ȥ���Ӱ�ť
                    bt.pop()                 #��ջ
                root.state = 0               #���ð�ť
        if root.����==None:
            root.����=չʾ�Ӱ�ť
        ����ť.�ӽ��.append(root)
class ͼƬ��ť:
    def __init__(root, ·��, λ��, ��С,����):
        root.·�� = ·��
        root.λ�� = λ��
        root.��С = ��С
        root.lst = []
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = tk.Button(image=root.����1b,command=����)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0], y=λ��[1])

global bt,��ť���
bt=[]
��ť���=0
def ��տؼ�():
    global bt
    for i in bt:
        i[1].destroy()
    bt.clear()
def ��ת������ҳ��():
    root.destroy()
def �޸����1��Ǯ():
    if �Ʋ�[1]==1:
        messagebox.showinfo("��ʾ",f"���{1}���Ʋ�")
    if �Ʋ�[1]!=1:
        y=askinteger("","����Ǯ")
        if y!=None:
            money[1]=y
            ���1�¼�.append(f"��Ǯ���޸ĵ�{money[1]}Ԫ")
        if stateall==0:
            ����ˢ��(1)
        ���������()
        ��տؼ�()
def �޸����2��Ǯ():
    if �Ʋ�[2]==1:
        messagebox.showinfo("��ʾ",f"���{2}���Ʋ�")
    if �Ʋ�[2]!=1:
        y=askinteger("","����Ǯ��")
        if y!=None:
            money[2]=y
        if stateall==1:
            ����ˢ��(2)
        ���������()
        ��տؼ�()
def �޸����3��Ǯ():
    if �Ʋ�[3]==1:
        messagebox.showinfo("��ʾ",f"���{3}���Ʋ�")
    if �Ʋ�[3]!=1:
        y=askinteger("","����Ǯ��")
        if y!=None:
            money[3]=y
        if stateall==2:
            ����ˢ��(3)
        ���������()
        ��տؼ�()
def �޸����4��Ǯ():
    if �Ʋ�[4]==1:
        messagebox.showinfo("��ʾ",f"���{4}���Ʋ�")
    if �Ʋ�[4]!=1:
        y=askinteger("","����Ǯ��")
        if y!=None:
            money[4]=y
        if stateall==3:
            ����ˢ��(4)
        ���������()
        ��տؼ�()
def �޸����1ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path=file_path.split(".")
    if newfile_path[-1] not in ["png","jepg","jpg"]:
        messagebox.showinfo("��ʾ","���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[1]=file_path
        ��ɫ1.������·��(file_path,1)
    ��տؼ�()
def �޸����2ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path=file_path.split(".")
    if newfile_path[-1] not in ["png","jepg","jpg"]:
        messagebox.showinfo("��ʾ","���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[2]=file_path
        ��ɫ2.������·��(file_path,2)
    ��տؼ�()
def �޸����3ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path=file_path.split(".")
    if newfile_path[-1] not in ["png","jepg","jpg"]:
        messagebox.showinfo("��ʾ","���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[3]=file_path
        ��ɫ3.������·��(file_path,3)
    ��տؼ�()
def �޸����4ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path=file_path.split(".")
    if newfile_path[-1] not in ["png","jepg","jpg"]:
        messagebox.showinfo("��ʾ","���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[4]=file_path
        ��ɫ4.������·��(file_path,4)
    ��տؼ�()
def ���1��Ϣ��ѯ����():
    a=�����ؼ�(���1�¼�)
    try:
        ��տؼ�()
    except:
        pass
def ���2��Ϣ��ѯ����():
    a=�����ؼ�(���2�¼�)
    ��տؼ�()
def ���3��Ϣ��ѯ����():
    a=�����ؼ�(���3�¼�)
    ��տؼ�()
def ���4��Ϣ��ѯ����():
    a=�����ؼ�(���4�¼�)
    ��տؼ�()
def �޸����ؼ۸񷽷�():
    global �ؼ�
    y=askinteger("",'����Ǯ��')
    if y!=None:
        �ؼ�=y
    ��տؼ�()
def �޸Ĺ�·�ѷ���():
    global ��·��
    y = askinteger("", '����Ǯ��')
    if y != None:
        ��·��= y
    ��տؼ�()
def ������Ϣ��ѯ����1():
    if ����.state==0:
        tk.messagebox.showinfo("��ʾ","����Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"����Ŀǰ�����{����.state}����")
    ��տؼ�()
def ������Ϣ��ѯ����2():
    if ���.state==0:
        tk.messagebox.showinfo("��ʾ","���Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"���Ŀǰ�����{���.state}����")
    ��տؼ�()
def ������Ϣ��ѯ����3():
    if �Ϻ�.state==0:
        tk.messagebox.showinfo("��ʾ","�Ϻ�Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"�Ϻ�Ŀǰ�����{�Ϻ�.state}����")
    ��տؼ�()
def ������Ϣ��ѯ����4():
    if ŦԼ.state==0:
        tk.messagebox.showinfo("��ʾ","ŦԼĿǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"ŦԼĿǰ�����{ŦԼ.state}����")
    ��տؼ�()
def ������Ϣ��ѯ����5():
    if ����.state==0:
        tk.messagebox.showinfo("��ʾ","����Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"����Ŀǰ�����{����.state}����")
    ��տؼ�()
def ������Ϣ��ѯ����6():
    if �׶�.state==0:
        tk.messagebox.showinfo("��ʾ","�׶�Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ",f"�׶�Ŀǰ�����{�׶�.state}����")
    ��տؼ�()
def ��������Ϣ��ʾ����():
    messagebox.showinfo("��ʾ","2022210993��پ��")
    ��տؼ�()
def ��ʾͼ��():
    a=Image.open("��ϷͼƬ/ͼ��.png")
    a.show()
    ��տؼ�()
�ļ�=����ť(0,0,"�ļ�                   ")
�༭=����ť(120,0,"�༭                   ")
�˳���ť=�Ӱ�ť("�˳���Ϸ   ",�ļ�,�˳�)
�򿪽���ҳ�水ť=�Ӱ�ť("��ת������ҳ��  ",�ļ�,��ת������ҳ��)


�޸����ؼ۸�=�Ӱ�ť("�޸����ؼ۸�",�༭,�޸����ؼ۸񷽷�)
�޸Ĺ�·��=�Ӱ�ť("�޸Ĺ�·��",�༭,�޸Ĺ�·�ѷ���)
�޸���ҽ�Ǯ��ť=�Ӱ�ť("�޸���ҽ�Ǯ",�༭,None)
�޸����1��Ǯ��ť=�Ӱ�ť("���1",�޸���ҽ�Ǯ��ť,�޸����1��Ǯ)
�޸����2��Ǯ��ť=�Ӱ�ť("���2",�޸���ҽ�Ǯ��ť,�޸����2��Ǯ)
�޸����3��Ǯ��ť=�Ӱ�ť("���3",�޸���ҽ�Ǯ��ť,�޸����3��Ǯ)
�޸����4��Ǯ��ť=�Ӱ�ť("���4",�޸���ҽ�Ǯ��ť,�޸����4��Ǯ)

�޸����ͷ��ť=�Ӱ�ť("�޸����ͷ��",�༭,None)
�޸����1ͷ��ť=�Ӱ�ť("���1",�޸����ͷ��ť,�޸����1ͷ�񷽷�)
�޸����2ͷ��ť=�Ӱ�ť("���2",�޸����ͷ��ť,�޸����2ͷ�񷽷�)
�޸����3ͷ��ť=�Ӱ�ť("���3",�޸����ͷ��ť,�޸����3ͷ�񷽷�)
�޸����4ͷ��ť=�Ӱ�ť("���4",�޸����ͷ��ť,�޸����4ͷ�񷽷�)


�����Ϣ��ѯ=����ť(240,0,"�����Ϣ��ѯ       ")
���1��Ϣ��ѯ��ť=�Ӱ�ť("���1",�����Ϣ��ѯ,���1��Ϣ��ѯ����)
���2��Ϣ��ѯ��ť=�Ӱ�ť("���2",�����Ϣ��ѯ,���2��Ϣ��ѯ����)
���3��Ϣ��ѯ��ť=�Ӱ�ť("���3",�����Ϣ��ѯ,���3��Ϣ��ѯ����)
���4��Ϣ��ѯ��ť=�Ӱ�ť("���4",�����Ϣ��ѯ,���4��Ϣ��ѯ����)

�ز���Ϣ��ѯ=����ť(360,0,"�ز���Ϣ��ѯ       ")
��ѯ����=�Ӱ�ť("����",�ز���Ϣ��ѯ,������Ϣ��ѯ����1)
��ѯ���=�Ӱ�ť("���",�ز���Ϣ��ѯ,������Ϣ��ѯ����2)
��ѯ�Ϻ�=�Ӱ�ť("�Ϻ�",�ز���Ϣ��ѯ,������Ϣ��ѯ����3)
��ѯŦԼ=�Ӱ�ť("ŦԼ",�ز���Ϣ��ѯ,������Ϣ��ѯ����4)
��ѯ����=�Ӱ�ť("����",�ز���Ϣ��ѯ,������Ϣ��ѯ����5)
��ѯ�׶�=�Ӱ�ť("�׶�",�ز���Ϣ��ѯ,������Ϣ��ѯ����6)

����=����ť(480,0,"����                  ")
ͼ����ť=�Ӱ�ť("ͼ��",����,��ʾͼ��)
�������ϸ�ڰ�ť=�Ӱ�ť("�������ϸ��",����,None)

���ఴť=����ť(600,0,"����              ")
��������Ϣ��ť=�Ӱ�ť("��������Ϣ",���ఴť,��������Ϣ��ʾ����)
�ؼ�=500
��·��=400
global ����
����x=0           #���������λ��
����y=50
����=[None]
def �����ʼ��():           #��forѭ���������26������Ļ���
    for _ in range(10):
        ����.append((����x+_*120,����y))
    for _ in range(3):
        ����.append((����x+1080,����y+_*120+120))
    for _ in range(10):
        ����.append((����x+1080-_*120,����y+480))
    for _ in range(3):
        ����.append((����x,����y+360-_*120))
�����ʼ��()
global x1,y1,x2,y2,x3,y3,x4,y4
x1=����[1][0]+1     #֮��Ϳ������±����ʽֱ��ȥ����Ӧ���򣬺ܷ���
y1=����[1][1]+1

x2=����[1][0]+51
y2=����[1][1]+1
x3=����[1][0]+1
y3=����[1][1]+51
x4=����[1][0]+51
y4=����[1][1]+51
global stateall,state1,state2,state3,state4
state1=1
state2=1
state3=1
state4=1
stateall=0



��ɫͼƬ�ļ�·��=[None,"��ϷͼƬ/���.png","��ϷͼƬ/ϲ����.jpeg","��ϷͼƬ/��ķè.jpeg","��ϷͼƬ/�����.jpg"]
def bubble_sort(arr):
    start=time.time()
    a=[]
    ������˳��=[]
    for _ in range(len(arr)-1):
        ������˳��.append(_+1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    for i in range(len(a)-1):   #ע��������len-1
        for j in range(len(a)-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]  #����
                ������˳��[j],������˳��[j+1]=������˳��[j+1],������˳��[j]  #���Ǹ���Ӧ����Ӧÿ����ɫ
    end=time.time()
    print(f'����һ��������Ҫ{end-start}��')
    return ������˳��

#coding=gbk
def shellSort(arr, k, reverse=False):
    a = []
    ������˳�� = []
    for _ in range(len(arr) - 1):
        ������˳��.append(_ + 1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    length = len(a)
    dk = k # ����һ������dk
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
    def __init__(self,name,location):
        self.name=name
        self.state=0
        self.next=None    #nextָ����һ�����
        self.number=0
        self.location=location
        cityList.add(self)   #��ʼ��ʱ�Զ���ӵ��б���
class citylist:
    def __init__(self):
        self.head=None    #�൱��c�������ͷָ���βָ��
        self.tail=None
    def add(self,city):
        if self.head==None:   #����������������Ϊ�գ�ͷβָ��ָ��ͬһ���
            self.head=city
            self.tail=city
        if self.head!=None:
            self.tail.next=city   #�������Ѿ���Ԫ�أ�ͷָ�벻����βָ�����ָ����Ԫ��
            self.tail=city
    def println(self):
        point=self.head
        while point!=None:
            print(point.name)
            point=point.next
    def name_search(self,name):   #�������ƵĲ���
        point=self.head   #����һ��ָ�룬��ָ��ͷ
        t=0
        while point!=None:   #ָ����ƣ�ƥ��
            if point.name==name:
                break
            t+=1
            point=point.next   #ָ����һ��
        if point==None:    #�Ҳ���
            return 0
        else:
            return t
    def location_search(self,location):   #����λ�õĲ���
        point = self.head    #����һ��ָ�룬��ָ��ͷ
        t = 0
        while point != None:   #ָ����ƣ�ƥ��
            if point.location == location:
                break
            t += 1
            point = point.next  #ָ����һ��
        if point == None:   #�Ҳ���
            return 0
        else:
            return t
cityList=citylist()   #ʵ����
����=city("����",2)
���=city("���",4)
�Ϻ�=city("�Ϻ�",13)
ŦԼ=city("ŦԼ",15)
����=city("����",20)
�׶�=city("�׶�",26)

def ���˵ز���ʾ(i):
    str=""
    point=cityList.head
    while point!=None:
        if point.state==i:
            str+=point.name
            str+=","
        point=point.next
    return str

def �Ʋ��ж�():
    global �Ʋ�,�Ʋ�����
    a=0
    for x in range(1,5):   #������û����Ǯ�Ǹ�����
        if money[x]<0:               #x��¼���������
            messagebox.showinfo("��ʾ",f"���{x}���Ʋ�")
            money[x]=0   #Ǯ�����㣬��Ȼ��һ�λ��ظ��ж�
            �Ʋ�[x]=1
            �Ʋ�����+=1
            messagebox.showinfo("��ʾ",f"��ʱ�Ʋ�{�Ʋ�����}��")
            if ����.state==x:
                ����.state=0
                messagebox.showinfo("��ʾ","���ݵķ����乫")
            if ���.state==x:
                ���.state=0
                messagebox.showinfo("��ʾ","��۵ķ����乫")
            if �Ϻ�.state==x:
                �Ϻ�.state=0
                messagebox.showinfo("��ʾ","�Ϻ��ķ����乫")
            if �Ϻ�.state==x:
                �Ϻ�.state=0
                messagebox.showinfo("��ʾ","ŦԼ�ķ����乫")
            if ŦԼ.state==x:
                ŦԼ.state=0
                messagebox.showinfo("��ʾ","�����ķ����乫")
            if �׶�.state==x:
                �׶�.state=0
                messagebox.showinfo("��ʾ","�׶صķ����乫")
            if x==1:
                ��ɫ1.����()
                ���1�¼�.append("���1���Ʋ�")
            if x==2:
                ��ɫ2.����()
                ���2�¼�.append("���2���Ʋ�")
            if x==3:
                ��ɫ3.����()
                ���3�¼�.append("���3���Ʋ�")
            if x==4:
                ��ɫ4.����()
                ���4�¼�.append("���4���Ʋ�")

            if �Ʋ�����==3:
                for _ in range(5):
                    if �Ʋ�[_]==0:
                        messagebox.showinfo("��ʾ",f"���{_}��ʤ")
                        root.destroy()
def �ж�(i):    #����i����Ҽ�����˼
    def ����2�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[2][0] + 1
        x�� = x�� + 118
        y�� = ����[2][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            if i == ����.state:  # ����
                ���1�¼�.append(f'������2��ʣ{money[i]}Ԫ')
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���1�¼�.append(f'������2�������{����.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�
                        ����.state = 1
                        ���1�¼�.append(f"���˷���2��������ݣ���ʣ{money[1]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���1�¼�.append(f"���˷���2����ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            if i == ����.state:
                ���2�¼�.append(f'������2��ʣ{money[i]}Ԫ')
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���2�¼�.append(f'������2�������{����.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ����.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        ����.state = 2
                        ���2�¼�.append(f"���˷���2��������ݣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���2�¼�.append(f"���˷���2����ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            if i == ����.state:  # �Լ��ĵط������ý���
                ���3�¼�.append(f'������2��ʣ{money[i]}Ԫ')
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[����.state] += ��·��
                ���3�¼�.append(f'������2�������{����.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        ����.state = 3
                        ���3�¼�.append(f"���˷���2��������ݣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���3�¼�.append(f"���˷���2����ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            if i == ����.state:  # ����
                ���4�¼�.append(f'������2��ʣ{money[i]}Ԫ')
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���4�¼�.append(f'������2�������{����.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        ����.state = 4
                        ���4�¼�.append(f"���˷���2��������ݣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���4�¼�.append(f"���˷���2����ʣ{money[i]}Ԫ")
    def ����3�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[3][0] + 1
        x�� = x�� + 118
        y�� = ����[3][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��100Ԫ���ݳ���")
            money[1] = money[1] - 100
            ���1�¼�.append(f"������3������100Ԫ���ݳ��ᣬ����{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��100Ԫ���ݳ���")
            money[2] = money[2] - 100
            ���2�¼�.append(f"������3������100Ԫ���ݳ��ᣬ����{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��100Ԫ���ݳ���")
            money[3] = money[3] - 100
            ���3�¼�.append(f"������3������100Ԫ���ݳ��ᣬ����{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��100Ԫ���ݳ���")
            money[4] = money[4] - 100
            ���4�¼�.append(f"������3������100Ԫ���ݳ��ᣬ����{money[i]}Ԫ")
    def ����4�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[4][0] + 1
        x�� = 479
        y�� = ����[4][1] + 1
        y�� = 119
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            if i == ���.state:  # ����
                ���1�¼�.append(f'������4��ʣ{money[i]}Ԫ')
            if i != ���.state and ���.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{���.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[���.state] += ��·��
                ���1�¼�.append(f'������4�������{���.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ���.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�
                        ���.state = 1
                        ���1�¼�.append(f"���˷���4��������ۣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���1�¼�.append(f"���˷���4����ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            if i == ���.state:
                ���2�¼�.append(f'������4��ʣ{money[i]}Ԫ')
            if i != ���.state and ���.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{���.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[���.state] += ��·��
                ���2�¼�.append(f'������4�������{���.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ���.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        ���.state = 2
                        ���2�¼�.append(f"���˷���4��������ۣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���2�¼�.append(f"���˷���4����ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            if i == ���.state:  # �Լ��ĵط������ý���
                ���3�¼�.append(f'������4��ʣ{money[i]}Ԫ')
            if i != ���.state and ���.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{���.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[���.state] += ��·��
                ���3�¼�.append(f'������4�������{���.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ���.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        ���.state = 3
                        ���3�¼�.append(f"���˷���4��������ۣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���3�¼�.append(f"���˷���4����ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            if i == ���.state:  # ����
                ���4�¼�.append(f'������4��ʣ{money[i]}Ԫ')
            if i != ���.state and ���.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{���.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[���.state] += ��·��
                ���4�¼�.append(f'������4�������{���.state}��{��·��}Ԫ��Ϊ��·��,ʣ{money[i]}Ԫ')
            if ���.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        ���.state = 4
                        ���4�¼�.append(f"���˷���4��������ۣ���ʣ{money[i]}Ԫ")
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���4�¼�.append(f"���˷���4����ʣ{money[i]}Ԫ")
    def ����5�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[5][0] + 1
        x�� = 599
        y�� = ����[5][1] + 1
        y�� = 119
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            money[1] += 200
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            ���1�¼�.append(f"������5�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[2] += 200
            ���2�¼�.append(f"������5�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[3] += 200
            ���3�¼�.append(f"������5�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[4] += 200
            ���4�¼�.append(f"������5�����200Ԫ�������ʣ{money[i]}Ԫ")
    def ����6�ж�(i):
                global money  # ����Ҫ��global���ܽӽ���
                x�� = ����[6][0] + 1
                x�� = x��+118
                y�� = ����[6][1] + 1
                y�� = y��+118
                if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
                    messagebox.showinfo("��ʾ", "�����Ĳ������ֻʣһ��")
                    money[1] = money[1] / 2
                    ���1�¼�.append(f"������6������Ĳ���ۼ��룬��ʣ{money[i]}Ԫ")
                if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
                    messagebox.showinfo("��ʾ", "�����Ĳ������ֻʣһ��")
                    money[2] = money[2] / 2
                    ���2�¼�.append(f"������6������Ĳ���ۼ��룬��ʣ{money[i]}Ԫ")
                if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
                    messagebox.showinfo("��ʾ", "�����Ĳ������ֻʣһ��")
                    money[3] = money[3] / 2
                    ���3�¼�.append(f"������6������Ĳ���ۼ��룬��ʣ{money[i]}Ԫ")
                if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
                    messagebox.showinfo("��ʾ", "�����Ĳ������ֻʣһ��")
                    money[4] = money[4] / 2
                    ���4�¼�.append(f"������6������Ĳ���ۼ��룬��ʣ{money[i]}Ԫ")
    def ����7�ж�(i):
        global money
        x�� = ����[7][0] + 1
        x�� = x�� + 118
        y�� = ����[7][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            ���1�¼�.append(f"���﷽��7����԰����ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            ���2�¼�.append(f"���﷽��7����԰����ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            ���3�¼�.append(f"���﷽��7����԰����ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            ���4�¼�.append(f"���﷽��7����԰����ʣ{money[i]}Ԫ")
    def ����8�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[8][0] + 1
        x�� = x�� + 118
        y�� = ����[8][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            ���1�¼�.append("���﷽��8��Ժ")
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���1�¼�.append(f"���˹��ݣ���ʣ{money[i]}Ԫ")
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���1�¼�.append(f"������ۣ���ʣ{money[i]}Ԫ")
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���1�¼�.append(f"�����Ϻ�����ʣ{money[i]}Ԫ")
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���1�¼�.append(f"����ŦԼ����ʣ{money[i]}Ԫ")
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���1�¼�.append(f"���˱�������ʣ{money[i]}Ԫ")
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���1�¼�.append(f"�����׶أ���ʣ{money[i]}Ԫ")
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            ���2�¼�.append("���﷽��8��Ժ")
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���2�¼�.append(f"���˹��ݣ���ʣ{money[i]}Ԫ")
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���2�¼�.append(f"������ۣ���ʣ{money[i]}Ԫ")
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���2�¼�.append(f"�����Ϻ�����ʣ{money[i]}Ԫ")
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���2�¼�.append(f"����ŦԼ����ʣ{money[i]}Ԫ")
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���2�¼�.append(f"���˱�������ʣ{money[i]}Ԫ")
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���2�¼�.append(f"�����׶أ���ʣ{money[i]}Ԫ")
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            ���3�¼�.append("���﷽��8��Ժ")
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���3�¼�.append(f"���˹��ݣ���ʣ{money[i]}Ԫ")
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���3�¼�.append(f"������ۣ���ʣ{money[i]}Ԫ")
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���3�¼�.append(f"�����Ϻ�����ʣ{money[i]}Ԫ")
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���3�¼�.append(f"����ŦԼ����ʣ{money[i]}Ԫ")
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���3�¼�.append(f"���˱�������ʣ{money[i]}Ԫ")
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���3�¼�.append(f"�����׶أ���ʣ{money[i]}Ԫ")
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            ���4�¼�.append("���﷽��8��Ժ")
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���4�¼�.append(f"���˹��ݣ���ʣ{money[i]}Ԫ")
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���4�¼�.append(f"������ۣ���ʣ{money[i]}Ԫ")
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���4�¼�.append(f"�����Ϻ�����ʣ{money[i]}Ԫ")
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���4�¼�.append(f"����ŦԼ����ʣ{money[i]}Ԫ")
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���4�¼�.append(f"���˱�������ʣ{money[i]}Ԫ")
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���4�¼�.append(f"�����׶أ���ʣ{money[i]}Ԫ")
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")


        # ������ʱ����װ����
    def ����9�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        global �Ʋ�����
        x�� = ����[9][0] + 1
        x�� = x�� + 118
        y�� = ����[9][1]
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            t = 1
            messagebox.showinfo("��ʾ", "������Ҷ�Ҫ����100Ԫ")
            money[i] = money[i] + 100 * (4 - �Ʋ�����)
            for _ in money[1:5]:
                if money[t] >= 0 and �Ʋ�[t] == 0:
                    money[t] -= 100
                t += 1
            ���1�¼�.append(f"���﷽��9����ȡ������Ҹ�100Ԫ����ʣ{money[1]}Ԫ")
            ���2�¼�.append(f"�����һ100Ԫ����ʣ{money[2]}Ԫ")
            ���3�¼�.append(f"�����һ100Ԫ����ʣ{money[3]}Ԫ")
            ���4�¼�.append(f"�����һ100Ԫ����ʣ{money[4]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            t = 1
            messagebox.showinfo("��ʾ", "������Ҷ�Ҫ����100Ԫ")
            money[i] = money[i] + 100 * (4 - �Ʋ�����)
            for _ in money[1:5]:
                if money[t] >= 0 and �Ʋ�[t] == 0:
                    money[t] -= 100
                t += 1
            ���2�¼�.append(f"���﷽��9����ȡ������Ҹ�100Ԫ����ʣ{money[2]}Ԫ")
            ���1�¼�.append(f"����Ҷ�100Ԫ����ʣ{money[1]}Ԫ")
            ���3�¼�.append(f"����Ҷ�100Ԫ����ʣ{money[3]}Ԫ")
            ���4�¼�.append(f"����Ҷ�100Ԫ����ʣ{money[4]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            t = 1
            messagebox.showinfo("��ʾ", "������Ҷ�Ҫ����100Ԫ")
            money[i] = money[i] + 100 * (4 - �Ʋ�����)
            for _ in money[1:5]:
                if money[t] >= 0 and �Ʋ�[t] == 0:
                    money[t] -= 100
                t += 1
            ���3�¼�.append(f"���﷽��9����ȡ������Ҹ�100Ԫ����ʣ{money[3]}Ԫ")
            ���2�¼�.append(f"�������100Ԫ����ʣ{money[2]}Ԫ")
            ���1�¼�.append(f"�������100Ԫ����ʣ{money[1]}Ԫ")
            ���4�¼�.append(f"�������100Ԫ����ʣ{money[4]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            t = 1
            messagebox.showinfo("��ʾ", "������Ҷ�Ҫ����100Ԫ")
            money[i] = money[i] + 100 * (4 - �Ʋ�����)
            for _ in money[1:5]:
                if money[t] >= 0 and �Ʋ�[t] == 0:
                    money[t] -= 100
                t += 1
            ���4�¼�.append(f"���﷽��9����ȡ������Ҹ�100Ԫ����ʣ{money[4]}Ԫ")
            ���2�¼�.append(f"�������100Ԫ����ʣ{money[2]}Ԫ")
            ���3�¼�.append(f"�������100Ԫ����ʣ{money[3]}Ԫ")
            ���1�¼�.append(f"�������100Ԫ����ʣ{money[1]}Ԫ")
    def ����10�ж�(i):

        x�� = ����[10][0] + 1
        x�� = x�� + 118
        y�� = ����[10][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            y = np.random.randint(1, 3)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ1_next()
            ���1�¼�.append(f"�����������ǰ��{y}������")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            y = np.random.randint(1, 3)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ2_next()
            ���2�¼�.append(f"�����������ǰ��{y}������")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            y = np.random.randint(1, 3)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ3_next()
            ���3�¼�.append(f"�����������ǰ��{y}������")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            y = np.random.randint(1, 3)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ4_next()
            ���4�¼�.append(f"�����������ǰ��{y}������")
    def ����11�ж�(i):  # Ӧ����xΪ1081-1200�ķ�Χ��yΪ121-239�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[11][0] + 1
        x�� = x�� + 118
        y�� = ����[11][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            money[1] += 200
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            ���1�¼�.append(f"���﷽��11�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[2] += 200
            ���2�¼�.append(f"���﷽��11�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[3] += 200
            ���3�¼�.append(f"���﷽��11�����200Ԫ�������ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "���200Ԫ���")
            money[4] += 200
            ���4�¼�.append(f"���﷽��11�����200Ԫ�������ʣ{money[i]}Ԫ")
    def ����12�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[12][0] + 1
        x�� = x�� + 118
        y�� = ����[12][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            messagebox.showinfo("��ʾ", "�㱻����թƭ��300Ԫ")
            money[1] = money[1] - 300
            ���1�¼�.append(f"���﷽��12��������թƭ300Ԫ����ʣ{money[i]}Ԫ")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "�㱻����թƭ��300Ԫ")
            money[2] = money[2] - 300
            ���2�¼�.append(f"���﷽��12��������թƭ300Ԫ����ʣ{money[i]}Ԫ")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "�㱻����թƭ��300Ԫ")
            money[3] = money[3] - 300
            ���3�¼�.append(f"���﷽��12��������թƭ300Ԫ����ʣ{money[i]}Ԫ")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "�㱻����թƭ��300Ԫ")
            money[4] = money[4] - 300
            ���4�¼�.append(f"���﷽��12��������թƭ300Ԫ����ʣ{money[i]}Ԫ")
    def ����13�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[13][0] + 1
        x�� = x�� + 118
        y�� = ����[13][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            if i == �Ϻ�.state:  # ����
                ���1�¼�.append(f'���﷽��13���Ϻ�����ʣ{money[i]}Ԫ')
            if i != �Ϻ�.state and �Ϻ�.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�Ϻ�.state] += ��·��
                ���1�¼�.append(f'���﷽��13���Ϻ��������{�Ϻ�.state}��{��·��}Ԫ��·��,��ʣ{money[i]}Ԫ')

            if �Ϻ�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�

                        �Ϻ�.state = 1
                        ���1�¼�.append(f'���﷽��13�������Ϻ�,��ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���1�¼�.append(f'���﷽��13,��ʣ{money[i]}Ԫ')
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            if i == �Ϻ�.state:
                ���2�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
            if i != �Ϻ�.state and �Ϻ�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�Ϻ�.state] += ��·��
                ���2�¼�.append(f'���﷽��13���Ϻ�,�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ')

            if �Ϻ�.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        �Ϻ�.state = 2
                        ���2�¼�.append(f'���﷽��13�������Ϻ�,��ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���2�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            if i == �Ϻ�.state:  # �Լ��ĵط������ý���
                ���3�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
            if i != �Ϻ�.state and �Ϻ�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[�Ϻ�.state] += ��·��
                ���3�¼�.append(f'���﷽��13���Ϻ�,�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·�ѣ���ʣ{money[i]}Ԫ')
            if �Ϻ�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        �Ϻ�.state = 3
                        ���3�¼�.append(f'���﷽��13�������Ϻ�,��ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���3�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            if i == �Ϻ�.state:  # ����
                ���4�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
            if i != �Ϻ�.state and �Ϻ�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�Ϻ�.state] += ��·��
                ���4�¼�.append(f'���﷽��13���Ϻ�,�����{�Ϻ�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ')
            if �Ϻ�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        �Ϻ�.state = 4
                        ���4�¼�.append(f'���﷽��13�������Ϻ�,��ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                    ���4�¼�.append(f'���﷽��13���Ϻ�,��ʣ{money[i]}Ԫ')
    def ����14�ж�(i):
                                    x�� = ����[14][0] + 1
                                    x�� = x�� + 118
                                    y�� = ����[14][1] + 1
                                    y�� = y�� + 118
                                    if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
                                        y = np.random.randint(1, 4)
                                        messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
                                        for _ in range(y):
                                            ͼƬ1_next()
                                        ���1�¼�.append(f'�������վ����ǰ��{y}������')
                                    if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
                                        y = np.random.randint(1, 4)
                                        messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
                                        for _ in range(y):
                                            ͼƬ2_next()
                                        ���2�¼�.append(f'�������վ����ǰ��{y}������')
                                    if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
                                        y = np.random.randint(1, 4)
                                        messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
                                        for _ in range(y):
                                            ͼƬ3_next()
                                        ���3�¼�.append(f'�������վ����ǰ��{y}������')
                                    if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
                                        y = np.random.randint(1, 4)
                                        messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
                                        for _ in range(y):
                                            ͼƬ4_next()
                                        ���4�¼�.append(f'�������վ����ǰ��{y}������')
    def ����15�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[15][0] + 1
        x�� = x�� + 118
        y�� = ����[15][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            if i == ŦԼ.state:  # ����
                ���1�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
            if i != ŦԼ.state and ŦԼ.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[ŦԼ.state] += ��·��
                ���1�¼�.append(f'���﷽��15��ŦԼ����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·�ѣ���ʣ{money[i]}Ԫ')
            if ŦԼ.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�
                        ŦԼ.state = 1
                        ���1�¼�.append(f'���﷽��15������ŦԼ����ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���1�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            if i == ŦԼ.state:
                ���2�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
            if i != ŦԼ.state and ŦԼ.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[ŦԼ.state] += ��·��
                ���2�¼�.append(f'���﷽��15��ŦԼ����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·�ѣ���ʣ{money[i]}Ԫ')

            if ŦԼ.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        ŦԼ.state = 2
                        ���2�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���2�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            if i == ŦԼ.state:  # �Լ��ĵط������ý���
                ���3�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
            if i != ŦԼ.state and ŦԼ.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[ŦԼ.state] += ��·��
                ���3�¼�.append(f'���﷽��15��ŦԼ����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·�ѣ���ʣ{money[i]}Ԫ')

            if ŦԼ.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        ŦԼ.state = 3
                        ���3�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���3�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            if i == ŦԼ.state:  # ����
                ���4�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
            if i != ŦԼ.state and ŦԼ.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[ŦԼ.state] += ��·��
                ���4�¼�.append(f'���﷽��15��ŦԼ����Ҫ�����{ŦԼ.state}��{��·��}Ԫ��Ϊ��·�ѣ���ʣ{money[i]}Ԫ')
            if ŦԼ.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        ŦԼ.state = 4
                        ���4�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ���4�¼�.append(f'���﷽��15��ŦԼ����ʣ{money[i]}Ԫ')
    def ����16�ж�(i):
                            global money  # ����Ҫ��global���ܽӽ���
                            x�� = ����[16][0] + 1
                            x�� = x�� + 118
                            y�� = ����[16][1] + 1
                            y�� = y�� + 118
                            max = 0
                            t = 0
                            t0 = 0
                            temp = 0
                            for _ in money:
                                if money[t] > max:
                                    max = money[t]
                                    t0 = t
                                t += 1

                            if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
                                messagebox.showinfo("��ϲ", "��һҹ����")
                                messagebox.showinfo("��ʾ", f"�㽫�����{t0}����Ǯ��")
                                temp = money[i]
                                money[i] = money[t0]
                                money[t0] = temp
                                ���1�¼�.append(f'���﷽��16�������{t0}����Ǯ�ƣ���ʣ{money[i]}Ԫ')
                            if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
                                messagebox.showinfo("��ϲ", "��һҹ����")
                                messagebox.showinfo("��ʾ", f"�㽫�����{t0}����Ǯ��")
                                temp = money[i]
                                money[i] = money[t0]
                                money[t0] = temp
                                ���2�¼�.append(f'���﷽��16�������{t0}����Ǯ�ƣ���ʣ{money[i]}Ԫ')
                            if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
                                messagebox.showinfo("��ϲ", "��һҹ����")
                                messagebox.showinfo("��ʾ", f"�㽫�����{t0}����Ǯ��")
                                temp = money[i]
                                money[i] = money[t0]
                                money[t0] = temp
                                ���3�¼�.append(f'���﷽��16�������{t0}����Ǯ�ƣ���ʣ{money[i]}Ԫ')
                            if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
                                messagebox.showinfo("��ϲ", "��һҹ����")
                                messagebox.showinfo("��ʾ", f"�㽫�����{t0}����Ǯ��")
                                temp = money[i]
                                money[i] = money[t0]
                                money[t0] = temp
                                ���4�¼�.append(f'���﷽��16�������{t0}����Ǯ�ƣ���ʣ{money[i]}Ԫ')


    def ����17�ж�(i):  # Ӧ����xΪ1081-1200�ķ�Χ��yΪ121-239�ķ�Χ
            global money  # ����Ҫ��global���ܽӽ���
            x�� = ����[17][0] + 1
            x�� = x�� + 118
            y�� = ����[17][1] + 1
            y�� = y�� + 118
            if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
                money[1] += 200
                messagebox.showinfo("��ʾ", "���200Ԫ���")
                ���1�¼�.append(f'���﷽��17�����200Ԫ����ʣ{money[i]}Ԫ')
            if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
                messagebox.showinfo("��ʾ", "���200Ԫ���")
                money[2] += 200
                ���2�¼�.append(f'���﷽��17�����200Ԫ����ʣ{money[i]}Ԫ')

            if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
                messagebox.showinfo("��ʾ", "���200Ԫ���")
                money[3] += 200
                ���3�¼�.append(f'���﷽��17�����200Ԫ����ʣ{money[i]}Ԫ')
            if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
                messagebox.showinfo("��ʾ", "���200Ԫ���")
                money[4] += 200
                ���4�¼�.append(f'���﷽��17�����200Ԫ����ʣ{money[i]}Ԫ')
    def ����18�ж�(i):
            global money  # ����Ҫ��global���ܽӽ���
            x�� = ����[18][0] + 1
            x�� = x�� + 118
            y�� = ����[18][1] + 1
            y�� = y�� + 118
            if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
                messagebox.showinfo("��ʾ", "����Ҫ300Ԫ���ܴ��山����")
                money[1] = money[1] - 300
                ���1�¼�.append(f'���﷽��18���۳�200Ԫ����ʣ{money[i]}Ԫ')

            if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
                messagebox.showinfo("��ʾ", "����Ҫ300Ԫ���ܴ��山����")
                money[2] = money[2] - 300
                ���2�¼�.append(f'���﷽��18���۳�200Ԫ����ʣ{money[i]}Ԫ')
            if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
                messagebox.showinfo("��ʾ", "����Ҫ300Ԫ���ܴ��山����")
                money[3] = money[3] - 300
                ���3�¼�.append(f'���﷽��18���۳�200Ԫ����ʣ{money[i]}Ԫ')
            if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
                messagebox.showinfo("��ʾ", "����Ҫ300Ԫ���ܴ��山����")
                money[4] = money[4] - 300
                ���4�¼�.append(f'���﷽��18���۳�200Ԫ����ʣ{money[i]}Ԫ')
    def ����20�ж�(i):   # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[20][0] + 1
        x�� = x�� + 118
        y�� = ����[20][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            ���1�¼�.append(f'���﷽��20����������ʣ{money[i]}Ԫ')
            if i == ����.state:  # ����
                pass
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���1�¼�[-1] = f'���﷽��20������,�����{����.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ'
            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�
                        ����.state = 1
                        ���1�¼�[-1] = f'���﷽��20�����򱱾�,��ʣ{money[i]}Ԫ'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            ���2�¼�.append(f'���﷽��20����������ʣ{money[i]}Ԫ')
            if i == ����.state:
                pass
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���2�¼�[-1] = f'���﷽��20������,�����{����.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ'

            if ����.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        ����.state = 2
                        ���2�¼�[-1] = f'���﷽��20�����򱱾�,��ʣ{money[i]}Ԫ'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            ���3�¼�.append(f'���﷽��20����������ʣ{money[i]}Ԫ')
            if i == ����.state:  # �Լ��ĵط������ý���
                pass
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[����.state] += ��·��
                ���3�¼�[-1] = f'���﷽��20������,�����{����.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ'

            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        ����.state = 3
                        ���3�¼�[-1] = f'���﷽��20�����򱱾�,��ʣ{money[i]}Ԫ'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            ���4�¼�.append(f'���﷽��20����������ʣ{money[i]}Ԫ')
            if i == ����.state:  # ����
                pass
            if i != ����.state and ����.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{����.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[����.state] += ��·��
                ���4�¼�[-1] = f'���﷽��20������,�����{����.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}Ԫ'

            if ����.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        ����.state = 4
                        ���4�¼�[-1] = f'���﷽��20�����򱱾�,��ʣ{money[i]}Ԫ'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
    def ����21�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[21][0] + 1
        x�� = x�� + 118
        y�� = ����[21][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            messagebox.showinfo("��ʾ", "����Ⱦ����������350")
            money[i] = money[i] - 350
            ���1�¼�.append(f'������21��������Ⱦ����������350Ԫ����ʣ{money[i]}Ԫ')
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "����Ⱦ����������350")
            money[i] = money[i] - 350
            ���2�¼�.append(f'������21��������Ⱦ����������350Ԫ����ʣ{money[i]}Ԫ')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "����Ⱦ����������350")
            money[i] = money[i] - 350
            ���3�¼�.append(f'������21��������Ⱦ����������350Ԫ����ʣ{money[i]}Ԫ')
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "����Ⱦ����������350")
            money[i] = money[i] - 350
            ���4�¼�.append(f'������21��������Ⱦ����������350Ԫ����ʣ{money[i]}Ԫ')
    def ����22�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[22][0] + 1
        x�� = x�� + 118
        y�� = ����[22][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            ���1�¼�.append(f'���﷽��22,��Ժ')
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���1�¼�.append(f'���˹���,��ʣ{money[i]}Ԫ')
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���1�¼�.append(f'�������,��ʣ{money[i]}Ԫ')
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���1�¼�.append(f'�����Ϻ�,��ʣ{money[i]}Ԫ')
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���1�¼�.append(f'����ŦԼ,��ʣ{money[i]}Ԫ')
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���1�¼�.append(f'���˱���,��ʣ{money[i]}Ԫ')
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���1�¼�.append(f'�����׶�,��ʣ{money[i]}Ԫ')
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            ���2�¼�.append(f'���﷽��22,��Ժ')
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���2�¼�.append(f'���˹���,��ʣ{money[i]}Ԫ')
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���2�¼�.append(f'�������,��ʣ{money[i]}Ԫ')
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���2�¼�.append(f'�����Ϻ�,��ʣ{money[i]}Ԫ')
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���2�¼�.append(f'����ŦԼ,��ʣ{money[i]}Ԫ')
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���2�¼�.append(f'���˱���,��ʣ{money[i]}Ԫ')
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���2�¼�.append(f'�����׶�,��ʣ{money[i]}Ԫ')
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            ���3�¼�.append(f'���﷽��22,��Ժ')
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���3�¼�.append(f'���˹���,��ʣ{money[i]}Ԫ')
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���3�¼�.append(f'�������,��ʣ{money[i]}Ԫ')
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���3�¼�.append(f'�����Ϻ�,��ʣ{money[i]}Ԫ')
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���3�¼�.append(f'����ŦԼ,��ʣ{money[i]}Ԫ')
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���3�¼�.append(f'���˱���,��ʣ{money[i]}Ԫ')
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���3�¼�.append(f'�����׶�,��ʣ{money[i]}Ԫ')
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            ���4�¼�.append(f'���﷽��22,��Ժ')
            t = 0
            ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
            if ans:
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���4�¼�.append(f'�����׶�,��ʣ{money[i]}Ԫ')
                if ���.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ���.state = 0
                        ���4�¼�.append(f'�������,��ʣ{money[i]}Ԫ')
                if �Ϻ�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �Ϻ�.state = 0
                        ���4�¼�.append(f'�����Ϻ�,��ʣ{money[i]}Ԫ')
                if ŦԼ.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ŦԼ.state = 0
                        ���4�¼�.append(f'����ŦԼ,��ʣ{money[i]}Ԫ')
                if ����.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        ����.state = 0
                        ���4�¼�.append(f'���˱���,��ʣ{money[i]}Ԫ')
                if �׶�.state == i:
                    t += 1
                    ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                    if ans1:
                        money[i] += �ؼ�
                        �׶�.state = 0
                        ���4�¼�.append(f'�����׶�,��ʣ{money[i]}Ԫ')
                if t == 0:
                    messagebox.showinfo("��ʾ", "��û�з���")
    def ����23�ж�(i):
        x�� = ����[23][0] + 1
        x�� = x�� + 118
        y�� = ����[23][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            y = np.random.randint(1, 2)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ1_next()
            ���1�¼�.append(f'������ͷ,��ǰ��{y}��')
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            y = np.random.randint(1, 2)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ2_next()
            ���2�¼�.append(f'������ͷ,��ǰ��{y}��')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            y = np.random.randint(1, 2)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ3_next()
            ���3�¼�.append(f'������ͷ,��ǰ��{y}��')
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            y = np.random.randint(1, 3)
            messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
            for _ in range(y):
                ͼƬ4_next()
            ���4�¼�.append(f'������ͷ,��ǰ��{y}��')
    def ����24�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[24][0] + 1
        x�� = x�� + 118
        y�� = ����[24][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��150Ԫ������")
            money[i] = money[i] - 150
            ���1�¼�.append(f'���﷽��24,����150Ԫ,��ʣ{money[i]}')
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��150Ԫ������")
            money[i] = money[i] - 150
            ���2�¼�.append(f'���﷽��24,����150Ԫ,��ʣ{money[i]}')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��150Ԫ������")
            money[i] = money[i] - 150
            ���3�¼�.append(f'���﷽��24,����150Ԫ,��ʣ{money[i]}')

        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "�㻨��150Ԫ������")
            money[i] = money[i] - 150
            ���4�¼�.append(f'���﷽��24,����150Ԫ,��ʣ{money[i]}')
    def ����25�ж�(i):
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[25][0] + 1
        x�� = x�� + 118
        y�� = ����[25][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            messagebox.showinfo("��ʾ", "�������Ϊ������300Ԫ")
            money[1] = money[1] + 300
            ���1�¼�.append(f'���﷽��25,����150Ԫ,��ʣ{money[i]}')

        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            messagebox.showinfo("��ʾ", "�������Ϊ������300Ԫ")
            money[2] = money[2] + 300
            ���2�¼�.append(f'���﷽��25,����150Ԫ,��ʣ{money[i]}')
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            messagebox.showinfo("��ʾ", "�������Ϊ������300Ԫ")
            money[3] = money[3] + 300
            ���3�¼�.append(f'���﷽��25,����150Ԫ,��ʣ{money[i]}')
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            messagebox.showinfo("��ʾ", "�������Ϊ������300Ԫ")
            money[4] = money[4] + 300
            ���4�¼�.append(f'���﷽��25,����150Ԫ,��ʣ{money[i]}')
    def ����26�ж�(i):  # Ӧ����xΪ481-599�ķ�Χ��yΪ1-119�ķ�Χ
        global money  # ����Ҫ��global���ܽӽ���
        x�� = ����[26][0] + 1
        x�� = x�� + 118
        y�� = ����[26][1] + 1
        y�� = y�� + 118
        if i == 1 and x�� <= x1 <= x�� and y�� <= y1 <= y��:
            ���1�¼�.append(f'���﷽��26,�׶�,��ʣ{money[i]}')
            if i == �׶�.state:  # ����
                pass
            if i != �׶�.state and �׶�.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�׶�.state] += ��·��
                ���1�¼�[-1] = f'���﷽��26,�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}'

            if �׶�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[1] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[1] -= �ؼ�
                        �׶�.state = 1
                        ���1�¼�[-1] = f'���﷽��26,�����׶�,��ʣ{money[i]}'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 2 and x�� <= x2 <= x�� and y�� <= y2 <= y��:
            ���2�¼�.append(f'���﷽��26,�׶�,��ʣ{money[i]}')
            if i == �׶�.state:
                pass
            if i != �׶�.state and �׶�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�׶�.state] += ��·��
                ���2�¼�[-1] = f'���﷽��26,�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}'

            if �׶�.state == 0:
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[2] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[2] -= �ؼ�
                        �׶�.state = 2
                        ���2�¼�[-1] = f'���﷽��26,�����׶�,��ʣ{money[i]}'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 3 and x�� <= x3 <= x�� and y�� <= y3 <= y��:
            ���3�¼�.append(f'���﷽��26,�׶�,��ʣ{money[i]}')
            if i == �׶�.state:  # �Լ��ĵط������ý���
                pass
            if i != �׶�.state and �׶�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��")  # ����
                money[i] -= ��·��
                money[�׶�.state] += ��·��
                ���3�¼�[-1] = f'���﷽��26,�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}'
            if �׶�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[3] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[3] -= �ؼ�
                        �׶�.state = 3
                        ���3�¼�[-1] = f'���﷽��26,�����׶�,��ʣ{money[i]}'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
        if i == 4 and x�� <= x4 <= x�� and y�� <= y4 <= y��:
            ���4�¼�.append(f'���﷽��26,�׶�,��ʣ{money[i]}')
            if i == �׶�.state:  # ����
                pass
            if i != �׶�.state and �׶�.state != 0:
                messagebox.showinfo("��ʾ", f"����Ҫ�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[�׶�.state] += ��·��
                ���4�¼�[-1] = f'���﷽��26,�����{�׶�.state}��{��·��}Ԫ��Ϊ��·��,��ʣ{money[i]}'

            if �׶�.state == 0:  # ���
                ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                if ans:
                    if money[4] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[4] -= �ؼ�
                        �׶�.state = 4
                        ���4�¼�[-1] = f'���﷽��26,�����׶�,��ʣ{money[i]}'
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")

    # start=time.time()
    ����10�ж�(i)
    ����14�ж�(i)
    ����23�ж�(i)
    #1�����
    ����2�ж�(i)
    ����3�ж�(i)
    ����4�ж�(i)
    ����5�ж�(i)
    ����6�ж�(i)
    ����7�ж�(i)
    ����8�ж�(i)
    ����9�ж�(i)
    #10��
    ����11�ж�(i)
    ����12�ж�(i)
    ����13�ж�(i)
    #14��
    ����15�ж�(i)
    ����16�ж�(i)
    ����17�ж�(i)
    ����18�ж�(i)
    #19�ǹ�԰
    ����20�ж�(i)
    ����21�ж�(i)
    ����22�ж�(i)
    #23��
    ����24�ж�(i)
    ����25�ж�(i)
    ����26�ж�(i)

    �Ʋ��ж�()
    # end=time.time()
    # print(f'���жϺ���ִ������{end-start}��')
class ͼƬ:
    def __init__(root,·��,λ��,��С):
        root.·��=·��
        root.λ��=λ��
        root.��С=��С
        root.lst=[]
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a =root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0],y=λ��[1])
    def replace(root,��λ��):
        root.lst[-1].place(x=��λ��[0],y=��λ��[1])
    def ��ͼƬ(root,���):
        root.lst[-1].destroy()
        root.lst.pop()
        root.����1a = Image.open(��ɫͼƬ�ļ�·��[���])  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((root.��С[0], root.��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=root.λ��[0], y=root.λ��[1])
    def ������·��(root,·��,i):
        root.lst[-1].destroy()
        root.lst.pop()
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((root.��С[0], root.��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        if i==1:
            root.lst[-1].place(x=x1, y=y1)
        if i==2:
            root.lst[-1].place(x=x2, y=y2)
        if i==3:
            root.lst[-1].place(x=x3, y=y3)
        if i==4:
            root.lst[-1].place(x=x4, y=y4)
    def ����(root):
        root.lst[-1].destroy()
def ��ͷˢ��(i):
    ��ͷ.replace((����[i][0]+25,����[i][1]+120))
class ͼƬ��ť:
    def __init__(root, ·��, λ��, ��С,����):
        root.·�� = ·��
        root.λ�� = λ��
        root.��С = ��С
        root.lst = []
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = tk.Button(image=root.����1b,command=����)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0], y=λ��[1])
class ͼƬ2:
    def __init__(root,·��,λ��):
        root.·��=·��
        root.λ��=λ��
        if ·��!=None:
            root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
            root.����1a =root.����1a.resize((110, 110))  # �涨ͼƬ��С
            root.����1b = ImageTk.PhotoImage(root.����1a)
            root.����1c = ttk.Label(image=root.����1b)
            root.����1c.place(x=����[λ��][0]+5,y=����[λ��][1]+5)   #��λ�þ�������ı��
        if ·��==None:
            root.����=tk.Label(text=λ��,font=12)
            root.����.place(x=����[λ��][0]+50,y=����[λ��][1]+50)
        w1.create_line(����[λ��][0],����[λ��][1],����[λ��][0]+120,����[λ��][1],width=5)
        w1.create_line(����[λ��][0], ����[λ��][1], ����[λ��][0], ����[λ��][1]+120, width=5)
        w1.create_line(����[λ��][0]+120, ����[λ��][1], ����[λ��][0] + 120, ����[λ��][1]+120, width=5)
        w1.create_line(����[λ��][0], ����[λ��][1]+120, ����[λ��][0] + 120, ����[λ��][1]+120, width=5)
class ����:
    def __init__(root,λ��,�ֺ�,����):
        root.λ��=λ��
        root.�ֺ�=�ֺ�
        root.����=����
        root.����=tk.Label(text=����,font=�ֺ�)
        root.����.place(x=λ��[0],y=λ��[1])
    def ����(root,����):
        root.����.destroy()
        root.���� = tk.Label(text=����, font=root.�ֺ�)
        root.����.place(x=root.λ��[0], y=root.λ��[1])
class �����ؼ�:
    def __init__(self,lst):
        ������ҳ�� = tk.Tk()
        # bttrt=tk.Button(������ҳ��)   #ģ������ѹ������ӵ�����ȥ
        # bttrt.pack()

        self.scrollbar_v = Scrollbar(������ҳ��)
        self.scrollbar_v.pack(side=RIGHT, fill=Y)                    #�ҹ�����
        self.scrollbar_h = Scrollbar(������ҳ��,orient=HORIZONTAL)     #ˮƽ������
        self.scrollbar_h.pack(side=BOTTOM, fill=X)
        self.text = Text(������ҳ��,width=40, height=40)
        self.text.config(yscrollcommand=self.scrollbar_v.set)  # text�󶨴�ֱ������
        self.text.config(xscrollcommand=self.scrollbar_h.set)  # text��ˮƽ������
        self.text.pack(expand=YES, fill=BOTH)

        for i in range(len(lst)):
            self.text.insert("end", lst[i]+"\n")

        self.scrollbar_v.config(command=self.text.yview)  # ��ֱ��������text
        self.scrollbar_h.config(command=self.text.xview)  # ˮƽ��������text

# ��������=�����ؼ�()
# ����25=ͼƬ("��ϷͼƬ/������Ϊ������300Ԫ.png",(3,243))
����1=ͼƬ2("��ϷͼƬ/���.png",1)
����2=ͼƬ2("��ϷͼƬ/����.png",2)
����3=ͼƬ2("��ϷͼƬ/�ݳ���.png",3)
����4=ͼƬ2("��ϷͼƬ/���.png",4)
����5=ͼƬ2("��ϷͼƬ/200���.png",5)
����6=ͼƬ2("��ϷͼƬ/�Ĳ��ֽ����.png",6)
����7=ͼƬ2("��ϷͼƬ/��԰1.png",7)
����8=ͼƬ2("��ϷͼƬ/��Ժ.png",8)
����9=ͼƬ2("��ϷͼƬ/������.png",9)
����10=ͼƬ2("��ϷͼƬ/�ɻ�.png",10)
����11=ͼƬ2("��ϷͼƬ/200���.png",11)
����12=ͼƬ2("��ϷͼƬ/����թƭ.png",12)
����13=ͼƬ2("��ϷͼƬ/�Ϻ�.png",13)
����14=ͼƬ2("��ϷͼƬ/����.jpg",14)
����15=ͼƬ2("��ϷͼƬ/ŦԼ.png",15)
����16=ͼƬ2("��ϷͼƬ/һҹ����.png",16)
����17=ͼƬ2("��ϷͼƬ/200���.png",17)
����18=ͼƬ2("��ϷͼƬ/�山.png",18)
����19=ͼƬ2("��ϷͼƬ/��԰2.png",19)
����20=ͼƬ2("��ϷͼƬ/����.png",20)
����21=ͼƬ2("��ϷͼƬ/������Ⱦ����.png",21)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
����22=ͼƬ2("��ϷͼƬ/��Ժ.png",22)
����23=ͼƬ2("��ϷͼƬ/�ִ�.jpg",23)
����24=ͼƬ2("��ϷͼƬ/2018.png",24)
����25=ͼƬ2("��ϷͼƬ/������Ϊ������300Ԫ.png",25)
����26 = ͼƬ2("��ϷͼƬ/�׶�.png", 26)

��ͷ = ͼƬ("��ϷͼƬ/���ϼ�ͷ.png", (����[1][0], ����[1][1] + 120), (35, 35))
��ʾͼƬ1 = ͼƬ(��ɫͼƬ�ļ�·��[1], (����[3][0], ����[3][1] + 240), (125, 125))
����1=����((����[3][0],����[3][1]+160),32,"�����ֵ����1")
����ͼƬ1=ͼƬ(r"C:\Users\liuzc\Desktop\python����\games\��ϷͼƬ\����ͼƬ1.png", (����[6][0], ����[6][1] + 120),(125, 230))
��������ͼƬ=ͼƬ(r"C:\Users\liuzc\Desktop\python����\games\��ϷͼƬ\��������.png", (����[7][0]+10, ����[7][1] + 120),(300, 230))
��Ǯ��Ϣ1=����((����[4][0]+10,����[4][1]+260),32,"���1���ʽ�Ϊ��1200")
�ز���Ϣ1=����((����[4][0]+10,����[4][1]+290),32,"���1�ĵز���\n")
�ز���Ϣ2=����((����[4][0]+10,����[4][1]+330),32,"")
����������=����((����[13][0]+120,0),32,"ʵʱ������")
�����������嵥=[]
������ͼƬ�嵥=[]
�����������嵥.append(����((����������.λ��[0],����������.λ��[1]+75),32,"NO.1�����1\n �ʽ�1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[1],(����������.λ��[0]+180,����������.λ��[1]+75),(50,50)))
�����������嵥.append(����((����������.λ��[0],����������.λ��[1]+200),32,"NO.2�����2\n �ʽ�: 1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[2],(����������.λ��[0]+180,����������.λ��[1]+200),(50,50)))

�����������嵥.append(����((����������.λ��[0],����������.λ��[1]+325),32,"NO.3:���3\n �ʽ�:1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[3],(����������.λ��[0]+180,����������.λ��[1]+325),(50,50)))

�����������嵥.append(����((����������.λ��[0],����������.λ��[1]+450),32,"NO.4:���4\n �ʽ�:1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[4],(����������.λ��[0]+180,����������.λ��[1]+450),(50,50)))
def ����ˢ��(i):
    ����1.����(f"�����ֵ����{i}")
    if �Ʋ�[i]==1:
        ����1.����(f"�����ֵ����{i}(���Ʋ���")
    ��Ǯ��Ϣ1.����(f"���{i}���ʽ�Ϊ:{money[i]}")
    �ز���Ϣ1.����(f"���{i}�ĵز���:")
    �ز���Ϣ2.����(���˵ز���ʾ(i))
def ���������():
    ����=bubble_sort(money)
    for _ in range(len(����)):
        �����������嵥[_].����(f"No.{_+1}:���{����[_]}\n �ʽ�: {money[����[_]]}")
        ������ͼƬ�嵥[_].��ͼƬ(����[_])


��ɫ1=ͼƬ(��ɫͼƬ�ļ�·��[1],(x1,y1),(47,47))
��ɫ2=ͼƬ(��ɫͼƬ�ļ�·��[2],(x2,y2),(47,47))
��ɫ3=ͼƬ(��ɫͼƬ�ļ�·��[3],(x3,y3),(47,47))
��ɫ4=ͼƬ(��ɫͼƬ�ļ�·��[4],(x4,y4),(47,47))

def ��ӽ�Ǯ��¼(i):
    global money
    if i==1 and �Ʋ�[1]==0:
        ���1��Ǯ��¼.append(money[1])
    if i==2 and �Ʋ�[2]==0:
        ���2��Ǯ��¼.append(money[2])
    if i==3 and �Ʋ�[3]==0:
        ���3��Ǯ��¼.append(money[3])
    if i==4 and �Ʋ�[4]==0:
        ���4��Ǯ��¼.append(money[4])
def main():
    global stateall,state1,state2,state3,state4
    global �Ʋ�
    if stateall%4==0:    #���1�غ�
        if �Ʋ�[1]==0:
            �ƶ�ͼƬ1()
            ��ͷˢ��(state1)
            �ж�(1)
        ��ͷˢ��(state2)
        ��ʾͼƬ1.��ͼƬ(2)
        ����ˢ��(2)
        ���������()
        # tk.Label(root, text=f'�ֵ����{stateall % 4 + 2}', font=24).place(x=320, y=150)
    if stateall%4==1:            #���2�غ�
        if �Ʋ�[2]==0:
            �ƶ�ͼƬ2()
            ��ͷˢ��(state2)
            �ж�(2)
        ��ͷˢ��(state3)
        ��ʾͼƬ1.��ͼƬ(3)
        ����ˢ��(3)
        ���������()
    if stateall%4==2:       #���3�غ�
        if �Ʋ�[3]==0:
            �ƶ�ͼƬ3()
            ��ͷˢ��(state3)
            �ж�(3)
        ��ͷˢ��(state4)
        ��ʾͼƬ1.��ͼƬ(4)
        ����ˢ��(4)
        ���������()
    if stateall%4==3:       #���4�غ�
        if �Ʋ�[4]==0:
            �ƶ�ͼƬ4()
            ��ͷˢ��(state4)
            �ж�(4)
        ��ͷˢ��(state1)
        ��ʾͼƬ1.��ͼƬ(1)
        ����ˢ��(1)
        ���������()
    stateall+=1
    ��ӽ�Ǯ��¼(stateall%4+1)

def ����():
    import numpy as np
    import tkinter
    import tkinter.messagebox  # ������
    y = np.random.randint(1, 7)   # ��Χ1-9��������10������������
    tkinter.messagebox.showinfo('����', f'����Ϊ{y}')  # ǰ���ͷ����������
    return y
def ͼƬ1_next():
        global state1, x1, y1
        state1 += 1
        if state1 == 27:
            state1 = 1
        x1 = ����[state1][0] + 1
        y1 = ����[state1][1] + 1
        ��ɫ1.replace((x1,y1))
def �ƶ�ͼƬ1():
    t=����()
    for x in range(t):
        ͼƬ1_next()

def ͼƬ2_next():
        global state2
        global x2
        global y2
        state2 += 1
        if state2 == 27:
            state2 = 1
        x2 = ����[state2][0] + 51
        y2 = ����[state2][1] + 1
        ��ɫ2.replace((x2,y2))
def �ƶ�ͼƬ2():
    t=����()
    for x in range(t):
        ͼƬ2_next()
def ͼƬ3_next():
        global state3
        global x3
        global y3
        state3 += 1
        if state3 == 27:
            state3 = 1
        x3 = ����[state3][0] + 1
        y3 = ����[state3][1] + 51
        ��ɫ3.replace((x3,y3))
def �ƶ�ͼƬ3():
    t=����()
    for x in range(t):
        ͼƬ3_next()
def ͼƬ4_next():
        global state4
        global x4
        global y4
        state4 += 1
        if state4 == 27:
            state4 = 1
        x4 = ����[state4][0] + 51
        y4 = ����[state4][1] + 51
        ��ɫ4.replace((x4,y4))
def �ƶ�ͼƬ4():
    t=����()
    for x in range(t):
        ͼƬ4_next()
������ť=ͼƬ��ť("��ϷͼƬ/������ť.png",(����[18][0],����[18][1]-100),(120,100),main)

root.mainloop()

����ҳ��=tk.Tk()
����ҳ��.geometry("500x600")
����ҳ��.title="����ҳ��"
����1a = Image.open("��ϷͼƬ/����ҳ��.png")  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
����1a =����1a.resize((500, 600))  # �涨ͼƬ��С
����1b = ImageTk.PhotoImage(����1a)
����1c = ttk.Label(image=����1b)
����1c.place(x=0,y=0)
def �������һ��Ǯͼ��():
    y=���1��Ǯ��¼
    print(y)
    x=list(map(lambda x:x,range(len(���1��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x,���1��Ǯ��¼)
    plt.show()
bt1=tk.Button(text="���һ�¼�",command=���1��Ϣ��ѯ����).place(x=200,y=300)
bt5=tk.Button(text="���һ��Ǯ�仯",command=�������һ��Ǯͼ��).place(x=200,y=350)
def ������Ҷ���Ǯͼ��():
    y=���2��Ǯ��¼
    print(y)
    x=list(map(lambda x:x,range(len(���2��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x,���2��Ǯ��¼)
    plt.show()
bt2=tk.Button(text="��Ҷ��¼�",command=���2��Ϣ��ѯ����).place(x=300,y=300)
bt6=tk.Button(text="��Ҷ���Ǯ�仯",command=������Ҷ���Ǯͼ��).place(x=300,y=350)
def �����������Ǯͼ��():
    y=���3��Ǯ��¼
    print(y)
    x=list(map(lambda x:x,range(len(���3��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x,���3��Ǯ��¼)
    plt.show()
bt3=tk.Button(text="������¼�",command=���3��Ϣ��ѯ����).place(x=200,y=400)
bt7=tk.Button(text="�������Ǯ�仯",command=�����������Ǯͼ��).place(x=200,y=450)
def ��������Ľ�Ǯͼ��():
    y=���4��Ǯ��¼
    print(y)
    x=list(map(lambda x:x,range(len(���4��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x,���4��Ǯ��¼)
    plt.show()
bt4=tk.Button(text="������¼�",command=���4��Ϣ��ѯ����).place(x=300,y=400)
bt8=tk.Button(text="����Ľ�Ǯ�仯",command=��������Ľ�Ǯͼ��).place(x=300,y=450)



����ҳ��.mainloop()