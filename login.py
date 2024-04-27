from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime
from registerartion import register
from adminlogin import admin_login_portal

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()



class login_window:
    def init_var(self):
        global phn_number
        phn_number=StringVar()
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")
        
        self.username=StringVar()
        self.password=StringVar()
        
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",justify="center",font=("Times New Roman",30,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1500,height=40)

        lbl_login_frame=LabelFrame(self.root,text="Login Window",border=3,relief=RIDGE,font=("Times New Roman",13,"bold"))
        lbl_login_frame.place(x=550,y=150,width=400,height=500)
        
        lbl_username=Label(lbl_login_frame,text="USERNAME (your email id)",font=("Times New Roman",15,"bold"))
        lbl_username.place(x=19,y=20,width=250,height=50)        
        entry_username=ttk.Entry(lbl_login_frame,font=("Times New Roman",12,"bold"),textvariable=self.username)
        entry_username.place(x=25,y=65,width=300,height=30)
        
        lbl_password=Label(lbl_login_frame,text="PASSWORD",font=("Times New Roman",15,"bold"))
        lbl_password.place(x=10,y=120,width=150,height=50)        
        entry_password=ttk.Entry(lbl_login_frame,font=("Times New Roman",12,"bold"),show="*",textvariable=self.password)
        entry_password.place(x=25,y=170,width=300,height=30)
        
        login_btn=Button(lbl_login_frame,text="LOGIN",justify="center",command=self.login,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        login_btn.place(x=100,y=220,width=185,height=35) 
        
        reg_btn=Button(lbl_login_frame,text="New User? Create account",justify="center",command=self.reg,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        reg_btn.place(x=25,y=310,width=185,height=35)     
        
        switch_access_btn=Button(lbl_login_frame,text="Switch to admin access",justify="center",command=self.admin_login,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        switch_access_btn.place(x=25,y=360,width=185,height=35)
        
        
        
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            cur.execute("select password from login_info where email=%s",(self.username.get(),))
            row=cur.fetchone()
            if row!=(self.password.get(),):
                messagebox.showerror("Incorrect","Invalid username or password")
            else:
                cur.execute("select Ref_id from customer where Email=%s",(self.username.get(),))
                phn_number=cur.fetchone()
                messagebox.showinfo("Successful", f"Welcome user {self.username.get()}")
                self.new_window=Toplevel(self.root)
                self.runFunction=room_details(self.new_window,phn_number)
            conn.commit()
            conn.close()
            
                
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.runFunction=register(self.new_window)
    
    def admin_login(self):
        self.new_window=Toplevel(self.root)
        self.runFunction=admin_login_portal(self.new_window)
    
        
    
    
    
        
        
        
class room_details:
    def __init__(self,root,phn_number):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")
        
        #----------------variables-------------
        self.var_ref=StringVar()
        self.var_ref.set(phn_number[0])
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomno=StringVar()
        self.var_noOfDays=StringVar()
        self.var_totalcost=StringVar()
        
        
    
        #========title========
        lbl_title=Label(self.root,text="BOOKING DETAILS",justify="center",font=("Times New Roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1500,height=40)
        
        #-----------label frame-----------
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("Times New Roman",10,"bold"))
        labelFrameLeft.place(x=0,y=40,width=470,height=470)
        
        self.fetch_contact()
        
        
        #------------cust details entry----------
        lbl_entry_contact=Label(labelFrameLeft,text="Ref ID: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_entry_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelFrameLeft,width=18,textvariable=self.var_ref,font=("Times New Roman",11,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W,padx=7)

        lbl_checkin=Label(labelFrameLeft,text="Check_in Date: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_checkin.grid(row=1,column=0,sticky=W)
        entry_checkin=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_checkin,font=("Times New Roman",11,"bold"))
        entry_checkin.grid(row=1,column=1)
        
        lbl_checkout=Label(labelFrameLeft,text="Check-out Date: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_checkout.grid(row=2,column=0,sticky=W)
        entry_checkout=ttk.Entry(labelFrameLeft, width=22,textvariable=self.var_checkout,font=("Times New Roman",11,"bold"))
        entry_checkout.grid(row=2,column=1)
        
        
        lbl_room_type=Label(labelFrameLeft,text="Room Type: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_room_type.grid(row=3,column=0,sticky=W)
        entry_room_type=ttk.Combobox(labelFrameLeft,width=22,textvariable=self.var_roomtype,font=("Times New Roman",11,"bold"),state="readonly")
        entry_room_type["value"]=("Single","Double","Delux")
        entry_room_type.grid(row=3,column=1)
        fetch_roomno_btn=Button(labelFrameLeft,text="FETCH ROOMS",command=self.show_available_rooms,justify="center",font=("Times New Roman",7,"bold"),bg="black",fg="gold",cursor="hand2")
        fetch_roomno_btn.place(x=380,y=105,width=80,height=20)
        
        lbl_available_room=Label(labelFrameLeft,text="Available Room: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_available_room.grid(row=4,column=0,sticky=W)
        entry_available_room=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_roomno, font=("Times New Roman",11,"bold"))
        entry_available_room.grid(row=4,column=1)
        
       

        
        lbl_no_of_days=Label(labelFrameLeft,text="No. of Days: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_no_of_days.grid(row=5,column=0,sticky=W)
        entry_no_of_days=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_noOfDays, font=("Times New Roman",11,"bold"),state="readonly")
        entry_no_of_days.grid(row=5,column=1)
        
        lbl_total_cost=Label(labelFrameLeft,text="Total Cost: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_total_cost.grid(row=6,column=0,sticky=W)
        entry_total_cost=ttk.Entry(labelFrameLeft,width=22,textvariable=self.var_totalcost, font=("Times New Roman",11,"bold"),state="readonly")
        entry_total_cost.grid(row=6,column=1)
        
        bill_btn=Button(labelFrameLeft,text="BILL",command=self.billing_button,justify="center",font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        bill_btn.grid(row=9,column=0,sticky=W)
        
        #------------button frame----------------
        btn_frame=Frame(labelFrameLeft,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=310,height=50)
        
        #---------------add buttons-------------
        add_btn=Button(btn_frame,text="ADD",justify="center",command=self.add_room_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        add_btn.place(x=0,y=0,width=100,height=45)        
        
        update_btn=Button(btn_frame,text="UPDATE",justify="center",command=self.update_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        update_btn.place(x=102,y=0,width=100,height=45)        
        
        delete_btn=Button(btn_frame,text="DELETE",justify="center",command=self.delete_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        delete_btn.place(x=204,y=0,width=90,height=45)        
        
        cust_frame=Button(self.root,text="LOGOUT",justify="center",command=self.logout,font=("Times New Roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_frame.place(x=1330,y=50,width=150,height=30)
        
        #----------------tabel frame-------------
        table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="All Room Bookings",font=("Times New Roman",11,"bold"))
        table_frame.place(x=490,y=300,height=400,width=810)
        
        
        #---------Show Customer Table---------------
        room_table_frame=Frame(table_frame,bd=3,relief=RIDGE)
        room_table_frame.place(x=0,y=40,width=800,height=330)
        
        self.Room_Details_Table=ttk.Treeview(room_table_frame,column=("Ref ID","Check-in Date","Check-out Date","Room Type","Room No","No. of Days","Total Cost"))
        
        self.Room_Details_Table.heading("Ref ID",text="Ref ID")
        self.Room_Details_Table.heading("Check-in Date",text="Check-in Date")
        self.Room_Details_Table.heading("Check-out Date",text="Check-out Date")
        self.Room_Details_Table.heading("Room Type",text="Room Type")
        self.Room_Details_Table.heading("Room No",text="Room No")
        self.Room_Details_Table.heading("No. of Days",text="No. of Days")
        self.Room_Details_Table.heading("Total Cost",text="Total Cost")
        
        
        self.Room_Details_Table["show"]="headings"
        
        self.Room_Details_Table.column("Ref ID", width=55)
        self.Room_Details_Table.column("Check-in Date", width=55)
        self.Room_Details_Table.column("Check-out Date", width=55)
        self.Room_Details_Table.column("Room Type", width=55)
        self.Room_Details_Table.column("Room No", width=55)
        self.Room_Details_Table.column("No. of Days", width=55)
        self.Room_Details_Table.column("Total Cost", width=55)
        
        self.Room_Details_Table.pack(fill=BOTH,expand=1)
        
        self.Room_Details_Table.bind("<ButtonRelease-1>",self.see_details)
        self.fetch_details()
        
        
    #-------------see details------------ 
    def see_details(self,event=""):
        cursor_row=self.Room_Details_Table.focus()
        content=self.Room_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomno.set(row[4])
        self.var_noOfDays.set(row[5])
        self.var_totalcost.set(row[6])
        
    #----------------update------------------
    def update_details(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Warning","Pleasy specify ref id")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            cur.execute("update room set Check_in_date=%s , Check_out_date=%s , Room_type=%s , Room_no=%s , No_of_days=%s , Total_cost=%s where Ref_id=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomno.get(),self.var_noOfDays.get(),self.var_totalcost.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo("Updated","Details Updated",parent=self.root)
    
    
    #-----------------delete--------------
    def delete_details(self):
        ask=messagebox.askyesno("Warning","Do you really want to delete the selected detail?",parent=self.root)
        if ask>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            query="delete from room where Room_no=%s"
            value=(self.var_roomno.get(),)
            cur.execute(query,value)
            var_room_no=self.var_roomno.get()[0]
     
            cur.execute("insert into roominfo values (%s,%s,%s)",(var_room_no,self.var_roomtype.get(),self.var_roomno.get()))
            
        else:
            if not ask:
                return
        conn.commit()
        self.fetch_details()
        conn.close()
        messagebox.showinfo("Deleted","Room Booking Deleted",parent=self.root)
             
            
    def fetch_details(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        cur=conn.cursor()
        cur.execute("select * from room where Ref_id=%s",(self.var_ref.get(),))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Room_Details_Table.delete(*self.Room_Details_Table .get_children())
            for i in rows:
                self.Room_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #--------------add data------------------
    def add_room_details(self):
        if self.var_ref.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                cur.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomno.get(),
                                                                            self.var_noOfDays.get(),
                                                                            self.var_totalcost.get()))
                cur.execute("delete from roominfo where Room_No=%s",(self.var_roomno.get(),))
                messagebox.showinfo("Successfull","Room Booked successfully",parent=self.root)
                
                conn.commit()
                self.fetch_details()
                conn.close()
                
                
                            
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Sommething went wrong:{str(es)}",parent=self.root)
        
    
    
    #----------billing button-------------
    def billing_button(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfDays.set((abs(outDate-inDate)).days)
        
        if(self.var_roomtype.get()=="Single"):
            x=float(self.var_noOfDays.get())
            tc="Rs. "+str(x*1000)
            self.var_totalcost.set(tc)
            
        elif(self.var_roomtype.get()=="Double"):
            x=float(self.var_noOfDays.get())
            tc="Rs. "+str(x*3000)
            self.var_totalcost.set(tc)   
            
        elif(self.var_roomtype.get()=="Delux"):
            x=float(self.var_noOfDays.get())
            tc="Rs. "+str(x*5000)
            self.var_totalcost.set(tc)
    
    
    
    def show_available_rooms(self):
        avail_room_table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Available Room Details",font=("Times New Roman",11,"bold"))
        avail_room_table_frame.place(x=900,y=45,height=250,width=250)
        
        
        self.Avail_Room_Details_Table=ttk.Treeview(avail_room_table_frame,column=("Floor No","Room No"))
        self.Avail_Room_Details_Table.heading("Floor No",text="Floor No")
        self.Avail_Room_Details_Table.heading("Room No",text="Room No")
        
        self.Avail_Room_Details_Table["show"]="headings"
        
        
        self.Avail_Room_Details_Table.column("Floor No", width=30)
        self.Avail_Room_Details_Table.column("Room No", width=30)
        
        self.Avail_Room_Details_Table.pack(fill=BOTH,expand=1)
        if self.var_roomtype.get()=="":
            messagebox.showerror("Error","Please select the room type")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel_management")
                cur = conn.cursor()
                cur.execute("SELECT Floor_No, Room_No FROM roominfo WHERE Room_Type = %s AND Room_No NOT IN (SELECT Room_no FROM room)", (self.var_roomtype.get(),))
                rows = cur.fetchall()
                if len(rows) != 0:
                    # Clear previous entries in Avail_Room_Details_Table
                    for item in self.Avail_Room_Details_Table.get_children():
                        self.Avail_Room_Details_Table.delete(item)
                    # Populate Avail_Room_Details_Table with fetched room details
                    for row in rows:
                        self.Avail_Room_Details_Table.insert("", END, values=row)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_contact(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please enter the ref id.")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            query=("select Name from customer where Ref_id=%s")
            value=(self.var_ref.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            if row==None:
                messagebox.showwarning("Error","Invalid ref id.")
            else:
                conn.commit()
                conn.close()
                
                
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE)
                showDataFrame.place(x=470,y=50,width=300,height=180)
            
                lblName=Label(showDataFrame,text="Name: ",font=("Times New Roman",11,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataFrame,text=row,font=("Times New Roman",11,"bold"))
                lbl.place(x=70,y=0)
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                query=("select Phone_no from customer where Ref_id=%s")
                value=(self.var_ref.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                
                lblName=Label(showDataFrame,text="Phone no: ",font=("Times New Roman",11,"bold"))
                lblName.place(x=0,y=30)
                lbl2=Label(showDataFrame,text=row,font=("Times New Roman",11,"bold"))
                lbl2.place(x=70,y=30)
                
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                query=("select Email from customer where Ref_id=%s")
                value=(self.var_ref.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                
                lblName=Label(showDataFrame,text="Email: ",font=("Times New Roman",11,"bold"))
                lblName.place(x=0,y=60)
                lbl3=Label(showDataFrame,text=row,font=("Times New Roman",11,"bold"))
                lbl3.place(x=70,y=60)
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                query=("select Gender from customer where Ref_id=%s")
                value=(self.var_ref.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                
                lblName=Label(showDataFrame,text="Gender: ",font=("Times New Roman",11,"bold"))
                lblName.place(x=0,y=90)
                lbl2=Label(showDataFrame,text=row,font=("Times New Roman",11,"bold"))
                lbl2.place(x=70,y=90)
    

        
        
    def logout(self):
        messagebox.showinfo("Log out","Logged out sucessfully")
        self.root.destroy()
        

        
        
        

        
        
        
if __name__=="__main__":
    main()