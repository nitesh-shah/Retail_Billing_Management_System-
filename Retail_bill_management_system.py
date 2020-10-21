from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import sqlite3

#class for front End UI
class product:
    def __init__(self,root):

        #create object reference of database as p
        p=Database()
        p.conn()
        
        self.root=root
        self.root.geometry('1366x700')
        #self.root.resizable(width=False, height=False)
        self.root.title("Retail Bill Management System")

        

        #create variable
        BillNo=StringVar()
        Name=StringVar()
        Date=StringVar()
        Gross=StringVar()
        Discount=StringVar()
        Net=StringVar()
        SGST=StringVar()
        CGST=StringVar()
        IGST=StringVar()
        Total=StringVar()
        ChequeNo=StringVar()
        Paid=IntVar()


        #############Calling Database methods to perform database operations#####
        def close():
            print("Closing Method Called")
            close=tkinter.messagebox.askyesno("Exit","Really want to close?")
            if close > 0: #yes=1 No=0
                root.destroy()
                print("Closed")
                return

        def clear():
            print("clear method called")
            self.txtBillNo.delete(0,END)
            self.txtName.delete(0,END)
            self.txtDate.delete(0,END)
            self.txtGross.delete(0,END)
            self.txtDiscount.delete(0,END)
            self.txtNet.delete(0,END)
            self.txtSGST.delete(0,END)
            self.txtCGST.delete(0,END)
            self.txtIGST.delete(0,END)
            self.txtTotal.delete(0,END)
            self.txtChequeNo.delete(0,END)
            
            print("Cleared")

        def insert():
            print("Insert method called")
            if(len(BillNo.get())!=0):
                p.insert(BillNo.get(),Name.get(),Date.get(),Gross.get(),Discount.get(),Net.get(),SGST.get(),CGST.get(),IGST.get(),Total.get(),ChequeNo.get(),Paid.get())
                detailsList.delete(0,END)
                detailsList.insert(END,BillNo.get(),Name.get(),Date.get(),Gross.get(),Discount.get(),Net.get(),SGST.get(),CGST.get(),IGST.get(),Total.get(),ChequeNo.get(),Paid.get())
            else:
                tkinter.messagebox.showinfo("BILLS","Please enter BillNO.")

            print("Insert Method Executed")


        # show detailed in the list
        def showDetails():
            print("Show method called")
            detailsList.delete(0,END)
            for row in p.show():
                detailsList.insert(END,row,str(""))
            print("Show method executed")

        #add to scroll bar

        def detailedList(event):#functiontobe called from scrollbar
            print("Detailed list called")
            global dl

            searchDL=detailsList.curselection()[0]
            dl=detailsList.get(searchDL)
            self.txtBillNo.delete(0,END)
            self.txtBillNo.insert(END,dl[0])
            
            self.txtName.delete(0,END)
            self.txtName.insert(END,dl[1])
            
            self.txtDate.delete(0,END)
            self.txtDate.insert(END,dl[2])
            
            self.txtGross.delete(0,END)
            self.txtGross.insert(END,dl[3])
            
            self.txtDiscount.delete(0,END)
            self.txtDiscount.insert(END,dl[4])
            
            self.txtNet.delete(0,END)
            self.txtNet.insert(END,dl[5])
            
            self.txtSGST.delete(0,END)
            self.txtSGST.insert(END,dl[6])
            
            self.txtCGST.delete(0,END)
            self.txtCGST.insert(END,dl[7])
            
            self.txtIGST.delete(0,END)
            self.txtIGST.insert(END,dl[8])
            
            self.txtTotal.delete(0,END)
            self.txtTotal.insert(END,dl[9])

            self.txtChequeNo.delete(0,END)
            self.txtChequeNo.insert(END,dl[10])


            

            print("Detailed list executed")

            #function to delete data or recordfrom databbase
        def delete():
            print("Delete method called")
            if(len(BillNo.get())!=0):
                p.delete(dl[0])
                clear()
                showDetails()   
            print("Delete method executed")

            #Search the record from table
        def search():
            print("search method called")
            detailsList.delete(0,END)
            for row in p.search(BillNo.get(),Name.get(),Date.get()):
                detailsList.insert(END,row,str(""))
            print("Search method executed")

            #update the record
        def update():
            print("update function called")
            if(len(BillNo.get())!=0):
                #print("dl[0]",dl[p])
                p.delete(dl[0])
            if(len(BillNo.get())!=0):
                p.insert(BillNo.get(),Name.get(),Date.get(),Gross.get(),Discount.get(),Net.get(),SGST.get(),CGST.get(),IGST.get(),Total.get(),ChequeNo.get(),Paid.get())                
                detailsList.delete(0,END)
                detailsList.insert(END,(BillNo.get(),Name.get(),Date.get(),Gross.get(),Discount.get(),Net.get(),SGST.get(),CGST.get(),IGST.get(),Total.get(),ChequeNo.get(),Paid.get()))
                tkinter.messagebox.showinfo("Payments","Updated")
            print("Update method Executed")

    ###CGST=net*2.5
    ###SGST=net*2.5
    ###Total=net+CGST+SGST
        def calculate():
            num1=Gross.get()
            num2=Discount.get()
            #if(num1.isdigit() or num2.isdigit()):
            num3=float(num1)-float(num2)
                
            num4=(num3*2.5)/100
            num5=(num3*2.5)/100
            num6=num3+num4+num5
            Net.set(round(num3,2))
        
            CGST.set(round(num4,2))
            SGST.set(round(num5,2))
            Total.set(round(num6,2))
                
                
            
            
            
            
   
    ####################################################################################

        #create the frame
        MainFrame=Frame(self.root,bg="black")
        MainFrame.grid()

        HeadFrame=Frame(MainFrame,bd=8,width=1090,padx=510,pady=0,bg="white",relief=RIDGE)
        HeadFrame.pack(side=TOP,expand=False)
        

        self.ITitle=Label(HeadFrame,font=('arial',50,'bold'),fg='red',text="Payments",justify=CENTER,bg='white')
        self.ITitle.grid()

        #operations to perform
        OperationFrame=Frame(MainFrame,bd=8,width=1090,height=50,padx=425,pady=5,bg='white',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
        

        #body frame
        BodyFrame=Frame(MainFrame,bd=8,width=1090,height=50,padx=145,pady=20,bg='white',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM,expand=False)

        #left body frame
        LeftBodyFrame=LabelFrame(BodyFrame,bd=5,width=654,height=360,bg='gray',relief=RIDGE,font=('arial',15,'bold'),text="Enter Details:",fg='white')
        LeftBodyFrame.pack(side=LEFT,fill='both', expand=False)
        #right body frame
        RightBodyFrame=LabelFrame(BodyFrame,bd=5,width=522,height=360,padx=20,pady=30,bg='gray',relief=RIDGE,font=('arial',15,'bold'),text="Details Entered:",fg='white')
        RightBodyFrame.pack(side=RIGHT,fill='both', expand=False)

                                            ######add widgets to left body frame#########
        #BillNo
        self.labelBillNo=Label(LeftBodyFrame,font=('arial',15,'bold'),text="BillNo:",padx=0,fg="red",bg='gray')
        self.labelBillNo.grid(row=0,column=0,sticky=W)
        self.txtBillNo=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=BillNo,width=30)
        self.txtBillNo.grid(row=0,column=1)

        ################################################################
        #Name
        self.labelName=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Name:",padx=0,fg="red",bg='gray')
        self.labelName.grid(row=1,column=0,sticky=W)
       # v=['nitesh']
        list1 = ['Canada','India','UK','Nepal','Iceland','South Africa']
        self.labelName=Combobox(LeftBodyFrame,values=list1,width=52,textvariable=Name)
        
            
        self.labelName.grid(row=1,column=1)
        #self.txtName=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Name,width=30)
        #self.txtName.grid(row=1,column=1)

        ###############################################################
        #Date
        self.labelDate=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Date:",padx=0,fg="red",bg='gray')
        self.labelDate.grid(row=2,column=0,sticky=W)
        self.txtDate=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Date,width=30)
        self.txtDate.grid(row=2,column=1)

        ################################################################
        #Gross
        self.labelGross=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Gross:",padx=0,fg="red",bg='gray')
        self.labelGross.grid(row=3,column=0,sticky=W)
        self.txtGross=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Gross,width=30)
        self.txtGross.grid(row=3,column=1)



        ################################################################
        #Discount
        self.labelDiscount=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Discount:",padx=0,fg="red",bg='gray')
        self.labelDiscount.grid(row=4,column=0,sticky=W)
        self.txtDiscount=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Discount,width=30)
        self.txtDiscount.grid(row=4,column=1)


        ################################################################
        #Net
        self.labelNet=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Net:",padx=0,fg="red",bg='gray')
        self.labelNet.grid(row=5,column=0,sticky=W)
        self.txtNet=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Net,width=30)
        self.txtNet.grid(row=5,column=1)


        #################################################################
        #SGST
        self.labelSGST=Label(LeftBodyFrame,font=('arial',15,'bold'),text="SGST:",padx=0,fg="red",bg='gray')
        self.labelSGST.grid(row=6,column=0,sticky=W)
        self.txtSGST=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=SGST,width=30)
        self.txtSGST.grid(row=6,column=1)
        




        #################################################################
        #CGST
        self.labelCGST=Label(LeftBodyFrame,font=('arial',15,'bold'),text="CGST:",padx=0,fg="red",bg='gray')
        self.labelCGST.grid(row=7,column=0,sticky=W)
        self.txtCGST=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=CGST,width=30)
        self.txtCGST.grid(row=7,column=1)
        






        #################################################################
        #IGST
        self.labelIGST=Label(LeftBodyFrame,font=('arial',15,'bold'),text="IGST:",padx=0,fg="red",bg='gray')
        self.labelIGST.grid(row=8,column=0,sticky=W)
        self.txtIGST=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=IGST,width=30)
        self.txtIGST.grid(row=8,column=1)





        ##################################################################
        #Total
        self.labelTotal=Label(LeftBodyFrame,font=('arial',15,'bold'),text="Total:",padx=0,fg="red",bg='gray')
        self.labelTotal.grid(row=9,column=0,sticky=W)
        self.txtTotal=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=Total,width=30)
        self.txtTotal.grid(row=9,column=1)


        ##ChequeNo
        self.labelChequeNo=Label(LeftBodyFrame,font=('arial',15,'bold'),text="ChequeNo:",padx=0,fg="red",bg='gray')
        self.labelChequeNo.grid(row=10,column=0,sticky=W)
        self.txtChequeNo=Entry(LeftBodyFrame,font=('arial',15,'bold'),textvariable=ChequeNo,width=30)
        self.txtChequeNo.grid(row=10,column=1,sticky=W)

        self.labelPaid=Checkbutton(LeftBodyFrame,text="Paid",variable=Paid,font=('arial',15,'bold'),fg="red",bg='gray')
        self.labelPaid.grid(row=10,column=2,sticky=W)

        
        #Calculate button
        self.buttonCalculate=Button(LeftBodyFrame, text='Calculate',font=('arial',15,'bold'),bd=4,command=calculate)
        self.buttonCalculate.grid(row=12,column=0)

        #insert button
        self.buttonInsert=Button(LeftBodyFrame, text='Insert',font=('arial',15,'bold'),bd=4,command=insert)
        self.buttonInsert.grid(row=12,column=1)

        self.buttonClear=Button(LeftBodyFrame, text='Done',font=('arial',15,'bold'),bd=4,command=clear)
        self.buttonClear.grid(row=12,column=2,sticky=W)



                                ###Scroll Bar To Right Pannel##
        scroll=Scrollbar(RightBodyFrame)
        scroll.grid(row=0,column=1,sticky='ns')
        
        ##ListBox
        detailsList=Listbox(RightBodyFrame,width=50,height=17,font=('arial',12,'bold'),yscrollcommand=scroll.set)
        #called above createddetailedlist fron init
        detailsList.bind('<<ListboxSelect>>',detailedList)
        detailsList.grid(row=0,column=0,)

        scroll.config(command=detailsList.yview)


                ##############Addd buttons to operation frames#####################
        self.buttonCreate=Button(OperationFrame, text='Create',font=('arial',15,'bold'),bd=4)
        self.buttonCreate.grid(row=0,column=1)

        self.buttonSearch=Button(OperationFrame, text='Search',font=('arial',15,'bold'),bd=4,command=search)
        self.buttonSearch.grid(row=0,column=2)

        self.buttonUpdate=Button(OperationFrame, text='update',font=('arial',15,'bold'),bd=4,command=update)
        self.buttonUpdate.grid(row=0,column=3)

        self.buttonDelete=Button(OperationFrame, text='Delete',font=('arial',15,'bold'),bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=4)

        self.buttonShow=Button(OperationFrame, text='Show',font=('arial',15,'bold'),bd=4,command=showDetails)
        self.buttonShow.grid(row=0,column=5)

        
        

        

        self.buttonClose=Button(OperationFrame, text='Close',font=('arial',15,'bold'),bd=4,command=close)
        self.buttonClose.grid(row=0,column=7)

        ##############Backend database Operations#############
class Database:
    def conn(self):
        print("Database: Connection method called")
        con = sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        query=('''create table if not exists payments(BillNo integer primary key,Name TEXT,Date DATE,Gross REAL,Discount REAL,Net REAL,SGST REAL,CGST REAL,IGST REAL,Total REAL,ChequeNo REAL,Paid TEXT)''')
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished \n")

    #insert
    def insert(self,BillNo,Name,Date,Gross,Discount,Net,SGST,CGST,IGST,Total,ChequeNo,Paid):
        print("Database: insert method called")
        con=sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        query=('''insert into payments values(?,?,?,?,?,?,?,?,?,?,?,?)''')
        cur.execute(query,(BillNo,Name,Date,Gross,Discount,Net,SGST,CGST,IGST,Total,ChequeNo,Paid))
        con.commit()
        con.close()
        print("Database : insert method finished \n")

    #show
    def show(self):
        print("Database: Show method called")
        con=sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        query="select * from payments"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database : Show method finished \n")
        return rows

    #delete
    def delete(self,BillNo):
        print("Database: delete method called",BillNo)
        con=sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        cur.execute("delete from payments where BillNo=?",(BillNo,))
        con.commit()
        con.close()
        print(BillNo,"Database : Delete method finished \n")

    #Search
    def search(self,BillNo="",Name="",Date=""):
        print("Database: Search method called")
        con=sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        cur.execute("select * from payments where BillNo=? or Name=? or Date=?",(BillNo,Name,Date))
        row=cur.fetchall()
        con.close()
        print(BillNo,"Database : Search method finished \n")
        return row

    #Update
    def update(self,BillNo="",Name="",Date="",Gross="",Discount="",Net="",SGST="",CGST="",IGST="",Total="",ChequeNo="",Paid=""):
        print("Database: update method called")
        con=sqlite3.connect("PNSHAH.db")
        cur=con.cursor()
        cur.execute("update payments set BillNo=?,Name=?,Date=?,Gross=?,Discount=?,Net=?,SGST=?,CGST=?,IGST=?,Total=?,ChequeNo=?,Paid=? where BillNo=?",(BillNo,Name,Date,Gross,Discount,Net,SGST,CGST,IGST,Total,BillNo,ChequeNo,Paid))
        con.commit()
        con.close()
        print(BillNo,"Database : Update method finished \n")


    
        
            
            
            

  

if __name__ == '__main__':
    root=Tk()
    
    application=product(root)
    root.mainloop()
