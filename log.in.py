from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title('Login system')
        self.root.geometry('1350x700+0+0')
        #images
        self.bg_img=ImageTk.PhotoImage(file="bg.jpg")
        self.user_icon=ImageTk.PhotoImage(file="user.png")
        self.pass_icon=ImageTk.PhotoImage(file="key.png")
        self.logo_icon=ImageTk.PhotoImage(file="logo1.png")
        #=======variables========
        self.usrName=StringVar()
        self.pass_=StringVar()


        bg_lbl=Label(self.root,image=self.bg_img).pack()
        title=Label(self.root,text="LogIn System",font=('times new roman',40,'bold'),bg='yellow',fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        
        Login_frame =Frame(self.root,bg='white')
        Login_frame.place(x=400,y=150)

        logo=Label(Login_frame,image=self.logo_icon,bg='white').grid(row=0,columnspan=2,pady=20)
        username=Label(Login_frame,text='Username',compound=LEFT,image=self.user_icon,font=('times new roman',20,'bold'),bg='white').grid(row=1,column=0,pady=20,padx=10,)
        password=Label(Login_frame,text='Password',compound=LEFT,image=self.pass_icon,font=('times new roman',20,'bold'),bg='white').grid(row=2,column=0,pady=20,padx=10,)

        txtuser=Entry(Login_frame,textvariable=self.usrName,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        txtpass=Entry(Login_frame,textvariable=self.pass_,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        login_btn=Button(Login_frame,text='Login',width=15,command=self.login,font=('times new roman',14,'bold'),bg='blue',fg='white').grid(row=3,column=1,pady=10)
    def login(self):
        if self.usrName.get()=='' or self.pass_.get()=='':
            messagebox.showerror("Error","All fields are required")    
        elif self.usrName.get()=='username' and self.pass_.get()=='password':
            messagebox.showinfo("successful","welcome login success") 
        else:
            messagebox.showerror("Error","Incorrect username or password entry")    
root = Tk()
obj=Login_System(root)
root.mainloop()