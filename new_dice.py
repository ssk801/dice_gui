'''
05-06 mar2024
making a tiny gui for rolling dice

handy customtkinter tutorial here: 
https://www.youtube.com/watch?v=iM3kjbbKHQU

customtkinter is a required library 
documentation here:
https://customtkinter.tomschimansky.com/documentation/

'''

import random
import customtkinter
from tkinter import messagebox


class DiceGUI:
    
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("640x360")

        #self.thisRoll=[]

        self.frame=customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20,padx=20,fill="both", expand=False)

        self.label=customtkinter.CTkLabel(master=self.frame, text="Let's Roll Some Dice!", font=("Roboto",32))
        self.label.pack(pady=12,padx=12)


        self.inputgrid=customtkinter.CTkFrame(self.frame)
        self.inputgrid.columnconfigure(0,weight=1)
        self.inputgrid.columnconfigure(1,weight=1)

        self.diceLabel=customtkinter.CTkLabel(master=self.inputgrid, text="Number of Dice", font=("Roboto",24))
        self.diceLabel.grid(row=0,column=0)

        #dice=customtkinter.CTkEntry(master=inputgrid, placeholder_text="Number of Dice")
        #dice.grid(row=0,column=1)

        self.dice2=customtkinter.CTkOptionMenu(master=self.inputgrid, values=['1','2','3','4','5','6','7','8','9','10'],font=("Roboto",24))
        self.dice2.grid(row=0,column=1)
        self.dice2.set('3')

        self.sidesLabel=customtkinter.CTkLabel(master=self.inputgrid, text="Number of Sides", font=("Roboto",24))
        self.sidesLabel.grid(row=1,column=0)

        #sides=customtkinter.CTkEntry(master=inputgrid, placeholder_text="Number of Sides")
        #sides.grid(row=1,column=1)

        self.sides2=customtkinter.CTkOptionMenu(master=self.inputgrid,values=['4','6','8','10','12','20','100'],font=("Roboto",24))
        self.sides2.grid(row=1,column=1)
        self.sides2.set('6')

        self.inputgrid.pack(pady=10,fill='x')

        self.button=customtkinter.CTkButton(master=self.frame, text="Roll!", command=self.rollDice, font=('Roboto',24))
        self.button.pack(pady=12,padx=12)

        #checkbox=customtkinter.CTkCheckBox(master=frame, text="Remember?")
        #checkbox.pack(pady=12,padx=12)

        #implement results in a gid with labels on the left

        self.resultgrid=customtkinter.CTkFrame(self.frame)
        self.resultgrid.columnconfigure(0,weight=1)
        self.resultgrid.columnconfigure(1,weight=1)
        self.resultgrid.columnconfigure(2,weight=1)

        self.results=customtkinter.CTkLabel(master=self.resultgrid, text="Dice: ", font=("Roboto",24), height=40)
        self.results.grid(row=0,column=0)

        self.resultSum=customtkinter.CTkLabel(master=self.resultgrid, text="Sum: ", font=("Roboto",24), height=40)
        self.resultSum.grid(row=1,column=0)

        self.results=customtkinter.CTkLabel(master=self.resultgrid, text="", font=("Roboto",24), height=40)
        self.results.grid(row=0,column=1,columnspan=2,sticky=customtkinter.W)

        self.resultSum=customtkinter.CTkLabel(master=self.resultgrid, text="", font=("Roboto",24), height=40)
        self.resultSum.grid(row=1,column=1,columnspan=2,sticky=customtkinter.W)

        self.resultgrid.pack(pady=10,fill='x')

        self.root.mainloop()

    def rollDice(self):
        # return [random.randint(1,d) for i in range(n)]
        self.resultArray=([random.randint(1,int(self.sides2.get())) for x in range(int(self.dice2.get()))])
        self.results.configure(text=(self.resultArray))
        self.resultSum.configure(text=(sum(self.resultArray)))
        #messagebox.showinfo(message=self.thisRoll)

DiceGUI()