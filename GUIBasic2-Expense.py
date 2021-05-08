# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Mr.R')
GUI.geometry('400x700+400+5')


############ MENU #############
menubar=Menu(GUI)
GUI.config(menu=menubar)
# File menu
filemenu=Menu(menubar)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import csv')
filemenu.add_command(label='Export to Googlesheet')
# Help menu
def About():
	messagebox.showinfo('About','สวัสดีครับโปรแกรมบันทึกข้อมูบ\nสนใจบริจาคให้เราไหม?')

helpmenu=Menu(menubar)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
# Donate
donatemenu=Menu(menubar)
menubar.add_cascade(label='Donate',menu=donatemenu)










#########################




tab=ttk.Notebook(GUI)
t1=Frame(tab)
t2=Frame(tab)
t1_img=PhotoImage(file='image2.png')
t2_img=PhotoImage(file='image3.png')
img1=PhotoImage(file='image1.png').subsample(1) #.subsample(1) เป็นการลดขนาดดรูปภาพนามสกุล PNG ((1)คือลด 1 เท่า) ไม่แนะนำลดขนด icon
img2=PhotoImage(file='bg1.png')
B2_img=PhotoImage(file='image4.png')
tab.pack(fill='both',expand=1,pady=20) # fill='both' เป็นคำสั่งขยาย tab ส่วน expand=1 ใช้เพื่อให้คำสั่ง fill ทำงาน อาจเปลี่ยนจาก 1 เป็น TRUE
tab.add(t1,text=f'{"บันทึกค่าใช้จ่าย":^{30}}',image=t1_img,compound='top') #compound='top' เป็นการควบคุมรูปภาพให้อยู่ด้านบนข้อความ
tab.add(t2,text=f'{"รายการบันทึก":^{30}}',image=t2_img,compound='top')
# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

F1 = Frame(t1)
F1.place(x=100,y=20)
F2 = Frame(t1)
F2.place(x=140,y=380) # .place(x=140,y=380) จะอยู่ตามค่า x และ y
F3=Frame(t2)
F3.pack() # .pack()จะอยู่ตรงกลาง

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showwarning('Error','กรุณากรอกราคา')
		return
	elif quantity == '':
		quantity = 1
	try:
		total = float(price) * float(quantity)
		# .get() คือดึงค่ามาจาก v_expense = StringVar()
		# clear ข้อมูลเก่า
		text = 'รายการ: {} ราคา: {} บาท\n'.format(expense,price)
		text1 = text + 'จำนวน: {} หน่วย รวมทั้งหมด: {} บาท'.format(quantity,total)
		v_result.set(text1)
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		dt = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
		dt1 = days[today] + '-' + dt
		
		show = StringVar()
		M = Label(t2,textvariable=show,font= FONT2,fg='blue')
		M.pack()
		
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [dt1,expense,price,quantity,total]
			fw.writerow(data)
			show1='วันที่: {} \nรายการ: {} ราคา: {} บาท รวม: {} หน่วย เป็นเงิน: {} บาท'.format(dt1,expense,price,quantity,total)
			show.set(show1)
		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
	except:
		print('ERROR')
		messagebox.showerror('ERROR','กรุณรกรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
		#messagebox.showwarning('ERROR','กรุณรกรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
		#messagebox.showinfo('ERROR','กรุณรกรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = ('TH SarabunPSK',20) 
FONT2 = ('TH SarabunPSK',16)# None เปลี่ยนเป็น 'Angsana New'

t1_logo=ttk.Label(F1,image=img1).pack()

#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1,).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------
N = ttk.Label(F3,text='รายการบันทึก',font=FONT1).pack()
#------text3--------
L = ttk.Label(F1,text='จำนวน (หน่วย)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

B2 = ttk.Button(F2,text=f'{"บันทึก":^{10}}',image=B2_img,command=Save,compound='left')
B2.pack(ipadx=5,ipady=10)

v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1, textvariable=v_result,font=FONT2,foreground='green')
# result = Label(F1, textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=85)

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8')as f:
		fr=csv.reader(f)
		data=list(fr)
	return data

#table
header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(t2,columns=header,show='headings',height=20)
resulttable.pack()

#for i in range(len(header)):
#resulttable.headings(header[i],text=header[i])
for h in header:
	resulttable.heading(h,text=h)

headerwidth=[150,70,45,45,45]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

def update_table():
	resulttable.delete(*resulttable.get_children())
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_table()

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()