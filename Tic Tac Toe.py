from tkinter import *
from tkinter import messagebox
import tkinter
import pymysql
window=Tk()

window.geometry("600x600")
window.maxsize(800,800)
window.title("TIC Tac Toe Project")
window.configure(background="lightgrey")

usernameVar=StringVar()
passwordVar=StringVar()
mobileNoVar=StringVar()
EmailVar=StringVar()

def logindataWindow():
    
    username = usernameVar.get()
    password = passwordVar.get()
    if (username=="" or password==""):
        messagebox.showerror("login","kindly fill all the credentials")
    else:
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="game")
        cursor = conn.cursor()
        query = "select * from users where username='{}' and password='{}'".format(username, password)
        cursor.execute(query)
        data = cursor.fetchall()
        admin = False
        for row in data:
            admin = True
        conn.close()
        if admin:
            mainwindow()
        else:
            messagebox.showerror("Invalid user", "Credentials entered are invalid")
            usernameVar.set("")
            passwordVar.set("")
        
        

def myfunc():
    tkinter.messagebox.showinfo("Help","RULES FOR TIC-TAC-TOE\n\n1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

def mainwindow():
    
    remove_all_widgets()
    frame.pack_forget()
    
    global buttonplay,Photolabel
    buttonplay = Button(window,bg = "white",fg="black", text = "Play",relief=SUNKEN, font = ("Times 26 bold"), height = 1, width = 5,command =lambda:player_name())
    buttonplay.grid(row=4,column=2, columnspan=2)
    buttonplay.pack(side=BOTTOM,anchor="s",fill="x")


    photo = PhotoImage(file="com.png")
    Photolabel = Label(image=photo)
    Photolabel.image = photo
    Photolabel.pack(side = TOP,fill = "both", expand = "yes")
    

def player_name():
    remove_all_widgets()
    buttonplay.pack_forget()
    Photolabel.pack_forget()

    global h1
    h1=Label(text="Player Details",font = ("Times 40 bold"),bg="lightgrey",fg="green")
    h1.pack()
    
    global p1,p2
    p1 = StringVar()
    p2 = StringVar()

    global frame3
    frame3 = Frame(window, borderwidth=5, bg="lightgrey")
    frame3.pack(side=TOP,anchor="s")
    
    lbl = Label(frame3, text="Player 1: X", font=('Helvetica', '10'))
    lbl.grid(row=9, column=0)
    lbl = Label(frame3, text="Player 2: O", font=('Helvetica', '10'))
    lbl.grid(row=10, column=0)
    player1_name = Entry(frame3, textvariable=p1)
    player1_name.grid(row=9, column=1)
    player2_name = Entry(frame3, textvariable=p2)
    player2_name.grid(row=10, column=1)

    buttonname = Button(frame3,bg = "white",fg="black", text = "Submit",relief=SUNKEN, font = ("Times 16 bold"), height = 1, width = 8,command =lambda:layout())
    buttonname.grid(row=12,column=1)
    
    
    
def new_game():
    remove_all_widgets()
    frame2.pack_forget()
    heading.pack_forget()
    layout()

def again_login():
    remove_all_widgets()
    frame0.pack_forget()
    loginWindow()
    
    


    
def layout():
    remove_all_widgets()
    frame3.pack_forget()
    h1.pack_forget()
    global heading
    heading=Label(text="Tic Tac Toe",font = ("Times 46 bold"),bg="lightgrey")
    heading.pack()
    global frame2
    frame2 = Frame(window, borderwidth=6, bg="grey", relief=SUNKEN)
    frame2.pack(side=TOP, anchor="n")
    
    global buttons,button1,button2,button3,button4,button5,button6,button7,button8,button9

    buttons = StringVar()

    button1 = Button(frame2,bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button1))
    button1.grid(row = 1, column = 0)

    button2 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button2))
    button2.grid(row = 1, column = 1)


    button3 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button3))
    button3.grid(row = 1, column = 2)


    button4 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button4))
    button4.grid(row = 2, column = 0)


    button5 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button5))
    button5.grid(row = 2, column = 1)

    button6 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button6))
    button6.grid(row = 2, column = 2)


    button7 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button7))
    button7.grid(row = 3, column = 0)


    button8 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button8))
    button8.grid(row = 3, column = 1)


    button9 = Button(frame2, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6,command = lambda:checkwin(button9))
    button9.grid(row = 3, column = 2)



    
    mymenu = Menu(window)

    mymenu.add_command(label="New Game", command=new_game)
    mymenu.add_command(label="Help", command=myfunc)
    mymenu.add_command(label="Exit", command=quit)
    window.config(menu=mymenu)



click = True
def checkwin(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("Winner Congrats",p1.get()+" won the game")
        
        
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("Winner Congrats ",p2.get()+" won the game")
        
      
    elif(button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
        button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
        button7["text"] != " " and button8["text"] != " " and button9["text"]!= " " and
        button3["text"] != " " and button5["text"] != " " and button7["text"] != " " and
        button1["text"] != " " and button5["text"] != " " and button9["text"] != " " and
        button1["text"] != " " and button4["text"] != " " and button7["text"] != " " and
        button2["text"] != " " and button5["text"] != " " and button8["text"] != " " and
        button3["text"] != " " and button6["text"] != " " and button9["text"] != " "):
        tkinter.messagebox.showinfo("No Winner", "Game Draw")
        
        
def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()

def SignupWindow():
    remove_all_widgets()
    frame.pack_forget()
    global frame0
    frame0 = Frame(window, borderwidth=5, bg="lightgrey")
    frame0.pack(side=TOP, anchor="s")
    
    usernameVar.set("")
    passwordVar.set("")
    mobileNoVar.set("")
    EmailVar.set("")
    titleLabel=Label(frame0,text="Tic Tac Toe",font="Arial 20",fg="green")
    titleLabel.grid(row=0,column=0,columnspan=6)
    
    loginLabel=Label(frame0,text="Signup",font="Arial 15")
    loginLabel.grid(row=1,column=2,columnspan=6)
    
    usernameLabel = Label(frame0, text="Username",width=15,height=2)
    usernameLabel.grid(row=2, column=2)

    passwordLabel = Label(frame0, text="Password",width=15,height=2)
    passwordLabel.grid(row=3, column=2)
    
    EmailLabel = Label(frame0, text="Mobile No.",width=15,height=2)
    EmailLabel.grid(row=4, column=2)
    
    mobileNoLabel = Label(frame0, text="Email Id",width=15,height=2)
    mobileNoLabel.grid(row=5, column=2)

    usernameEntry= Entry(frame0, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3)

    passwordEntry = Entry (frame0, textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3)
    
    mobileNoEntry= Entry(frame0, textvariable=mobileNoVar)
    mobileNoEntry.grid(row=4, column=3)

    EmailEntry = Entry (frame0, textvariable = EmailVar)
    EmailEntry.grid(row=5,column=3)
    
    
    loginButton=Button(frame0,text="Login",width=20, height=2,command=lambda:again_login())
    loginButton.grid(row=6,column=2)
    
    loginButton=Button(frame0,text="Signup",width=20, height=2,command=lambda:SignupdataWindow())
    loginButton.grid(row=6,column=3)        

def loginWindow():
 
    global frame
    
    
    
    frame = Frame(window, borderwidth=5, bg="lightgrey")
    frame.pack(side=TOP, anchor="s")
    
    titleLabel = Label (frame,text = "Tic Tac Toe", font =("Times 46 bold"),bg="lightgrey")
    titleLabel.grid(row=0,column=0,columnspan=4,padx=(40,0),pady=(10,0))
    

    loginLabel = Label(frame,text="Admin Login", font = "Arial 30",fg="green",bg="lightgrey")
    loginLabel.grid(row = 1, column=2,columnspan=2,padx=(50,0),pady=10)

    usernameLabel = Label(frame, text = "Username",bg="lightgrey")
    usernameLabel.grid(row=2, column=2,padx=20,pady=5)

    passwordLabel = Label(frame, text = "Password",bg="lightgrey")
    passwordLabel.grid(row=3, column=2,padx=20,pady=5)

    usernameEntry = Entry(frame ,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=3,padx=20,pady=5)

    passwordEntry = Entry(frame, textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=5)

    loginButton = Button(frame, text="Login", width = 20, height=2,bg="white", command = lambda:logindataWindow())
    loginButton.grid(row=4,column=3)

    signup = Button(frame, text="Sign up", width = 20, height=2,bg="white", command = lambda:SignupWindow())
    signup.grid(row=4,column=2)

    
    
def SignupdataWindow():
    a=usernameVar.get()
    b=passwordVar.get()
    c=mobileNoVar.get()
    d=EmailVar.get()

    if a=="" or b=="" or c=="" or d=="" :
        messagebox.showerror("Signup","Kindly fill all the credentials correctly")
    else:
        conn=pymysql.connect(host="localhost",user="root",passwd="",db="game")
        cursor=conn.cursor()
        query1="select username from users "
        cursor.execute(query1)
        data=cursor.fetchall()
        list(data)
        f=0
        for i in data:
            p=list(i)
            if a==i[0]:
                f+=1
        if f==0:
            query="insert into users(username,password,mobileNo,emailid) value('{}','{}','{}','{}')".format(a,b,c,d)
            cursor.execute(query)
            conn.commit()
            conn.close()
            messagebox.showinfo("SignUp","Username and Password created")
            again_login()
        else:
            messagebox.showerror("Signup","Username already in use Try another one")
            usernameVar.set("")
            passwordVar.set("")
            mobileNoVar.set("")
            EmailVar.set("")
    


loginWindow()

window.mainloop()
