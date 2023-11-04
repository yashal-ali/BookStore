
from turtle import bgcolor
import tkinter as tk # used to import all the functionality from the module tkinter
from PIL import Image,ImageTk
from turtle import bgcolor
from tkinter import messagebox
from store_admin import *
from customer import User
class Id:
    def idd(self):
          # this function is used to increment the id of the user
        with open('user_log.csv', 'r') as f:  # this line is used to open the file in read mode
            x = f.readlines()  # this line return the list in a string
            if '\n' in x:  # used to check the last id that was assigned so that the next user is given incremented id
                x.remove('\n')
                print(x)
            if x == []:  # sees if no id has been assigned yet so it assumes the id as 0
                self.new_id = 0
            else:
                self.new_id = (x[-1][0])  # gets the last id assigned
class AboutUs:
    def __init__(self):#display the about us of shop
        self.root_1 =tk.Toplevel()
        self.root_1.title("List App")
        self.root_1.geometry("1199x600+100+50")
        self.root_1.resizable(False,False)
        self.root_1.title("The Nerdy Spot")
        self.bg2=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image_1=tk.Label(self.root_1,image=self.bg2).place(x=0,y=0,relwidth=1,relheight=1)
        
        #=== About us Frame===
        self.Frame_aboutus__=tk.Frame(self.root_1,bg="white")
        self.Frame_aboutus__.place(x=350,y=150,height=340,width=500)
        tk.Label(self.Frame_aboutus__,text="The Books  Spot",font=("Impact",35,"bold"),fg="white",bg="#d77337",width=23 ,height=1).place(x=0,y=0)  

        tk.Label(self.Frame_aboutus__, text="A perfect place for all biblophiles.\nWe have a wide and unlimited collection of books\n Delivering amazing books to your\ndoorstep at your convenience 24/7 nation wide\nFor futher queries ,call us at \n 021-87607284\nOr emailus at:\nsneks@bookspot.pk",font=("Impact",15),bg="white",fg="#d77337").place(x=30,y=80)
        self.root_1.mainloop()


class main_screen(StoreAdmin,User):
    id = 0
   
    def __init__(self, id=0):
        super().__init__() 
        i = Id()  # making i an instance of ID ,composition is used here
        i.idd()  # defining a function with in a function and then calling it to check the id
        main_screen.id = int(i.new_id)  # sets the id as the last id assigned
        # main_screen.id = main_screen.new_id  
        self.root = tk.Tk()
        self.root.title("Book Store")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.root.title("The Book Spot")
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image=tk.Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #===main screen frame===
        self.Frame_login__=tk.Frame(self.root,bg="white")
        self.Frame_login__.place(x=350,y=150,height=340,width=500)
        tk.Label(self.Frame_login__, text="The Books  Spot",font=("Impact",35,"bold"),fg="white",bg="#d77337",width=23 ,height=1).place(x=0,y=0)  
        tk.Button(self.Frame_login__,cursor="hand2",text="ADMIN",fg="white",bg="#d77337",command=lambda:[self.root.destroy (),self.store_admin_login()],font=("times new roman",20)).place(x=150,y=160,width=180,height=40)
        tk.Button(self.Frame_login__,cursor="hand2",text="CUSTOMER",command=self.login,fg="white",bg="#d77337",font=("times new roman",20)).place(x=150,y=210,width=180,height=40)
        tk.Button(self.Frame_login__,cursor="hand2",text="ABOUT US",fg="white",bg="#d77337",font=("times new roman",20),command=AboutUs).place(x=150,y=110,width=180,height=40)

        self.root.mainloop()  # an infinite loop to run the gui till called off

    # creating a main screen after the login/sign up that asks the user to login or register

        
        
    def login(self):
        #this function display the login screen
        self.root.destroy()
        self.root1 = tk.Tk()
        self.root1.title("Book Store")
        self.root1.geometry("1199x600+100+50")
        self.root1.resizable(False,False)
        self.root1.title("The Book Spot")
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image=tk.Label(self.root1,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.Frame_login__3=tk.Frame(self.root1,bg="white")
        self.Frame_login__3.place(x=350,y=100,height=450,width=500)

        title=tk.Label(self.Frame_login__3,text="LOGIN PLEASE!",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=5)
        desc=tk.Label(self.Frame_login__3,text="Provide Your Account Information",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=80)

        lbl_user=tk.Label(self.Frame_login__3,text="ID's:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=130)
        self.txt_id=tk.Entry(self.Frame_login__3,font=("Times new roman",15),bg="lightgray")
        self.txt_id.place(x=90,y=160,width=350,height=35)


        lbl_user=tk.Label(self.Frame_login__3,text="Username:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=200)
        self.txt_user=tk.Entry(self.Frame_login__3,font=("Times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=230,width=350,height=35)

        lbl_pass=tk.Label(self.Frame_login__3,text="Password:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=270)
        self.txt_pass=tk.Entry(self.Frame_login__3,font=("Times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=300,width=350,height=35)
        
        login_btn=tk.Button(self.Frame_login__3,cursor="hand2",text="Login",command=self.login_verify,fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=400,width=180,height=40)

        signup_btn=tk.Button(self.Frame_login__3,cursor="hand2",text="Sign Up",command=self.sign_up,fg="white",bg="#d77337",font=("times new roman",20)).place(x=280,y=400,width=180,height=40)
        self.root1.mainloop()
    
    def sign_up(self):
        #this function is used to display the signup page to register the user
        self.Frame_login__3.destroy()
        self.Frame_signup__4=tk.Frame(self.root1,bg="white")
        self.Frame_signup__4.place(x=300,y=150,height=400,width=600)
        
        title=tk.Label(self.Frame_signup__4,text="SIGNUP PLEASE!",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=tk.Label(self.Frame_signup__4,text="Provide Your Credentials",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        new_user=tk.Label(self.Frame_signup__4,text="Username:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=tk.Entry(self.Frame_signup__4,font=("Times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        new_pass=tk.Label(self.Frame_signup__4,text="Password:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_newpass=tk.Entry(self.Frame_signup__4,font=("Times new roman",15),bg="lightgray")
        self.txt_newpass.place(x=90,y=240,width=350,height=35)

        signup_new_btn=tk.Button(self.Frame_signup__4,command=self.register_user,cursor="hand2",text="Signup",fg="white",bg="#d77337",font=("times new roman",20)).place(x=170,y=300,width=180,height=40)


    def login_sucess(self):
        #this function used to display the messagre if user login successfully!
        messagebox.showinfo("Login success","Login Success")
        self.root1.destroy()
        self.customer_option()

    def user_not_found(self):  # telling the user if the entered password or id is not found
        messagebox.showerror("Error","no such user found")

    def login_verify(self):  # verifing the password and username
        username1 = self.txt_user.get()
        password1 = self.txt_pass.get()
        id1 = self.txt_id.get()  # gets the id of the user
        # self.txt_user.delete(0, tk.END)
        # self.txt_pass.delete(0, tk.END)
        # self.txt_id.delete(0, tk.END)

        with open('user_log.csv', 'r') as f:  # opening the file of user_login
            value = f.read()  # reading it
            # this line of the code will run if the id,password and username are correct
            if (id1+','+username1+' '+password1)in value:
                self.login_sucess()  # calling the login success fuction to display the screen
            else:  # if user is not found than we call the user not found fuction to display it on the screen
                self.user_not_found()


    def register_user(self): 
       #this function is used to register the user
        self.username_info = self.txt_user.get()
        self.password_info = self.txt_newpass.get()
        main_screen.id += 1
        self.txt_user.delete(0, tk.END)
        self.txt_newpass.delete(0, tk.END)
        if self.username_info=="" and self.password_info=="":
            messagebox.showerror("Error","No space can be blank")
        else: 
            messagebox.showinfo("Successful","Username/Password saved")
        # this line of code is used to open the user_login file
            file = open('user_log.csv', "a+")
        # it appends all the info entered by the user in the user_login file
            file.write(str(main_screen.id)+','+self.username_info +
                   ' ' + self.password_info+','+'\n')
            file.close()
            tk.Label(
              self.Frame_signup__4, text=f'Your id is {main_screen.id} bring it when you comeback',font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=340) 
            self.again_open_window()
    def again_open_window(self):
        messagebox.showinfo("registration ","Successfully!!")
        self.root1.destroy()
        main_screen()

main_screen()
