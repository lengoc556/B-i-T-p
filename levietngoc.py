import tkinter as tk
import csv
from datetime import datetime
from tkinter import messagebox

a=tk.Tk()
a.title('Bai Tap')
a.geometry('1100x400')


def find_birthdays():
    today = datetime.today().strftime("%d-%m")
    birthdays_today = []

    try:
        with open("file.csv", "r", newline="") as a:
            reader = csv.reader(a)
            next(reader)
            for row in reader:
                if len(row) > 4:
                    birth_date = row[4]

                    if birth_date == today:
                        birthdays_today.append(row[1])

        if birthdays_today:
            messagebox.showinfo("Sinh nhật hôm nay", "\n".join(birthdays_today))
        else:
            messagebox.showinfo("Không có sinh nhật hôm nay", "Không có ai có sinh nhật hôm nay.")

    except FileNotFoundError:
        messagebox.showerror("Lỗi", "File CSV không tồn tại.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")


def LUU():
    ma=txtMA.get()
    ten=txtTEN.get()
    donvi=txtDONVI.get()
    chucdanh=txt.get()
    birth=sinh.get()
    cc=cccd.get()
    ngaycap=nc.get()
    place=noicap.get()
    d=[[ma,ten,donvi,chucdanh,birth,cc,place]]
    if not place or not ma or not ten or not donvi or not birth or not chucdanh or not cc or not ngaycap:
        messagebox.showwarning('Thiếu thông tin')
        return
    try:
        with open("file.csv","a") as a:
            s=csv.writer(a)
            s.writerow(d)

        messagebox.showinfo('Thành công')
        txtMA.delete(0,tk.END())
        txtTEN.delete(0,tk.END())
        txtDONVI.delete(0,tk.END())
        txt.delete(0,tk.END())
        sinh.delete(0,tk.END())
        cccd.delete(0,tk.END())
        nc.delete(0,tk.END())
        noicap.delete(0,tk.END())
    except Exception:
        messagebox.showerror('lỗi')


def export_to_csv():
    try:
        # Đọc dữ liệu từ CSV
        data = []
        with open("file.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

        # Kiểm tra nếu dữ liệu không trống
        if not data:
            messagebox.showwarning("Lỗi", "File CSV trống.")
            return

        today = datetime.today()

        for row in data:
            if len(row) > 4:
                birth_date_str = row[4]
                try:
                    birth_date = datetime.strptime(birth_date_str, "%d-%m")
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                except ValueError:
                    age = None

                row.append(age)


        data_sorted = sorted(data[1:], key=lambda x: x[-1], reverse=True)

        with open("Danh_sach_theo_tuoi.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data[0] + ['Tuổi'])
            writer.writerows(data_sorted)

        messagebox.showinfo("Xuất CSV", "Danh sách đã được xuất ra file CSV thành công!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")


labela=tk.Label(a,text='Thông tin nhân viên',font=('Arial',30))
labela.place(x=6,y=5,width=300,height=80)

labelMA=tk.Label(a,text='Mã *',width=50,font=('Arial',16))
labelMA.place(x=2,y=75,width=80)
txtMA=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
txtMA.place(x=25,y=100,width=220,height=30)

labelTEN=tk.Label(a,text='Tên *',font=('Arial',16))
labelTEN.place(x=247,y=75)
txtTEN=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
txtTEN.place(x=250,y=100,width=280,height=30)

labelDONVI=tk.Label(a,text='Đơn vị *',font=('Arial',16))
labelDONVI.place(x=14,y=140,width=80)
txtDONVI=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
txtDONVI.place(x=25,y=165,height=30,width=505)

chucdanh=tk.Label(a,text='Chức danh *',font=('Arial',16))
chucdanh.place(x=15,y=205,width=110)
txt=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
txt.place(x=25,y=230,width=505,height=30)

ngay=tk.Label(a,text='Ngày sinh',font=('Arial',16))
ngay.place(x=580,y=75)
sinh=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
sinh.place(x=580,y=100,height=30,width=200)

sex=tk.Label(a,text='Giới tính',font=('Arial',16))
sex.place(x=820,y=75)
nam = tk.Radiobutton(a, text="Nam", variable=tk.StringVar(value="Chưa chọn"), value="Nam",font=('Arial',16))
nam.place(x=820,y=100)
nu = tk.Radiobutton(a, text="Nữ", variable=tk.StringVar(value="Chưa chọn"), value="Nữ",font=('Arial',16))
nu.place(x=900,y=100)

cc=tk.Label(text='Số CCCD',font=('Arial',16))
cc.place(x=580,y=140)
cccd=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
cccd.place(x=580,y=165,height=30,width=300)

ngaycap=tk.Label(text='Ngày cấp',font=('Arial',16))
ngaycap.place(x=885,y=140)
nc=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
nc.place(x=885,y=165,height=30,width=190)

noi=tk.Label(text='Nơi cấp',font=('Arial',16))
noi.place(x=580,y=205)
noicap=tk.Entry(a,font=('Arial',21),highlightthickness=1,highlightbackground='black')
noicap.place(x=580,y=230,height=30,width=500)

luu=tk.Button(text='Lưu',font=('Arial',16),command=LUU)
luu.place(x=23,y=280,height=30,width=60)

find_button = tk.Button(a, text="Tìm sinh nhật hôm nay", command=find_birthdays, font=("Arial", 16))
find_button.place(x=125,y=280,height=30,width=200)

export_button = tk.Button(a, text='Xuất Excel', font=('Arial', 16), command=export_to_csv)
export_button.place(x=375, y=280, height=30, width=150)



a.mainloop()