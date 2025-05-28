import socket

def get_local_ip():
    try:
        # 创建一个UDP套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个公共的IP地址（不发送数据，仅用于获取本机IP）
        s.connect(("8.8.8.8", 80))
        # 获取本机IP地址
        ip = s.getsockname()[0]
    finally:
        # 关闭套接字
        s.close()
    return ip
def 骰子():
    import numpy as np
    import tkinter
    import tkinter.messagebox  # 弹窗库
    y = np.random.randint(1, 7)  # 范围1-9（不包括10），数量三个
    tkinter.messagebox.showinfo('骰子', f'数字为{y}')  # 前面标头，后面内容
    return y
# 测试函数
if __name__ == "__main__":
    local_ip = get_local_ip()
    print("本地IP地址是:", local_ip)