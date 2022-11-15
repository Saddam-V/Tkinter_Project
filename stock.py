import abc
from asyncio.windows_events import NULL
from cgitb import enable
from msilib.schema import ListBox
import datetime
from multiprocessing.connection import wait
import tkinter as tk
from tkinter import *
from tkinter import ttk
#from tkinter import BOTH, BOTTOM, END, LEFT, RIDGE, RIGHT, TOP, W, Button, Canvas, Entry, Frame, Label, LabelFrame, Scrollbar, StringVar, ttk
import tkinter.messagebox
from turtle import bgcolor
import stdDatabase_BackEnd
from matplotlib.pyplot import title
import sqlite3
import os
import win32api
import random
from tkinter import filedialog


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Al-Sams Data Management")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, stock, rpay, bill, user, rtrn):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, stock, rpay respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        style = ttk.Style()

        button1 = ttk.Button(self, text="STOCK", style="big.TButton",
                             command=lambda: controller.show_frame(stock))

        style.configure('big.TButton2', font=(
            None, 30, 'bold'), background="blue4")
        style.configure('big.TButton', font=(
            None, 30, 'bold'), foreground="blue4")
        # putting the button in its place by
        # using grid
        button1.pack(fill=BOTH, expand=True)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="RPAY", style="big.TButton",
                             command=lambda: controller.show_frame(rpay))

        # putting the button in its place by
        # using grid
        button2.pack(fill=BOTH, expand=True)

        button3 = ttk.Button(self, text="BILL", style="big.TButton",
                             command=lambda: controller.show_frame(bill))

        # putting the button in its place by
        # using grid
        button3.pack(fill=BOTH, expand=True)

        button4 = ttk.Button(self, text="USER", style="big.TButton",
                             command=lambda: controller.show_frame(user))

        # putting the button in its place by
        # using grid
        button4.pack(fill=BOTH, expand=True)

        button5 = ttk.Button(self, text="RETURN", style="big.TButton",
                             command=lambda: controller.show_frame(rtrn))

        # putting the button in its place by
        # using grid
        button5.pack(fill=BOTH, expand=True)

        # button4 = ttk.Button(self, text ="Payment",
        # command = lambda : controller.show_frame(rpay))

        # # putting the button in its place by
        # # using grid
        # button4.grid(row = 2, column = 1, padx = 10, pady = 10)

        # button5 = ttk.Button(self, text ="User Info",
        # command = lambda : controller.show_frame(rpay))

        # # putting the button in its place by
        # # using grid
        # button5.grid(row = 2, column = 1, padx = 10, pady = 10)


# second window frame stock
class stock(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

#####################################################################################################################
        # self.parent=parent
        # self.parent.title("Student database system")
        # self.parent.config(bg="snow3")
        # stock.config(width=200)
        Cat = StringVar()
        Num = StringVar()
        Meter = StringVar()
        Dob = StringVar()
        Dob2 = StringVar()
        Age = StringVar()

        # Gender = StringVar()
        # Adress = StringVar()
        # Mobile = StringVar()
        # Roomno = StringVar()
        # Blockno = StringVar()
        # Course = StringVar()
        # =============================================================Functions===============================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Al-Sams Data Management System", "Do you want to Exit the program?")
            if iExit > 0:
                parent.destroy()
                return

        def printreceived():
            scrol_y = Scrollbar(MainFrame, orient=VERTICAL)
            textarea1 = Text(MainFrame, yscrollcommand=scrol_y)
            # scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=textarea1.yview)
            textarea1.delete(1.0, END)
            con = sqlite3.connect("StockEntry.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM entry")
            res = cur.fetchall()
            textarea1.insert(
                END, "Orders Received\n Si  Cat    Col   Met Luff  Date \n")
            for row in res:
                textarea1.insert(END, str(row) + "\n")
            con.close()

            textarea1.configure(font='arial 13 bold')
            currentDateTime = datetime.datetime.now()
            cwd = os.getcwd()
            bill_details1 = textarea1.get('1.0', END)
            f1 = open("bills/"+str(currentDateTime.date())+"received.txt", "w")
            f1.write(bill_details1)
            f1.close()
            win32api.ShellExecute(
                0, "print", cwd + "/bills/"+str(currentDateTime.date())+"received.txt", None, ".", 0)

        def printnotreceived():
            scrol_y = Scrollbar(MainFrame, orient=VERTICAL)
            textarea1 = Text(MainFrame, yscrollcommand=scrol_y)
            # scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=textarea1.yview)
            textarea1.delete(1.0, END)
            con = sqlite3.connect("StockEntry.db")
            cur = con.cursor()
            textarea1.insert(
                END, "\n\nOrders Not Received\n Si  Cat    Col   Met Luff  Date \n")
            cur.execute("SELECT * FROM entry3")
            res2 = cur.fetchall()
            for row in res2:
                textarea1.insert(END, str(row) + "\n")
            con.close()

            textarea1.configure(font='arial 13 bold')
            currentDateTime = datetime.datetime.now()
            cwd = os.getcwd()
            bill_details1 = textarea1.get('1.0', END)
            f1 = open("bills/"+str(currentDateTime.date()) +
                      "notreceived.txt", "w")
            f1.write(bill_details1)
            f1.close()
            win32api.ShellExecute(
                0, "print", cwd + "/bills/"+str(currentDateTime.date())+"notreceived.txt", None, ".", 0)

        def printtotal():
            scrol_y = Scrollbar(MainFrame, orient=VERTICAL)
            textarea1 = Text(MainFrame, yscrollcommand=scrol_y)
            # scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=textarea1.yview)
            textarea1.delete(1.0, END)
            con = sqlite3.connect("StockEntry.db")
            cur = con.cursor()
            textarea1.insert(
                END, "\n\nTotal Stock\n Si  Cat    Col   Met Luff  Date \n")
            cur.execute("SELECT * FROM entry2")
            res3 = cur.fetchall()
            for row in res3:
                textarea1.insert(END, str(row) + "\n")
            con.close()

            textarea1.configure(font='arial 13 bold')
            currentDateTime = datetime.datetime.now()
            cwd = os.getcwd()
            bill_details1 = textarea1.get('1.0', END)
            f1 = open("bills/"+str(currentDateTime.date())+"total.txt", "w")
            f1.write(bill_details1)
            f1.close()
            win32api.ShellExecute(
                0, "print", cwd + "/bills/"+str(currentDateTime.date())+"total.txt", None, ".", 0)

        def Stdrec(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)

            self.txtCat.delete(0, END)
            self.txtCat.insert(END, sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtLna.delete(0, END)
            self.txtLna.insert(END, sd[3])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[4])
            # self.txtDob.delete(0, END)
            # self.txtDob.insert(END, sd[5])

            # self.txtGender.delete(0, END)
            # self.txtGender.insert(END, sd[6])
            # self.txtAdress.delete(0, END)
            # self.txtAdress.insert(END, sd[7])
            # self.txtMobile.delete(0, END)
            # self.txtMobile.insert(END, sd[8])
            # self.txtroomno.delete(0, END)
            # self.txtroomno.insert(END, sd[9])
            # self.txtBlkno.delete(0, END)
            # self.txtBlkno.insert(END, sd[10])
            # self.txtCrs.delete(0, END)
            # self.txtCrs.insert(END, sd[11])

        def cleardata():
            self.txtCat.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtDob2.delete(0, END)
            # self.txtGender.delete(0, END)
            # self.txtAdress.delete(0, END)
            # self.txtMobile.delete(0, END)
            # self.txtroomno.delete(0, END)
            # self.txtBlkno.delete(0, END)
            # self.txtCrs.delete(0, END)

        def addData():
            try:
                if(len(Cat.get()) != 0):
                    # bll = bill(parent,controller)
                    # clr=bll.clearall
                    # clr()
                    stdDatabase_BackEnd.addEntRec(
                        Cat.get(), Num.get(), Meter.get(), Age.get(), sd[0])
                    # , Dob.get() , Age.get() , Gender.get() , Adress.get() ,Mobile.get(), \
                    #                                 Roomno.get(), Blockno.get() , Course.get()
                    studentlist.delete(0, END)
                    studentlist.insert(
                        END, (Cat.get(), Num.get(), Meter.get()))
                    cleardata()
            except:
                tkinter.messagebox.showerror("Error", "Clear bills first!")

        def addOrder():
            try:
                if(len(Cat.get()) != 0):
                    # bll = bill(parent,controller)
                    # clr=bll.clearall
                    # clr()
                    stdDatabase_BackEnd.addOrdRec(
                        Cat.get(), Num.get(), Age.get())
                    # , Dob.get() , Age.get() , Gender.get() , Adress.get() ,Mobile.get(), \
                    #                                 Roomno.get(), Blockno.get() , Course.get()
                    studentlist.delete(0, END)
                    studentlist.insert(END, (Cat.get(), Num.get(), Age.get()))
                    cleardata()
            except:
                tkinter.messagebox.showerror("Error", "Clear bills first!")

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.Viewdata():
                studentlist.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def DisplayOrders():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.Vieworders():
                studentlist.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def DisplayTotalData():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.Viewtotaldata():
                studentlist.insert(END, row, str(
                    "--------------------------------------------------"))

        def deleteData():
            if(len(Cat.get()) != 0):
                # bill.clear()
                stdDatabase_BackEnd.deletRec(sd[0], Meter.get(), Age.get())
                cleardata()
                studentlist.delete(0, END)

        def Searchdatabase():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.searchdata(Cat.get(), Num.get(), Meter.get(), Dob.get(), Dob2.get()):
                studentlist.insert(END, row, str(""))

        def Searchorders():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.searchorders(Cat.get(), Num.get(), Age.get(), Dob.get(), Dob2.get()):
                studentlist.insert(END, row, str(""))

        def SearchTotaldata():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.searchtotaldata(Cat.get(), Num.get(), Meter.get(), Dob.get()):
                studentlist.insert(END, row, str(""))

        def DisplayOptions():
            x = clicked.get()
            if(x == "Received"):
                DisplayData()
            elif(x == "NotReceived"):
                DisplayOrders()
            elif(x == "Total"):
                DisplayTotalData()
            else:
                tkinter.messagebox.showerror("Error", "Select an option")

        def SearchOption():
            x2 = clicked2.get()
            if(x2 == "Received"):
                Searchdatabase()
            elif(x2 == "NotReceived"):
                Searchorders()
            elif(x2 == "Total"):
                SearchTotaldata()
            else:
                tkinter.messagebox.showerror("Error", "Select an option")

        def PrintOption():
            x3 = clicked3.get()
            if(x3 == "Received"):
                printreceived()
            elif(x3 == "NotReceived"):
                printnotreceived()
            elif(x3 == "Total"):
                printtotal()
            else:
                tkinter.messagebox.showerror("Error", "Select an option")

        # def UpdateDatabase():
        #     if(len(Cat.get())!=0):
        #         stdDatabase_BackEnd.deletRec(sd[0])

            # if (len(Cat.get()) != 0):
            #     stdDatabase_BackEnd.addStdRec(Cat.get(), Num.get(), Meter.get())
            #     studentlist.delete(0, END)
            #     studentlist.insert(END, (Cat.get(), Num.get(), Meter.get()))

        # =============================================================FRAMES===================================================================

        MainFrame = Frame(self, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP)

        # self.canv = Canvas(TitFrame, width=250, height=70, bg='white')
        # self.canv.grid(row=0,column=0)

        self.lblTit = Label(TitFrame, font=('arial', 25, 'bold'),
                            text="AL-SAMS DATA MANAGEMENT SYSTEM", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=800, height=90,
                            padx=1, pady=1, bg="snow3", relief=RIDGE)
        ButtonFrame.pack(side=RIGHT)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray60", fg="black", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Data Entry\n")
        DataFrameLEFT.pack(side=TOP)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray30", fg="white", relief=RIDGE,
                                    font=('arial', 15, 'bold'), text="Details\n    CT CR M L D")
        DataFrameRIGHT.pack(side=BOTTOM)

        # ========================================================Labels and Entry Widget===================================================================

        self.lblCat = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'), text="Catalogue :", padx=1, pady=3, bg="gray60")
        self.lblCat.grid(row=0, column=0, sticky=W)
        self.txtCat = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Cat, width=30)
        self.txtCat.grid(row=0, column=1)

        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Colour :", padx=2, pady=5,
                            bg="gray60")
        self.lblFna.grid(row=1, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Num, width=30)
        self.txtFna.grid(row=1, column=1)

        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Meter", padx=2, pady=5,
                            bg="gray60")
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Meter, width=30)
        self.txtLna.grid(row=2, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Luffa:", padx=2, pady=2,
                            bg="gray60")
        self.lblAge.grid(row=3, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Age, width=30)
        self.txtAge.grid(row=3, column=1)

        self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date From:", padx=2, pady=5,
                            bg="gray60")
        self.lblDob.grid(row=4, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Dob, width=30)
        self.txtDob.grid(row=4, column=1)

        self.lblDob2 = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date To:", padx=2, pady=5,
                             bg="gray60")
        self.lblDob2.grid(row=5, column=0, sticky=W)
        self.txtDob2 = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Dob2, width=30)
        self.txtDob2.grid(row=5, column=1)

        # self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Year:", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblGender.grid(row=5, column=0, sticky=W)
        # self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        # self.txtGender.grid(row=5, column=1)

        # self.lblAdress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Parents Mobile:", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblAdress.grid(row=6, column=0, sticky=W)
        # self.txtAdress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Adress, width=39)
        # self.txtAdress.grid(row=6, column=1)

        # self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student Mobile:", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblMobile.grid(row=7, column=0, sticky=W)
        # self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        # self.txtMobile.grid(row=7, column=1)

        # self.lblroomno = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Room no:", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblroomno.grid(row=8, column=0, sticky=W)
        # self.txtroomno = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Roomno, width=39)
        # self.txtroomno.grid(row=8, column=1)

        # self.lblBlkno = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Block:", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblBlkno.grid(row=9, column=0, sticky=W)
        # self.txtBlkno = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Blockno, width=39)
        # self.txtBlkno.grid(row=9, column=1)

        # self.lblCrs = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Warden name:", padx=2, pady=2,
        #                       bg="aquamarine")
        # self.lblCrs.grid(row=10, column=0, sticky=W)
        # self.txtCrs = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Course, width=39)
        # self.txtCrs.grid(row=10, column=1)

        # ========================================================ScrollBar and ListBox===================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = tk.Listbox(DataFrameRIGHT, width=70, height=10, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', Stdrec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # ========================================================Button Widget===================================================================

        self.btnAddData = Button(ButtonFrame, text="Add New Order", font=(
            'arial', 14, 'bold'), fg="black", bg="seashell3", width=13, height=1, bd=4, command=addOrder)
        self.btnAddData.grid(row=0, column=0, padx=10, pady=10)

        self.btnAddData = Button(ButtonFrame, text="Add To Stock", font=(
            'arial', 14, 'bold'), fg="white", bg="seashell4", width=13, height=1, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=1, padx=10, pady=30)

        clicked = StringVar()
        clicked.set("Select")
        options = [
            "Received",
            "NotReceived",
            "Total"
        ]
        drop = OptionMenu(ButtonFrame, clicked, *options)
        drop.grid(row=1, column=0, padx=10, pady=30)
        self.btnSearch = Button(ButtonFrame, text="Display", font=(
            'arial', 14, 'bold'), fg="white", bg="seashell4", width=14, height=1, bd=4, command=DisplayOptions)
        self.btnSearch.grid(row=1, column=1, padx=10, pady=10)

        # self.btnDispay = Button(ButtonFrame, text="Received", font=(
        #     'arial', 12, 'bold'), fg="black", bg="seashell3", width=9, height=1, bd=4, command=DisplayData)
        # self.btnDispay.grid(row=1, column=0, padx=10, pady=10)

        # self.btnDispay = Button(ButtonFrame, text="Not Received", font=(
        #     'arial', 12, 'bold'), fg="black", bg="seashell3", width=11, height=1, bd=4, command=DisplayOrders)
        # self.btnDispay.grid(row=1, column=2, padx=10, pady=10)

        clicked2 = StringVar()
        clicked2.set("Select")
        drop = OptionMenu(ButtonFrame, clicked2, *options)
        drop.grid(row=2, column=0, padx=10, pady=30)
        self.btnSearch = Button(ButtonFrame, text="Search", font=(
            'arial', 14, 'bold'), fg="white", bg="seashell4", width=14, height=1, bd=4, command=SearchOption)
        self.btnSearch.grid(row=2, column=1, padx=10, pady=10)

        clicked3 = StringVar()
        clicked3.set("Select")
        drop = OptionMenu(ButtonFrame, clicked3, *options)
        drop.grid(row=3, column=0, padx=10, pady=30)
        self.btnSearch = Button(ButtonFrame, text="Print", font=(
            'arial', 14, 'bold'), fg="white", bg="seashell4", width=14, height=1, bd=4, command=PrintOption)
        self.btnSearch.grid(row=3, column=1, padx=10, pady=10)

        # self.btnSearch = Button(ButtonFrame, text="Search Received", font=(
        #     'arial', 11, 'bold'), fg="black", bg="seashell3", width=14, height=1, bd=4, command=Searchdatabase)
        # self.btnSearch.grid(row=2, column=0, padx=10, pady=30)

        # self.btnSearch = Button(ButtonFrame, text="Search Not Received", font=(
        #     'arial', 11, 'bold'), fg="black", bg="seashell3", width=16, height=1, bd=4, command=Searchorders)
        # self.btnSearch.grid(row=2, column=2, padx=10, pady=30)

        # self.btnSearch = Button(ButtonFrame, text="Search Total Stock", font=(
        #     'arial', 14, 'bold'), fg="white", bg="seashell4", width=14, height=1, bd=4, command=SearchTotaldata)
        # self.btnSearch.grid(row=5, column=0, padx=10, pady=10)

        # self.btnSearch = Button(ButtonFrame, text="Display Total Stock", font=(
        #     'arial', 14, 'bold'), fg="white", bg="seashell4", width=14, height=1, bd=4, command=DisplayTotalData)
        # self.btnSearch.grid(row=5, column=2, padx=10, pady=10)

        self.btnClear = Button(ButtonFrame, text="Clear", font=(
            'arial', 14, 'bold'), fg="white", bg="grey", width=6, height=1, bd=4, command=cleardata)
        self.btnClear.grid(row=4, column=0, padx=10, pady=10)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=(
            'arial', 14, 'bold'), fg="white", bg="grey", width=6, height=1, bd=4, command=deleteData)
        self.btnDelete.grid(row=4, column=1, padx=10, pady=10)

        # self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command = UpdateDatabase)
        # self.btnUpdate.grid(row=0, column=5, padx=10, pady=10)

        # self.btnExit = Button(ButtonFrame, text="Exit", font=(
        #     'arial', 14, 'bold'), fg="white", bg="grey", width=6, height=1, bd=4, command=iExit)
        # self.btnExit.grid(row=9, column=1, padx=10, pady=10)

        style = ttk.Style()
        ##########################################################################################################################
        style.configure('big2.TButton', font=(
            None, 20, 'bold'), foreground="black")
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(ButtonFrame, text="Home", style="big2.TButton",
                             command=lambda: controller.show_frame(Home))

        # putting the button in its place
        # by using grid
        button1.grid(row=5, column=0, padx=10, pady=10)

        # button3 = ttk.Button(ButtonFrame, text="Print Received", style="big2.TButton",
        #                      command=printreceived)
        # button3.grid(row=9, column=0, padx=10, pady=10)

        # button4 = ttk.Button(ButtonFrame, text="Print Not Received", style="big2.TButton",
        #                      command=printnotreceived)
        # button4.grid(row=9, column=1, padx=10, pady=10)

        # button5 = ttk.Button(ButtonFrame, text="Print Total", style="big2.TButton",
        #                      command=printtotal)
        # button5.grid(row=9, column=2, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(ButtonFrame, text="Bills", style="big2.TButton",
                             command=lambda: controller.show_frame(bill))

        # putting the button in its place by
        # using grid
        button2.grid(row=5, column=1, padx=10, pady=10)


# third window frame rpay
class rpay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Rate = StringVar()
        Paid = StringVar()

        def Stdrec2(event):
            global sd
            searchstd = studentlist2.curselection()[0]
            sd = studentlist2.get(searchstd)
            self.txttopay.delete(0, END)
            self.txtpaid.config(text=str(sd[7]) + "/" + str(sd[8]))
            self.txttotal.config(text=str(sd[8]))
            # self.txttopay.delete(0, END)
            # # self.txttopay.insert(END,sd[6])
            # self.txtpaid.delete(0, END)
            # self.txtpaid.insert(END, (sd[7], "/",sd[6]))

        def AddToPaylist():
            if(len(Rate.get()) != 0):
                stdDatabase_BackEnd.Rpaydata(Rate.get(), sd[0])
                studentlist2.delete(0, END)
                studentlist2.insert(END, (Rate.get()))
                self.txttopay.delete(0, END)

        def amountpaid():
            if(len(Rate.get()) != 0):
                stdDatabase_BackEnd.amountpaid(Rate.get())
                studentlist2.delete(0, END)
                self.txttopay.delete(0, END)

        def displayRpay():
            studentlist2.delete(0, END)
            for row in stdDatabase_BackEnd.ViewRpay():
                studentlist2.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def ttpay():
            val = stdDatabase_BackEnd.ttpay()
            studentlist2.delete(0, END)
            studentlist2.insert(END, val)

        def tpaid():
            val = stdDatabase_BackEnd.tpaid()
            studentlist2.delete(0, END)
            studentlist2.insert(END, val)

        def printdatarpay():
            scrol_y = Scrollbar(MainFrame, orient=VERTICAL)
            textarea1 = Text(MainFrame, yscrollcommand=scrol_y)
            # scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=textarea1.yview)
            textarea1.delete(1.0, END)
            con = sqlite3.connect("StockEntry.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM total")
            res = cur.fetchall()
            textarea1.insert(
                END, "Riyadh Payments\n Si Topay   Paid    Date \n")
            for row in res:
                textarea1.insert(END, str(row) + "\n")

            con.close()

            textarea1.configure(font='arial 13 bold')
            currentDateTime = datetime.datetime.now()
            cwd = os.getcwd()
            bill_details1 = textarea1.get('1.0', END)
            f1 = open("bills/"+str(currentDateTime.date())+"rpay.txt", "w")
            f1.write(bill_details1)
            f1.close()
            win32api.ShellExecute(
                0, "print", cwd + "/bills/"+str(currentDateTime.date())+"rpay.txt", None, ".", 0)

        MainFrame = Frame(self, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP)

        # self.canv = Canvas(TitFrame, width=250, height=70, bg='white')
        # self.canv.grid(row=0,column=0)

        self.lblTit = Label(TitFrame, font=('arial', 25, 'bold'),
                            text="AL-SAMS DATA MANAGEMENT SYSTEM", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=1200, height=90,
                            padx=1, pady=1, bg="snow3", relief=RIDGE)
        ButtonFrame.pack(side=RIGHT)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=400, height=200, padx=20, bg="gray60", fg="black", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Data Entry\n")
        DataFrameLEFT.pack(side=TOP)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray30", fg="white", relief=RIDGE,
                                    font=('arial', 15, 'bold'), text="Details\n    CT CR M L D")
        DataFrameRIGHT.pack(side=BOTTOM)

        self.lbltopay = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'), text="Rate/Paid :", padx=1, pady=3, bg="gray60")
        self.lbltopay.grid(row=0, column=0, sticky=W)
        self.txttopay = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Rate, width=39)
        self.txttopay.grid(row=0, column=1)

        self.lblpaid = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Paid :", padx=2, pady=5,
                             bg="gray60")
        self.lblpaid.grid(row=1, column=0, sticky=W)
        self.txtpaid = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'),  width=39)
        self.txtpaid.grid(row=1, column=1)

        self.lbltotal = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Total :", padx=2, pady=5,
                              bg="gray60")
        self.lbltotal.grid(row=2, column=0, sticky=W)
        self.txttotal = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'),  width=39)
        self.txttotal.grid(row=2, column=1)

        self.btnAddData = Button(ButtonFrame, text="Amount Paid", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=15, height=1, bd=4, command=amountpaid)
        self.btnAddData.grid(row=0, column=1, padx=10, pady=10)

        self.btnDispay = Button(ButtonFrame, text="Add to payment List", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=21, height=1, bd=4, command=AddToPaylist)
        self.btnDispay.grid(row=1, column=1, padx=10, pady=10)

        self.btnDispay = Button(ButtonFrame, text="Display", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=21, height=1, bd=4, command=displayRpay)
        self.btnDispay.grid(row=2, column=1, padx=10, pady=10)

        self.btnDispay2 = Button(ButtonFrame, text="Total To Pay", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=21, height=1, bd=4, command=ttpay)
        self.btnDispay2.grid(row=3, column=1, padx=10, pady=10)

        self.btnDispay3 = Button(ButtonFrame, text="Total Paid", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=21, height=1, bd=4, command=tpaid)
        self.btnDispay3.grid(row=4, column=1, padx=10, pady=10)

        self.btnDispay3 = Button(ButtonFrame, text="Print Rpay", font=(
            'arial', 12, 'bold'), fg="black", bg="seashell3", width=21, height=1, bd=4, command=printdatarpay)
        self.btnDispay3.grid(row=5, column=1, padx=10, pady=10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(ButtonFrame, text="Stock",
                             command=lambda: controller.show_frame(stock))

        # putting the button in its place by
        # using grid
        button1.grid(row=6, column=0, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(ButtonFrame, text="Home",
                             command=lambda: controller.show_frame(Home))

        # putting the button in its place by
        # using grid
        button2.grid(row=6, column=2, padx=10, pady=10)

        # ========================================================ScrollBar and ListBox===================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist2 = tk.Listbox(DataFrameRIGHT, width=93, height=19, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist2.bind('<<ListboxSelect>>', Stdrec2)
        studentlist2.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist2.yview)


class bill(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # root=Tk()
        # root.title("bill slip")
        # root.geometry('1280x720')
        # bg_color='#4D0039'
        c_name = StringVar()
        c_phone = StringVar()
        item = StringVar()
        color = StringVar()
        Rate = StringVar()
        quantity = StringVar()
        Rate.set('')
        quantity.set('')
        bill_no = StringVar()
        User = StringVar()

        def disable_button():
            textarea.config(state=DISABLED)

        def enable_button():
            textarea.config(state=NORMAL)

        def welcome():
            currentDateTime = datetime.datetime.now()
            enable_button()
            textarea.delete(1.0, END)
            textarea.insert(END, "      Welcome")
            textarea.insert(END, f"\nUser:\t{str(User.get())}")
            textarea.insert(END, f"\nDate:\t{str(currentDateTime.date())}")
            textarea.insert(END, f"\n\nBill Number:\t{bill_no.get()}")
            textarea.insert(END, f"\nCustomer Name:\t{c_name.get()}")
            textarea.insert(END, f"\nPhone Number:\t{c_phone.get()}")
            textarea.insert(END, f"\n\n==============================")
            textarea.insert(END, "\nCat  Color  QTY  Rate  Price")
            textarea.insert(END, f"\n==============================\n")
            textarea.configure(font='arial 10 bold')

         # ========================Bill area================
        F3 = Frame(self, relief=GROOVE, bd=10)
        F3.place(x=700, y=180, width=780, height=500)

        bill_title = Label(
            F3, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=textarea.yview)
        textarea.pack()
        welcome()

        disable_button()

        def setbillno():
            try:
                file1 = open("billno.txt", "r")
                y = file1.read()
                print(y)
                z = int(y)+1
                print("here")
                print(z)
                bill_no.set(str(z))
                file1.close()

                file = open('billno.txt', 'w')
                file.write(str(z))
                file.close()
                print(z)
            #    bill_no.set(str(y))
            except:
                file = open('billno.txt', 'w')
                file.write('100')
                bill_no.set('100')
                file.close()
        # Python code to illustrate read() mode
        setbillno()

        def Stdrec3(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)
            # self.c_name.delete(0,END)
            # self.txtpaid.config(text = str(sd[7]) + "/" + str(sd[8]))
            # self.txttotal.config(text = str(sd[8]))
            cname_txt.insert(END, sd[1])
            cphone_txt.insert(END, (sd[2]))
        # ======================variable=================

        global l
        l = []
        bg_color = "seashell4"
        # =========================Functions================================

        def additm():
            # clear()
            if User.get() == "":
                tkinter.messagebox.showerror("Error", "Please select the User")
            else:
                enable_button()
                y = stdDatabase_BackEnd.additem(
                    item.get(), color.get(), quantity.get())
                print(y)
                if(y != 0):
                    n = Rate.get()
                    m = float(quantity.get())*float(n)
                    l.append(m)
                    if item.get() != '':
                        textarea.insert(
                            (13.0+float(len(l)-1)), f"{item.get()} - {color.get()} - {quantity.get()} - {Rate.get()}  -  { m}\n")
                    else:
                        tkinter.messagebox.showerror(
                            'Error', 'Please enter item')
                else:
                    tkinter.messagebox.showerror(
                        'Error', 'Stock is insufficient!')
                    clearall()
                # c_name.set('')
                # c_phone.set('')
                item.set('')
                Rate.set('')
                quantity.set('')
                color.set('')
                disable_button()

        def gbill():
            if c_name.get() == "" or c_phone.get() == "" or User.get() == "":
                tkinter.messagebox.showerror(
                    "Error", "Customer detail are must")
            else:

                textAreaText = textarea.get(12.0, (13.0+float(len(l))))
                welcome()
                textarea.insert(END, textAreaText)
                textarea.insert(END, f"\n========================")
                textarea.insert(END, f"\nTotal Paybill Amount :\t  {sum(l)}")
                print(l)
                textarea.insert(END, f"\n\n========================")

                save_bill()

        def displaybills():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.Viewbills(User.get()):
                studentlist.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def clearall():
            l.clear()
            c_name.set('')
            c_phone.set('')
            item.set('')
            Rate.set('')
            quantity.set('')
            color.set('')
            User.set("")
            stdDatabase_BackEnd.clearcon()
            welcome()

        def exit():
            op = tkinter.messagebox.askyesno(
                "Exit", "Do you really want to exit?")
            if op > 0:
                self.destroy()

        def save_bill():
            # file_to_print = filedialog.askopenfilename(
            #  initialdir="/", title="Select file",
            #  filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
            # print(file_to_print)
            # if file_to_print:

            #     # Print Hard Copy of File
            #     win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

            stdDatabase_BackEnd.billgenerated(c_name.get(), c_phone.get(
            ), item.get(), color.get(), User.get(), bill_no.get(), sum(l))
            # Python code to create a file

            setbillno()

            # file1 = open("billno.txt", "r")
            # x=file1.read()
            # print(x)
            # file1.close()
            # x = int(x)+1

            # file = open('billno.txt','w')
            # file.write(str(x))
            # file.close()
            # print(x)
            # bill_no.set(str(x))

            cwd = os.getcwd()
            bill_details = textarea.get('1.0', END)
            x = int(bill_no.get()) - 1
            nm = c_name.get()
            f1 = open("bills/"+str(nm)+"_"+str(x)+".txt", "w")
            f1.write(bill_details)
            f1.close()
            win32api.ShellExecute(
                0, "print", cwd + "/bills/"+str(nm)+"_"+str(x)+".txt", None, ".", 0)
            clearall()
            welcome()
            disable_button()

        def printdatarpay():
            scrol_y = Scrollbar(F4, orient=VERTICAL)
            textarea1 = Text(F4, yscrollcommand=scrol_y)
            # scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=textarea1.yview)
            textarea1.delete(1.0, END)
            con = sqlite3.connect("StockEntry.db")
            cur = con.cursor()
            if(User.get() == "Saleem"):
                cur.execute("SELECT * FROM entry4 WHERE Usr='Saleem'")
            elif(User.get() == "Rajeeb"):
                cur.execute("SELECT * FROM entry4 WHERE Usr='Rajeeb'")
            else:
                cur.execute("SELECT * FROM entry4")
            res = cur.fetchall()
            textarea1.insert(END, "Bills\n \n")
            for row in res:
                textarea1.insert(END, str(row) + "\n")

            con.close()
            crntuser = User.get()
            textarea1.configure(font='arial 13 bold')
            currentDateTime = datetime.datetime.now()
            cwd = os.getcwd()
            bill_details1 = textarea1.get('1.0', END)
            f1 = open("bills/"+str(currentDateTime.date()) +
                      "_"+str(crntuser)+"bill.txt", "w")
            f1.write(bill_details1)

            f1.close()
            win32api.ShellExecute(0, "print", cwd + "/bills/"+str(
                currentDateTime.date())+"_"+str(crntuser)+"bill.txt", None, ".", 0)

        # title=Label(self,pady=2,text="Al-Sams Data Management",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
        # title.pack(fill=X)

        # =================Product Frames=================
        F1 = LabelFrame(self, bd=10, relief=GROOVE, text='Customer Details', font=(
            'times new romon', 15, 'bold'), fg='gold', bg=bg_color)
        F1.place(x=0, y=00, relwidth=1)

        cname_lbl = Label(F1, text='Customer Name', font=('times new romon', 18, 'bold'),
                          bg=bg_color, fg='white').grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold',
                          relief=SUNKEN, bd=7).grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone No. ', font=('times new romon', 18, 'bold'),
                           bg=bg_color, fg='white').grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone,
                           relief=SUNKEN, bd=7).grid(row=0, column=3, padx=10, pady=5)

        F2 = LabelFrame(self, text='Details', font=(
            'times new romon', 18, 'bold'), fg='gold', bg=bg_color)
        F2.place(x=20, y=80, width=620, height=650)

        F4 = LabelFrame(self, text='Bills', font=(
            'times new romon', 18, 'bold'), fg='gold', bg=bg_color)
        F4.place(x=20, y=500, width=620, height=450)

        itm = Label(F2, text='Catelogue', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=0, column=0, padx=3, pady=2)
        itm_txt = Entry(F2, width=20, textvariable=item, font='arial 15 bold',
                        relief=SUNKEN, bd=7).grid(row=0, column=1, padx=1, pady=2)

        itm = Label(F2, text='Color', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=1, column=0, padx=3, pady=2)
        itm_txt = Entry(F2, width=20, textvariable=color, font='arial 15 bold',
                        relief=SUNKEN, bd=7).grid(row=1, column=1, padx=1, pady=2)

        n = Label(F2, text='Meter', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=2, column=0, padx=3, pady=2)
        n_txt = Entry(F2, width=20, textvariable=quantity, font='arial 15 bold',
                      relief=SUNKEN, bd=7).grid(row=2, column=1, padx=1, pady=2)

        rate = Label(F2, text='Rate', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
            row=3, column=0, padx=3, pady=2)
        rate_txt = Entry(F2, width=20, textvariable=Rate, font='arial 15 bold',
                         relief=SUNKEN, bd=7).grid(row=3, column=1, padx=1, pady=2)

        # =========================Buttons======================
        btn1 = Button(F2, text='Add item', font='arial 10 bold',
                      command=additm, padx=5, pady=5, bg='grey', width=10)
        btn1.grid(row=0, column=3, pady=25, padx=90)
        btn2 = Button(F2, text='Generate Bill', font='arial 10 bold',
                      padx=5, pady=5, command=gbill, bg='grey', width=10)
        btn2.grid(row=1, column=3, pady=25, padx=90)
        btn3 = Button(F2, text='Clear', font='arial 10 bold',
                      command=clearall, padx=5, pady=5, bg='grey', width=10)
        btn3.grid(row=2, column=3, padx=90, pady=25,)
        btn4 = Button(F2, text='Display', font='arial 10 bold',
                      command=displaybills, pady=5, bg='grey', width=10)
        btn4.grid(row=3, column=3, pady=25)

        btn5 = Button(F3, text='Print bills', font='arial 10 bold',
                      command=printdatarpay, pady=5, bg='grey', width=10)
        btn5.pack(side=LEFT)

        button1 = ttk.Button(F2, text="stock",
                             command=lambda: controller.show_frame(stock))

        # putting the button in its place by
        # using grid
        button1.grid(row=4, column=3, padx=90, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(F2, text="Home",
                             command=lambda: controller.show_frame(Home))
        button2.grid(row=4, column=0, padx=29, pady=10)

        Radiobutton(F2, text="Saleem", variable=User, value="Saleem",
                    indicator=0, background="white").grid(row=4, column=1, padx=0, pady=0)
        Radiobutton(F2, text="Rajeeb", variable=User, value="Rajeeb",
                    indicator=0, background="white").grid(row=4, column=2, padx=0, pady=0)

        scrollbar = Scrollbar(F4)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = tk.Listbox(F4, width=79, height=10, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', Stdrec3)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # layout2

        # putting the button in its place by
        # using grid


class user(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       # root=Tk()
       # root.title("bill slip")
       # root.geometry('1280x720')
       # bg_color='#4D0039'

        Desc = StringVar()
        uservar = StringVar()
        Amount = IntVar()

        def Stdrec3(event):
            global sd
            searchstd = studentlist3.curselection()[0]
            sd = studentlist3.get(searchstd)
            # self.txttopay.delete(0,END)
            # self.txtpaid.config(text = str(sd[7]) + "/" + str(sd[8]))

            self.txttopay.delete(0, END)
            self.txttopay.insert(END, sd[1])
            self.txtpaid.delete(0, END)
            self.txtpaid.insert(END, sd[2])

        def usr():

            stdDatabase_BackEnd.addusrs(
                Desc.get(), Amount.get(), uservar.get())
            studentlist3.delete(0, END)
            studentlist3.insert(END, (Desc.get(), Amount.get(), uservar.get()))
            self.txttopay.delete(0, END)

        def Viewbilltotal():
            tbill = stdDatabase_BackEnd.Viewbilltotal(uservar.get())
            studentlist3.delete(0, END)
            studentlist3.insert(END, tbill)

        def displayusrstotal():

            studentlist3.delete(0, END)
            rownw = stdDatabase_BackEnd.Viewusrstotal(uservar.get())
            studentlist3.insert(END, rownw)

        def billpaid():
            if(Amount.get() != None):
                stdDatabase_BackEnd.billpaid(Amount.get(), uservar.get())
                studentlist3.delete(0, END)
                self.txttopay.delete(0, END)

        def usrpaid():
            if(Amount.get() != None):
                stdDatabase_BackEnd.usrpaid(Amount.get(), uservar.get())
                studentlist3.delete(0, END)
                self.txttopay.delete(0, END)

        # def usr2():

        #     stdDatabase_BackEnd.amountpaid(Desc.get(),Amount.get(),uservar.get())
        #     studentlist3.delete(0,END)
        #     studentlist3.insert(END,(Desc.get(),Amount.get()))
        #     self.txttopay.delete(0,END)

        def displayusrs():
            stdDatabase_BackEnd.Viewusrstotal(uservar.get())
            studentlist3.delete(0, END)
            for row in stdDatabase_BackEnd.Viewusrs(uservar.get()):
                studentlist3.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def deldtl():
            stdDatabase_BackEnd.deletusrRec(sd[0])
            studentlist3.delete(0, END)

        MainFrame = Frame(self, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP)

        # self.canv = Canvas(TitFrame, width=250, height=70, bg='white')
        # self.canv.grid(row=0,column=0)

        self.lblTit = Label(TitFrame, font=('arial', 25, 'bold'),
                            text="AL-SAMS DATA MANAGEMENT SYSTEM", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=1200, height=90,
                            padx=1, pady=1, bg="snow3", relief=RIDGE)
        ButtonFrame.pack(side=RIGHT)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray60", fg="black", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Data Entry\n")
        DataFrameLEFT.pack(side=TOP)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray30", fg="white", relief=RIDGE,
                                    font=('arial', 15, 'bold'), text="Details\n    CT CR M L D")
        DataFrameRIGHT.pack(side=BOTTOM)

        self.lbltopay = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'), text="Description :", padx=1, pady=3, bg="gray60")
        self.lbltopay.grid(row=0, column=0, sticky=W)
        self.txttopay = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Desc, width=39)
        self.txttopay.grid(row=0, column=1)

        self.lblpaid = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Amount", padx=2, pady=5,
                             bg="gray60")
        self.lblpaid.grid(row=1, column=0, sticky=W)
        self.txtpaid = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'),  textvariable=Amount, width=39)
        self.txtpaid.grid(row=1, column=1)

        Radiobutton(DataFrameLEFT, text="Saleem", variable=uservar, value="Saleem",
                    indicator=0, background="white").grid(row=4, column=0, padx=0, pady=0)
        Radiobutton(DataFrameLEFT, text="Rajeeb", variable=uservar, value="Rajeeb",
                    indicator=0, background="white").grid(row=4, column=2, padx=0, pady=0)

        btn1 = Button(ButtonFrame, text='Add item', font='arial 10 bold',
                      command=usr, padx=5, pady=5, bg='grey', width=10)
        btn1.grid(row=0, column=3, pady=25, padx=2)
        lbtn = Button(ButtonFrame, text='Usr paid', font='arial 10 bold',
                      padx=5, pady=5, command=usrpaid, bg='grey', width=10)
        lbtn.grid(row=2, column=4, pady=25, padx=2)
        btn2 = Button(ButtonFrame, text='Display', font='arial 10 bold',
                      padx=5, pady=5, command=displayusrs, bg='grey', width=10)
        btn2.grid(row=3, column=4, pady=25, padx=2)
        btn3 = Button(ButtonFrame, text='Display Total', font='arial 10 bold',
                      command=displayusrstotal, padx=5, pady=5, bg='grey', width=10)
        btn3.grid(row=1, column=4, padx=2, pady=25,)
        btn3 = Button(ButtonFrame, text='Delete', font='arial 10 bold',
                      command=deldtl, padx=5, pady=5, bg='grey', width=10)
        btn3.grid(row=3, column=3, padx=2, pady=25,)
        btn4 = Button(ButtonFrame, text='Bill Total', font='arial 10 bold',
                      command=Viewbilltotal, padx=5, pady=5, bg='grey', width=10)
        btn4.grid(row=1, column=3, padx=2, pady=25,)
        btn4 = Button(ButtonFrame, text='Bill Paid', font='arial 10 bold',
                      command=billpaid, padx=5, pady=5, bg='grey', width=10)
        btn4.grid(row=2, column=3, padx=2, pady=25,)

        # button1 = ttk.Button(ButtonFrame, text ="stock",
        #                     command = lambda : controller.show_frame(stock))

        # # putting the button in its place by
        # # using grid
        # button1.grid(row = 3, column = 3,padx=90, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(ButtonFrame, text="Home",
                             command=lambda: controller.show_frame(Home))
        button2.grid(row=4, column=3, padx=29, pady=10)

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist3 = tk.Listbox(DataFrameRIGHT, width=99, height=19, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist3.bind('<<ListboxSelect>>', Stdrec3)
        studentlist3.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist3.yview)


class rtrn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Cat = StringVar()
        Num = StringVar()
        Meter = StringVar()
        uservar = StringVar()
        rate = StringVar()

        def Stdrec(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)
            self.txtCat.delete(0, END)
            self.txtCat.insert(END, sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtLna.delete(0, END)
            self.txtLna.insert(END, sd[3])

        def DisplayReturn():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.DisplayReturn():
                studentlist.insert(END, row, str(
                    "--------------------------------------------------------------------------------------------"))

        def RtrnOrder():
            stdDatabase_BackEnd.RtrnOrder(
                Cat.get(), Num.get(), Meter.get(), rate.get(), uservar.get())
            cleardata()

        def cleardata():
            self.txtCat.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtrate.delete(0, END)
            uservar.set("")

        MainFrame = Frame(self, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP)

        # self.canv = Canvas(TitFrame, width=250, height=70, bg='white')
        # self.canv.grid(row=0,column=0)

        self.lblTit = Label(TitFrame, font=('arial', 25, 'bold'),
                            text="AL-SAMS DATA MANAGEMENT SYSTEM", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=800, height=90,
                            padx=1, pady=1, bg="snow3", relief=RIDGE)
        ButtonFrame.pack(side=RIGHT)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray60", fg="black", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Data Entry\n")
        DataFrameLEFT.pack(side=TOP)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=200, padx=20, bg="gray30", fg="white", relief=RIDGE,
                                    font=('arial', 15, 'bold'), text="Details\n    CT CR M L D")
        DataFrameRIGHT.pack(side=BOTTOM)

        # ========================================================Labels and Entry Widget===================================================================

        self.lblCat = Label(DataFrameLEFT, font=(
            'arial', 20, 'bold'), text="Catalogue :", padx=1, pady=3, bg="gray60")
        self.lblCat.grid(row=0, column=0, sticky=W)
        self.txtCat = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Cat, width=30)
        self.txtCat.grid(row=0, column=1)

        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Colour :", padx=2, pady=5,
                            bg="gray60")
        self.lblFna.grid(row=1, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Num, width=30)
        self.txtFna.grid(row=1, column=1)

        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Meter", padx=2, pady=5,
                            bg="gray60")
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=Meter, width=30)
        self.txtLna.grid(row=2, column=1)

        self.rate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Rate", padx=2, pady=5,
                          bg="gray60")
        self.rate.grid(row=3, column=0, sticky=W)
        self.txtrate = Entry(DataFrameLEFT, font=(
            'arial', 20, 'bold'), textvariable=rate, width=30)
        self.txtrate.grid(row=3, column=1)

        Radiobutton(DataFrameLEFT, text="Saleem", variable=uservar, value="Saleem",
                    indicator=0, background="white").grid(row=4, column=0, padx=0, pady=0)
        Radiobutton(DataFrameLEFT, text="Rajeeb", variable=uservar, value="Rajeeb",
                    indicator=0, background="white").grid(row=4, column=2, padx=0, pady=0)

        # ========================================================ScrollBar and ListBox===================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = tk.Listbox(DataFrameRIGHT, width=70, height=10, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', Stdrec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # ========================================================Button Widget===================================================================
        self.btnAddData = Button(ButtonFrame, text="Return", font=(
            'arial', 14, 'bold'), fg="black", bg="seashell3", width=17, height=1, bd=4, command=RtrnOrder)
        self.btnAddData.grid(row=0, column=1, padx=10, pady=10)

        self.btnDispay = Button(ButtonFrame, text="Display Returns", font=(
            'arial', 14, 'bold'), fg="black", bg="seashell3", width=17, height=1, bd=4, command=DisplayReturn)
        self.btnDispay.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(ButtonFrame, text="Home",
                             command=lambda: controller.show_frame(Home))
        button2.grid(row=4, column=3, padx=29, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
