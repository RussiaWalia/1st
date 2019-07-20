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
            (400, 250),
            Image.ANTIALIAS))
    Label(
        window,
        image=img).pack()
    d = get_ocr(path)
    get_result(d)
    window.mainloop()


def open_f():
    path = filedialog.askopenfilename(initialdir="C:/Users/lenovo PC/Desktop/", title="select file")
    fill_f(path)


# uloading button
window = Tk()
window.title("FRAUD DETECTOR")
window.geometry("1000x800")

Button(
    window,
    text='Upload credit card',
    command=open_f,font="Helvetica 18 bold", bg="blue", fg="white",
    height=5, width=25).pack()


def get_result(d):
    if d[0:4] == "4000":
        Label(
            window,
            text="WHITE CARD",
            fg="red", font="Helvetica 18 bold").place(x=800, y=250, in_=window)
    if d[0:4] != "4000":
        Label(
            window,
            text="BLACK CARD",fg="red", font="Helvetica 18 bold").place(x=800, y=250, in_=ub)
    window.mainloop()


window.mainloop()
