from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import mysql.connector

class login:

    def __init__(self):

        self.conn=mysql.connector.connect(host='localhost', user='root', password='',database='tinder')
        self.mycursor=self.conn.cursor()
        self.root=Tk()

        self.img = ImageTk.PhotoImage(Image.open('tind.jpg')) #image_source: https://is2-ssl.mzstatic.com/image/thumb/Purple115/v4/60/92/6b/60926b25-57e3-889c-1195-57390ae3739c/source/512x512bb.jpg
        self.panel= Label(self.root, image=self.img)
        self.panel.pack()

        self.root.title('login')

        self.root.minsize(800,720)
        self.root.maxsize(800,720)

        self.email_label=Label(self.root, text='Enter email',bg="crimson",fg="white")
        self.email_label.pack(fill=X)
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack()

        self.password_label=Label(self.root, text='Enter password',bg="crimson",fg="white")
        self.password_label.pack(fill=X)
        self.password_input=Entry(self.root,show="*",width=50)
        self.password_input.pack()

        self.button=Button(self.root, text='LOGIN',font="Bold",bg="deep pink",fg="white",command=lambda :self.perform())
        self.button.pack(fill=X)

        self.result=Label(self.root, text='', fg='red')
        self.result.pack()

        self.button1 = Button(self.root, text='Not a member? Create an account',font="bold",bg="deep pink" ,fg="white",command=lambda: self.register())
        self.button1.pack()

        self.root.mainloop()

    def perform(self):

        email=self.email_input.get()
        password=self.password_input.get()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
        user_list=self.mycursor.fetchall()
        c=0
        for i in user_list:
                c = c + 1
                current_user = i

        if ((c >0) and (len(email)!=0) and (len(password)!=0)):
            tkinter.messagebox.showinfo("Welcome","Login successful")

            self.current_user_id = current_user[0]

            self.user_menu()
        else:
            tkinter.messagebox.showerror("Error", "please fill the required fields correctly")

    def register(self):

        self.root1=Toplevel()
        self.root1.title("Register")
        self.root1.maxsize(800,800)
        self.root1.minsize(800,800)
        self.img2 = ImageTk.PhotoImage(Image.open('index.png'))
        self.panel2 = Label(self.root1, image=self.img2)
        self.panel2.pack()

        self.a= Label(self.root1,text="NAME")
        self.a.pack()
        self.a_input=Entry(self.root1,width="30")
        self.a_input.pack()

        self.b = Label(self.root1, text="EMAIL")
        self.b.pack()
        self.b_input=Entry(self.root1,wdth=30)
        self.b_input.pack()

        self.c = Label(self.root1, text="PASSWORD")
        self.c.pack()
        self.c_input=Entry(self.root1,show="*",width=30)
        self.c_input.pack()

        self.d = Label(self.root1, text="GENDER: Male/Female")
        self.d.pack()
        self.d_input=Entry(self.root1,width=30)
        self.d_input.pack()

        self.e = Label(self.root1, text="AGE")
        self.e.pack()
        self.e_input=Entry(self.root1,width="30")
        self.e_input.pack()

        self.f = Label(self.root1, text="CITY")
        self.f.pack()
        self.f_input=Entry(self.root1,width=30)
        self.f_input.pack()

        self.button2 = Button(self.root1, text='CREATE', command=lambda: self.func())
        self.button2.pack()
        self.result1=Label(self.root1, text=" ")
        self.result1.pack()

        self.root1.mainloop()

    def func(self):
        error=0;
        p = self.a_input.get()
        q = self.b_input.get()
        if ('@' in q):
            self.mycursor.execute('''SELECT * FROM `users` WHERE `email` LIKE '{}' '''.format(q))
            email_list = self.mycursor.fetchall()
            for i in email_list:
                if (q == i[2]):
                    error="An account has already been created in this email id ..pls register again with another mail id"
        else:
             error="Invalid email id"
        r = self.c_input.get()
        if (len(r) > 4):
            self.label14=Label(self.root1,text='✔').pack()
        else:
            error="MUST BE A STRONG PASSWORD(HINT:- MAKE SURE PASSWORD LENGTH IS GREATER THAN 4,PLEASE ENTER PASSWORD AGAIN"
        s = self.d_input.get()
        t = self.e_input.get()
        u = self.f_input.get()
        if error==0:
            self.mycursor.execute("""INSERT INTO `users` (`User-id`,`name`,`email`,`password`,`gender`,`age`,`city`)VALUES(NULL,'{}','{}','{}','{}','{}','{}')""".format(p, q, r, s, t, u))
            self.conn.commit()
            self.result1.configure(text="success")
            self.btn6=Button(self.root1,text="<- GO to login page",command=lambda: self.perform()).pack()
            self.root1.destroy()
        else:
            self.result1.configure(text="ERROR!  "+error)

    def user_menu(self):

        self.root2=Toplevel()
        self.root2.minsize(720,1360)
        self.root2.maxsize(720,1360)
        self.root2.title("TINDER")
        self.img1= ImageTk.PhotoImage(Image.open('t.jpg'))
        self.panel1 = Label(self.root2,image=self.img1)
        self.panel1.pack()

        self.info_label=Label(self.root2,font="bold",text="How would you like to proceed?",bg="blue",fg="white")
        self.info_label.pack(fill=X)
        self.btn1=Button(self.root2,font="bold",text="VIEW ALL USERS",fg="white",bg="crimson",command=lambda:self.view_users())
        self.btn1.pack(fill=X)
        self.btn2 = Button(self.root2,font="bold", text="VIEW PROPOSALS",fg="white",bg="crimson",command=lambda:self.view_proposals())
        self.btn2.pack(fill=X)
        self.btn3 = Button(self.root2,font="bold" ,text="VIEW ALL REQUESTS",fg="white",bg="crimson",command=lambda:self.view_requests())
        self.btn3.pack(fill=X)
        self.btn4 = Button(self.root2,font="bold", text="VIEW ALL MATCHES",fg="white",bg="crimson",command=lambda:self.view_matches())
        self.btn4.pack(fill=X)
        self.btn5 = Button(self.root2,font="bold", text="LOGOUT",fg="white",bg="crimson",command=lambda:self.logout())
        self.btn5.pack(fill=X)

    def view_users(self,i=0):
        self.root3=Tk()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `User-id` NOT LIKE '{}' AND `User-id` NOT IN(SELECT `juliet-id` FROM `proposals` WHERE `romeo-id` LIKE '{}')""".format(self.current_user_id, self.current_user_id))
        all_users_list = self.mycursor.fetchall()
        self.disp= Frame(self.root3)
        self.disp.pack()
        if i < len(all_users_list):
            users = all_users_list[i]
            info = """Name: {} \nGender: {} \nAge: {} \nCity: {}""".format(users[1], users[4], users[5], users[6])
            Label(self.disp, text=info).pack()
            Button(self.root3, font="italic", text="Propose",command=lambda: (self.propose(users[0],i+1),self.root3.quit())).pack()
            Button(self.root3, font ="italic", text= "Reject", command=lambda: self.view_users(i+1)).pack()
        self.root3.mainloop()

    def propose(self,juliet_id,romeo_id):
        self.mycursor.execute("""INSERT INTO `proposals` (`id`, `romeo-id`, `juliet-id`) VALUES(NULL, '{}','{}')""".format(self.current_user_id,juliet_id))
        self.conn.commit()
        tkinter.messagebox.showinfo("REQUEST SEND!")
        self.view_users(romeo_id)

    def view_proposals(self):
        self.root4=Tk()
        self.label6=Label(self.root4,text="The users whom you have proposed ",fg="white",bg="red",font="bold").pack()
        self.mycursor.execute("""SELECT u.`name`, u.`gender`,u.`city`,u.`age` FROM `proposals` p JOIN `users` u ON p.`juliet-id` = u.`User-id` WHERE p.`romeo-id` LIKE '{}'""".format(self.current_user_id))
        proposed_user_list = self.mycursor.fetchall()
        for i in proposed_user_list:
            users = '  ||  '
            users = users.join(str(x) for x in i)
            Label(self.root4, text=users).pack()
        self.root4.mainloop()

    def view_requests(self):
        self.root5=Tk()
        self.label8=Label(self.root5,text="YOUR REQUESTS ARE ").pack()
        self.mycursor.execute("""SELECT u.`name`, u.`gender`,u.`city`,u.`age` FROM `proposals` p JOIN `users` u ON p.`romeo-id` = u.`User-id`  WHERE p.`juliet-id` LIKE '{}'""".format(self.current_user_id))
        requested_user_list = self.mycursor.fetchall()
        for i in requested_user_list:
            users = '  ||  '
            users = users.join(str(x) for x in i)
            Label(self.root5, text=users).pack()
        self.root5.mainloop()

    def view_matches(self):
        self.root6=Tk()
        self.label11=Label(self.root6,text="SUCCESSFUL MATCHES! ").pack()
        self.mycursor.execute("""SELECT `name`,`gender`,`age`,`city` FROM `users` WHERE `User-id` IN (SELECT `juliet-id` FROM `proposals` WHERE `romeo-id` LIKE '{}' AND `juliet-id` IN (SELECT `romeo-id` FROM `proposals` WHERE `juliet-id` LIKE '{}'))""".format(self.current_user_id, self.current_user_id))
        matched_user = self.mycursor.fetchall()
        for i in matched_user:
            users = '  ||  '
            users = users.join(str(x) for x in i)
            Label(self.root6, text=users).pack()
        self.root6.mainloop()

    def logout(self):
            self.root7=Tk()
            self.label15=Label(self.root7,text="Are you sure you want to logout?",fg="blue" ).pack()
            self.button_out= Button(self.root7,text="YES",command=lambda:self.log()).pack()
            self.button_out = Button(self.root7, text="NO", command=lambda: self.user_menu()).pack()
            self.root7.mainloop()

    def log(self):
        tkinter.messagebox.showinfo("LOGGED OUT SUCCESSFULLY")

        self.root7.destroy()
        self.root2.destroy()
obj=login()