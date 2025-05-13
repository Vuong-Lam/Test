import tkinter as tk
import random as rd
root= tk.Tk()
root.title("Tính tổng và trung bình ngẫu nhiên")
root.geometry("500x500")

label_danhsach=tk.Label(root,text="Dãy số:")
label_danhsach.grid(row=0,column=0,padx=10,pady=10,sticky="w")

label_from=tk.Label(root,text="Từ: ")
label_from.grid(row=1,column=0,padx=10,pady=10,sticky="w")
entry_from=tk.Entry(root,width=10)
entry_from.grid(row=1,column=1,padx=10,pady=10,sticky="w")
label_to=tk.Label(root,text="Đến: ")
label_to.grid(row=1,column=2,padx=10,pady=10,sticky="w")
entry_to=tk.Entry(root,width=10)
entry_to.grid(row=1,column=3,padx=10,pady=10,sticky="w")

label_count=tk.Label(root,text="Số lượng: ")
label_count.grid(row=2,column=0,padx=10,pady=10,sticky="w")
entry_count=tk.Entry(root,width=10)
entry_count.grid(row=2,column=1,padx=10,pady=10,sticky="w")

label_tong=tk.Label(root,text="Tong:")
label_tong.grid(row=3,column=0,padx=10,pady=10,sticky="w")

label_trungbinh=tk.Label(root,text="Trung bình:")
label_trungbinh.grid(row=3,column=1,padx=10,pady=10,sticky="w")

def Taoso():
    try:
        count=int(entry_count.get())
        fro=int(entry_from.get())
        to=int(entry_to.get())
        ds=[]
        for i in range(0,count):
            ds.append(rd.randint(fro,to))
        label_danhsach.config(text="Dãy số gồm: "+','.join(map(str,ds)))
    except ValueError:
        label_danhsach.config("Vui lòng nhập số hợp lệ")

button_random=tk.Button(root,text="Tạo dãy số",command=Taoso)
button_random.grid(row=4,column=0,padx=10,pady=10,sticky="w")

root.mainloop()
