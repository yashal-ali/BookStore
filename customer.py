import csv
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import Tk, messagebox
import pandas as pd
class User:
      

  def customer_option (self):
      #this function is  used to display the  user/customer option 
      self.root2 = tk.Tk()
      self.root2.title("List App")
      self.root2.geometry("1199x600+100+50")
      self.root2.resizable(False,False)
      self.bg=ImageTk.PhotoImage(file="image.jpg")
      self.bg_image=tk.Label(self.root2,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
      self.content = tk.StringVar()
      self.Frame=tk.Frame(self.root2,bg="white")
      self.Frame.place(x=350,y=150,height=350,width=450)
      
      title=tk.Label(self.Frame,text="BOOK STORE",font=("Impact",35,"bold"),fg="white",bg="#d77337",width=20,height=2).place(x=0,y=0)

      login_btn5=tk.Button(self.Frame,cursor="hand2",text="Products",fg="white",bg="#d77337",command=lambda:[self.root2.destroy(),self.products()],font=("times new roman",20)).place(x=150,y=170,width=180,height=40)

      login_btn6=tk.Button(self.Frame,cursor="hand2",command=lambda:[self.verify1()],text="Cart",fg="white",bg="#d77337",font=("times new roman",20)).place(x=150,y=220,width=180,height=40)

      self.root2.mainloop()  

  def products(self):
      #this function is used to display the product option
      self.root3 = tk.Tk()
      self.root3.title("Book Store")
      self.root3.geometry("1299x690+100+50")
      self.root3.resizable(False,False)
      self.bg=ImageTk.PhotoImage(file="image.jpg")
      self.bg_image=tk.Label(self.root3,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
      self.Frame1=tk.Frame(self.root3,bg="white")
      self.Frame1.place(x=170,y=0,height=650,width=855)
      title=tk.Label(self.Frame1,text="PRODUCT",font=("Impact",35,"bold"),fg="white",bg="#d77337",width=38,height=1).place(x=0,y=0)

      self.scrollbar=tk.Scrollbar(self.root3)
      self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

      self.listbox = tk.Listbox(self.Frame1,font=("Calibri", 15),height=10, yscrollcommand=self.scrollbar.set )
      self.listbox.pack(pady=60,fill=tk.BOTH,expand=True)
      self.scrollbar.config(command=self.listbox.yview)
      login_btn4=tk.Button(self.Frame1,command=lambda:[self.verify1()],cursor="hand2",text="View Cart",fg="white",bg="#d77337",font=("times new roman",20)).place(x=420,y=570,width=180,height=40)
      new_pass=tk.Label(self.Frame1,text="id",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=220,y=500)
      self.given_id=tk.Entry(self.Frame1,font=("Times new roman",15),bg="lightgray")
      self.given_id.place(x=220,y=530,width=350,height=35)
      login_btn3=tk.Button(self.Frame1,cursor="hand2",text="Add Cart",fg="white",bg="#d77337",font=("times new roman",20),command=lambda:[self.clicked()]).place(x=220,y=570,width=180,height=40)
      self.list_data = [] #add product from csv file to list 
      self.add_cart=[] 
      self.retrievedata1()
      self.root3.mainloop()

   
  def retrievedata1(self):
      #this function use pandas library ,read file then display  user product
         try:
          df = pd.read_csv('books.csv')
          df = df.reset_index()
          for index, row in df.iterrows():
             
            self.listbox.insert(tk.END,  (row['BOOK'], row['AUTHOR'], row['PRICE']))
            self.list_data.append( (row['BOOK'], row['AUTHOR'], row['PRICE']))
          print(self.list_data)
          print(df)
         except:
            pass

        

          
  def clicked(self):
      #this function vertify the id and then add the product in user cart
      if self.given_id.get()=="":
            messagebox.showerror("Error","No space can be blank")
      
      else: 
            self.selected = self.listbox.get(self.listbox.curselection())
            self.selected3=list(self.selected)
            self.add_cart.append(self.selected3)
            messagebox.showinfo("","item add successfully")
            self.view_id()
       
  def verify1(self):
      #this frame verify the user id and then call the function of view cart
        # self.root3.destroy()
        self.Frame.destroy()
        # self.root4 = tk.Tk()
        # self.root4.title("List App")
        # self.root4.geometry("1199x600+100+50")
        # self.root4.resizable(False,False)
        # self.root4.title("The Nerdy Spot")
        # self.bg=ImageTk.PhotoImage(file="image.jpg")
        # self.bg_image=tk.Label(self.root4,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.verify=tk.Frame(self.root2,bg="white")
        self.verify.place(x=350,y=100,height=450,width=500)

        title=tk.Label(self.verify,text="Verification!",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=10)
        desc=tk.Label(self.verify,text="Provide Your Account Information",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user=tk.Label(self.verify,text="ID's:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=150)
        self.txt_id=tk.Entry(self.verify,font=("Times new roman",15),bg="lightgray")
        self.txt_id.place(x=90,y=180,width=350,height=35)

        login_btn=tk.Button(self.verify,cursor="hand2",text="Verify",command=lambda:[self.view_cart()],fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=250,width=180,height=40)
  def view_cart(self):
      #if id present in the hist.csv display the user cart
        self.id=int(self.txt_id.get())
        self.newid=self.id-1
        df = pd.read_csv('user_history.csv')
        x = df.loc[self.newid,'bookincart'].replace("'",'').replace("[",'').replace("]",'')
        l = x.split('0,')
        new_l = []
        for i in l:
          i += '0'
          new_l.append(i)
        p=new_l[-1]
        para=str(p)[:-1]
        new_l.pop()
        new_l.append(para)
        self.car = []
    
      #   print(self.car)
        self.root2.destroy()
        self.root5 = tk.Tk()
        self.root5.title("List App")
        self.root5.geometry("1299x690+100+50")
        self.root5.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image=tk.Label(self.root5,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.Frame1=tk.Frame(self.root5,bg="white")
        self.Frame1.place(x=170,y=0,height=650,width=855)
        self.Frame2=tk.Frame(self.root5,bg="white")
        self.Frame2.place(x=170,y=15,height=600,width=855)
        title=tk.Label(self.Frame2,text="VIEW CART",font=("Impact",35,"bold"),fg="white",bg="#d77337",width=38,height=1).place(x=0,y=0)
        
        self.scrollbar=tk.Scrollbar(self.root5)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox2= tk.Listbox(self.Frame2,font=("Calibri", 15),height=15, yscrollcommand=self.scrollbar.set )
        self.listbox2.pack(pady=60,fill=tk.BOTH,expand=True)
        self.scrollbar.config(command=self.listbox2.yview)
        lbl_user=tk.Label(self.Frame2,text="ID's:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=220,y=470)
        self.txt_id2=tk.Entry(self.Frame2,font=("Times new roman",15),bg="lightgray")
        self.txt_id2.place(x=220,y=500,width=180,height=40)
        login_btn1=tk.Button(self.Frame2,cursor="hand2",text="Remove Item",fg="white",bg="#d77337",font=("times new roman",20),command=self.delete_selected2).place(x=450,y=550,width=180,height=40)

        login_btn2=tk.Button(self.Frame2,cursor="hand2",text="Check Out",fg="white",bg="#d77337",font=("times new roman",20),command=lambda:[self.checkout()]).place(x=450,y=500,width=180,height=40)

  
        
        for i in new_l:
                z = i.split(',')
                self.car.append(z)
        for j in self.car:
            self.listbox2.insert(tk.END,j )

        self.root5.mainloop()
     
  def checkout(self):
      #this fuunction generate the bill 
        self.root5.destroy()
        self.root6=tk.Tk()
        self.root6.title("Checkout")
        self.root6.geometry("800x1000+100+50")
        self.root6.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image=tk.Label(self.root6,image=self.bg).place(x=-0,y=0,relwidth=1,relheight=1)

         #===Checkout Frame===
        self.Frame_checkout=tk.Frame(self.root6,bg="white")
        self.Frame_checkout.place(x=30,y=65,height=550,width=700)

        title1=tk.Label(self.Frame_checkout,text="Your Bill",font=("Impact",35),fg="black",bg="white").pack()
        self.newid=self.id-1
        df = pd.read_csv('user_history.csv')
        x = df.loc[self.newid,'bookincart'].replace("'",'').replace("[",'').replace("]",'')
        l = x.split('0,')
        new_l = []
        for i in l:
          i += '0'
          new_l.append(i)
        r=new_l[-1]
        rt=str(r)[:-1]
        new_l.pop()
        new_l.append(rt)
        self.car = []
        for i in new_l:
              z = i.split(',')
              self.car.append(z) 
        for j in self.car:   
          tk.Label(self.Frame_checkout,text=j,font=("Goudy old style",15,"bold"),fg="gray",bg="white").pack()
        self.bill=0
      
        for i in range (len(self.car)):
              print(self.car)
              ab=self.car[i][2]
              self.c=int(ab)
              self.bill=self.bill+self.c
        desc1=tk.Label(self.Frame_checkout,text="Your total bill :{}$".format(self.bill),font=("Goudy old style",15),fg="black",bg="white").pack()
        df = pd.read_csv('user_history.csv')
        w =str(self.car) 
        df.loc[self.newid,'bookbuy'] = w
        df.to_csv('user_history.csv', index=False)
        login=tk.Button(self.Frame2,cursor="hand2",text="QUIT",fg="white",bg="#d77337",font=("times new roman",20),command=self.root1.destroy).place(x=450,y=500,width=180,height=40)

   
  def delete_selected2(self): 
      #this function is used to remove the products in user cart  
      if  self.txt_id2.get()=="":
            messagebox.showerror("Error","No space can be blank")
      
        
      self.selected = self.listbox2.get(self.listbox2.curselection())
      print(self.selected)
      self.selected3=list(self.selected)
      self.car.pop(self.car.index(self.selected3))
      self.listbox2.delete(tk.ANCHOR)
      self.id=int(self.txt_id2.get())
      self.newid=self.id-1
      df = pd.read_csv('user_history.csv')
      w =str(self.car)
      df.loc[self.newid,'bookincart'] = w
      df.to_csv('user_history.csv', index=False)
      messagebox.showinfo("Successful","ITEM REMOVE  SUCCESSFULLY ")
    
      
  def view_id(self):
      #check the id if id is in the history file then display the  user cart ()
        if self.given_id.get()=="":
            messagebox.showerror("Error","No space can be blank")
        self.id=int(self.given_id.get())
        self.newid=self.id-1
        df = pd.read_csv('user_history.csv')
        x = df.loc[self.newid,'bookincart']
        y = x.strip('"')
        z = y.strip('[')
        w = z.strip(']')
        w =str(self.add_cart) + "," + w
        df.loc[self.newid,'bookincart'] = w
        df.to_csv('user_history.csv', index=False)
        self.root3.mainloop()
# us=User()
# us.products()