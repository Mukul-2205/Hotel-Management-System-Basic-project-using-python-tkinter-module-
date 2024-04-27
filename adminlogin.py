from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from hotel import HotelManagementSys


class admin_login_portal:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")
        
        #-----------variables---------------
        self.var_username=StringVar()
        self.var_passsword=StringVar()
        
        
        #========title========
        lbl_title=Label(self.root,text="ADMIN LOGIN",justify="center",font=("Times New Roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1500,height=40)
        
        lbl_login_frame=LabelFrame(self.root,text="Admin Login Portal",border=3,relief=RIDGE,font=("Times New Roman",13,"bold"))
        lbl_login_frame.place(x=550,y=150,width=400,height=500)
        
        
        
        
        lbl_username=Label(lbl_login_frame,text="ADMIN USERNAME ",font=("Times New Roman",15,"bold"))
        lbl_username.place(x=5,y=20,width=250,height=50)        
        entry_username=ttk.Entry(lbl_login_frame,font=("Times New Roman",12,"bold"),textvariable=self.var_username)
        entry_username.place(x=25,y=65,width=300,height=30)
        
        lbl_password=Label(lbl_login_frame,text="PASSWORD",font=("Times New Roman",15,"bold"))
        lbl_password.place(x=10,y=120,width=150,height=50)        
        entry_password=ttk.Entry(lbl_login_frame,font=("Times New Roman",12,"bold"),show="*",textvariable=self.var_passsword)
        entry_password.place(x=25,y=170,width=300,height=30)
        
        login_btn=Button(lbl_login_frame,text="LOGIN",justify="center",command=self.login,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        login_btn.place(x=100,y=220,width=185,height=35) 
        
        
    def home_page(self):
        self.new_win=Toplevel(self.root)
        self.runFunc=HotelManagementSys(self.new_win)
        
        
    def login(self):
        if self.var_username.get()=="" or self.var_passsword.get()=="":
            messagebox.showerror("Error","Incomplete Details")
        elif self.var_username.get()=="admin" and self.var_passsword.get()=="password":
            messagebox.showinfo("Sucessfull","Admin Login Successfull")
            self.home_page()
        else:
            messagebox.showerror("Error","Invalid Credentials")
        
        



if __name__=="__main__":
    root=Tk()
    obj=admin_login_portal(root)
    root.mainloop()