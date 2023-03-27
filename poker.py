import tkinter as tk
from tkinter import messagebox, ttk as ttk


def poker():
    final = ""
    a = []
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    oxo = [0, 0, 0, 0, 0]
    check = 0

    tmp = entry1.get().split(" ")
    # tmp=[1,2,3,4,5]
    try:
        for i in range(len(tmp)):
            a.append(int(tmp[i]))
            oxo[i] = int(tmp[i]) + 1
    except:
        messagebox.showinfo("錯誤", "請輸入五個數字")
    for i in range(len(a)):
        cnt[a[i]] += 1
    print(cnt)
        # 判斷鐵支
    for i in range(14):
        if (cnt[i] == 4):
            final = "鐵支"
        # 判斷葫蘆
    for i in range(14):
        for j in range(14):
            if (cnt[i] == 3 and cnt[j] == 2):
                final = "葫蘆"
                print("葫蘆")
        # 判斷 two pa
    for i in range(14):
        if (cnt[i] == 2 and cnt[i - 1] == 2):
            final = "two pa"
            print("two pa")
        # 判斷順子
    for i in range(13):
        if cnt[i] == cnt[i + 1] and cnt[i] == 1:
            check += 1
        if check == 4:
            final = "順子"
            print("順子")
            break
        labe3 = tk.Label(window, text=("花色是:" + combo1.get() + "\n排型是:" + final))
        labe3.place(x=150, y=60)


window = tk.Tk()
window.title("撲克牌遊戲")
window.geometry('250x100')

label1 = tk.Label(window, text='花色')
label1.place(x=0, y=0)

combo1 = ttk.Combobox(window, values=[
    '梅花',
    '愛心',
    '黑桃',
    '方塊'])
combo1.place(x=40, y=0)

label2 = tk.Label(window, text="數字")
label2.place(x=0, y=30)
entry1 = tk.Entry(window)
entry1.place(x=40, y=30)

btn1 = tk.Button(window, text="確定", width=10, command=poker)
btn1.place(x=0, y=60)

window.mainloop()