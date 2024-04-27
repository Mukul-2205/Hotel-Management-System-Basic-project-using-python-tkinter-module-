from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_info:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1290x740+205+78")
        
        
        self.var_floor=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomno=StringVar()
        
        #========title========
        lbl_title=Label(self.root,text="ROOM AVAILABILITY",justify="center",font=("Times New Roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1300,height=40)
        
        #-----------label frame-----------
        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM DETAILS",font=("Times New Roman",10,"bold"))
        labelFrameLeft.place(x=0,y=40,width=500,height=350)
        
        #-----------parameters------------
        lbl_floor=Label(labelFrameLeft,text="Floor No.: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_floor.grid(row=0,column=0,sticky=W)
        entry_floor=ttk.Entry(labelFrameLeft,width=18,textvariable=self.var_floor,font=("Times New Roman",11,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W,padx=7)
        
        lbl_roomtype=Label(labelFrameLeft,text="Room Type: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_roomtype.grid(row=1,column=0,sticky=W)
        entry_roomtype=ttk.Combobox(labelFrameLeft,width=18,textvariable=self.var_roomtype,font=("Times New Roman",11,"bold"),state="readonly")
        entry_roomtype["values"]=("Single","Double","Delux")
        entry_roomtype.grid(row=1,column=1,sticky=W,padx=7)
        
        lbl_roomno=Label(labelFrameLeft,text="Room No.: ",font=("Times New Roman",13,"bold"),pady=5)
        lbl_roomno.grid(row=2,column=0,sticky=W)
        entry_roomno=ttk.Entry(labelFrameLeft,width=18,textvariable=self.var_roomno,font=("Times New Roman",11,"bold"))
        entry_roomno.grid(row=2,column=1,sticky=W,padx=7)
        
        #------------button frame----------------
        btn_frame=Frame(labelFrameLeft,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=270,width=500,height=50)
        
        #---------------add buttons-------------
        add_btn=Button(btn_frame,text="ADD",justify="center",command=self.add_room_info,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        add_btn.place(x=0,y=0,width=110,height=45)        
        
        update_btn=Button(btn_frame,text="UPDATE",justify="center",command=self.update_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        update_btn.place(x=120,y=0,width=110,height=45)        
        
        delete_btn=Button(btn_frame,text="DELETE",justify="center",command=self.delete_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        delete_btn.place(x=240,y=0,width=110,height=45)        
        
        reset_btn=Button(btn_frame,text="RESET",justify="center",command=self.reset_details,font=("Times New Roman",11,"bold"),bg="black",fg="gold",cursor="hand2")
        reset_btn.place(x=360,y=0,width=110,height=45)    
        
        #----------------tabel frame-------------
        table_frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="Room Information",font=("Times New Roman",11,"bold"))
        table_frame.place(x=550,y=40,height=350,width=550)
         
        #---------Show Room Info Table---------------
        room_info_frame=Frame(table_frame,bd=3,relief=RIDGE)
        room_info_frame.place(x=0,y=0,width=540,height=330)
        
        self.Room_Info_Table=ttk.Treeview(room_info_frame,column=("Floor No","Room Type","Room No."))
        
        self.Room_Info_Table.heading("Floor No",text="Floor No")
        self.Room_Info_Table.heading("Room Type",text="Room Type")
        self.Room_Info_Table.heading("Room No.",text="Room No.")
        
        
        self.Room_Info_Table["show"]="headings"
        
        self.Room_Info_Table.column("Floor No", width=70)
        self.Room_Info_Table.column("Room Type", width=70)
        self.Room_Info_Table.column("Room No.", width=70)
       
        self.Room_Info_Table.pack(fill=BOTH,expand=1)
        self.Room_Info_Table.bind("<ButtonRelease-1>",self.see_details)
        self.fetch_details()

    def add_room_info(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                cur=conn.cursor()
                cur.execute("insert into roominfo values(%s,%s,%s)",(self.var_floor.get(),
                                                                 self.var_roomtype.get(),
                                                                 self.var_roomno.get()))
                            
                messagebox.showinfo("Successfull","Room Added successfully",parent=self.root)
                
                conn.commit()
                self.fetch_details()
                conn.close()
                
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Sommething went wrong:{str(es)}",parent=self.root)
                
    def fetch_details(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        cur=conn.cursor()
        cur.execute("select * from roominfo")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Room_Info_Table.delete(*self.Room_Info_Table.get_children())
            for i in rows:
                self.Room_Info_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def see_details(self,event=""):
        cursor_row=self.Room_Info_Table.focus()
        content=self.Room_Info_Table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomtype.set(row[1])
        self.var_roomno.set(row[2])

    #----------------update------------------
    def update_details(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Warning","Pleasy specify floor number")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            cur=conn.cursor()
            cur.execute("update roominfo set Room_Type=%s , Room_No=%s where Floor_No=%s",(self.var_roomtype.get(),self.var_roomno.get(),self.var_floor.get()))
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
            query="delete from roominfo where Room_No=%s"
            value=(self.var_roomno.get(),)
            cur.execute(query,value)
            
            
            
        else:
            if not ask:
                return
        conn.commit()
        self.fetch_details()
        conn.close()
        messagebox.showinfo("Deleted","Room Info Deleted",parent=self.root)
        
        
    #------------reset-----------------
    def reset_details(self):
        self.var_floor.set("")
        self.var_roomtype.set("")
        self.var_roomno.set("")
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=room_info(root)
    root.mainloop()