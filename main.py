# coding=gbk
# 2024/8/13�����е��жϷ���ͳһ��װ��ʡ�˼�����
# 2024/11/6���жϷ�����װ����ʡ�˼�����
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

# ��һ���֣�����ҳ������
��ʼҳ�� = tk.Tk()
��ʼҳ��.geometry("500x600")

��ʼҳ��state = 0
��ʼҳ��.����1a = Image.open("��ϷͼƬ/���̷���.png")  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
��ʼҳ��.����1a = ��ʼҳ��.����1a.resize((500, 600))  # �涨ͼƬ��С
��ʼҳ��.����1b = ImageTk.PhotoImage(��ʼҳ��.����1a)
��ʼҳ��.����1c = ttk.Label(image=��ʼҳ��.����1b)
��ʼҳ��.����1c.place(x=0, y=0)


def �˳�():
    quit()


class ͼƬ��ť:
    def __init__(��ʼҳ��, ·��, λ��, ��С, ����):
        ��ʼҳ��.·�� = ·��
        ��ʼҳ��.λ�� = λ��
        ��ʼҳ��.��С = ��С
        ��ʼҳ��.lst = []
        ��ʼҳ��.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        ��ʼҳ��.����1a = ��ʼҳ��.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        ��ʼҳ��.����1b = ImageTk.PhotoImage(��ʼҳ��.����1a)
        ��ʼҳ��.����1c = tk.Button(image=��ʼҳ��.����1b, command=����)
        ��ʼҳ��.lst.append(��ʼҳ��.����1c)
        ��ʼҳ��.lst[-1].place(x=λ��[0], y=λ��[1])
global ai_
ai_=[]
def ��ʼ��Ϸ1():
    global ��ʼҳ��state,ai_
    ��ʼҳ��.destroy()
    ��ʼҳ��state = 1
    ai_=[0,0,1,1,1]
def ��ʼ��Ϸ2():
    global ��ʼҳ��state,ai_
    ��ʼҳ��.destroy()
    ��ʼҳ��state = 1
    ai_ = [0, 0, 0, 1, 1]
def ��ʼ��Ϸ3():
    global ��ʼҳ��state,ai_
    ��ʼҳ��.destroy()
    ��ʼҳ��state = 1
    ai_ = [0, 0, 0, 0, 0]
��ʼ��Ϸ��ť1 = ͼƬ��ť("��ϷͼƬ/������Ϸ.png", (50, 200), (120, 60), ��ʼ��Ϸ1)
��ʼ��Ϸ��ť2 = ͼƬ��ť("��ϷͼƬ/˫����Ϸ.png", (50, 275), (120, 60), ��ʼ��Ϸ2)
��ʼ��Ϸ��ť3 = ͼƬ��ť("��ϷͼƬ/������Ϸ.png", (50, 350), (120, 60), ��ʼ��Ϸ3)
�˳���Ϸ��ť = ͼƬ��ť("��ϷͼƬ/�˳���Ϸ.png", (330, 350), (120, 60), �˳�)
��ʼҳ��.mainloop()
if ��ʼҳ��state == 0:
    quit()

# 1200x600,ÿ��10����ÿ��5����ÿ����120*120
root = tk.Tk()
root.geometry("1600x750")  # ���˿�
w1 = Canvas(root, width=1200, height=650, background='blue')
w1.place(x=0, y=0)

# ��ʼ����Ǯ
global money
money = [0, 1200, 1200, 1200, 1200]  # �������б����洢��
���1��Ǯ��¼ = [money[1]]
���2��Ǯ��¼ = [money[2]]
���3��Ǯ��¼ = [money[3]]
���4��Ǯ��¼ = [money[4]]
global �Ʋ�, �Ʋ�����
�Ʋ����� = 0
�Ʋ� = [1, 0, 0, 0, 0]  # �����Ʋ�״̬
global ����¼�
����¼� = []
for _ in range(5):
    ����¼�.append([])
����¼�[1] = []
����¼�[2] = []
����¼�[3] = []
����¼�[4] = []


class ����ť:
    def __init__(root, x, y, �ı�):
        root.�ı� = �ı�
        root.x = x
        root.y = y
        root.�ӽ�� = []
        root.state = 0
        global y0
        y0 = y

        def չʾ�Ӱ�ť():
            global bt, ��ť���
            if len(bt) == 0:  # bt�ǰ�ť��ջ����ջΪ�գ�˵��û�а�ť��չ��
                root.state = 0  # ��ť��state��ʾ���ǰ�ť�Ƿ��Ѿ������¹���state=0ʱ�������ť��չ����state=1ʱ���۵���
            else:
                ��ť��� = 0  # ��ť���������ǰ�ť��������ջ��ջ
            if root.state == 0:
                if len(bt) > 0:  # ���б�ĸ���ť����չ��״̬����գ�������֤��������
                    for _ in range(len(bt)):
                        bt[_][1].destroy()
                bt.clear()
                for _ in range(len(root.�ӽ��)):  # ����չ���Լ����ӽڵ�
                    ��ť��� += 1
                    root.�ӽ��[_].x = x
                    root.�ӽ��[_].y = 27 * _ + 30  # ���ӽڵ�õ�λ�ã�����鿴
                    root.�ӽ��[_].��� = ��ť���
                    if len(root.�ӽ��[_].�ӽ��) > 0:
                        root.�ӽ��[_].���� += ">"
                    root.�ӽ��[_].���� = root.�ӽ��[_].����.ljust(20, " ")  # �����ӽڵ�
                    b = tk.Button(text=root.�ӽ��[_].����, command=root.�ӽ��[_].����)  # Ϊ�ӽڵ㴫��
                    bt.append((��ť���, b))  # ��ջ���������ӽڵ�
                    bt[-1][1].place(x=root.x, y=27 * _ + 30)
                root.state += 1
                # print(root.x)
            elif root.state == 1:  # state=1��˼���ٵ�����۵�
                ��ť��� = 0  # ���ð�ť��Ų��������������ظ�չ��
                for _ in root.�ӽ��:  # ���ӽڵ㶼����Ϊû�������״̬
                    _.state = 0
                for _ in range(len(bt)):  # ��ջ����ջ���Ƴ��Ӱ�ť���ﵽ�۵���Ч��
                    bt[-1 - _][1].destroy()
                root.state = 0

                bt.clear()  # ���ջ��Ϊ�´�չ��׼��
                # print(bt)

        root.��ť = tk.Button(text=�ı� + ">", command=չʾ�Ӱ�ť, height=1)
        root.��ť.place(x=x, y=y)


class �Ӱ�ť:
    def __init__(root, ����, ����ť, ����):
        root.���� = ����
        root.���� = ����
        root.�ӽ�� = []
        root.state = 0
        root.x = 0
        root.y = 0
        root.��� = 0

        def չʾ�Ӱ�ť():
            global bt, ��ť���
            if root.��� == 0:
                ��ť��� += 1  # ���������������������ջ
                root.��� = ��ť���
            if root.��� == len(bt):
                root.state = 0  # �����Ӱ�ť
            if root.state == 0:
                for _ in range(len(root.�ӽ��)):
                    root.�ӽ��[_].x = root.x + 80  # �Ӱ�ťλ�ã����Ӱ�ť�͸���ť��
                    root.�ӽ��[_].y = root.y + _ * 27  # �Ӱ�ťλ�ã����Ӱ�ť�͸���ť��
                    b = tk.Button(text=root.�ӽ��[_].����, command=root.�ӽ��[_].����)  # �����Ӱ�ť����
                    bt.append((��ť���, b))  # ��ջ�洢�Ӱ�ť�������
                    bt[-1][1].place(x=root.x + 100, y=root.y + _ * 27)
                root.state += 1  # չ�����ٵ���ͱ���۵�״̬
            elif root.state == 1:
                for _ in root.�ӽ��:
                    _.state = 0
                Ҫ��ȥ�İ�ť���� = len(bt) - root.���  # ��˼�ǰ��Լ����Ӱ�ť���۵��ˣ������������ĸ���ť�����۵�
                for _ in range(Ҫ��ȥ�İ�ť����):
                    bt[-1][1].destroy()  # ��ջ��ȥ���Ӱ�ť
                    bt.pop()  # ��ջ
                root.state = 0  # ���ð�ť

        if root.���� == None:
            root.���� = չʾ�Ӱ�ť
        ����ť.�ӽ��.append(root)


class ͼƬ��ť:
    def __init__(root, ·��, λ��, ��С, ����):
        root.·�� = ·��
        root.λ�� = λ��
        root.��С = ��С
        root.lst = []
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = tk.Button(image=root.����1b, command=����)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0], y=λ��[1])

global bt, ��ť���
bt = []
��ť��� = 0

def ��տؼ�():
    global bt
    for i in bt:
        i[1].destroy()
    bt.clear()

def ��ת������ҳ��():
    root.destroy()

def �޸����1��Ǯ():
    if �Ʋ�[1] == 1:
        messagebox.showinfo("��ʾ", f"���{1}���Ʋ�")
    if �Ʋ�[1] != 1:
        y = askinteger("", "����Ǯ")
        if y != None:
            money[1] = y
            ����¼�[1].append(f"��Ǯ���޸ĵ�{money[1]}Ԫ")
        if stateall == 0:
            ����ˢ��(1)
        ���������()
        ��տؼ�()


def �޸����2��Ǯ():
    if �Ʋ�[2] == 1:
        messagebox.showinfo("��ʾ", f"���{2}���Ʋ�")
    if �Ʋ�[2] != 1:
        y = askinteger("", "����Ǯ��")
        if y != None:
            money[2] = y
        if stateall == 1:
            ����ˢ��(2)
        ���������()
        ��տؼ�()


def �޸����3��Ǯ():
    if �Ʋ�[3] == 1:
        messagebox.showinfo("��ʾ", f"���{3}���Ʋ�")
    if �Ʋ�[3] != 1:
        y = askinteger("", "����Ǯ��")
        if y != None:
            money[3] = y
        if stateall == 2:
            ����ˢ��(3)
        ���������()
        ��տؼ�()


def �޸����4��Ǯ():
    if �Ʋ�[4] == 1:
        messagebox.showinfo("��ʾ", f"���{4}���Ʋ�")
    if �Ʋ�[4] != 1:
        y = askinteger("", "����Ǯ��")
        if y != None:
            money[4] = y
        if stateall == 3:
            ����ˢ��(4)
        ���������()
        ��տؼ�()


def �޸����1ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("��ʾ", "���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[1] = file_path
        ��ɫ[0].������·��(file_path, 1)
    ��տؼ�()


def �޸����2ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("��ʾ", "���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[2] = file_path
        ��ɫ[1].������·��(file_path, 2)
    ��տؼ�()


def �޸����3ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("��ʾ", "���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[3] = file_path
        ��ɫ[2].������·��(file_path, 3)
    ��տؼ�()


def �޸����4ͷ�񷽷�():
    file_path = filedialog.askopenfilename()
    newfile_path = file_path.split(".")
    if newfile_path[-1] not in ["png", "jepg", "jpg"]:
        messagebox.showinfo("��ʾ", "���򿪵Ĳ���ͼƬ")
    else:
        ��ɫͼƬ�ļ�·��[4] = file_path
        ��ɫ[3].������·��(file_path, 4)
    ��տؼ�()


def ���1��Ϣ��ѯ����():
    print(����¼�[1])
    a = �����ؼ�(����¼�[1])

    try:
        ��տؼ�()
    except:
        pass


def ���2��Ϣ��ѯ����():
    a = �����ؼ�(����¼�[2])
    ��տؼ�()


def ���3��Ϣ��ѯ����():
    a = �����ؼ�(����¼�[3])
    ��տؼ�()


def ���4��Ϣ��ѯ����():
    a = �����ؼ�(����¼�[4])
    ��տؼ�()


def �޸����ؼ۸񷽷�():
    global �ؼ�
    y = askinteger("", '����Ǯ��')
    if y != None:
        �ؼ� = y
    ��տؼ�()


def �޸Ĺ�·�ѷ���():
    global ��·��
    y = askinteger("", '����Ǯ��')
    if y != None:
        ��·�� = y
    ��տؼ�()


def ������Ϣ��ѯ����1():
    if ����.state == 0:
        tk.messagebox.showinfo("��ʾ", "����Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"����Ŀǰ�����{����.state}����")
    ��տؼ�()


def ������Ϣ��ѯ����2():
    if ���.state == 0:
        tk.messagebox.showinfo("��ʾ", "���Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"���Ŀǰ�����{���.state}����")
    ��տؼ�()


def ������Ϣ��ѯ����3():
    if �Ϻ�.state == 0:
        tk.messagebox.showinfo("��ʾ", "�Ϻ�Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"�Ϻ�Ŀǰ�����{�Ϻ�.state}����")
    ��տؼ�()


def ������Ϣ��ѯ����4():
    if ŦԼ.state == 0:
        tk.messagebox.showinfo("��ʾ", "ŦԼĿǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"ŦԼĿǰ�����{ŦԼ.state}����")
    ��տؼ�()


def ������Ϣ��ѯ����5():
    if ����.state == 0:
        tk.messagebox.showinfo("��ʾ", "����Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"����Ŀǰ�����{����.state}����")
    ��տؼ�()


def ������Ϣ��ѯ����6():
    if �׶�.state == 0:
        tk.messagebox.showinfo("��ʾ", "�׶�Ŀǰ����")
    else:
        tk.messagebox.showinfo("��ʾ", f"�׶�Ŀǰ�����{�׶�.state}����")
    ��տؼ�()


def ��������Ϣ��ʾ����():
    messagebox.showinfo("��ʾ", "2022210993��پ��")
    ��տؼ�()


def ��ʾͼ��():

    a = Image.open("��ϷͼƬ/ͼ��.png")
    a.show()
    ��տؼ�()

�ļ� = ����ť(0, 0, "�ļ�                   ")
�༭ = ����ť(120, 0, "�༭                   ")
�˳���ť = �Ӱ�ť("�˳���Ϸ   ", �ļ�, �˳�)
�򿪽���ҳ�水ť = �Ӱ�ť("��ת������ҳ��  ", �ļ�, ��ת������ҳ��)

�޸����ؼ۸� = �Ӱ�ť("�޸����ؼ۸�", �༭, �޸����ؼ۸񷽷�)
�޸Ĺ�·�� = �Ӱ�ť("�޸Ĺ�·��", �༭, �޸Ĺ�·�ѷ���)
�޸���ҽ�Ǯ��ť = �Ӱ�ť("�޸���ҽ�Ǯ", �༭, None)
�޸����1��Ǯ��ť = �Ӱ�ť("���1", �޸���ҽ�Ǯ��ť, �޸����1��Ǯ)
�޸����2��Ǯ��ť = �Ӱ�ť("���2", �޸���ҽ�Ǯ��ť, �޸����2��Ǯ)
�޸����3��Ǯ��ť = �Ӱ�ť("���3", �޸���ҽ�Ǯ��ť, �޸����3��Ǯ)
�޸����4��Ǯ��ť = �Ӱ�ť("���4", �޸���ҽ�Ǯ��ť, �޸����4��Ǯ)

�޸����ͷ��ť = �Ӱ�ť("�޸����ͷ��", �༭, None)
�޸����1ͷ��ť = �Ӱ�ť("���1", �޸����ͷ��ť, �޸����1ͷ�񷽷�)
�޸����2ͷ��ť = �Ӱ�ť("���2", �޸����ͷ��ť, �޸����2ͷ�񷽷�)
�޸����3ͷ��ť = �Ӱ�ť("���3", �޸����ͷ��ť, �޸����3ͷ�񷽷�)
�޸����4ͷ��ť = �Ӱ�ť("���4", �޸����ͷ��ť, �޸����4ͷ�񷽷�)

�����Ϣ��ѯ = ����ť(240, 0, "�����Ϣ��ѯ       ")
���1��Ϣ��ѯ��ť = �Ӱ�ť("���1", �����Ϣ��ѯ, ���1��Ϣ��ѯ����)
���2��Ϣ��ѯ��ť = �Ӱ�ť("���2", �����Ϣ��ѯ, ���2��Ϣ��ѯ����)
���3��Ϣ��ѯ��ť = �Ӱ�ť("���3", �����Ϣ��ѯ, ���3��Ϣ��ѯ����)
���4��Ϣ��ѯ��ť = �Ӱ�ť("���4", �����Ϣ��ѯ, ���4��Ϣ��ѯ����)

�ز���Ϣ��ѯ = ����ť(360, 0, "�ز���Ϣ��ѯ       ")
��ѯ���� = �Ӱ�ť("����", �ز���Ϣ��ѯ, ������Ϣ��ѯ����1)
��ѯ��� = �Ӱ�ť("���", �ز���Ϣ��ѯ, ������Ϣ��ѯ����2)
��ѯ�Ϻ� = �Ӱ�ť("�Ϻ�", �ز���Ϣ��ѯ, ������Ϣ��ѯ����3)
��ѯŦԼ = �Ӱ�ť("ŦԼ", �ز���Ϣ��ѯ, ������Ϣ��ѯ����4)
��ѯ���� = �Ӱ�ť("����", �ز���Ϣ��ѯ, ������Ϣ��ѯ����5)
��ѯ�׶� = �Ӱ�ť("�׶�", �ز���Ϣ��ѯ, ������Ϣ��ѯ����6)

���� = ����ť(480, 0, "����                  ")
ͼ����ť = �Ӱ�ť("ͼ��", ����, ��ʾͼ��)
�������ϸ�ڰ�ť = �Ӱ�ť("�������ϸ��", ����, None)

���ఴť = ����ť(600, 0, "����              ")
��������Ϣ��ť = �Ӱ�ť("��������Ϣ", ���ఴť, ��������Ϣ��ʾ����)
�ؼ� = 500
��·�� = 400
global ����
����x = 0  # ���������λ��
����y = 50
���� = [None]

def �����ʼ��():  # ��forѭ���������26������Ļ���
    for _ in range(10):
        ����.append((����x + _ * 120, ����y))
    for _ in range(3):
        ����.append((����x + 1080, ����y + _ * 120 + 120))
    for _ in range(10):
        ����.append((����x + 1080 - _ * 120, ����y + 480))
    for _ in range(3):
        ����.append((����x, ����y + 360 - _ * 120))

�����ʼ��()

global XX, YY
XX = [0, 0, 0, 0, 0]
YY = [0, 0, 0, 0, 0]
XX[1] = ����[1][0] + 1  # ֮��Ϳ������±����ʽֱ��ȥ����Ӧ���򣬺ܷ���
YY[1] = ����[1][1] + 1

XX[2] = ����[1][0] + 51
YY[2] = ����[1][1] + 1
XX[3] = ����[1][0] + 1
YY[3] = ����[1][1] + 51
XX[4] = ����[1][0] + 51
YY[4] = ����[1][1] + 51
global stateall, state1, state2, state3, state4
state1 = 1
state2 = 1
state3 = 1
state4 = 1
stateall = 0

��ɫͼƬ�ļ�·�� = [None, "��ϷͼƬ/���.png", "��ϷͼƬ/ϲ����.jpeg", "��ϷͼƬ/��ķè.jpeg", "��ϷͼƬ/�����.jpg"]


def bubble_sort(arr):
    start = time.time()
    a = []
    ������˳�� = []
    for _ in range(len(arr) - 1):
        ������˳��.append(_ + 1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    for i in range(len(a) - 1):  # ע��������len-1
        for j in range(len(a) - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # ����
                ������˳��[j], ������˳��[j + 1] = ������˳��[j + 1], ������˳��[j]  # ���Ǹ���Ӧ����Ӧÿ����ɫ
    end = time.time()
    print(f'����һ��������Ҫ{end - start}��')
    return ������˳��


# coding=gbk
def shellSort(arr, k, reverse=False):
    a = []
    ������˳�� = []
    for _ in range(len(arr) - 1):
        ������˳��.append(_ + 1)
    for _ in arr:
        a.append(_)
    a.remove(a[0])
    length = len(a)
    dk = k  # ����һ������dk
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
        self.next = None  # nextָ����һ�����
        self.number = 0
        self.location = location
        cityList.add(self)  # ��ʼ��ʱ�Զ���ӵ��б���


class citylist:
    def __init__(self):
        self.head = None  # �൱��c�������ͷָ���βָ��
        self.tail = None

    def add(self, city):
        if self.head == None:  # ����������������Ϊ�գ�ͷβָ��ָ��ͬһ���
            self.head = city
            self.tail = city
        if self.head != None:
            self.tail.next = city  # �������Ѿ���Ԫ�أ�ͷָ�벻����βָ�����ָ����Ԫ��
            self.tail = city

    def println(self):
        point = self.head
        while point != None:
            print(point.name)
            point = point.next

    def name_search(self, name):  # �������ƵĲ���
        point = self.head  # ����һ��ָ�룬��ָ��ͷ
        t = 0
        while point != None:  # ָ����ƣ�ƥ��
            if point.name == name:
                break
            t += 1
            point = point.next  # ָ����һ��
        if point == None:  # �Ҳ���
            return 0
        else:
            return t

    def location_search(self, location):  # ����λ�õĲ���
        point = self.head  # ����һ��ָ�룬��ָ��ͷ
        t = 0
        while point != None:  # ָ����ƣ�ƥ��
            if point.location == location:
                break
            t += 1
            point = point.next  # ָ����һ��
        if point == None:  # �Ҳ���
            return 0
        else:
            return t


cityList = citylist()  # ʵ����
���� = city("����", 2)
��� = city("���", 4)
�Ϻ� = city("�Ϻ�", 13)
ŦԼ = city("ŦԼ", 15)
���� = city("����", 20)
�׶� = city("�׶�", 26)


def ���˵ز���ʾ(i):
    str = ""
    point = cityList.head
    while point != None:
        if point.state == i:
            str += point.name
            str += ","
        point = point.next
    return str


def �Ʋ��ж�():
    global �Ʋ�, �Ʋ�����
    a = 0
    for x in range(1, 5):  # ������û����Ǯ�Ǹ�����
        if money[x] < 0:  # x��¼���������
            messagebox.showinfo("��ʾ", f"���{x}���Ʋ�")
            money[x] = 0  # Ǯ�����㣬��Ȼ��һ�λ��ظ��ж�
            �Ʋ�[x] = 1
            �Ʋ����� += 1
            messagebox.showinfo("��ʾ", f"��ʱ�Ʋ�{�Ʋ�����}��")
            if ����.state == x:
                ����.state = 0
                messagebox.showinfo("��ʾ", "���ݵķ����乫")
            if ���.state == x:
                ���.state = 0
                messagebox.showinfo("��ʾ", "��۵ķ����乫")
            if �Ϻ�.state == x:
                �Ϻ�.state = 0
                messagebox.showinfo("��ʾ", "�Ϻ��ķ����乫")
            if �Ϻ�.state == x:
                �Ϻ�.state = 0
                messagebox.showinfo("��ʾ", "ŦԼ�ķ����乫")
            if ŦԼ.state == x:
                ŦԼ.state = 0
                messagebox.showinfo("��ʾ", "�����ķ����乫")
            if �׶�.state == x:
                �׶�.state = 0
                messagebox.showinfo("��ʾ", "�׶صķ����乫")
            ��ɫ[x - 1].����()
            ����¼�[x].append(f"���{x}���Ʋ�")

            if �Ʋ����� == 3:
                for _ in range(5):
                    if �Ʋ�[_] == 0:
                        messagebox.showinfo("��ʾ", f"���{_}��ʤ")
                        root.destroy()

def �ж�(i,ai=None):  # ����i����Ҽ�����˼,�������ж��ж�
    def ���з����ж�(������, i, city):
        x�� = ����[������][0] + 1
        x�� = x�� + 118
        y�� = ����[������][1] + 1
        y�� = y�� + 118
        global money
        if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
            if i == city.state:  # ����
                ����¼�[i].append(f'���﷽��13��{city.name}����ʣ{money[i]}Ԫ')
            if i != city.state and city.state != 0:
                messagebox.showinfo("��ʾ", f"��{i}��Ҫ�����{city.state}��{��·��}Ԫ��Ϊ��·��")
                money[i] -= ��·��
                money[city.state] += ��·��
                ����¼�[i].append(
                    f'���﷽��{������}��{city.name}�������{city.state}��{��·��}Ԫ��·��,��ʣ{money[i]}Ԫ')

            if city.state == 0:  # ���
                if ai==None:
                    ans = askokcancel("��ʾ", f"��Ҫ��{�ؼ�}Ԫ�����")
                else:
                    ans=random.randint(0,1)
                if ans:
                    if money[i] >= �ؼ�:
                        messagebox.showinfo("��ʾ", "�ɹ�����")
                        money[i] -= �ؼ�

                        city.state = i
                        ����¼�[i].append(f'���﷽��13������{city.name},��ʣ{money[i]}Ԫ')
                    else:
                        messagebox.showinfo("��ʾ", "Ǯ����")
                        ����¼�[i].append(f'���﷽��{������},��ʣ{money[i]}Ԫ')
    def �����ж�(������, i, ����Ч��, ��������=None, ����=None):  # i��������
        global money
        x�� = ����[������][0] + 1
        x�� = x�� + 118
        y�� = ����[������][1] + 1
        y�� = y�� + 118

        if ����Ч�� == "����Ǯ":
            if ���� > 0:
                ���� = '+'
            else:
                ���� = ''
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                messagebox.showinfo("��ʾ", f"{��������},{����}{����}Ԫ")
                money[i] = money[i] +����
                ����¼�[i].append(f"������{������}��{��������},{����}{����}Ԫ����ʣ{money[i]}Ԫ")
        if ����Ч�� == "����":
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                messagebox.showinfo("��ʾ", ��������)
                money[i] = money[i] / 2
                ����¼�[i].append(f"������{������}��{��������}����ʣ{money[i]}Ԫ")

        if ����Ч�� == "���·���":
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                ����¼�[i].append(f"������{������}��{��������}����ʣ{money[i]}Ԫ")
        if ����Ч��=="�۲�":
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                t = 1
                messagebox.showinfo("��ʾ", "������Ҷ�Ҫ����100Ԫ")
                money[i] = money[i] + 100 * (4 - �Ʋ�����)
                for _ in money[1:5]:
                    if money[t] >= 0 and �Ʋ�[t] == 0:
                        money[t] -= 100
                    t += 1
                ����¼�[i].append(f"����{������}����ȡ������Ҹ�100Ԫ����ʣ{money[i]}Ԫ")
                temp_llst=[0,1,2,3,4]
                temp_llst[i]=0
                for ii in temp_llst:
                    if ii !=0:
                        ����¼�[ii].append(f"�����{i}����100Ԫ����ʣ{money[ii]}Ԫ")

        if ����Ч��=="��Ժ":
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                ����¼�[i].append(f"���﷽��{������}��Ժ")
                t = 0
                if ai==None:
                    ans = askokcancel("��Ժ��ʾ", "Ҫ��Ѻ�����������ֽ���")
                else:
                    ans=random.randint(0,1)
                if ans:
                    if ����.state == i:
                        t += 1
                        if ai==None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѹ��ݵķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            ����.state = 0
                            ����¼�[i].append(f"���˹��ݣ���ʣ{money[i]}Ԫ")
                    if ���.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ����۵ķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            ���.state = 0
                            ����¼�[i].append(f"������ۣ���ʣ{money[i]}Ԫ")
                    if �Ϻ�.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���Ϻ��ķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            �Ϻ�.state = 0
                            ����¼�[i].append(f"�����Ϻ�����ʣ{money[i]}Ԫ")
                    if ŦԼ.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ��ŦԼ�ķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            ŦԼ.state = 0
                            ����¼�[i].append(f"����ŦԼ����ʣ{money[i]}Ԫ")
                    if ����.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ�ѱ����ķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            ����.state = 0
                            ����¼�[i].append(f"���˱�������ʣ{money[i]}Ԫ")
                    if �׶�.state == i:
                        t += 1
                        if ai == None:
                            ans1 = askokcancel("��Ժ��ʾ", f"Ҫ���׶صķ���������")
                        else:
                            ans1 = random.randint(0, 1)
                        if ans1:
                            money[i] += �ؼ�
                            �׶�.state = 0
                            ����¼�[i].append(f"�����׶أ���ʣ{money[i]}Ԫ")
                    if t == 0:
                        messagebox.showinfo("��ʾ", "��û�з���")
        if ����Ч��=="ǰ��":
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                y = np.random.randint(1, ����)
                messagebox.showinfo("��ʾ", f"��ǰ��{y}������")
                for _ in range(y):
                    if i==1:
                        ͼƬ1_next()
                    if i==2:
                        ͼƬ2_next()
                    if i==3:
                        ͼƬ3_next()
                    if i==4:
                        ͼƬ4_next()
                ����¼�[i].append(f"����{��������}����ǰ��{y}������")
        if ����Ч��=="����Ǯ��":
            max = 0
            t = 0
            t0 = 0
            temp = 0
            for _ in money:
                if money[t] > max:
                    max = money[t]
                    t0 = t
                t += 1
            if x�� <= XX[i] <= x�� and y�� <= YY[i] <= y��:
                messagebox.showinfo("��ϲ", "��һҹ����")
                messagebox.showinfo("��ʾ", f"�㽫�����{t0}����Ǯ��")
                temp = money[i]
                money[i] = money[t0]
                money[t0] = temp
                ����¼�[i].append(f'���﷽��{������}�������{t0}����Ǯ�ƣ���ʣ{money[i]}Ԫ')

    �����ж�(3, i, "����Ǯ", ��������="���ݳ���", ����=-100)
    �����ж�(5, i, "����Ǯ", ��������="�õ����", ����=100)
    �����ж�(6, i, "����", ��������="�����Ĳ������ֻʣһ��")
    �����ж�(7, i, "���·���", ��������="��԰")
    �����ж�(8,i,"��Ժ")
    �����ж�(9,i,"�۲�")
    �����ж�(10,i,"ǰ��",����=3,��������="����")
    �����ж�(11, i, "����Ǯ", ��������="�õ����", ����=200)
    �����ж�(12, i, "����Ǯ", ��������="������թƭ", ����=-300)
    �����ж�(14,i,"ǰ��",����=4,��������="����վ")
    �����ж�(16, i, "����Ǯ��")
    �����ж�(17, i, "����Ǯ", ��������="�õ����", ����=200)
    �����ж�(18, i, "����Ǯ", ��������="�����山����Ҫ��Ǯ����", ����=-300)
    �����ж�(21, i, "����Ǯ", ��������="��Ⱦ������������", ����=-350)
    �����ж�(22, i, "��Ժ")
    �����ж�(23, i, "ǰ��", ����=2, ��������="��ͷ")
    �����ж�(24, i, "����Ǯ", ��������="������", ����=-150)
    �����ж�(25, i, "����Ǯ", ��������="������Ϊ������", ����=300)
    ���з����ж�(2, i, ����)
    ���з����ж�(4, i, ���)
    # 10��
    # ����13�ж�(i)
    ���з����ж�(13, i, �Ϻ�)
    # 14��
    ���з����ж�(15, i, ŦԼ)
    # 19�ǹ�԰
    ���з����ж�(20, i, ����)
    ���з����ж�(26, i, �׶�)
    �Ʋ��ж�()
    # end=time.time()
    # print(f'���жϺ���ִ������{end-start}��')

class ͼƬ:
    def __init__(root, ·��, λ��, ��С):
        root.·�� = ·��
        root.λ�� = λ��
        root.��С = ��С
        root.lst = []
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0], y=λ��[1])

    def replace(root, ��λ��):
        root.lst[-1].place(x=��λ��[0], y=��λ��[1])

    def ��ͼƬ(root, ���):
        root.lst[-1].destroy()
        root.lst.pop()
        root.����1a = Image.open(��ɫͼƬ�ļ�·��[���])  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((root.��С[0], root.��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=root.λ��[0], y=root.λ��[1])

    def ������·��(root, ·��, i):
        root.lst[-1].destroy()
        root.lst.pop()
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((root.��С[0], root.��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = ttk.Label(image=root.����1b)
        root.lst.append(root.����1c)
        if i == 1:
            root.lst[-1].place(x=XX[1], y=YY[1])
        if i == 2:
            root.lst[-1].place(x=XX[2], y=YY[2])
        if i == 3:
            root.lst[-1].place(x=XX[3], y=YY[3])
        if i == 4:
            root.lst[-1].place(x=XX[4], y=YY[4])

    def ����(root):
        root.lst[-1].destroy()


def ��ͷˢ��(i):
    ��ͷ.replace((����[i][0] + 25, ����[i][1] + 120))

class ͼƬ��ť:
    def __init__(root, ·��, λ��, ��С, ����):
        root.·�� = ·��
        root.λ�� = λ��
        root.��С = ��С
        root.lst = []
        root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
        root.����1a = root.����1a.resize((��С[0], ��С[1]))  # �涨ͼƬ��С
        root.����1b = ImageTk.PhotoImage(root.����1a)
        root.����1c = tk.Button(image=root.����1b, command=����)
        root.lst.append(root.����1c)
        root.lst[-1].place(x=λ��[0], y=λ��[1])

class ͼƬ2:
    def __init__(root, ·��, λ��):
        root.·�� = ·��
        root.λ�� = λ��
        if ·�� != None:
            root.����1a = Image.open(·��)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
            root.����1a = root.����1a.resize((110, 110))  # �涨ͼƬ��С
            root.����1b = ImageTk.PhotoImage(root.����1a)
            root.����1c = ttk.Label(image=root.����1b)
            root.����1c.place(x=����[λ��][0] + 5, y=����[λ��][1] + 5)  # ��λ�þ�������ı��
        if ·�� == None:
            root.���� = tk.Label(text=λ��, font=12)
            root.����.place(x=����[λ��][0] + 50, y=����[λ��][1] + 50)
        w1.create_line(����[λ��][0], ����[λ��][1], ����[λ��][0] + 120, ����[λ��][1], width=5)
        w1.create_line(����[λ��][0], ����[λ��][1], ����[λ��][0], ����[λ��][1] + 120, width=5)
        w1.create_line(����[λ��][0] + 120, ����[λ��][1], ����[λ��][0] + 120, ����[λ��][1] + 120, width=5)
        w1.create_line(����[λ��][0], ����[λ��][1] + 120, ����[λ��][0] + 120, ����[λ��][1] + 120, width=5)


class ����:
    def __init__(root, λ��, �ֺ�, ����):
        root.λ�� = λ��
        root.�ֺ� = �ֺ�
        root.���� = ����
        root.���� = tk.Label(text=����, font=�ֺ�)
        root.����.place(x=λ��[0], y=λ��[1])

    def ����(root, ����):
        root.����.destroy()
        root.���� = tk.Label(text=����, font=root.�ֺ�)
        root.����.place(x=root.λ��[0], y=root.λ��[1])


class �����ؼ�:
    def __init__(self, lst):
        ������ҳ�� = tk.Tk()
        # bttrt=tk.Button(������ҳ��)   #ģ������ѹ������ӵ�����ȥ
        # bttrt.pack()

        self.scrollbar_v = Scrollbar(������ҳ��)
        self.scrollbar_v.pack(side=RIGHT, fill=Y)  # �ҹ�����
        self.scrollbar_h = Scrollbar(������ҳ��, orient=HORIZONTAL)  # ˮƽ������
        self.scrollbar_h.pack(side=BOTTOM, fill=X)
        self.text = Text(������ҳ��, width=40, height=40)
        self.text.config(yscrollcommand=self.scrollbar_v.set)  # text�󶨴�ֱ������
        self.text.config(xscrollcommand=self.scrollbar_h.set)  # text��ˮƽ������
        self.text.pack(expand=YES, fill=BOTH)

        for i in range(len(lst)):
            self.text.insert("end", lst[i] + "\n")

        self.scrollbar_v.config(command=self.text.yview)  # ��ֱ��������text
        self.scrollbar_h.config(command=self.text.xview)  # ˮƽ��������text


# ��������=�����ؼ�()
# ����25=ͼƬ("��ϷͼƬ/������Ϊ������300Ԫ.png",(3,243))
����1 = ͼƬ2("��ϷͼƬ/���.png", 1)
����2 = ͼƬ2("��ϷͼƬ/����.png", 2)
����3 = ͼƬ2("��ϷͼƬ/�ݳ���.png", 3)
����4 = ͼƬ2("��ϷͼƬ/���.png", 4)
����5 = ͼƬ2("��ϷͼƬ/200���.png", 5)
����6 = ͼƬ2("��ϷͼƬ/�Ĳ��ֽ����.png", 6)
����7 = ͼƬ2("��ϷͼƬ/��԰1.png", 7)
����8 = ͼƬ2("��ϷͼƬ/��Ժ.png", 8)
����9 = ͼƬ2("��ϷͼƬ/������.png", 9)
����10 = ͼƬ2("��ϷͼƬ/�ɻ�.png", 10)
����11 = ͼƬ2("��ϷͼƬ/200���.png", 11)
����12 = ͼƬ2("��ϷͼƬ/����թƭ.png", 12)
����13 = ͼƬ2("��ϷͼƬ/�Ϻ�.png", 13)
����14 = ͼƬ2("��ϷͼƬ/����.jpg", 14)
����15 = ͼƬ2("��ϷͼƬ/ŦԼ.png", 15)
����16 = ͼƬ2("��ϷͼƬ/һҹ����.png", 16)
����17 = ͼƬ2("��ϷͼƬ/200���.png", 17)
����18 = ͼƬ2("��ϷͼƬ/�山.png", 18)
����19 = ͼƬ2("��ϷͼƬ/��԰2.png", 19)
����20 = ͼƬ2("��ϷͼƬ/����.png", 20)
����21 = ͼƬ2("��ϷͼƬ/������Ⱦ����.png", 21)  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
����22 = ͼƬ2("��ϷͼƬ/��Ժ.png", 22)
����23 = ͼƬ2("��ϷͼƬ/�ִ�.jpg", 23)
����24 = ͼƬ2("��ϷͼƬ/2018.png", 24)
����25 = ͼƬ2("��ϷͼƬ/������Ϊ������300Ԫ.png", 25)
����26 = ͼƬ2("��ϷͼƬ/�׶�.png", 26)

��ͷ = ͼƬ("��ϷͼƬ/���ϼ�ͷ.png", (����[1][0], ����[1][1] + 120), (35, 35))
��ʾͼƬ1 = ͼƬ(��ɫͼƬ�ļ�·��[1], (����[3][0], ����[3][1] + 240), (125, 125))
����1 = ����((����[3][0], ����[3][1] + 160), 32, "�����ֵ����1")
����ͼƬ1 = ͼƬ(r"��ϷͼƬ\����ͼƬ1.png", (����[6][0], ����[6][1] + 120),
                 (125, 230))
��������ͼƬ = ͼƬ(r"��ϷͼƬ\��������.png",
                    (����[7][0] + 10, ����[7][1] + 120), (300, 230))
��Ǯ��Ϣ1 = ����((����[4][0] + 10, ����[4][1] + 260), 32, "���1���ʽ�Ϊ��1200")
�ز���Ϣ1 = ����((����[4][0] + 10, ����[4][1] + 290), 32, "���1�ĵز���\n")
�ز���Ϣ2 = ����((����[4][0] + 10, ����[4][1] + 330), 32, "")
���������� = ����((����[13][0] + 120, 0), 32, "ʵʱ������")
�����������嵥 = []
������ͼƬ�嵥 = []
�����������嵥.append(����((����������.λ��[0], ����������.λ��[1] + 75), 32, "NO.1�����1\n �ʽ�1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[1], (����������.λ��[0] + 180, ����������.λ��[1] + 75), (50, 50)))
�����������嵥.append(����((����������.λ��[0], ����������.λ��[1] + 200), 32, "NO.2�����2\n �ʽ�: 1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[2], (����������.λ��[0] + 180, ����������.λ��[1] + 200), (50, 50)))

�����������嵥.append(����((����������.λ��[0], ����������.λ��[1] + 325), 32, "NO.3:���3\n �ʽ�:1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[3], (����������.λ��[0] + 180, ����������.λ��[1] + 325), (50, 50)))

�����������嵥.append(����((����������.λ��[0], ����������.λ��[1] + 450), 32, "NO.4:���4\n �ʽ�:1200"))
������ͼƬ�嵥.append(ͼƬ(��ɫͼƬ�ļ�·��[4], (����������.λ��[0] + 180, ����������.λ��[1] + 450), (50, 50)))


def ����ˢ��(i):
    ����1.����(f"�����ֵ����{i}")
    if �Ʋ�[i] == 1:
        ����1.����(f"�����ֵ����{i}(���Ʋ���")
    ��Ǯ��Ϣ1.����(f"���{i}���ʽ�Ϊ:{money[i]}")
    �ز���Ϣ1.����(f"���{i}�ĵز���:")
    �ز���Ϣ2.����(���˵ز���ʾ(i))

def ���������():
    ���� = bubble_sort(money)
    for _ in range(len(����)):
        �����������嵥[_].����(f"No.{_ + 1}:���{����[_]}\n �ʽ�: {money[����[_]]}")
        ������ͼƬ�嵥[_].��ͼƬ(����[_])


��ɫ = []
��ɫ.append(ͼƬ(��ɫͼƬ�ļ�·��[1], (XX[1], YY[1]), (47, 47)));
��ɫ.append(ͼƬ(��ɫͼƬ�ļ�·��[2], (XX[2], YY[2]), (47, 47)));
��ɫ.append(ͼƬ(��ɫͼƬ�ļ�·��[3], (XX[3], YY[3]), (47, 47)));
��ɫ.append(ͼƬ(��ɫͼƬ�ļ�·��[4], (XX[4], YY[4]), (47, 47)))

def ��ӽ�Ǯ��¼(i):
    global money
    if i == 1 and �Ʋ�[1] == 0:
        ���1��Ǯ��¼.append(money[1])
    if i == 2 and �Ʋ�[2] == 0:
        ���2��Ǯ��¼.append(money[2])
    if i == 3 and �Ʋ�[3] == 0:
        ���3��Ǯ��¼.append(money[3])
    if i == 4 and �Ʋ�[4] == 0:
        ���4��Ǯ��¼.append(money[4])

def main():
    global stateall, state1, state2, state3, state4
    global �Ʋ�
    if stateall % 4 == 0:  # ���1�غ�
        if �Ʋ�[1] == 0:
            �ƶ�ͼƬ1()
            ��ͷˢ��(state1)
            �ж�(1)
        ��ͷˢ��(state2)
        ��ʾͼƬ1.��ͼƬ(2)
        ����ˢ��(2)
        ���������()
        # tk.Label(root, text=f'�ֵ����{stateall % 4 + 2}', font=24).place(x=320, y=150)
    if stateall % 4 == 1:  # ���2�غ�
        if �Ʋ�[2] == 0:
            �ƶ�ͼƬ2()
            ��ͷˢ��(state2)
            �ж�(2,ai=ai_[2])     #�Ƿ�ai�������
        ��ͷˢ��(state3)
        ��ʾͼƬ1.��ͼƬ(3)
        ����ˢ��(3)
        ���������()
    if stateall % 4 == 2:  # ���3�غ�
        if �Ʋ�[3] == 0:
            �ƶ�ͼƬ3()
            ��ͷˢ��(state3)
            �ж�(3,ai=ai_[3])
        ��ͷˢ��(state4)
        ��ʾͼƬ1.��ͼƬ(4)
        ����ˢ��(4)
        ���������()
    if stateall % 4 == 3:  # ���4�غ�
        if �Ʋ�[4] == 0:
            �ƶ�ͼƬ4()
            ��ͷˢ��(state4)
            �ж�(4,ai=ai_[4])
        ��ͷˢ��(state1)
        ��ʾͼƬ1.��ͼƬ(1)
        ����ˢ��(1)
        ���������()
    stateall += 1
    ��ӽ�Ǯ��¼(stateall % 4 + 1)

def ����():
    import numpy as np
    import tkinter
    import tkinter.messagebox  # ������
    y = np.random.randint(1, 7)  # ��Χ1-9��������10������������
    tkinter.messagebox.showinfo('����', f'����Ϊ{y}')  # ǰ���ͷ����������
    return y

def ͼƬ1_next():
    global state1, XX,YY

    state1 += 1
    if state1 == 27:
        state1 = 1
    XX[1] = ����[state1][0] + 1
    YY[1] = ����[state1][1] + 1
    ��ɫ[0].replace((XX[1], YY[1]))

def �ƶ�ͼƬ1():
    t = ����()
    for x in range(t):
        ͼƬ1_next()

def ͼƬ2_next():
    global state2
    global XX
    global YY
    state2 += 1
    if state2 == 27:
        state2 = 1
    XX[2] = ����[state2][0] + 51
    YY[2] = ����[state2][1] + 1
    ��ɫ[1].replace((XX[2], YY[2]))

def �ƶ�ͼƬ2():
    t = ����()
    for x in range(t):
        ͼƬ2_next()

def ͼƬ3_next():
    global state3
    global XX
    global YY
    state3 += 1
    if state3 == 27:
        state3 = 1
    XX[3] = ����[state3][0] + 1
    YY[3] = ����[state3][1] + 51
    ��ɫ[2].replace((XX[3], YY[3]))

def �ƶ�ͼƬ3():
    t = ����()
    for x in range(t):
        ͼƬ3_next()

def ͼƬ4_next():
    global state4
    global XX
    global YY
    state4 += 1
    if state4 == 27:
        state4 = 1
    XX[4] = ����[state4][0] + 51
    YY[4] = ����[state4][1] + 51
    ��ɫ[3].replace((XX[4], YY[4]))

def �ƶ�ͼƬ4():
    t = ����()
    for x in range(t):
        ͼƬ4_next()

������ť = ͼƬ��ť("��ϷͼƬ/������ť.png", (����[18][0], ����[18][1] - 100), (120, 100), main)

root.mainloop()

����ҳ�� = tk.Tk()
����ҳ��.geometry("500x600")
����ҳ��.title = "����ҳ��"
����1a = Image.open("��ϷͼƬ/����ҳ��.png")  # ������Ϊ��Ҫ��ʾ��ͼ�λ��������ͼƬ
����1a = ����1a.resize((500, 600))  # �涨ͼƬ��С
����1b = ImageTk.PhotoImage(����1a)
����1c = ttk.Label(image=����1b)
����1c.place(x=0, y=0)

def �������һ��Ǯͼ��():
    y = ���1��Ǯ��¼
    print(y)
    x = list(map(lambda x: x, range(len(���1��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, ���1��Ǯ��¼)
    plt.show()

bt1 = tk.Button(text="���һ�¼�", command=���1��Ϣ��ѯ����).place(x=200, y=300)
bt5 = tk.Button(text="���һ��Ǯ�仯", command=�������һ��Ǯͼ��).place(x=200, y=350)

def ������Ҷ���Ǯͼ��():
    y = ���2��Ǯ��¼
    print(y)
    x = list(map(lambda x: x, range(len(���2��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, ���2��Ǯ��¼)
    plt.show()

bt2 = tk.Button(text="��Ҷ��¼�", command=���2��Ϣ��ѯ����).place(x=300, y=300)
bt6 = tk.Button(text="��Ҷ���Ǯ�仯", command=������Ҷ���Ǯͼ��).place(x=300, y=350)

def �����������Ǯͼ��():
    y = ���3��Ǯ��¼
    print(y)
    x = list(map(lambda x: x, range(len(���3��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, ���3��Ǯ��¼)
    plt.show()

bt3 = tk.Button(text="������¼�", command=���3��Ϣ��ѯ����).place(x=200, y=400)
bt7 = tk.Button(text="�������Ǯ�仯", command=�����������Ǯͼ��).place(x=200, y=450)

def ��������Ľ�Ǯͼ��():
    y = ���4��Ǯ��¼
    print(y)
    x = list(map(lambda x: x, range(len(���4��Ǯ��¼))))
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], color='r')
    plt.plot(x, ���4��Ǯ��¼)
    plt.show()

bt4 = tk.Button(text="������¼�", command=���4��Ϣ��ѯ����).place(x=300, y=400)
bt8 = tk.Button(text="����Ľ�Ǯ�仯", command=��������Ľ�Ǯͼ��).place(x=300, y=450)

����ҳ��.mainloop()
