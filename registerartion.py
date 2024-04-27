from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")
        
        #-----------variables---------------
        self.var_ref=StringVar()
        x=random.randint(100, 9999)
        self.var_ref.set(str(x))
        
        self.var_name=StringVar()
        self.var_mail=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()
        self.var_pass=StringVar()
        
        
        #========title========
        lbl_title=Label(self.root,text="REGISTRATION WINDOW",justify="center",font=("Times New Roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1500,height=40)
        
        lbl_login_frame=LabelFrame(self.root,text="Registration Window",border=3,relief=RIDGE,font=("Times New Roman",13,"bold"))
        lbl_login_frame.place(x=550,y=150,width=400,height=500)
        
        lbl_entry_ref=Label(lbl_login_frame,text="Ref ID: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_entry_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(lbl_login_frame,width=22,font=("Times New Roman",11,"bold"),textvariable=self.var_ref,state="readonly")
        entry_ref.grid(row=0,column=1)
        
        lbl_name_ref=Label(lbl_login_frame,text="Name: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_name_ref.grid(row=2,column=0,sticky=W)
        entry_name=ttk.Entry(lbl_login_frame,width=22,textvariable=self.var_name,font=("Times New Roman",11,"bold"))
        entry_name.grid(row=2,column=1)
        
        lbl_phone_ref=Label(lbl_login_frame,text="Phone No: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_phone_ref.grid(row=4,column=0,sticky=W)
        entry_phone=ttk.Entry(lbl_login_frame,textvariable=self.var_phone, width=22,font=("Times New Roman",11,"bold"))
        entry_phone.grid(row=4,column=1)
        
        lbl_mail_ref=Label(lbl_login_frame,text="Email ID: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_mail_ref.grid(row=6,column=0,sticky=W)
        entry_mail=ttk.Entry(lbl_login_frame,width=22,textvariable=self.var_mail, font=("Times New Roman",11,"bold"))
        entry_mail.grid(row=6,column=1)
        
        lbl_gender_ref=Label(lbl_login_frame,text="Gender: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_gender_ref.grid(row=8,column=0,sticky=W)
        entry_gender=ttk.Combobox(lbl_login_frame,width=22,textvariable=self.var_gender,font=("Times New Roman",11,"bold"),state="readonly")
        entry_gender["value"]=("Male","Female","Others")
        entry_gender.grid(row=8,column=1)
        
        lbl_pass_ref=Label(lbl_login_frame,text="Password: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_pass_ref.grid(row=9,column=0,sticky=W)
        entry_pass=ttk.Entry(lbl_login_frame,width=22,textvariable=self.var_pass, font=("Times New Roman",11,"bold"))
        entry_pass.grid(row=9,column=1)
        
        add_btn=Button(lbl_login_frame,text="REGISTER NOW",justify="center",command=self.add_cust_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        add_btn.place(x=10,y=300,width=150,height=30)     
        
        
        
        
        
        
        
        
        
        
        
        
    #-----------adding customer------------
    def add_cust_details(self):
        if self.var_phone.get()=="" or self.var_mail.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            cur.execute("select * from customer where Email=%s",(self.var_mail.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists")
            else:
                try:
                    cur.execute("insert into customer values(%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_phone.get(),self.var_mail.get(),self.var_gender.get()))
                    cur.execute("insert into login_info values(%s,%s,%s)",(self.var_mail.get(),self.var_pass.get(),self.var_ref.get()))
                    messagebox.showinfo("Successfull","Registered successfully",parent=self.root)
                    
                    conn.commit()
                    conn.close()
                    
                    
                except Exception as es:
                    messagebox.showwarning("Warning",f"Sommething went wrong:{str(es)}",parent=self.root)
            
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=register(root)
    root.mainloop()
        