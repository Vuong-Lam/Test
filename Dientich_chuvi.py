import tkinter as tk
root=tk.Tk()
root.title("Tính diện tích, chu vi")
root.geometry("500x500")

label_chieudai=tk.Label(root,text="Chiều dài: ")
label_chieudai.grid(row=0,column=0,padx=10,pady=10,sticky="w")
entry_chieudai=tk.Entry(root,width=10)
entry_chieudai.grid(row=0,column=1,padx=10,pady=10)

label_chieurong=tk.Label(root,text="Chiều rộng: ")
label_chieurong.grid(row=1,column=0,padx=10,pady=10,sticky="w")
entry_chieurong=tk.Entry(root,width=10)
entry_chieurong.grid(row=1,column=1,padx=10,pady=10)

def tinhdientich():
    chieudai=float(entry_chieudai.get())
    chieurong=float(entry_chieurong.get())
    try:
        result =chieudai*chieurong
        label_dientich.config(text=f"Diện tích: {result}")
    except ValueError:
        label_dientich.config(text="Vui Lòng Nhập số hợp lệ")

def tinhchuvi():
    chieudai=float(entry_chieudai.get())
    chieurong=float(entry_chieurong.get())
    try:
        result =chieudai*2+chieurong*2
        label_chuvi.config(text=f"Chuvi: {result}")
    except ValueError:
        label_chuvi.config(text="Vui Lòng Nhập số hợp lệ")

button_dientich=tk.Button(root,text="Diện tích",command=tinhdientich)
button_dientich.grid(row=2,column=0,padx=10,pady=10,sticky="W")
label_dientich=tk.Label(root,text="Diện tích: ",fg="blue")
label_dientich.grid(row=2,column=1,padx=10,pady=10,sticky="w")

button_chuvi=tk.Button(root,text="Chu vi",command=tinhchuvi)
button_chuvi.grid(row=3,column=0,sticky="w",padx=10,pady=10)
label_chuvi=tk.Label(root,text="Chu vi: ",fg="blue")
label_chuvi.grid(row=3,column=1,padx=10,pady=10,sticky="w")

root.mainloop()