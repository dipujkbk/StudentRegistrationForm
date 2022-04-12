from tkinter import *
from tkinter import ttk
window=Tk()
window.title("STUDENT REGISTRATION FORM")
window.geometry('800x600')
window.configure(background="blue violet");
a = Label(window ,text = "FIRST NAME ",fg="white",bg="blue violet").grid(row = 0,column = 0)
b = Label(window ,text = "LAST NAME ",fg="white",bg="blue violet").grid(row = 1,column = 0)
c = Label(window ,text = "DATE OF BIRTH ",fg="white",bg="blue violet").grid(row = 2,column = 0)
d = Label(window ,text = "EMAIL ID ",fg="white",bg="blue violet").grid(row = 3,column = 0)
e = Label(window ,text = "MOBILE NUMBER ",fg="white",bg="blue violet").grid(row = 4,column = 0)
f = Label(window ,text = "GENDER ",fg="white",bg="blue violet").grid(row = 5,column = 0)
g = Label(window ,text = "ADDRESS ",fg="white",bg="blue violet").grid(row = 6,column = 0)
h = Label(window ,text = "CITY ",fg="white",bg="blue violet").grid(row = 9,column = 0)
i = Label(window ,text = "PINCODE ",fg="white",bg="blue violet").grid(row = 10,column = 0)
j = Label(window ,text = "STATE ",fg="white",bg="blue violet").grid(row = 11,column = 0)
k = Label(window ,text = "COUNTRY ",fg="white",bg="blue violet").grid(row = 12,column = 0)
l = Label(window ,text = "HOBBIES ",fg="white",bg="blue violet").grid(row = 13,column = 0)
m = Label(window ,text = "QUALIFICATIONS ",fg="white",bg="blue violet").grid(row = 16,column = 0)
n = Label(window ,text = "COURSES APPLIED FOR ",fg="white",bg="blue violet").grid(row = 23,column = 0)

e1=Entry(window,fg="black",bg="white").grid(row = 0,column = 10)
ttk.Label(window,text="(max 30 character A-Z and a-z)",font=("Helvetica",7),background="blue violet",foreground="white").grid(row=0,column=11)

e2=Entry(window,fg="black",bg="white").grid(row = 1,column = 10)
ttk.Label(window,text="(max 30 character A-Z and a-z)",font=("Helvetica",7),background="blue violet",foreground="white").grid(row=1,column=11)

day=StringVar()
day = ttk.Combobox(window,width=5,textvariable=day)
day.grid(row=2,column=10)
ttk.Label(window, text = "Day:",state='readonly',background="white").grid(row=2,column=10)
day['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')

month=StringVar()
month=ttk.Combobox(window,width=7,textvariable=month)
month.grid(row=2,column=11)
ttk.Label(window,text="Month:",state='readonly',background="white").grid(row=2,column=11)
month['values']=('January','February','March','April','May','June','July','August','September','October','November','December')

year=IntVar()
year=ttk.Combobox(window,width=6,textvariable=year)
year.grid(row=2,column=12)
ttk.Label(window,text="Year:",state='readonly',background="white").grid(row=2,column=12)
year['values']=(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021)

e3=Entry(window,fg="black",bg="white").grid(row=3,column=10)

e4=Entry(window,fg="black",bg="white").grid(row=4,column=10)
ttk.Label(window,text="10 digit number",font=("Helvetica",7),background="blue violet",foreground="white").grid(row=4,column=11)

radio=IntVar()
R1=Radiobutton(window,bg="blue violet",fg="white",text="Male",variable=radio,value=1).grid(row=5,column=10)
R2=Radiobutton(window,bg="blue violet",fg="white",text="Female",variable=radio,value=2).grid(row=5,column=11)

e3=Entry(window,fg="black",bg="white").grid(row=6,column=10)

e4=Entry(window,fg="black",bg="white").grid(row=9,column=10)

e5=Entry(window,fg="black",bg="white").grid(row=10,column=10)

e6=Entry(window,fg="black",bg="white").grid(row=11,column=10)

e7=Entry(window,fg="black",bg="white").grid(row=12,column=10)

C1=Checkbutton(window,text = "Drawing",background="blue violet",foreground="white").grid(row=13,column=10)
C2=Checkbutton(window,text="Singing",background="blue violet",foreground="white").grid(row=13,column=11)
C3=Checkbutton(window,text="Dancing",background="blue violet",foreground="white").grid(row=13,column=12)
C4=Checkbutton(window,text="Sketching",background="blue violet",foreground="white").grid(row=13,column=13)
C5=Checkbutton(window,text="Others",background="blue violet",foreground="white").grid(row=14,column=10)
e8=Entry(window,fg="black",bg="white").grid(row=14,column=11)

ttk.Label(window,text="SI.No.Examination",background="blue violet",foreground="white").grid(row=15,column=8)
ttk.Label(window,text="Board",background="blue violet",foreground="white").grid(row=15,column=11)
ttk.Label(window,text="Percentage",background="blue violet",foreground="white").grid(row=15,column=12)
ttk.Label(window,text="Year Of Passing",background="blue violet",foreground="white").grid(row=15,column=13)
ttk.Label(window,text="1 Class X",background="blue violet",foreground="white").grid(row=17,column=8)
ttk.Label(window,text="2 Class XII",background="blue violet",foreground="white").grid(row=18,column=8)
ttk.Label(window,text="3 Graduation",background="blue violet",foreground="white").grid(row=19,column=8)
ttk.Label(window,text="4 Masters",background="blue violet",foreground="white").grid(row=20,column=8)
e9=Entry(window,fg="black",bg="white").grid(row=17,column=11)
e10=Entry(window,fg="black",bg="white").grid(row=17,column=12)
e11=Entry(window,fg="black",bg="white").grid(row=17,column=13)
e12=Entry(window,fg="black",bg="white").grid(row=18,column=11)
e13=Entry(window,fg="black",bg="white").grid(row=18,column=12)
e14=Entry(window,fg="black",bg="white").grid(row=18,column=13)
e15=Entry(window,fg="black",bg="white").grid(row=19,column=11)
e16=Entry(window,fg="black",bg="white").grid(row=19,column=12)
e17=Entry(window,fg="black",bg="white").grid(row=19,column=13)
e18=Entry(window,fg="black",bg="white").grid(row=20,column=11)
e19=Entry(window,fg="black",bg="white").grid(row=20,column=12)
e20=Entry(window,fg="black",bg="white").grid(row=20,column=13)

radio=IntVar()
R3=Radiobutton(window,bg="blue violet",fg="white",text="BCA",variable=radio,value=1).grid(row=23,column=10)
R4=Radiobutton(window,fg="white",bg="blue violet",text="B.Com",variable=radio,value=2).grid(row=23,column=11)
R5=Radiobutton(window,fg="white",bg="blue violet",text="B.Sc",variable=radio,value=3).grid(row=23,column=12)
R6=Radiobutton(window,fg="white",bg="blue violet",text="B.A.",variable=radio,value=4).grid(row=23,column=13)


B1=Button(window,text="SUBMIT").grid(row=24,column=11)
B2=Button(window,text="RESET").grid(row=24,column=13)
window.mainloop()