import tkinter as tk
root    = tk.Tk()
root.title("Kiểm tra tính nguyên tố")
root.geometry("500x300")

label_nhapso=tk.Label(root,text="Nhập số: ")
label_nhapso.grid(row=0,column=0,padx=10,pady=10)
entry_nhapso=tk.Entry(root,width=10)
entry_nhapso.grid(row=0,column=1,padx=10,pady=10)



label_ketqua=tk.Label(text="Kết quả")
label_ketqua.grid(row=1,column=0,columnspan=2,padx=10,pady=10,sticky="w")

def Checkso(n):
    if n<2:
        return False
    else:
        for i in range (2,int(n**0.5)+1):
            if n%i==0:
                return False
            
        return True
    
def Kiemtrasnt():
    try:
        sokt=int(float(entry_nhapso.get()))
        if Checkso(sokt):
            label_ketqua.config(text="True")
        else:
            label_ketqua.config(text="False")
    except ValueError:
        label_ketqua.config(text="Vui Lòng Nhập số hợp lệ")

kiemtra=tk.Button(text="Kiểm tra",command=Kiemtrasnt)
kiemtra.grid(row=4,column=0,padx=10,pady=10)

def Danhsach():
    try:
        sokt=int(float(entry_nhapso.get()))
        if sokt <2:
            label_ketqua.config(text="KhÔng có snt nhỏ hơn 2.")
            return
        ds=[]
        for i in range(2,sokt+1):
            if Checkso(i):
                ds.append(i)
        label_ketqua.config(text="Các số nguyên tố gồm: "+",".join(map(str,ds)))

    except ValueError:
        label_ketqua.config(text="Vui Lòng Nhập số hợp lệ")

danhsach=tk.Button(text="Danh sach SNT",command=Danhsach)
danhsach.grid(row=5,column=0)
root.mainloop()
