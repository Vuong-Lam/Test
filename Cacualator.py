import tkinter as tk
root =tk.Tk()
root.title("Máy tính đơn giản")
root.geometry("300x200")

entry1= tk.Entry(root, width=10)
entry1.pack(pady=5)

entry2= tk.Entry(root, width=10)
entry2.pack(pady=5)

def add_number():
    num1= float(entry1.get())
    num2=float(entry2.get())
    try:
        result=num1+num2
        label.config(text=f"Kết quả: {result}")
    except ValueError:
        label.config(text="Vui lòng nhập số hợp lệ")
def sub_number():
    num1= float(entry1.get())
    num2=float(entry2.get())   
    try:
        result=num1-num2
        label.config(text=f"Kết quả: {result}")
    except ValueError:
        label.config(text="Vui lòng nhập số hợp lệ")
def mul_number():
    num1= float(entry1.get())
    num2=float(entry2.get())
    try:
        result=num1*num2
        label.config(text=f"Kết quả: {result}")
    except ValueError:
        label.config(text="Vui lòng nhập số hợp lệ")
def div_number():
    num1= float(entry1.get())
    num2=float(entry2.get())
    try:
        result=num1/num2
        label.config(text=f"Kết quả: {result}")
    except ValueError:
        label.config(text="Vui lòng nhập số hợp lệ")
button1=tk.Button(root,text="+",command=add_number)
button1.pack(pady=5)

button2=tk.Button(root,text="-",command=sub_number)
button2.pack(pady=5)

button3=tk.Button(root,text="X",command=mul_number)
button3.pack(pady=5)

button4=tk.Button(root,text=":",command=div_number)
button4.pack(pady=5)

label= tk.Label(root,text="Kết quả")
label.pack(pady=5)



root.mainloop()


