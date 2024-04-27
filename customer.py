from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1290x740+205+78")
        
        #========title========
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",justify="center",font=("Times New Roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1300,height=40)
        
        #-----------label frame-----------
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Times New Roman",10,"bold"))
        labelFrameLeft.place(x=0,y=40,width=400,height=480)
        
        #-----------variables---------------
        self.var_ref=StringVar()
        x=random.randint(100, 9999)
        self.var_ref.set(str(x))
        self.password=StringVar()
        self.var_name=StringVar()
        self.var_mail=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()
        
        
        
        #----------options and entry--------
        
        #------------cust details entry----------
        lbl_entry_ref=Label(labelFrameLeft,text="Ref ID: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_entry_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelFrameLeft,width=22,font=("Times New Roman",11,"bold"),textvariable=self.var_ref,state="readonly")
        entry_ref.grid(row=0,column=1)
        
        lbl_name_ref=Label(labelFrameLeft,text="Name: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_name_ref.grid(row=1,column=0,sticky=W)
        entry_name=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_name,font=("Times New Roman",11,"bold"))
        entry_name.grid(row=1,column=1)
        
        lbl_phone_ref=Label(labelFrameLeft,text="Phone No: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_phone_ref.grid(row=2,column=0,sticky=W)
        entry_phone=ttk.Entry(labelFrameLeft,textvariable=self.var_phone, width=22,font=("Times New Roman",11,"bold"))
        entry_phone.grid(row=2,column=1)
        
        lbl_mail_ref=Label(labelFrameLeft,text="Email ID: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_mail_ref.grid(row=3,column=0,sticky=W)
        entry_mail=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_mail, font=("Times New Roman",11,"bold"))
        entry_mail.grid(row=3,column=1)
        
        lbl_gender_ref=Label(labelFrameLeft,text="Gender: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_gender_ref.grid(row=4,column=0,sticky=W)
        entry_gender=ttk.Combobox(labelFrameLeft,width=22,textvariable=self.var_gender,font=("Times New Roman",11,"bold"),state="readonly")
        entry_gender["value"]=("Male","Female","Others")
        entry_gender.grid(row=4,column=1)
        
        lbl_pass=Label(labelFrameLeft,text="Create Password: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_pass.grid(row=5,column=0,sticky=W)
        entry_pass=ttk.Entry(labelFrameLeft,width=22,show="*",textvariable=self.password, font=("Times New Roman",11,"bold"))
        entry_pass.grid(row=5,column=1)
        
        #------------button frame----------------
        btn_frame=Frame(labelFrameLeft,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=390,height=50)
        
        #---------------add buttons-------------
        add_btn=Button(btn_frame,text="ADD",justify="center",command=self.add_cust_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        add_btn.place(x=0,y=0,width=100,height=45)        
        
        update_btn=Button(btn_frame,text="UPDATE",justify="center",command=self.update_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        update_btn.place(x=102,y=0,width=100,height=45)        
        
        delete_btn=Button(btn_frame,text="DELETE",justify="center",command=self.delete_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        delete_btn.place(x=204,y=0,width=90,height=45)        
        
        reset_btn=Button(btn_frame,text="RESET",justify="center",command=self.reset_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        reset_btn.place(x=296,y=0,width=95,height=45)        
        
        #----------------tabel frame-------------
        table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="ALL CUSTOMERS DETAILS",font=("Times New Roman",11,"bold"))
        table_frame.place(x=410,y=50,height=600,width=870)
        
        lbl_searchby=Label(table_frame,text="Search By: ",font=("Times New Roman",11,"bold"))
        lbl_searchby.grid(row=0,column=0)        
        
        self.var_search=StringVar()
        search_combo=ttk.Combobox(table_frame,textvariable=self.var_search,font=("Times New Roman",11,"bold"),width=22,height=16,state="readonly")
        search_combo["value"]=("Phone_no","Ref_id")
        search_combo.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(table_frame,width=22,textvariable=self.txt_search, font=("Times New Roman",11,"bold"))
        entry_search.grid(row=0,column=2,padx=2)
        
        search_btn=Button(table_frame,text="SEARCH",justify="center",command=self.search,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        search_btn.grid(row=0,column=3,padx=2)
        showall_btn=Button(table_frame,text="SHOW ALL",justify="center",command=self.fetch_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        showall_btn.grid(row=0,column=4,padx=2)
        
        
        
        #---------Show Customer Table---------------
        data_table_frame=Frame(table_frame,bd=3,relief=RIDGE)
        data_table_frame.place(x=0,y=40,width=860,height=530)
        
        self.Cust_Details_Table=ttk.Treeview(data_table_frame,column=("Ref","Name","Phone","Email","Gender"))
        
        self.Cust_Details_Table.heading("Ref",text="Ref ID")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("Phone",text="Phone No.")
        self.Cust_Details_Table.heading("Email",text="Email ID")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Ref", width=100)
        self.Cust_Details_Table.column("Name", width=100)
        self.Cust_Details_Table.column("Phone", width=100)
        self.Cust_Details_Table.column("Email", width=100)
        self.Cust_Details_Table.column("Gender", width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.see_details)
        self.fetch_details()
        
        
    #--------------fetching details from mysql database----------------
    def fetch_details(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        cur=conn.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #-----------adding customer------------
    def add_cust_details(self):
        if self.var_phone.get()=="" or self.var_mail.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_phone.get(),self.var_mail.get(),self.var_gender.get()))
                messagebox.showinfo("Successfull","Details added successfully",parent=self.root)
                cur.execute("insert into login_info values(%s,%s,%s)",(self.var_mail.get(),self.password.get(),self.var_ref.get()))
                conn.commit()
                self.fetch_details()
                conn.close()
                
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Sommething went wrong:{str(es)}",parent=self.root)
        
        
    def see_details(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_phone.set(row[2])
        self.var_mail.set(row[3])
        self.var_gender.set(row[4])
        
    def update_details(self):
        if self.var_phone.get()=="":
            messagebox.showerror("Warning","Pleasy specify phone number")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            cur.execute("update customer set Name=%s , Phone_no=%s , Email=%s , Gender=%s where Ref_id=%s",(self.var_name.get(),self.var_phone.get(),self.var_mail.get(),self.var_gender.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo("Updated","Details Updated",parent=self.root)
            
    def delete_details(self):
        ask=messagebox.askyesno("Warning","Do you really want to delete the selected detail?",parent=self.root)
        if ask>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            query="delete from customer where Ref_id=%s"
            value=(self.var_ref.get(),)
            cur.execute(query,value)
            
        else:
            if not ask:
                return
        conn.commit()
        self.fetch_details()
        conn.close()
        
        
    def reset_details(self):
        
        self.var_name.set("")
        self.var_phone.set("")
        self.var_mail.set("")
        self.var_gender.set("")
        
        x=random.randint(100, 9999)
        self.var_ref.set(str(x))
        
        
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        cur=conn.cursor()
        
        if self.var_search.get() == "" or self.txt_search.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter a value",parent=self.root)
        else:
            try:
                cur.execute("SELECT * FROM customer WHERE " + str(self.var_search.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Info", "No record found")
            except Exception as e:
                messagebox.showerror("Error", f"Error in fetching data: {str(e)}")
            conn.close()
        

        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=cust_window(root)
    root.mainloop()