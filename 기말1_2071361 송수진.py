from tkinter import*
from tkinter import font
root=Tk()
root.title("피자주문하기")
root.geometry("800x800")

font=font.Font(family="바탕체", size=18, weight="bold")
lbl1=Label(root, text="HS 피자스쿨에 오신것을 환영합니다.", font=font)
lbl1.grid(row=0,column=0)
lbl2=Label(root, text="--------------------- 메뉴 ---------------------")
lbl2.grid(row=1,column=0)
lblO1=Label(root, text="-----------------------------------------------")
lblO1.grid(row=8,column=0)
lblO2=Label(root, text="[주문한 피자]")
lblO2.grid(row=9,column=0)
lbl4=Label(root,text="[총금액]")
lbl4.grid(row=4,column=7)
lbl5=Label(root, text="")
lbl5.grid(row=4,column=8)

#버튼함수
def button():
    lbl5.configure(text="")
    lbl3.configure(text="")
def btt():
    root.destroy()

#버튼
btn1=Button(root, text="지우기", fg='white',bg='gray', command=button)
btn1.grid(row=3,column=7)
btn2=Button(root, text="종료하기", fg='white',bg='gray', command=btt)
btn2.grid(row=3,column=8)

#피자함수
def pizza():
    if(value1.get()==1)and(value2.get()==1)and(value3.get()==1):
        lbl3.configure(text="옥수수피자,쉬림프핫치킨피자,콤비네이션피자")
        lbl5.configure(text="72000원")
    elif(value1.get()==1)and(value2.get()==0)and(value3.get()==0):
        lbl3.configure(text="옥수수피자")
        lbl5.configure(text="22000원")
    elif(value1.get()==1)and(value2.get()==1)and(value3.get()==0):
        lbl3.configure(text="옥수수피자,쉬림프핫치킨피자")
        lbl5.configure(text="53000원")
    elif(value1.get()==1)and(value2.get()==0)and(value3.get()==1):
        lbl3.configure(text="옥수수피자,콤비네이션피자")
        lbl5.configure(text="41000원")
    elif(value1.get()==0)and(value2.get()==1)and(value3.get()==1):
        lbl3.configure(text="쉬림프핫치킨피자,콤비네이션피자")
        lbl5.configure(text="50000원")
    elif(value1.get()==0)and(value2.get()==1)and(value3.get()==0):
        lbl3.configure(text="쉬림프핫치킨피자")
        lbl5.configure(text="31000원")
    elif(value1.get()==0)and(value2.get()==0)and(value3.get()==1):
        lbl3.configure(text="콤비네이션피자")
        lbl5.configure(text="19000원")
    else:
        lbl3.configure(text="")
        lbl5.configure(text="0원")
    
#피자버튼
value1=IntVar()
chb1=Checkbutton(root, text="옥수수피자/22000원", variable=value1, command=pizza)
chb1.grid(row=2,column=0)
value2=IntVar()
chb2=Checkbutton(root, text="쉬림프핫치킨피자/31000원", variable=value2, command=pizza)
chb2.grid(row=4,column=0)
value3=IntVar()
chb3=Checkbutton(root, text="콤비네이션피자/19000원", variable=value3, command=pizza)
chb3.grid(row=6,column=0)

#피자그림
photo1=PhotoImage(file="옥수수피자.png")
iMlbl1=Label(root,image=photo1)
iMlbl1.grid(row=3,column=0)
photo2=PhotoImage(file="쉬프림핫치킨피자.png")
iMlbl2=Label(root,image=photo2)
iMlbl2.grid(row=5,column=0)
photo3=PhotoImage(file="콤비네이션피자.png")
iMlbl3=Label(root,image=photo3)
iMlbl3.grid(row=7,column=0)

#피자주문
lbl3=Label(root,text="",fg='red')
lbl3.grid(row=10,column=0)

root.mainloop()
