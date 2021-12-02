import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # 가로*세로

# 기차 예매 시스템이라 가정


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")


def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")


def okcancle():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반 좌석입니다. 예매 하시겠습니까?")


def retrycancle():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도 하시겠습니까? ")


def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")


def yesnocancle():
    response = msgbox.askyesnocancel(
        title=None, message="에매 내역이 저장되지않았습니다.\n 저장후 프로그램을 종료하시겠습니까?")
    if response == 1:  # 재시도
        print("예")
    elif response == 0:  # 아니오
        print("아니오")
    else:            # 취소
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancle, text="확인 취소").pack()
Button(root, command=retrycancle, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancle, text="예 아니오 취소").pack()


root.mainloop()
