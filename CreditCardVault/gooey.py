from tkinter.ttk import *
from tkinter import *
# import cryptMe 
from cryptMe import *
from customtkinter import *
import mysql.connector
import sqlite3
import dbconnect
from CTkTable import *

# The key is "RunItBack" 
class App(CTk):
    def __init__(self):
        #Connect first 
        #dbconnect.connect()
        self.conn = mysql.connector.connect(host='localhost', port=3307,database='creditcard_vault', user='root',password='')
        self.cryptMe = AESCipher("RunItBack")
        #The GUI starts here 
        self.root = CTk()
        self.root.title("VAULT")
        self.root.geometry("400x300")
        self.root.grid_rowconfigure(0, weight=1)  
        self.root.grid_columnconfigure(0, weight=1)

        self.frame = CTkFrame(master=self.root)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.initialText = CTkLabel(master=self.frame, text = "Welcome! Please select the appropriate operation.", justify=RIGHT)
        self.initialText.grid(row = 0, columnspan = 1, padx = 20, pady = (20,0))

        self.regBtn = CTkButton(master=self.frame, text= "User Registration", command= lambda: self.registration())
        self.regBtn.grid(row = 1 , column = 0 ,padx = 20, pady = (20,0))

        self.LoginBtn = CTkButton(master=self.frame, text= "Login", command= lambda: self.login())
        self.LoginBtn.grid(row = 2 , column = 0 ,padx = 20, pady = (20,0))
        

    def registration(self):
            dbconnect.connect()
            if self.root.winfo_exists():
                self.topnotch = CTkToplevel(self.root)
                self.topnotch.title("User Registration")
                self.topnotch.geometry("800x500")
                self.topnotch.grid_rowconfigure(0, weight=1)  # configure grid system
                self.topnotch.grid_columnconfigure(0, weight=1)
                self.topframe = CTkFrame(master=self.topnotch)
                self.topframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
                self.topnotch.focus()
                self.WelcomeText = CTkLabel(master=self.topframe, text = "Welcome! Proceed by filling in relevant details.", justify=RIGHT)
                self.WelcomeText.grid(row = 0, columnspan = 2, padx = 20, pady = (20,0))

                self.userName_label = CTkLabel(master=self.topframe, text = "Full Name:", justify=RIGHT)
                self.userName_label.grid(row = 1 , column = 0 ,padx = 20, pady = (20,0) )

                self.userName = CTkEntry(master=self.topframe, placeholder_text="Enter your full name", width=200, height=25, border_width=2,corner_radius=10)
                self.userName.grid(row = 1 , column = 1 , padx = 20 , pady = (20,0))

                self.password_label = CTkLabel(master=self.topframe, text = "Password:", justify=RIGHT)
                self.password_label.grid(row = 2 , column = 0 ,padx = 20 )

                self.password = CTkEntry(master=self.topframe, placeholder_text= "Enter Password", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.password.grid(row = 2 , column = 1, padx = 20)

                self.repassword = CTkEntry(master=self.topframe, placeholder_text= "Please Confirm Password", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.repassword.grid(row = 3 , column = 1, padx = 20)

                stan = self.cryptMe.hash(self.password.get())
                uncle = self.cryptMe.hash(self.repassword.get())
                
                if stan != uncle:
                    self.password.config(bg = "red")
                    self.repassword.config(bg = "red")
                else:
                    print("Passwords match") 

                self.email_label = CTkLabel(master=self.topframe, text = "Email:", justify=RIGHT)
                self.email_label.grid(row = 4 , column = 0 ,padx = 20 )

                self.email = CTkEntry(master=self.topframe, placeholder_text= "example@email.com", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.email.grid(row = 4 , column = 1, padx = 20)

                self.phone_label = CTkLabel(master=self.topframe, text = "Phone Number:", justify=RIGHT)
                self.phone_label.grid(row = 5 , column = 0 ,padx = 20 )

                self.phone = CTkEntry(master=self.topframe, placeholder_text= "0712000000", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.phone.grid(row = 5 , column = 1, padx = 20)

                self.address_label = CTkLabel(master=self.topframe, text = "Address:", justify=RIGHT)
                self.address_label.grid(row = 6 , column = 0 ,padx = 20 )

                self.address = CTkEntry(master=self.topframe, placeholder_text= "Enter Address", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.address.grid(row = 6 , column = 1, padx = 20)

                self.country_label = CTkLabel(master=self.topframe, text = "Country:", justify=RIGHT)
                self.country_label.grid(row = 7 , column = 0 ,padx = 20 )

                self.country = CTkEntry(master=self.topframe, placeholder_text= "Enter Country", width=200, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.country.grid(row = 7 , column = 1, padx = 20)

                self.RegisterBtn = CTkButton(master=self.topframe, text= "Submit", command= self.regToDB)
                self.RegisterBtn.grid(row = 8 , column = 1 ,padx = 20, pady = (20,0))

                self.topnotch.attributes('-topmost', True)

            else:
                self.new_window = CTkToplevel()
                self.new_window.focus()
                self.new_window.attributes('-topmost', True)


                
 
    def regToDB(self):
        dbconnect.connect()
        print("reached here")
        try:
            mycursor = self.conn.cursor()
            insert = "INSERT INTO creditcard_vault.client (fullname, password, email, phoneNo, address, country) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.userName.get(), self.cryptMe.hash(self.password.get()), self.email.get(), self.phone.get(), self.address.get(), self.country.get())
            # insert = "INSERT INTO creditcard_vault.admin (fullname, password, email, role) VALUES (%s, %s, %s, %s)"
            # values = (self.userName.get(), self.cryptMe.hash(self.password.get()), self.email.get(), 1)
            mycursor.execute( insert, values)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(e)
        
        
        print("Successfully Registered an account.")
        if self.root.winfo_exists():
                self.regnotch = CTkToplevel(self.root)
                self.regnotch.title("Success!")
                self.regnotch.geometry("600x400")
                self.regnotch.grid_rowconfigure(0, weight=1)  # configure grid system
                self.regnotch.grid_columnconfigure(0, weight=1)
                self.regframe = CTkFrame(master=self.regnotch)
                self.regframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
                self.regnotch.focus()
                self.SuccessText = CTkLabel(master=self.regframe, text = "Successfully Registered an account. Would you like to store your card?", justify=RIGHT)
                self.SuccessText.grid(row = 0, columnspan = 2, padx = 20, pady = (20,0))
                self.cardBtn = CTkButton(master=self.regframe, text= "Store Card", command= self.CardInfo)
                self.cardBtn.grid(row = 2 , column = 1 ,padx = 20, pady = (20,0))
                self.exitBtn = CTkButton(master=self.regframe, text= "Exit", command= lambda: self.root.destroy())
                self.exitBtn.grid(row = 3 , column = 1 ,padx = 20, pady = (20,0))
                
                self.regnotch.attributes('-topmost', True)
        else:
                self.othernew_window = CTkToplevel()
                self.othernew_window.focus()
                self.othernew_window.attributes('-topmost', True)
       
        #print(f"User input: {tea}")
      
    def CardInfo(self):
            dbconnect.connect()
            if self.root.winfo_exists():
                self.topnotch = CTkToplevel(self.root)
                self.topnotch.title("Card Information")
                self.topnotch.geometry("500x300")
                self.topnotch.grid_rowconfigure(0, weight=1)  # configure grid system
                self.topnotch.grid_columnconfigure(0, weight=1)
                self.topframe = CTkFrame(master=self.topnotch)
                self.topframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
                self.topnotch.focus()   
                self.cardNum_label = CTkLabel(master=self.topframe, text = "Credit Card Number: ", justify=RIGHT)
                self.cardNum_label.grid(row = 1 , column = 0 ,padx = 20, pady = (20,0))

                self.cardNum = CTkEntry(master=self.topframe, width=200, height=25, border_width=2,corner_radius=10)
                self.cardNum.grid(row = 1 , column = 1, padx = 20, pady = (20,0))

                self.cardName_label = CTkLabel(master=self.topframe, text = "Card Name:", justify=RIGHT)
                self.cardName_label.grid(row = 2 , column = 0 ,padx = 20 )

                Opvariable = StringVar(value="Visa")  # set initial value
                self.cardName = CTkOptionMenu(master=self.topframe, values = [ "Visa","Master Card","American Express","Chase","Citi Bank"],variable=Opvariable)
                self.cardName.grid(row = 2 , column = 1 , padx = 20 )

                self.expiry_label = CTkLabel(master=self.topframe, text = "Expiry Date:", justify=RIGHT)
                self.expiry_label.grid(row = 3 , column = 0 ,padx = 20 )
                
                self.expiry = CTkEntry(master=self.topframe, placeholder_text="MM-YYYY", width=200, height=25, border_width=2,corner_radius=10)
                self.expiry.grid(row = 3 , column = 1, padx = 20 )

                self.cvv_label = CTkLabel(master=self.topframe, text = "CVV:", justify=RIGHT)
                self.cvv_label.grid(row = 4 , column = 0 ,padx = 20 )

                self.cvv = CTkEntry(master=self.topframe, width=100, height=25, border_width=2,corner_radius=10, justify=LEFT)
                self.cvv.grid(row = 4 , column = 1, padx = 20)

                self.cardregBtn = CTkButton(master=self.topframe, text= "Submit Card", command= self.submitCard)
                self.cardregBtn.grid(row = 5 , column = 1 ,padx = 20, pady = (20,0))

                self.topnotch.attributes('-topmost', True)

            else:
                self.new_window = CTkToplevel()
                self.new_window.focus()
                self.new_window.attributes('-topmost', True)

    def submission(self):
        dbconnect.connect()
        mycursor = self.conn.cursor(buffered=True)
        selectUser = "SELECT email FROM client WHERE email = %s"
        selectAdmin = "SELECT email FROM admin WHERE email = %s"
        passCheck1= "SELECT password FROM client WHERE password = %s"
        passCheck2= "SELECT password FROM admin WHERE password = %s"
        user = [self.email.get()]
        passWord = [self.cryptMe.hash(self.password.get())]
        mycursor.execute(selectUser, user)
        if mycursor.rowcount == 1:
            print("User found")
            mycursor.execute(passCheck1, passWord )
            if mycursor.rowcount==1:
                print("User Authenticated")
                self.build()
            else:
                print("User password incorrect")
            # myresult = mycursor.fetchone()
        else:
            print("User not found")

        mycursor.execute(selectAdmin, user)        
        if mycursor.rowcount == 1:
            print("Admin found")
            mycursor.execute(passCheck2, passWord)
            if mycursor.rowcount==1:
                print("Admin Authenticated ")
                self.adminPanel()
            else:
                print("Admin password incorrect")

        else:
            print("Admin not found")
        
    def build(self):
        self.bubble = CTkToplevel(self.root)
        self.bubble.title("Personal Vault")
        self.bubble.geometry("400x300")
        self.bubble.grid_rowconfigure(0, weight=1)
        self.bubble.grid_columnconfigure(0, weight=1)
        self.bubbleframe = CTkFrame(master=self.bubble)
        self.bubbleframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bubble.focus()
        self.bubble.attributes('-topmost', True)

        self.initialText = CTkLabel(master=self.bubbleframe, text = "Welcome Back! Lock in...",  justify=RIGHT)
        self.initialText.grid(row = 0, columnspan = 1, padx = 20, pady = (20,0))
        self.cardBtn = CTkButton(master=self.bubbleframe, text= "Store Card", command= self.CardInfo)
        self.cardBtn.grid(row = 2 , column = 1 ,padx = 20, pady = (20,0))
        self.viewDetails = CTkButton(master=self.bubbleframe, text= "View Details", command= self.ViewSelf)
        self.viewDetails.grid(row = 3 , column = 1 ,padx = 20, pady = (20,0))
        self.viewCard = CTkButton(master=self.bubbleframe, text= "View Card Number", command= self.viewCardNum)
        self.viewCard.grid(row = 4 , column = 1 ,padx = 20, pady = (20,0))

    def adminPanel(self):
        self.bubble = CTkToplevel()
        self.bubble.title("Admin Panel")
        self.bubble.geometry("400x300")
        self.bubble.grid_rowconfigure(0, weight=1)
        self.bubble.grid_columnconfigure(0, weight=1)
        self.bubbleframe = CTkFrame(master=self.bubble)
        self.bubbleframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bubble.focus()
        self.initialText = CTkLabel(master=self.bubbleframe, text = "Welcome Back! Amara.",  justify=RIGHT)
        self.initialText.grid(row = 0, columnspan = 1, padx = 20, pady = (20,0))
        self.cardBtn = CTkButton(master=self.bubbleframe, text= "View Users", command= self.ViewUsers)
        self.cardBtn.grid(row = 2 , column = 0,padx = 20, pady = (20,0))
        self.bubble.attributes('-topmost', True)

    def ViewSelf(self):
        mycursor = self.conn.cursor()
        select = "SELECT client_id FROM client WHERE email = %s"
        email = [self.email.get()]
        mycursor.execute(select, email)
        result = mycursor.fetchone()
        id = result
        print(id)
        #query = "SELECT client.fullname, client.email, client.phoneNo, creditcard.cardName, creditcard.cardNo, creditcard.expiration_date, FROM client, creditcard" # WHERE creditcard.client_id = %s" 
        query = "SELECT client.fullname, client.email, client.phoneNo, creditcard.cardName, creditcard.cardNo, creditcard.expiration_date FROM client, creditcard WHERE creditcard.client_id = client.client_id AND client.client_id = %s"
        mycursor.execute(query,id)
        result = mycursor.fetchall()
        column_names = [column[0] for column in mycursor.description]
        tableValues = [["Fullname", "Email", "PhoneNo", "Card Name", "Card Number", "Expiration Date"]] + result
        if result is not None:
            # GUI portion using customtkinter (assuming you already have it installed)

            for x in result:
                print(x)
            self.view = CTkToplevel()
            self.view.title("User List")
            self.view.geometry("1200x400")
            self.view.grid_rowconfigure(0, weight=1)  # configure grid system
            self.view.grid_columnconfigure(0, weight=1)
            self.viewframe = CTkFrame(master=self.view)
            self.viewframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.view.focus() 
            table = CTkTable(master=self.viewframe, row=2, values=tableValues)  # Use fetched data headings=column_names,
            table.pack(expand=True, fill="both", padx=20, pady=20)
            self.view.attributes('-topmost', True)

    def viewCardNum(self):

        mycursor = self.conn.cursor()
        select = "SELECT client_id FROM client WHERE email = %s"
        email = [self.email.get()]
        mycursor.execute(select, email)
        result = mycursor.fetchone()
        id = result
        mycursor = self.conn.cursor()
        select = "SELECT cardNo,token FROM creditcard WHERE client_id = %s"
        mycursor.execute(select, id)
        result = mycursor.fetchone()
        anything = result[0]
        tokenNo = result[1]
        words = "Use this token to make purchases: " + tokenNo
        print(result[0], result[1])
        card = self.cryptMe.decrypt(anything)
        NumberWithWords = "Card Number: " + card

        popup = CTkToplevel(self.bubble)
        popup.title("Card Number")
        popup.geometry("700x300")
        popup.grid_rowconfigure(0, weight=1)
        popup.grid_columnconfigure(0, weight=1)
        popupframe = CTkFrame(master=popup)
        popupframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        popup.focus()
        popup.attributes('-topmost', True)
        cardNum = CTkLabel(master=popupframe, text = NumberWithWords,  justify=RIGHT)
        cardNum.grid(row = 1, columnspan = 1, padx = 20, pady = (20,0))
        token = CTkLabel(master=popupframe, text = words ,  justify=RIGHT)
        token.grid(row = 2, columnspan = 1, padx = 20, pady = (20,0))


    def ViewUsers(self):
        mycursor = self.conn.cursor()
        select = "SELECT * FROM client"
        query = "SELECT client_id, fullname, email, phoneNo, updated_at FROM client" 

        mycursor.execute(query)
        result = mycursor.fetchall()
        column_names = [column[0] for column in mycursor.description]
        # Fetch data from the database
        tabValues = [["Client ID", "Fullname", "Email", "PhoneNo", "Updated Logs"]] + result
        if result is not None:
            # GUI portion using customtkinter (assuming you already have it installed)

            for x in result:
                print(x)
            self.view = CTkToplevel(self.bubble)
            self.view.title("User List")
            self.view.geometry("800x600")
            self.view.grid_rowconfigure(0, weight=1)  # configure grid system
            self.view.grid_columnconfigure(0, weight=1)
            self.viewframe = CTkFrame(master=self.view)
            self.viewframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.view.focus() 
            table = CTkTable(master=self.viewframe,  values=tabValues)  # Use fetched data headings=column_names,
            table.pack(expand=True, fill="both", padx=20, pady=20)
            self.view.attributes('-topmost', True)
            
        else:
            print("Error fetching data. Please check connection and query.")
        # for x in result:
        #     print(x)

    def submitCard(self):
        mycursor = self.conn.cursor()
        select = "SELECT client_id FROM client WHERE email = %s"
        target = [self.email.get()]
        mycursor.execute(select, target)
        result = mycursor.fetchone()
        insert = "INSERT INTO creditcard (token, cardNo, cardName, expiration_date, cvv, client_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.cryptMe.hash(self.cardNum.get()),self.cryptMe.encrypt(self.cardNum.get()), self.cardName.get(), self.expiry.get(), self.cvv.get(),str(result[0]))
        
        mycursor.execute( insert, values)
        self.conn.commit()

        print("Card Submitted")

    
    def login(self):
            if self.root.winfo_exists():
                self.loginPanel = CTkToplevel(self.root)
                self.loginPanel.title("User Login")
                self.loginPanel.geometry("500x200")
                self.loginPanel.grid_rowconfigure(0, weight=1)  # configure grid system
                self.loginPanel.grid_columnconfigure(0, weight=1)
                self.logframe = CTkFrame(master=self.loginPanel)
                self.logframe.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
                self.loginPanel.focus()

                email_label = CTkLabel(master=self.logframe, text = "Email: ", justify=RIGHT)
                email_label.grid(row = 0 , column = 0 ,padx = 20, pady = (20,0) )

                self.email = CTkEntry(master=self.logframe, placeholder_text="Enter your Email", width=200, height=25, border_width=2,corner_radius=10)
                self.email.grid(row = 0 , column = 1 , padx = 20 , pady = (20,0))

                password_label = CTkLabel(master=self.logframe, text = "Password: ", justify=RIGHT)
                password_label.grid(row = 1 , column = 0 ,padx = 20 )

                self.password = CTkEntry(master=self.logframe, placeholder_text="eg. myPassword ", width=200, height=25, border_width=2,corner_radius=10)
                self.password.grid(row = 1 , column = 1 , padx = 20 )

                label = CTkLabel(master=self.logframe, text = "", justify=RIGHT)
                label.grid(row = 3 , column = 1 ,padx = 20 )

                self.SubmitBtn = CTkButton(master=self.logframe, text= "Login", command= self.submission)
                self.SubmitBtn.grid(row = 2 , column = 1 ,padx = 20, pady = (20,0))

                self.loginPanel.attributes('-topmost', True)

            else:
                new_window = CTkToplevel()
                new_window.focus()
                new_window.attributes('-topmost', True)
                
if __name__ == "__main__":
    app = App()
    app.root.mainloop()

