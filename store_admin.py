
import tkinter as tk
import csv
from abc import ABC, abstractmethod

from PIL import Image,ImageTk
from nbformat import write
import pandas as pd
from tkinter import messagebox
class StoreDetails:
    #show the store products 
    def  product_option (self):
      self.root2 =tk.Tk()
      self.root2.title("Book Store")
      self.root2.geometry("1199x600+100+50")
      self.root2.resizable(False,False)
      self.bg=ImageTk.PhotoImage(file="image.jpg")
      self.bg_image=tk.Label(self.root2,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
      self.content = tk.StringVar()
      self.entry = tk.Entry(self.root2, textvariable=self.content,font=("Times new roman",15),bg="lightgray")
      self.entry.place(x=150,y=7,width=820,height=30)
    

      self.button = tk.Button(self.root2, text="Add Item",cursor="hand2",height=2,width=20 ,fg="white",bg="#d77337",bd=0,font=("time new roman", 12) , command=self.clicked1)
      self.button.place(x=300 ,y=55)

      self.button_delete = tk.Button(self.root2,text="Delete", command=self.delete2,cursor="hand2",height=2,width=20 ,fg="white",bg="#d77337",bd=0,font=("time new roman", 12) )
      self.button_delete.place(x=500 ,y=55)
            
            
      self.button_delete_selected = tk.Button(self.root2,text="Delete Selected", command=self.delete_selected,cursor="hand2",height=2,width=20 ,fg="white",bg="#d77337",bd=0,font=("time new roman", 12))
      self.button_delete_selected.place(x=700 ,y=55)

      self.title=tk.Label(self.root2,text="Product",width=85,font=("Impact",20,"bold"),fg="white",bg="#d77337").place(y=110)

      self.scrollbar=tk.Scrollbar(self.root2)
      self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

      self.listbox = tk.Listbox(self.root2 ,font=("Calibri", 15),height=15, yscrollcommand=self.scrollbar.set )
      self.listbox.pack(padx=50,pady=155,fill=tk.BOTH,expand=True)
      self.scrollbar.config(command=self.listbox.yview)


      self.bquit = tk.Button(self.root2, text="Quit and save", command=self.quit1,cursor="hand2",height=2,width=20 ,fg="white",bg="#d77337",bd=0,font=("time new roman", 12))
      self.bquit.place(x=490,y=480)
      self.retrievedata1()
      self.root2.mainloop()
    

    def retrievedata1(self):
        #read the save1.csv then append the details in list_data
        self.list_data = []
        try:
           python_csv_file=open('books.csv', 'r')
           python_csv_read=csv.reader(python_csv_file)
           for row in python_csv_read:
             self.listbox.insert(tk.END, row)
             self.list_data.append(row)
        except:
             pass

    def clicked1(self):
        #this function add the product in stocks
        self.selected = self.listbox.get(self.listbox.curselection())
        self.selected3=list(self.selected)
        self.list_data.append(self.selected3)
        self.listbox.insert(tk.END,self.content.get())
    #    self.list_data.append(self.content.get())
        messagebox.showinfo("Successful","ITEM ADD SUCCESSFULLY ")

    def delete2(self):
     #this function delete all the product present in the stock
        self.listbox.delete(0, tk.END)
        self.list_data = []

    def delete_selected(self):
    #this function delete the seleted product in the stocks
            self.selected5 = self.listbox.get(self.listbox.curselection())
            self.listbox.delete(tk.ANCHOR)
            self.list_data.pop(self.list_data.index(self.selected5))
            messagebox.showinfo("Successful","ITEM Deleted SUCCESSFULLY ")
    def quit1(self):

        #    print(self.list_data)
            python_csv_file=open('books.csv', 'w',newline='')
            # python_csv_read=csv.writer(python_csv_file)
        #    for row in self.list_data :
        #        self.python_csv_read.write(row)
        #        print(row)
            write = csv.writer(python_csv_file)
            write.writerows(self.list_data)
            self.root2.destroy()


class Account(ABC):#importing the abstract class module
    #passing abstract class as parameter so that further instance of this class can not be created,
#the reason that we have made trhis class abstracy because we wnant to secure user privacy
  def __init__(self, username1,password1):#this constructor takes the essential credisentials of the user and librarian as password
    self.password1 = password1
    self.username1=username1
  

class StoreAdmin(Account,StoreDetails):#this class inherits from the abstract class Account,so that we can use its attributes
# this class also inherit all attributes from class storeDetails 
    def __init__(self, password1="0987654321",username1='SNEKS'):#we have used method overriding here, and have called the constructor of the account class here
     super().__init__(password1="0987654321", username1='SNEKS')
    #this function display the admin login page
    def store_admin_login(self):      
        self.root1=tk.Tk()
        self.root1.title("Login System")
        self.root1.geometry("1199x600+100+50")
        self.root1.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="image/img.jpg")
        self.bg_image=tk.Label(self.root1,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #===Login Frame===
        self.Frame_login=tk.Frame(self.root1,bg="white")
        self.Frame_login.place(x=350,y=150,height=370,width=500)

        title=tk.Label(self.Frame_login,text="LOGIN PLEASE!",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=tk.Label(self.Frame_login,text="Provide Your Account Information",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        
        lbl_user=tk.Label(self.Frame_login,text="Username:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=tk.Entry(self.Frame_login,font=("Times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=tk.Label(self.Frame_login,text="Password:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=tk.Entry(self.Frame_login,font=("Times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        forget_btn=tk.Button(self.Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=tk.Button(self.Frame_login,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=180,y=320,width=180,height=40)

        self.root1.mainloop()
    def login_function(self):
        #vertify the admin
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields Are Required")

        elif self.txt_pass.get()!=self.password1 or self.txt_user.get()!=self.username1:
            messagebox.showerror("Error","Invalid Username/Password")
        else:
            messagebox.showinfo("WELCOME!",f"WELCOME {self.txt_user.get()}")
            self.admin_page()
    def admin_page(self):
        #show the admin option
        self.Frame_login.destroy()
        self.Frame_login1=tk.Frame(self.root1,bg="white")
        self.Frame_login1.place(x=350,y=150,height=340,width=500)
        tk.Label(self.Frame_login1, text="OPTIONS", width="300", height="4" ,fg="white",bg="#d77337",font=("Bodoni MT Black", 15)).pack()
        login_btn=tk.Button(self.Frame_login1,cursor="hand2",text="Accounts ",fg="white",bg="#d77337",font=("times new roman",20),command=self.user_account).place(x=150,y=150,width=180,height=40)
        login_btn=tk.Button(self.Frame_login1,cursor="hand2",text="Store Details",fg="white",bg="#d77337",font=("times new roman",20),command=self.view_detail).place(x=150,y=200,width=180,height=40)

    def user_account(self):
        #this function display the user accounts  and their id 
        self.Frame_login1.destroy()
        self.Frame_login2=tk.Frame(self.root1,bg="white")
        self.Frame_login2.place(x=250,y=100,height=500,width=700)
        tk.Button(self.Frame_login2, text="Customer History",command=self.show_id,fg="white",bg="#d77337",font=("times new roman",15) ,height="1", width="15").pack(pady=2)
        tk.Label(self.Frame_login2, text="USERNAME  IDS",fg="white",bg="#d77337",font=("times new roman",20),width=100).pack(pady=2)
        self.user_log=open('user_log.csv', 'r')
        self.user_log_re=csv.reader(self.user_log)
        
        for row in self.user_log_re:
            a=row[1].split()
            tk.Label(self.Frame_login2,text=f".{a[0]}\t\t\t.{row[0]}",fg="#d77337",bg="white").pack(pady=1)
      
    def view_detail(self):
        #this function call product_option inherit by store details
        self.root1.destroy()
        self.product_option()
        
        self.root2.mainloop()
        
    def show_id(self):
        self.Frame_login2.destroy()

        self.verify=tk.Frame(self.root1,bg="white")
        self.verify.place(x=350,y=100,height=350,width=500)

        title=tk.Label(self.verify,text="Verification!",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=10)
        desc=tk.Label(self.verify,text="Provide Your Account Information",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=tk.Label(self.verify,text="ID's:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=150)
        self.txt_id=tk.Entry(self.verify,font=("Times new roman",15),bg="lightgray")
        self.txt_id.place(x=90,y=180,width=350,height=35)

        login_btn=tk.Button(self.verify,cursor="hand2",text="Verify",command=self.user_history,fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=250,width=180,height=40)
    
    def user_history(self):
        #this function use pandas library 
        #this function open hist.csv and add the userename or id in list
        self.id=self.txt_id.get()
        if self.id=="":
                messagebox.showerror("Error","No space can be blank")
        else: 
            messagebox.showinfo("Successful","id is correct ")
            self.newid=int(self.id)-1
            df = pd.read_csv('user_history.csv')
            x = df.loc[self.newid,'bookincart'].replace("'",'').replace("[",'').replace("]",'')
            u= df.loc[self.newid,'bookbuy'].replace("'",'').replace("[",'').replace("]",'')
            a=u.split('0,')
            l = x.split('0,')
            new_l = []
            new_2=[]
            for k in a:
                k+="0"
                new_2.append(k)
            a1=new_2[-1]
            if a1 !="":
                e=new_2[-1]
                new_2.pop()
                o=str(e)[:-1]
                new_2.append(o)
            for i in l:
              i += '0'
              new_l.append(i)
          
            t=new_l[-1]
            new_l.pop()
            h=str(t)[:-1]
            new_l.append(h)
            self.car = []
            self.car2=[]
            self.verify.destroy()
            self.Frame1=tk.Frame(self.root1,bg="white")
            self.Frame1.place(x=170,y=0,height=650,width=855)
            title=tk.Label(self.Frame1,text="CART",font=("Impact",25,"bold"),fg="white",bg="#d77337",width=58,height=1).pack()
            self.scrollbar=tk.Scrollbar(self.root1)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.listbox2= tk.Listbox(self.Frame1,font=("Calibri", 15),height=10, yscrollcommand=self.scrollbar.set )
            self.listbox2.pack(fill=tk.BOTH,expand=True)
            self.scrollbar.config(command=self.listbox2.yview)
            title=tk.Label(self.Frame1,text="BUY",font=("Impact",25,"bold"),fg="white",bg="#d77337",width=50,height=1).pack()
            self.scrollbar2=tk.Scrollbar(self.root1)
            self.scrollbar2.pack(side=tk.LEFT, fill=tk.Y)
            self.listbox3= tk.Listbox(self.Frame1,font=("Calibri", 15),height=10, yscrollcommand=self.scrollbar.set )
            self.listbox3.pack(fill=tk.BOTH,expand=True)
            login_btn=tk.Button(self.Frame1,cursor="hand2",text="quit",fg="white",bg="#d77337",font=("times new roman",20),command=self.root1.destroy).place(x=350,y=500)
            for i in new_l:
                z = str(i).split(',')
                self.car.append(z)
            for i in new_2:
                c= str(i).split(',')
                self.car2.append(c)
            for j in self.car:
               self.listbox2.insert(tk.END,j )
            for q in self.car2:
                self.listbox3.insert(tk.END,q)

# store=StoreAdmin()
# store.store_admin_login()