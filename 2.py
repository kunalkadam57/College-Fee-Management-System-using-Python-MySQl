from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="bvcoe")

class Application:
	def __init__(self,master):
		self.master = master
		self.master.title("College Fee Management System")
		self.master.geometry("1400x750+0+0")
		self.master.configure(bg="#172B5A")
		#Variables
		nm = StringVar()
		contact = StringVar()
		mail = StringVar()
		eno = StringVar()
		fee = StringVar()
		dept = StringVar()
		yr = StringVar()
		cat = StringVar()

		#Functions
		def ireset():
			self.dataDisplay.delete("1.0",END)
			

		def iclear():
			nm.set("")
			contact.set("")
			mail.set("")
			fee.set("")

		

		def iExit():
			iExit = tkinter.messagebox.askyesno("College Fee Management System","Confirm if you want to exit")
			if iExit > 0:
				root.destroy()
				return

		def iDisplay():
			self.dataDisplay.insert(END,"\n\tSTUDENT DETAIL\t\n\nName : "+nm.get()+"\nContact No : "+contact.get()
				+"\nGmaiil Id : "+mail.get()+"\nFee: "+fee.get()+"\nDepartment : "+dept.get()+"\nYear : "+yr.get()+"\nCaste Category : "+
				cat.get()+"\n")

		def iSubmit():
	
			mycursor = db.cursor()
			sql = "create database if not exists CLG"
			mycursor.execute(sql)
			sql = "use CLG"
			mycursor.execute(sql)
			sql = "create table if not exists ENTRIES1 (Name varchar(20),Contact varchar(10),Gmail varchar(35),Fee varchar(20),Department varchar(6),Year varchar(4),Category varchar(20))"
			mycursor.execute(sql)
			mycursor.execute("insert into ENTRIES1 (Name,Contact,Gmail,Fee,Department,Year,Category)values(%s,%s,%s,%s,%s,%s,%s)",(nm.get(),contact.get(),mail.get(),fee.get(),dept.get(),yr.get(),cat.get(),))
			db.commit()

		def aReset():
			self.analysisDisplay.delete("1.0",END)

		def aExit():
			self.master1.destroy()
			return			
		def aDAnalysis():
			self.analysisDisplay.insert(END,"\n\t\t\tDEPARTMENTAL ANALYSIS\t\t\t\n")
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Department='C.M'"
			c.execute(sql)
			data = c.fetchall()
			ccount=0
			for i in data:
				ccount=ccount+1
			
			sql = "select Name,Contact from ENTRIES1 where Department='I.T'"
			c.execute(sql)
			data = c.fetchall()
			icount=0
			for i in data:
				icount=icount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Department='E.X.T.C'"
			c.execute(sql)
			data = c.fetchall()
			ecount=0
			for i in data:
				ecount=ecount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Department='INSTRU'"
			c.execute(sql)
			data = c.fetchall()
			incount=0
			for i in data:
				incount=incount+1

			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Department='CHEM'"
			c.execute(sql)
			data = c.fetchall()
			chcount=0
			for i in data:
				chcount=chcount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Department='MECH'"
			c.execute(sql)
			data = c.fetchall()
			mcount=0
			for i in data:
				mcount=mcount+1


			self.analysisDisplay.insert(END,"\nTotal Entries From \nComputer Department = "+str(ccount)+
				"\nIT Department = "+str(icount)+"\nEXTC Department = "+str(ecount)+"\nInstrumentaiton Department = "+str(incount)
				+"\nChemcial Department = "+str(chcount)+"\nMechanical Department = "+str(mcount)+"\n")


		def aYAnalysis():
			self.analysisDisplay.insert(END,"\n\t\t\tYEAR WISE ANALYSIS\t\t\t\n")
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Year='F.E'"
			c.execute(sql)
			data = c.fetchall()
			fcount=0
			for i in data:
				fcount=fcount+1
			
			sql = "select Name,Contact from ENTRIES1 where Year='S.E'"
			c.execute(sql)
			data = c.fetchall()
			scount=0
			for i in data:
				scount=scount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Year='T.E'"
			c.execute(sql)
			data = c.fetchall()
			tcount=0
			for i in data:
				tcount=tcount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Year='B.E'"
			c.execute(sql)
			data = c.fetchall()
			bcount=0
			for i in data:
				bcount=bcount+1

	
			self.analysisDisplay.insert(END,"\nTotal Entries From \nFirst Year = "+str(fcount)+
				"\nSecond Year = "+str(scount)+"\nThird Year = "+str(tcount)+"\nFinal Year = "+str(bcount)+"\n")

		def aCatAnalysis():
			self.analysisDisplay.insert(END,"\n\t\t\tCATEGORY WISE ANALYSIS\t\t\t\n")
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Category='OPEN'"
			c.execute(sql)
			data = c.fetchall()
			tcount=0
			for i in data:
				tcount=tcount+1
			
			sql = "select Name,Contact from ENTRIES1 where Category='O.B.C'"
			c.execute(sql)
			data = c.fetchall()
			gcount=0
			for i in data:
				gcount=gcount+1
			
			c = db.cursor()
			c.execute("use CLG")
			sql = "select Name,Contact from ENTRIES1 where Category='OTHERS'"
			c.execute(sql)
			data = c.fetchall()
			fcount=0
			for i in data:
				fcount=fcount+1

			self.analysisDisplay.insert(END,"\nTotal Entries For\nOPEN = "+str(tcount)+
				"\nO.B.C = "+str(gcount)+"\nOTHERS = "+str(fcount)+"\n")




		def iShow():
			self.master1 = Toplevel(master)
			self.master1.title("Analysis of Entries")
			self.master1.geometry("750x750")
			self.LAFrame = Frame(self.master1,width=370,height=750,bd=3,relief=RAISED,bg="blue")
			self.LAFrame.pack(side=LEFT)
			self.RAFrame = Frame(self.master1,width=370,height=750,bd=3,relief=RAISED,bg="white")
			self.RAFrame.pack(side=RIGHT)
			self.analysisDisplay = Text(self.RAFrame,font="3ds 15",bg="white",fg="black",width=370,height=750)
			self.analysisDisplay.pack(side=RIGHT)
			self.Lanalysis = Label(self.LAFrame,text="Analysis Board",font="3ds 30",bg="#0035B4",fg="white").grid(row=0,column=1)
			self.DAnalysis = Button(self.LAFrame,font="3ds 18 bold",text="DEPT ANALYSIS",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=aDAnalysis).grid(row=2,column=1)
			self.YRAnalysis = Button(self.LAFrame,font="3ds 18 bold",text="YEAR ANALYSIS",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=aYAnalysis).grid(row=3,column=1)
			self.CATAnalysis = Button(self.LAFrame,font="3ds 18 bold",text="CATEGORY ANALYSIS",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=aCatAnalysis).grid(row=4,column=1)
			self.RReset = Button(self.LAFrame,font="3ds 18 bold",text="RESET",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=aReset).grid(row=5,column=1)
			self.RExit = Button(self.LAFrame,font="3ds 18 bold",text="EXIT",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=aExit).grid(row=6,column=1)


		#Frames
		self.TopFrame = Frame(master,width=1400,bd=3,relief=RAISED)
		self.TopFrame.pack(side=TOP)
		self.LeftFrame = Frame(master,width=900,height=700,bd=3,relief=RIDGE,bg="maroon")
		self.LeftFrame.place(x=0,y=82)
		self.RightFrame = Frame(master,width=500,height=700,bd=3,relief=SUNKEN,bg="grey")
		self.RightFrame.place(x=900,y=82)
		self.BottomFrame = Frame(master,width=1400,height=200,bd=3,relief=RAISED,bg="black")
		self.BottomFrame.place(x=0,y=600)
		#Heading
		self.Title = Label(self.TopFrame,text="FEE MANAGEMENT SYSTEM",font="3ds 44 bold",bg="#0035B4",fg="yellow",width=40)
		self.Title.grid(row=0,column=1)
		#Labels
		self.name = Label(self.LeftFrame,text="Name",font="3ds 30",bg="yellow",fg="white")
		self.name.grid(row=0,column=0,sticky=W)
		self.contactNo = Label(self.LeftFrame,text="Contact No",font="3ds 30",bg="yellow",fg="white")
		self.contactNo.grid(row=1,column=0,sticky=W)
		self.gmailId = Label(self.LeftFrame,text="Gmail",font="3ds 30",bg="yellow",fg="white")
		self.gmailId.grid(row=2,column=0,sticky=W)
		self.department = Label(self.LeftFrame,text="Department",font="3ds 30",bg="yellow",fg="white")
		self.department.grid(row=4,column=0,sticky=W)
		self.year = Label(self.LeftFrame,text="Year",font="3ds 30",bg="yellow",fg="white")
		self.year.grid(row=5,column=0,sticky=W)
		self.fee = Label(self.LeftFrame,text="Fee",font="3ds 30",bg="yellow",fg="white")
		self.fee.grid(row=3,column=0,sticky=W)
		self.event = Label(self.LeftFrame,text="Caste Category",font="3ds 30",bg="yellow",fg="white")
		self.event.grid(row=6,column=0,sticky=W)
		#Entry boxes
		self.ename = Entry(self.LeftFrame,font="3ds 15 bold",width=30,bd=6,relief=FLAT,textvariable=nm)
		self.ename.grid(row=0,column=2)
		self.econtactNo = Entry(self.LeftFrame,font="3ds 15 bold",width=30,bd=6,relief=FLAT,textvariable=contact)
		self.econtactNo.grid(row=1,column=2)
		self.egmailId = Entry(self.LeftFrame,font="3ds 15 bold",width=30,bd=6,relief=FLAT,textvariable=mail)
		self.egmailId.grid(row=2,column=2)
		#Creating Drop down list
		self.edepartment = ttk.Combobox(self.LeftFrame,font="3ds 15 bold",width=30,textvariable=dept)
		self.edepartment['value']=('',"C.M","I.T","E.X.T.C","INSTRU","CHEM","MECH")
		self.edepartment.current(1)#setting default value to C.M
		self.edepartment.grid(row=4,column=2)
		self.eyear = ttk.Combobox(self.LeftFrame,font="3ds 15 bold",width=30,textvariable=yr)
		self.eyear['value']=('',"F.E","S.E","T.E","B.E")
		self.eyear.current(1)
		self.eyear.grid(row=5,column=2)
		self.efee = Entry(self.LeftFrame,font="3ds 15 bold",width=30,bd=6,relief=FLAT,textvariable=fee)
		self.efee.grid(row=3,column=2)
		self.eevent = ttk.Combobox(self.LeftFrame,font="3ds 15 bold",width=30,textvariable=cat)
		self.eevent['value']=('',"OPEN","O.B.C","OTHERS")
		self.eevent.current(1)
		self.eevent.grid(row=6,column=2)
		#Buttons
		self.submit = Button(self.LeftFrame,font="3ds 18 bold",text="SUBMIT",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=iSubmit)
		self.submit.grid(row=9,column=2)
		self.display = Button(self.LeftFrame,font="3ds 18 bold",text="DISPLAY DATA",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=iDisplay)
		self.display.grid(row=7,column=2)
		self.reset = Button(self.LeftFrame,font="3ds 18 bold",text="CLEAR DATA",bg="black",fg="white",relief=RAISED,bd=3,width=20,command=iclear)
		self.reset.grid(row=8,column=2)
		self.showAnalysis = Button(self.BottomFrame,font="3ds 18 bold",text="SHOW ANALYSIS",bg="black",fg="white",relief=RAISED,bd=3,width=30,command=iShow)
		self.showAnalysis.grid(row=1,column=0)
		self.resetAnalysis = Button(self.BottomFrame,font="3ds 18 bold",text="RESET ANALYSIS",bg="black",fg="white",relief=RAISED,bd=3,width=30,command=ireset)
		self.resetAnalysis.grid(row=1,column=2)
		self.exit = Button(self.BottomFrame,font="3ds 18 bold",text="EXIT",bg="black",fg="white",relief=RAISED,bd=3,width=30,command=iExit)
		self.exit.grid(row=1,column=4)
		#Text Boxes
		self.dataDisplay = Text(self.RightFrame,font="3ds 15",bg="white",fg="black",width=500,height=700)
		self.dataDisplay.grid(row=0,column=0)
root = Tk()
b = Application(root)
root.mainloop()