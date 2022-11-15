from asyncio.windows_events import NULL
import sqlite3
import datetime
import os
import sys
import datetime
import tkinter.messagebox

# BackEnd


currentDateTime = datetime.datetime.now()
currentDate = currentDateTime.date()


def resource_path(relative_path):
    # """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#################################################################   STOCK   ########################################################################
def entrydata():
    currentDateTime = datetime.datetime.now()
    currentDate = currentDateTime.date()
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS entry (id INTEGER PRIMARY KEY, Cat text, Num text, Meter INTEGER, Luffa INTEGER, Date TIMESTAMp , Topay INTEGER , Paid INTEGER, Total INTEGER) ")
    # con.commit()
    # con.close()

    # con2 = sqlite3.connect("TotalStock.db")
    # cur2 = con2.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS entry2 (id INTEGER PRIMARY KEY, Cat text, Num text, Meter INTEGER, Date TIMESTAMP)")
    # con2.commit()
    # con2.close()

    # con3 = sqlite3.connect("TotalOrder.db")
    # cur3 = con3.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS entry3 (id INTEGER PRIMARY KEY, Cat text, Num text, Meter INTEGER, Luffa INTEGER , Date TIMESTAMP )")

    cur.execute("CREATE TABLE IF NOT EXISTS entry4 (id INTEGER PRIMARY KEY, CN text, PN text,Usr text,BN text,BA INTEGER, Date TIMESTAMP )")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS entry5 (id INTEGER PRIMARY KEY, Desc text, Amnt INTEGER,Usr text, Date TIMESTAMP )")
    # cur.execute("CREATE TABLE IF NOT EXISTS totalS (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
    # cur.execute("CREATE TABLE IF NOT EXISTS totalR (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
    con.commit()
    con.close()


def addEntRec(Cat="", Num="", Meter="", Age="", id=""):
    currentDateTime = datetime.datetime.now()
    currentDate = currentDateTime.date()
    entrydata()
    print(Meter)
    con = sqlite3.connect("StockEntry.db")
    # con2 = sqlite3.connect("TotalStock.db")
    # con3 = sqlite3.connect("TotalOrder.db")
    cur = con.cursor()
    # cur2 = con2.cursor()
    # cur3 = con3.cursor()
    if(Meter != ""):
        cur.execute("INSERT INTO entry VALUES (NULL,?,?,?,?,?,?,?,?)",
                    (Cat, Num, Meter, Age, currentDate, "", "", ""))

    length = cur.execute(
        "SELECT COUNT(ALL) from entry2 WHERE Cat=? AND Num=?", (Cat, Num))
    leng = cur.fetchone()
    print(leng[0])
    if(leng[0] == 0 and Meter != ""):
        cur.execute("INSERT INTO entry2 VALUES (NULL,?,?,?,?)",
                    (Cat, Num, Meter, currentDate))
        print("success")
        try:
            cur.execute("DELETE FROM entry3 WHERE id=?", (id,))
        except:
            print("No such orders")

    elif(leng[0] == 1 and Meter != ""):
        meter = cur.execute(
            "SELECT METER from entry2 WHERE Cat=? AND Num=?", (Cat, Num))
        mtr = cur.fetchone()
        val = float(Meter) + mtr[0]
        print(val)
        cur.execute("UPDATE entry2 SET Meter=?,Date=? WHERE Cat=? AND Num=?",
                    (val, currentDate, Cat, Num))
        try:
            cur.execute("DELETE FROM entry3 WHERE id=?", (id,))
        except:
            print("No such orders")

    else:
        print('Error! There are more than 1 value')

    con.commit()
    # con2.commit()
    # con3.commit()
    con.close()
    # con2.close()
    # con3.close()


def addOrdRec(Cat, Num, Age):
    currentDateTime = datetime.datetime.now()
    currentDate = currentDateTime.date()
    entrydata()
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("INSERT INTO entry3 VALUES (NULL,?,?,?,?,?)",
                (Cat, Num, "", Age, currentDate))
    con.commit()
    con.close()


def Viewdata():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM entry")
    row = cur.fetchall()
    con.close()
    return row


def Vieworders():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM entry3")
    row = cur.fetchall()
    con.close()
    return row


def Viewtotaldata():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM entry2")
    row = cur.fetchall()
    con.close()
    return row


def deletRec(id, Meter="", Age=""):
    if(Meter != ""):
        con = sqlite3.connect("StockEntry.db")
        cur = con.cursor()
        cur.execute("DELETE FROM entry WHERE id=? AND Meter=?", (id, Meter))
        con.commit()
        con.close()
    elif(Meter == "" and Age != ""):
        con3 = sqlite3.connect("StockEntry.db")
        cur3 = con3.cursor()
        cur3.execute("DELETE FROM entry3 WHERE id=? AND Luffa=?", (id, Age))
        con3.commit()
        con3.close()


def searchdata(Cat="", Num="", Meter="", Dob="", Dob2=""):
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()

    if(Num != "" and Meter != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Num=? AND Meter=? AND Date BETWEEN ? AND ?",
                    (Cat, Num, Meter, Dob, Dob2))
    elif(Num != "" and Meter != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Num=? AND Meter=? AND Date BETWEEN ? AND ?",
                    (Num, Meter, Dob, Dob2))
    elif(Num != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Num=? AND Date BETWEEN ? AND ?",
                    (Cat, Num, Dob, Dob2))
    elif(Meter != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Meter=? AND Date BETWEEN ? AND ?",
                    (Cat, Meter, Dob, Dob2))
    elif(Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Date BETWEEN ? AND ?",
                    (Cat, Dob, Dob2))
    elif(Num != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Num=? AND Date BETWEEN ? AND ?",
                    (Num, Dob, Dob2))
    elif(Meter != "" and Dob != ""):
        cur.execute("SELECT * FROM entry WHERE Meter=? AND Date BETWEEN ? AND ?",
                    (Meter, Dob, Dob2))

    elif(Num != "" and Meter != "" and Cat != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Num=? AND Meter=?",
                    (Cat, Num, Meter))
    elif(Num != "" and Meter != ""):
        cur.execute("SELECT * FROM entry WHERE Num=? AND Meter=?",
                    (Num, Meter))
    elif(Num != "" and Cat != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Num=? OR Meter=?",
                    (Cat, Num, Meter))
    elif(Meter != "" and Cat != ""):
        cur.execute("SELECT * FROM entry WHERE Cat=? AND Meter=?",
                    (Cat, Meter))
    else:
        cur.execute("SELECT * FROM entry WHERE Cat=? OR Num=? OR Meter=? OR Date BETWEEN ? AND ?",
                    (Cat, Num, Meter, Dob, Dob2))

    row = cur.fetchall()
    con.close()
    return row


def searchorders(Cat="", Num="", Luffa="", Dob="", Dob2=""):
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()

    if(Num != "" and Luffa != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Num=? AND Luffa=? AND Date BETWEEN ? AND ?",
                    (Cat, Num, Luffa, Dob, Dob2))
    elif(Num != "" and Luffa != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Num=? AND Luffa=? AND Date BETWEEN ? AND ?",
                    (Num, Luffa, Dob, Dob2))
    elif(Num != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Num=? AND Date BETWEEN ? AND ?",
                    (Cat, Num, Dob, Dob2))
    elif(Luffa != "" and Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Luffa=? AND Date BETWEEN ? AND ?",
                    (Cat, Luffa, Dob, Dob2))
    elif(Cat != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Date BETWEEN ? AND ?",
                    (Cat, Dob, Dob2))
    elif(Num != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Num=? AND Date BETWEEN ? AND ?",
                    (Num, Dob, Dob2))
    elif(Luffa != "" and Dob != ""):
        cur.execute("SELECT * FROM entry3 WHERE Luffa=? AND Date BETWEEN ? AND ?",
                    (Luffa, Dob, Dob2))

    elif(Num != "" and Luffa != "" and Cat != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Num=? AND Luffa=?",
                    (Cat, Num, Luffa))
    elif(Num != "" and Luffa != ""):
        cur.execute("SELECT * FROM entry3 WHERE Num=? AND Luffa=?",
                    (Num, Luffa))
    elif(Num != "" and Cat != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Num=? OR Luffa=?",
                    (Cat, Num, Luffa))
    elif(Luffa != "" and Cat != ""):
        cur.execute("SELECT * FROM entry3 WHERE Cat=? AND Luffa=?",
                    (Cat, Luffa))
    else:
        cur.execute("SELECT * FROM entry3 WHERE Cat=? OR Num=? OR Luffa=? OR Date BETWEEN ? AND ?",
                    (Cat, Num, Luffa, Dob, Dob2))

    row = cur.fetchall()
    con.close()
    return row


def searchtotaldata(Cat="", Num="", Meter="", Dob=""):
    con2 = sqlite3.connect("StockEntry.db")
    cur2 = con2.cursor()

    if(Num != "" and Meter != "" and Cat != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Num=? AND Meter=? AND Date=?",
                     (Cat, Num, Meter, Dob))
    elif(Num != "" and Meter != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Num=? AND Meter=? AND Date=?",
                     (Num, Meter, Dob))
    elif(Num != "" and Cat != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Num=? AND Date=?",
                     (Cat, Num, Dob))
    elif(Meter != "" and Cat != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Meter=? AND Date=?",
                     (Cat, Meter, Dob))
    elif(Cat != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Date=?",
                     (Cat, Dob))
    elif(Num != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Num=? AND Date=?",
                     (Num, Dob))
    elif(Meter != "" and Dob != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Meter=? AND Date=?",
                     (Meter, Dob))

    elif(Num != "" and Meter != "" and Cat != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Num=? AND Meter=?",
                     (Cat, Num, Meter))
    elif(Num != "" and Meter != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Num=? AND Meter=?",
                     (Num, Meter))
    elif(Num != "" and Cat != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Num=? OR Meter=?",
                     (Cat, Num, Meter))
    elif(Meter != "" and Cat != ""):
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? AND Meter=?",
                     (Cat, Meter))
    else:
        cur2.execute("SELECT * FROM entry2 WHERE Cat=? OR Num=? OR Meter=? OR Date=?",
                     (Cat, Num, Meter, Dob))

    row = cur2.fetchall()
    con2.close()
    return row
#######################################################  Rpay  ##################################################################


def Rpaydata(Rate="", idnew=""):
    entrydata()
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    payval = cur.execute("SELECT Topay from entry WHERE id=?", (idnew,))
    pval = cur.fetchone()
    meter = cur.execute("SELECT Meter from entry WHERE id=?", (idnew,))
    mtr = cur.fetchone()

    if(pval[0] == ''):
        cur.execute(
            "CREATE TABLE IF NOT EXISTS total (id INTEGER PRIMARY KEY, Topay INTEGER, Paid INTEGER, Date TIMESTAMP )")
        newval = float(mtr[0])*float(Rate)
        cur.execute("UPDATE entry SET Topay=?, Total=? WHERE id=?",
                    (newval, newval, idnew))
        try:
            last_row1 = cur.execute('SELECT Topay from total').fetchall()[-1]
        except:
            last_row1 = (0,)
        newtopay1 = float(last_row1[0]) + float(newval)
        cur.execute("INSERT into total VALUES (NULL,?,?,?)",
                    (newtopay1, "", currentDate))
        allvalue1 = cur.execute('SELECT * from total').fetchall()[-1]
        print(allvalue1)
        print("inif")
    else:
        pass
        # newval = float(Rate)*float(mtr[0]) + float(pval[0])#here
        # print(newval)
        # cur.execute("UPDATE entry SET Topay=? WHERE id=?",(newval,idnew))
    # # val = float(Meter) + mtr[0]
    # cur.execute("CREATE TABLE IF NOT EXISTS entry3 (id INTEGER PRIMARY KEY, Cat text, Num text, Meter INTEGER, Luffa INTEGER, Topay INTEGER, Paid INTEGER)")
    # for i in data:
    con.commit()
    con.close()


def ViewRpay():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM entry")
    row = cur.fetchall()
    con.close()
    return row


def amountpaid(Paid=""):
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS total (id INTEGER PRIMARY KEY, Topay INTEGER, Paid INTEGER, Date TIMESTAMP )")
    # cur.execute("SELECT Topay from total WHERE id=?",(idnew,))
    last_row = cur.execute('SELECT Topay from total').fetchall()[-1]
    print(last_row)
    newtopay = float(last_row[0]) - float(Paid)
    cur.execute("INSERT into total VALUES (NULL,?,?,?)",
                (newtopay, Paid, currentDate))
    allvalue = cur.execute('SELECT * from total').fetchall()[-1]
    print(allvalue)

    # tp = cur.fetchone()
    # cur.execute("SELECT Paid from entry WHERE id=?",(idnew,))
    # pd = cur.fetchone()
    # val = float(tp[0]) - float(Paid)
    # cur.execute("UPDATE entry SET Topay=? WHERE id=?",(val,idnew))
    # if(pd[0]==''):
    #     cur.execute("UPDATE entry SET Paid=? WHERE id=?",(Paid,idnew))

    # else:
    #     pdval = float(pd[0]) + float(Paid)

    #     cur.execute("UPDATE entry SET Paid=? WHERE id=?",(pdval,idnew))
    con.commit()
    con.close()


def ttpay():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    val = cur.execute('SELECT Topay from total').fetchall()[-1]
    # cur.execute("SELECT SUM(Topay) FROM total")
    print(val)
    return val


def tpaid():
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    # val = cur.execute('SELECT Topay from total').fetchall()[-1]
    cur.execute("SELECT SUM(Paid) FROM total")
    val = cur.fetchone()
    print(val)
    con.close()
    return val


#################################################################### bill ##############################################################
def billgenerated(CN="", PN="", CT="", CL="", Usr="", BN="", BA=""):
    currentDateTime = datetime.datetime.now()
    currentDate = currentDateTime.date()
    # entrydata()

    # if(Usr == "Saleem"):
    #     curuniq.execute(
    #         "CREATE TABLE IF NOT EXISTS totalS (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
    #     try:
    #         last_row2 = curuniq.execute(
    #             'SELECT Topaybill from totalS').fetchall()[-1]
    #     except:
    #         last_row2 = (0,)
    #     try:
    #         last_topayusr = curuniq.execute(
    #             'SELECT Topayusr from totalS').fetchall()[-1]
    #     except:
    #         last_topayusr = (0,)
    #     newval2 = float(last_row2[0]) + float(BA)
    #     curuniq.execute("INSERT into totalS VALUES (NULL,?,?,?,?,?)",
    #                     (newval2, 0, last_topayusr[0], 0, currentDate))
    # allvalue2 = curuniq.execute('SELECT * from total').fetchall()[-1]
    # print(allvalue2)
    # elif(Usr == "Rajeeb"):
    curuniq.execute(
        "CREATE TABLE IF NOT EXISTS totalR (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
    try:
        last_row2 = curuniq.execute(
            'SELECT Topaybill from totalR').fetchall()[-1]
    except:
        last_row2 = (0,)
    try:
        last_topayusr = curuniq.execute(
            'SELECT Topayusr from totalR').fetchall()[-1]
    except:
        last_topayusr = (0,)
    newval2 = float(last_row2[0]) + float(BA)
    curuniq.execute("INSERT into totalR VALUES (NULL,?,?,?,?,?)",
                    (newval2, 0, last_topayusr[0], 0, currentDate))
    # allvalue2 = curuniq.execute('SELECT * from total').fetchall()[-1]
    # print(allvalue2)

    # print("inif")

    # con = sqlite3.connect("StockEntry.db")
    # cur = con.cursor()
    curuniq.execute("INSERT INTO entry4 VALUES (NULL,?,?,?,?,?,?)",
                    (CN, PN, Usr, BN, BA, currentDate))
    conuniq.commit()
    conuniq.close()
    # con.commit()
    # con.close()


def Viewbills(user=""):
    con = sqlite3.connect("StockEntry.db")
    cur = con.cursor()
    if(user == ""):
        cur.execute("SELECT * FROM entry4")
    elif(user != ""):
        cur.execute("SELECT * FROM entry4 WHERE Usr=?", (user,))
    row = cur.fetchall()
    con.close()
    return row


conuniq = sqlite3.connect("StockEntry.db")
curuniq = conuniq.cursor()


def clearcon():
    conuniq.close()


def additem(CT="", CL="", QT=""):
    global conuniq
    global curuniq

    # con = sqlite3.connect("StockEntry.db")
    # cur = con.cursor()
    try:
        Tval = curuniq.execute(
            "SELECT Meter from entry2 WHERE Cat=? AND Num=?", (CT, CL))
        val = curuniq.fetchone()
        print(val[0])
        if((float(val[0])-float(QT)) >= 0):
            Fval = float(val[0])-float(QT)
            curuniq.execute(
                "UPDATE entry2 SET Meter=? WHERE Cat=? AND Num=?", (Fval, CT, CL))
        else:
            print("else")
            return 0
    except:

        conuniq = sqlite3.connect("StockEntry.db")
        print("abc")
        curuniq = conuniq.cursor()

        Tval = curuniq.execute(
            "SELECT Meter from entry2 WHERE Cat=? AND Num=?", (CT, CL))
        val = curuniq.fetchone()
        print(val[0])
        if((float(val[0])-float(QT)) >= 0):
            Fval = float(val[0])-float(QT)
            curuniq.execute(
                "UPDATE entry2 SET Meter=? WHERE Cat=? AND Num=?", (Fval, CT, CL))
        else:
            print("else")
            return 0


###############################################################   user   #########################################################

# def addusrs(Desc, Amnt, usr):
#     entrydata()
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     # if(usr==""):
#     #     tkinter.messagebox.showerror("Error", "Please select User")
#     # elif(usr=="Saleem"):
#     #     # val = cur.execute('SELECT Topay from total').fetchall()[-1]
#     #     last_row = cur.execute('SELECT Topaybill from totalS').fetchall()[-1]
#     #     last_topayusr = curuniq.execute('SELECT Topayusr from totalS').fetchall()[-1]
#     # elif(usr=="Rajeeb"):
#     #     last_row = cur.execute('SELECT Topaybill from totalR').fetchall()[-1]
#     #     last_topayusr = curuniq.execute('SELECT Topayusr from totalR').fetchall()[-1]
#     # if(usr=="Saleem"):
#     #     newusramnt=last_topayusr[0]+Amnt

#     if(usr == "Saleem"):
#         cur.execute("CREATE TABLE IF NOT EXISTS totalS (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
#         try:
#             last_row2 = cur.execute(
#                 'SELECT Topaybill from totalS').fetchall()[-1]
#             print("onesuccess")
#         except:
#             last_row2 = (0,)
#         try:
#             last_topayusr = cur.execute(
#                 'SELECT Topayusr from totalS').fetchall()[-1]
#             print(last_topayusr)
#         except:
#             last_topayusr = (0,)
#             print("twosuccess")
#         print(last_topayusr[0])
#         print(Amnt)
#         newval2 = int(last_topayusr[0]) + int(Amnt)
#         print(newval2)
#         cur.execute("INSERT into totalS VALUES (NULL,?,?,?,?,?)",
#                     (last_row2[0], 0, newval2, 0, currentDate))
#         # allvalue2 = cur.execute('SELECT * from total').fetchall()[-1]

#     elif(usr == "Rajeeb"):
#         cur.execute("CREATE TABLE IF NOT EXISTS totalR (id INTEGER PRIMARY KEY, Topaybill INTEGER, Paidbill INTEGER, Topayusr INTEGER, Paidusr INTEGER, Date TIMESTAMP )")
#         try:
#             last_row2 = cur.execute(
#                 'SELECT Topaybill from totalR').fetchall()[-1]
#         except:
#             last_row2 = (0,)
#         try:
#             last_topayusr = cur.execute(
#                 'SELECT Topayusr from totalR').fetchall()[-1]
#         except:
#             last_topayusr = (0,)
#         newval2 = float(last_topayusr[0]) + float(Amnt)
#         cur.execute("INSERT into totalR VALUES (NULL,?,?,?,?,?)",
#                     (last_row2[0], 0, newval2, 0, currentDate))
#         allvalue2 = cur.execute('SELECT * from totalS').fetchall()[-1]
#         allvalue = cur.execute('SELECT * from totalR').fetchall()[-1]
#     cur.execute("INSERT INTO entry5 VALUES (NULL,?,?,?,?)",
#                 (Desc, Amnt, usr, currentDate))
#     con.commit()
#     con.close()


# def Viewusrs(user=""):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     if(user == ""):
#         cur.execute("SELECT * FROM entry5")
#     elif(user != ""):
#         cur.execute("SELECT * FROM entry5 WHERE Usr=?", (user,))
#     row = cur.fetchall()
#     con.close()
#     return row


# def Viewbilltotal(user=""):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     if(user == ""):
#         tkinter.messagebox.showerror("Error", "Please select User")
#     elif(user == "Saleem"):
#         # val = cur.execute('SELECT Topay from total').fetchall()[-1]
#         val = cur.execute('SELECT Topaybill from totalS').fetchall()[-1]
#     elif(user == "Rajeeb"):
#         # val = cur.execute('SELECT Topay from total').fetchall()[-1]
#         val = cur.execute('SELECT Topaybill from totalR').fetchall()[-1]
#         # cur.execute("SELECT SUM(BA FROM entry4 WHERE Usr=?",(user,))
#         # val = cur.fetchone()
#     con.close()
#     print(val)
#     return val


# def Viewusrstotal(user=""):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     if(user == ""):
#         pass
#     elif(user == "Saleem"):
#         row = cur.execute('SELECT Topayusr FROM totalS').fetchall()[-1]
#         print(row)
#     elif(user == "Rajeeb"):
#         row = cur.execute('SELECT Topayusr FROM totalR').fetchall()[-1]

#     con.close()
#     return row


# def billpaid(Paid="", Usr=""):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     # cur.execute("SELECT Topay from total WHERE id=?",(idnew,))
#     if(Usr == "Saleem"):
#         last_row = cur.execute('SELECT Topaybill from totalS').fetchall()[-1]
#         last_topayusr = cur.execute(
#             'SELECT Topayusr from totalS').fetchall()[-1]
#     elif(Usr == "Rajeeb"):
#         last_row = cur.execute('SELECT Topaybill from totalR').fetchall()[-1]
#         last_topayusr = cur.execute(
#             'SELECT Topayusr from totalR').fetchall()[-1]

#     print(last_row)
#     newtopay = float(last_row[0]) - float(Paid)
#     if(Usr == "Saleem"):
#         cur.execute("INSERT into totalS VALUES (NULL,?,?,?,?,?)",
#                     (newtopay, Paid, last_topayusr[0], 0, currentDate))
#     elif(Usr == "Rajeeb"):
#         cur.execute("INSERT into totalR VALUES (NULL,?,?,?,?,?)",
#                     (newtopay, Paid, last_topayusr[0], 0, currentDate))
#     allvalue = cur.execute('SELECT * from totalS').fetchall()[-1]
#     allvalue1 = cur.execute('SELECT * from totalR').fetchall()[-1]
#     print(allvalue)
#     print(allvalue1)
#     con.commit()
#     con.close()


# def usrpaid(Paid="", Usr=""):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     # cur.execute("SELECT Topay from total WHERE id=?",(idnew,))
#     if(Usr == "Saleem"):
#         last_row = cur.execute('SELECT Topaybill from totalS').fetchall()[-1]
#         last_topayusr = curuniq.execute(
#             'SELECT Topayusr from totalS').fetchall()[-1]
#     elif(Usr == "Rajeeb"):
#         last_row = cur.execute('SELECT Topaybill from totalR').fetchall()[-1]
#         last_topayusr = curuniq.execute(
#             'SELECT Topayusr from totalR').fetchall()[-1]

#     print(last_row)
#     newtopay = float(last_topayusr[0]) - float(Paid)
#     if(Usr == "Saleem"):
#         cur.execute("INSERT into totalS VALUES (NULL,?,?,?,?,?)",
#                     (last_row[0], Paid, newtopay, 0, currentDate))
#     elif(Usr == "Rajeeb"):
#         cur.execute("INSERT into totalR VALUES (NULL,?,?,?,?,?)",
#                     (last_row[0], Paid, newtopay, 0, currentDate))
#     # allvalue = cur.execute('SELECT * from totalS').fetchall()[-1]
#     # allvalue1 = cur.execute('SELECT * from totalR').fetchall()[-1]
#     # print(allvalue)
#     # print(allvalue1)
#     con.commit()
#     con.close()


# def deletusrRec(id):
#     con = sqlite3.connect("StockEntry.db")
#     cur = con.cursor()
#     cur.execute("DELETE FROM entry5 WHERE id=?", (id,))
#     con.commit()
#     con.close()


########################################  Return  ##############################################################

def RtrnOrder(Cat="", Num="", Meter="", rate="", uservar=""):
    conn = sqlite3.connect("StockEntry.db")
    curn = conn.cursor()
    curn.execute("CREATE TABLE IF NOT EXISTS return (id INTEGER PRIMARY KEY, Cat text, Num text, Meter INTEGER, Rate INTEGER, UserVar text, Date TIMESTAMp) ")
    # curn.execute("SELECT SUM(Total) FROM return")
    # val = curn.fetchone()
    # print(val)
    curn.execute("INSERT into return VALUES (NULL,?,?,?,?,?,?)",
                 (Cat, Num, Meter, rate, uservar, currentDate))

    length = curn.execute(
        "SELECT COUNT(ALL) from entry2 WHERE Cat=? AND Num=?", (Cat, Num))
    leng = curn.fetchone()
    print(leng[0])
    if(leng[0] == 0 and Meter != ""):
        curn.execute("INSERT INTO entry2 VALUES (NULL,?,?,?,?)",
                     (Cat, Num, Meter, currentDate))
        print("success")

    elif(leng[0] == 1 and Meter != ""):
        meter = curn.execute(
            "SELECT METER from entry2 WHERE Cat=? AND Num=?", (Cat, Num))
        mtr = curn.fetchone()
        val = float(Meter) + mtr[0]
        print(val)
        curn.execute("UPDATE entry2 SET Meter=?,Date=? WHERE Cat=? AND Num=?",
                     (val, currentDate, Cat, Num))

    else:
        print('Error! There are more than 1 value')

    Paid = float(Meter)*float(rate)
    conn.commit()
    conn.close()
    # billpaid(Paid, uservar)


def DisplayReturn():
    conr = sqlite3.connect("StockEntry.db")
    curr = conr.cursor()
    curr.execute("SELECT * FROM return")
    row = curr.fetchall()
    conr.close()
    return row
