import serial
import re
import numpy as np
import matplotlib.pyplot as plt
import datetime
import csv
import tkinter

y_range = 2000


def serial_communication():
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d_%H%M%S') + '.csv'
    ser = serial.Serial('COM7', 9600, timeout=0.01)
    for _ in range(2):
        ser.readline()
    regex = re.compile('\d+')
    fig, ax = plt.subplots(1, 1)
    ax.set_ylim((0, y_range))
    count = []
    data = []
    for i in range(150):
        count.append(i)
        get_data = str(ser.readline())
        print(get_data)
        value = int(regex.findall(get_data)[0])
        data.append(value)
        line, = ax.plot(count, data, color='blue')
        plt.pause(0.01)
        line.remove()

        with open(filename, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([value])

    for _ in range(1000):
        get_data = str(ser.readline())
        print(get_data)
        value = int(regex.findall(get_data)[0])
        data.pop(0)
        data.append(value)
        line, = ax.plot(count, data, color='blue')
        plt.pause(0.01)
        line.remove()

        with open(filename, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([value])

    ser.close()


def confirm():
    ser = serial.Serial('COM7', 9600, timeout=0.01)
    regex = re.compile('\d+')
    fig, ax = plt.subplots(1, 1)
    ax.set_ylim((0, y_range))
    count = []
    data = []
    for i in range(150):
        count.append(i)
        get_data = str(ser.readline())
        print(get_data)
        value = int(regex.findall(get_data)[0])
        data.append(value)
        line, = ax.plot(count, data, color='blue')
        plt.pause(0.01)
        line.remove()

    while True:
        get_data = str(ser.readline())
        print(get_data)
        value = int(regex.findall(get_data)[0])
        data.pop(0)
        data.append(value)
        line, = ax.plot(count, data, color='blue')
        plt.pause(0.01)
        line.remove()

    # ser.close()


def array_del():
    hoge = [3, 2, 4, 5, 6, 3]
    print(hoge)
    print(hoge.pop(0))
    print(hoge)


def graph():
    # left = np.array([10, 20, 30, 40, 50])
    # height = np.array([100, 300, 200, 500, 400])
    # plt.plot(left, height, marker="D")
    # plt.show()

    # 描画領域を取得
    fig, ax = plt.subplots(1, 1)
    # y軸方向の描画幅を指定
    ax.set_ylim((-1.1, 1.1))
    # x軸:時刻
    x = np.arange(0, 100, 0.5)

    y = np.sin(2.0 * np.pi * (x * 1) / 100)
    print(y)
    print(len(y))
    # グラフを描画する
    # line, = ax.plot(x, y, color='blue')
    ax.plot(x, y, color='blue')
    plt.show()
    # # 周波数を高くしていく
    # for Hz in np.arange(0.1, 3.1, 0.1):
    #     # sin波を取得
    #     y = np.sin(2.0 * np.pi * (x * Hz) / 100)
    #     # グラフを描画する
    #     line, = ax.plot(x, y, color='blue')
    #     # 次の描画まで0.01秒待つ
    #     plt.pause(0.1)
    #     # グラフをクリア
    #     line.remove()


def gui():
    tki = tkinter.Tk()
    tki.geometry('240x200')  # 画面サイズの設定
    tki.title('SCC')  # 画面タイトルの設定

    # ボタンの作成
    btn_start = tkinter.Button(tki, text='START', command=show_message(1))
    btn_start.place(x=100, y=40)
    btn_stop = tkinter.Button(tki, text='STOP', command=tki.quit)
    btn_stop.place(x=100, y=120)

    # 画面をそのまま表示
    tki.mainloop()


def show_message(index):
    def inner():
        serial_communication()
    return inner


def end_code(index):
    def inner():
        # ser = serial.Serial('COM7', 9600, timeout=0)
        # ser.close()
        # exit()
        print("-------------------------------------------------")
    return inner


if __name__ == "__main__":
    confirm()
