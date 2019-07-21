from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract


def get_cc_num(str):
    list0 = ""
    for y in str:
        if y in "0123456789":
            list0 += y   #will keep to adding numbers to list
    return list0[0:16]  #16 digits of card

def get_ocr(path):
    str = pytesseract.image_to_string(Image.open(path))
    cc_num = get_cc_num(str)
    return cc_num

# GUI
def fill_f(path):
    img = ImageTk.PhotoImage(
        Image.open(path).resize(
            (250, 250),
            Image.ANTIALIAS))
    Label(
        ub,
        image=img).pack()
    d = get_ocr(path)
    get_result(d)
    ub.mainloop()


def open_f():
    path = filedialog.askopenfilename(initialdir="C:/Users/lenovo PC/Desktop/", title="select file")
    fill_f(path)


# uloading button
ub = Tk()
ub.title("FRAUD DETECTOR")
ub.geometry("500x470")

Button(
    ub,
    text='Upload credit card',
    command=open_f, font=50, bg="blue", fg="white",
    height=5, width=50).pack()


def get_result(d):
    if d[0:4] == "4000":
        Label(
            ub,
            text="WHITE CARD",
            fg="red", font=25).place(x=10, y=10, in_=ub)
    if d[0:4] != "4000":
        Label(
            ub,
            text="BLACK CARD").place(x=10, y=10, in_=ub)
    ub.mainloop()


ub.mainloop()
