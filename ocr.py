a="4000 0000 6789 6544 \n 1344"
a1="5000 1234 8590 3832 \n 82943"
a2="4002 1234 8777 3232  \n 332"
a3="4000 1234 9598 9850 38"

input_=[a,a1,a2,a3]

for x in input_:
    list0=""
    for y in x:
        
        if y in "0123456789":
            list0 += y   #will keep to adding numbers to list
        if y in " ":
            print("")
           
            
    d= list0[0:16]  #16 digits of card
    
    print(d)
    
    if d[0:4]== "4000":   #condition for black and white card
        print("its a WHITE CARD")
    else:
        print("its a BLACK CARD")
        

#GUI

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

def fill_f(path):
    img=ImageTk.PhotoImage(Image.open(path))
    Label(
        ub,
        image=img).pack()
#Tk().update_idletasks()
    get_result()

def open_f():
    path = filedialog.askopenfilename( initialdir="C:/Users/lenovo PC/Desktop/", title="select file")
    fill_f(path)


#uloading button
ub=Tk()    
ub.title("FRAUD DETECTOR")
ub.geometry("500x470")

Button(
    ub,
    text ='Upload credit card',
    command = open_f,font=50,bg="blue",fg="white",
    height=5, width=50).pack()        

# FOR DISPLAYING BLACK\WHITE
def get_result():
    if d[0:4]=="4000":
        label=Label(ub,text="WHITE CARD",fg="red",font=25).pack(side = LEFT)
        label.pack()
        Tk().update_idletasks()
        
    if d[0:4]!="4000":
        label=Label(ub,text=" BLACK CARD").pack(side=BOTTOM)
