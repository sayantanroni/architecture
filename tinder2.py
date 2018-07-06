
import mysql.connector
class Tinder:
    def __init__(self):
        #connect to the database
        self.conn=mysql.connector.connect(host='localhost', user='root', password='',database='tinder')
        self.mycursor=self.conn.cursor()
        self.menu()

    def menu(self):
        x=input('''Let us connect with you
        Enter your choice:
        1.Create an acc
        2.Login
        3.Exit''')
        if x=='1':
            self.register()
        elif x=='2':
            self.login()
        else:
            print("Bye")

    def register(self):
        a=input("Enter your name ")
        p=input("Enter your email ")
        if('@' in p ):
            self.mycursor.execute('''SELECT * FROM `users` WHERE `email` LIKE '{}' '''.format(p))
            email_list = self.mycursor.fetchall()
            for i in email_list:
                if (p == i[2]):
                    print("An account has already been created in this email id ..pls register again with another mail id")
                    self.register()
        else:
            print("Please try again with a valid mail id. ")
            self.register()

        b=(input(" create a password"))

        if(len(b)>4):
                    print('✔')

        else:
                    print("MUST BE A STRONG PASSWORD(HINT:- MAKE SURE PASSWORD LENGTH IS GREATER THAN 4")
                    print("enter pass again")
                    self.register()
        c=input("Gender?")
        d=input("Age?")
        e=input("City")
        self.mycursor.execute('''INSERT INTO `users`(`User-id`, `name`, `email`, `password`, `gender`, `age`, `city`)VALUES(NULL, '{}','{}','{}','{}','{}','{}')'''.format(a,p,b,c,d,e)) #this would send the string to the database
        self.conn.commit()
        print("Registration successful")
        self.login()

    def login(self):
            email = input("Enter your email id ")
            password = input("Enter the password ")
            self.mycursor.execute('''SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' '''.format(email, password))
            user_list = self.mycursor.fetchall()
            c = 0
            for i in user_list:
                c = c + 1
                current_user = i
            if c > 0:
                print("Login successful..you are welcome ")
                self.current_user_id = current_user[0]
                print(self.current_user_id)
                self.user_menu()
            else:
                print("Try Again")
                self.login()

    def user_menu(self):
            n = input("""How would you like to proceed
            1.View all users
            2.View proposals
            3.View requests
            4.View matches
            5.Logout
            6.Exit""")
            if n == '1':
                self.view_users()
            elif n == '2':
                self.view_proposals()
            elif n == '3':
                self.view_requests()
            elif n == '4':
                self.view_matches()
            elif n=='5':
                self.logout()
            else:
                print("Press any to exit")


    def view_users(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `User-id` NOT LIKE '{}' AND `User-id` NOT IN(SELECT `juliet-id` FROM `proposals` WHERE `romeo-id` LIKE '{}')""".format(self.current_user_id, self.current_user_id))
        all_users_list=self.mycursor.fetchall()
        for i in all_users_list:
            print(i[0],'|',i[1],'|',i[4],'|',i[5],'|',i[6])
            print("-------------------------------------------")
        juliet_id=input("enter the id of the user u want to propose")
        self.propose(self.current_user_id, juliet_id)

    def propose(self, romeo_id, juliet_id):
        self.mycursor.execute("""INSERT INTO `proposals` (`id`, `romeo-id`, `juliet-id`) VALUES(NULL, '{}','{}')""".format(romeo_id, juliet_id))
        self.conn.commit()
        print("REQUEST SEND!")
        self.user_menu()

    def view_proposals(self):
        print("the users whom you have proposed ")
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON p.`juliet-id` = u.`User-id` WHERE p.`romeo-id` LIKE '{}'""".format(self.current_user_id))
        proposed_user_list=self.mycursor.fetchall()
        for i in proposed_user_list:
            print( i[4], '|', i[7], '|', i[8], '|', i[9])
            print("---------------------------------------------")
        self.user_menu()

    def view_requests(self):
        print("YOUR REQUESTS ARE ")
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON p.`romeo-id` = u.`User-id`  WHERE p.`juliet-id` LIKE '{}'""".format(self.current_user_id))
        requested_user_list = self.mycursor.fetchall()
        for i in requested_user_list:
            print(i[4], '|', i[7], '|', i[8], '|', i[9])
            print("---------------------------------------------")
        self.user_menu()

    def view_matches(self):
        print("SUCCESSFUL MATCHES! ")
        self.mycursor.execute("""SELECT `name`,`gender`,`age`,`city` FROM `users` WHERE `User-id` IN (SELECT `juliet-id` FROM `proposals` WHERE `romeo-id` LIKE '{}' AND `juliet-id` IN (SELECT `romeo-id` FROM `proposals` WHERE `juliet-id` LIKE '{}'))""".format(self.current_user_id, self.current_user_id))
        matched_user = self.mycursor.fetchall()
        for i in matched_user:
            print(i[0],'|',i[1],'|',i[2],'|',i[3])
            print("---------------------------------------------")
        self.user_menu()

    def logout(self):
        X=input("""Are you sure you want to Log out of Tinder?
        YES    NO """)
        if X=='Y' or X=='y':
            print("LOGGED OUT SUCCESSFULLY")
            self.login()
        elif(X=='N' or X=='n'):
            self.user_menu()
user=Tinder()




