from tkinter import*
from PIL import Image,ImageTk
from customer import*
from roomdetails import room_details
from availableroom import room_info
import PIL.Image

class HotelManagementSys:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")
                
        #========title========
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",justify="center",font=("Times New Roman",30,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1500,height=40)

        #------------frame----------- 
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=40,width=1500,height=760)
        
        #--------options heading---------
        lbl_opt=Label(main_frame,text="OPTIONS",justify="center",font=("Times New Roman",20,"bold"),bg="black",fg="gold")
        lbl_opt.place(x=0,y=0,width=200,height=25)
        
        #---------options frame----------
        opt_frame=Frame(main_frame,bd=4,relief=RIDGE)
        opt_frame.place(x=0,y=25,width=200,height=200)
        
        #-------------options-------------
        cust_frame=Button(opt_frame,text="CUSTOMER",justify="center",command=self.cust_details,font=("Times New Roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_frame.place(x=0,y=0,width=200,height=50)
        

        cust_frame=Button(opt_frame,text="BOOKING",justify="center",command=self.roomdetails,font=("Times New Roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_frame.place(x=0,y=50,width=200,height=50)
        
        cust_frame=Button(opt_frame,text="ROOM DETAILS",justify="center",command=self.room_info,font=("Times New Roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_frame.place(x=0,y=100,width=200,height=50)
        
        cust_frame=Button(opt_frame,text="LOGOUT",justify="center",command=self.logout,font=("Times New Roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_frame.place(x=0,y=150,width=200,height=50)
        
        
        
        #=--------------background img-----------
        img1=PIL.Image.open(r"C:\Users\Mukul\Desktop\Hotel Management Project\tajhotel.jpg")
        img1=img1.resize((1295,750),PIL.Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(main_frame,image=self.photoimg1,bd=4,relief=RIDGE)
        lbl_img1.place(x=200,y=0,width=1295,height=750)
        
        
        img2=PIL.Image.open(r"C:\Users\Mukul\Desktop\Hotel Management Project\tajlogo.jpg")
        img2=img2.resize((200,560),PIL.Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(main_frame,image=self.photoimg2,bd=4,relief=RIDGE,width=190,height=550)
        lbl_img2.place(x=0,y=230)
        
    #---------adding cust details------------
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.runFunction=cust_window(self.new_window)
    
    #---------------adding room details-------
    def roomdetails(self):
        self.new_window=Toplevel(self.root)
        self.runFunction=room_details(self.new_window)
   #-------------room info----------------
    def room_info(self):
        self.new_window=Toplevel(self.root)
        self.runFunction=room_info(self.new_window)
   
    def logout(self):
        messagebox.showinfo("Log out","Logged out sucessfully")
        self.root.destroy()
       
    
        
        
if __name__=="__main__":
    root=Tk();
    obj=HotelManagementSys(root)
    root.mainloop()