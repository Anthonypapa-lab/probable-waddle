from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('C:/Users/Hp/Desktop/store project/store management software/database/store.db')
c = conn.cursor()

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        # master i sinheriting from Tk()
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=250,y=0)

        # labels and entries for the window
        self.name_1 = Label(master, text='Enter product name',font=('arial 18 bold'))
        self.name_1.place(x=0, y=70)

        self.stock_1 = Label(master, text='Enter Stock', font=('arial 18 bold'))
        self.stock_1.place(x=0, y=120)

        self.cp_1 = Label(master, text='Enter Cost price', font=('arial 18 bold'))
        self.cp_1.place(x=0, y=170)

        self.sp_1 = Label(master, text='Enter Selling price', font=('arial 18 bold'))
        self.sp_1.place(x=0, y=220)

        self.vendor_1 = Label(master, text='Enter Vendor name', font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=270)

        self.vendor_phoneno_1 = Label(master, text='Enter Vendor phone no.', font=('arial 18 bold'))
        self.vendor_phoneno_1.place(x=0, y=320)

        # entries for the labels
        self.name_e = Entry(master, width =25, font=('arial 18 bold'))
        self.name_e.place(x=300,y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=300, y=120)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=300, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=300, y=230)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=300, y=280)

        self.vendor_phoneno_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phoneno_e.place(x=300, y=330)

        # button to add to the database
        self.btn_add = Button(master,text = 'Add to database' ,width =25, height = 2, bg= 'steelblue', fg = 'white', command = self.get_items)
        self.btn_add.place(x=425, y=380)

        # text box for the logs
        self.tBox=Text(master,width = 60, height = 18)
        self.tBox.place(x=650,y=70)

    def get_items(self, *args, **kwargs):
        # get from entry boxes
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phoneno = self.vendor_phoneno_e.get()

        if self.name == '' or self.cp == '' or self.sp == '' or self.stock == '':
            tkinter.messagebox.showinfo('Error', 'Please fill all the required fields')
        else:
            # dynamic entries
            self.totalcp = float(self.cp) * float(self.stock)
            self.totalsp = float(self.sp) * float(self.stock)
            self.assumed_profit = float(self.totalsp) - float(self.totalcp)

            sql = 'INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno)Values(?,?,?,?,?,?,?,?.?)'
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phoneno))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")


root = Tk()
b = Database(root)

root.title('Add to the database')
root.mainloop()