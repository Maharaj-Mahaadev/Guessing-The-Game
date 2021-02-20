# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:14:34 2021

@author: Maharaj Mahaadev
"""





x=str(input("Registered or Login \n"))
if x=="Login":
    name1=str(input("Enter your name \n "))
    y=str(input("Enter password \n"))
    name2=("D:/Notepad/name.txt")
    with open(name2, 'r') as file_object:
        for line in file_object:
            if line == name1:
                print("User present \n")
            else:
                print("User not present, Register to proceed \n")
                
elif x=="Register":
    print("Enter a name: \n")
    name2=open("D:/Notepad/name.txt", "a")
    name2.write(input())
    age2=open("D:/Notepad/age2.txt", "a")
    try:
        age2.write(int(input()))
    except Exception as e:
        print("Can't register due to \n", e)
    loc2=open("D:/Notepad/loc2.txt", "a")
    loc2.write(input())
    pos2=open("D:/Notepad/pos2.txt", "a")
    pos3=str(input("Enter Photgrapher or Customer \n"))
    if pos3=="Photographer " or pos3== "Customer":
        pos2.write(pos3)
    else:
        print("Enter Correct Response \n")
        
    
    print("User Successfully Registered \n")
else:
    print("Error \n")
    
    
import keyring


service_id = 'IM_YOUR_APP!'

keyring.set_password(service_id, 'dustin', 'my secret password')
password = keyring.get_password(service_id, 'dustin') 


import keyring

MAGIC_USERNAME_KEY = 'im_the_magic_username_key'


service_id = 'IM_YOUR_APP!'  

username = 'dustin'


keyring.set_password(service_id, username, "password")


keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)


username = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
password = keyring.get_password(service_id, username)

print("To book service, enter the following \n")
name=str(input("Enter your name \n"))
try:
    dateD=int(input("Enter the date to reserve \n"))
    dateM=int(input("\n"))
    dateY=int(input("\n"))
    timeM=int(input("Enter the time to reserve \n"))
    timeH=int(input("\n"))
    photo=int(input("Enter the no. of photos required \n"))
except:
    print("Invalid date or time or quantity \n")
loc=str(input("Enter the location \n"))
rate=0
for i in range(0,photo):
    quality=str(input("Enter the quality of the photo required \n"))
    if quality=="high" or "High":
        rate+=15
    
    elif quality=="medium" or "Medium":
        rate+=10
    
    elif quality== "low " or "Low":
        rate+=5
    
    else:
        print("Incorrect quality selected \n")
    camera=str(input("Enter the type of camera needed \n"))
    if camera=="Sony" or camera=="sony":
        rate+=55
    elif camera=="Nikon" or camera=="nikon":
        rate+=45
    elif camera=="Canon" or camera=="canon":
        rate+=50
    else:
        print("Invalid camera selected \n")
print("The total price for the photography session selected is ", rate)
name3=("D:/Notepad/name.txt")
with open(name3, 'r') as file_object:
        for line in file_object:
            if line == name1:
                loc3=("D:/Notepad/loc2.txt")
                with open(loc3,'r') as file_object2:
                    for line2 in file_object2:
                        if line2 == loc:
                            print("Photographer has been assigned to \n", loc)
                        else:
                            print("No photographer available \n")
                
            else:
                print("User Not registered \n")
                
print("Thank you for using our app \n")


import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

       
        self.contents = tk.StringVar()
       
        self.contents.set("Enter Name")
        
        self.entrythingy["textvariable"] = self.contents

       
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Register"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=self.master.destroy)
        self.quit1 = tk.Button(self, text="Login", fg="blue"
                              )
        self.quit.pack(side="bottom")
        self.quit1.pack(side="left")
        
    

    def say_hi(self):
        print("Enter the name in the space provided down below")

root = tk.Tk()
myapp = App(root)
myapp.mainloop()


