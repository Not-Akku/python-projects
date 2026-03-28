import tkinter as tk

#### FLAMES CALCULATOR WINDOW CLASS ####
class flamesWindow:
    def __init__(self, master):

        #creating the window controls...
        self.master = master
        self.master.title("FLAMES CALCULATOR")
        self.master.geometry("400x300")

        self.nameOneVar = tk.StringVar()
        self.nameTwoVar = tk.StringVar()
        self.nameOneLabel = tk.Label(self.master, text= "Name one: ").pack()
        self.nameOneEntry = tk.Entry(self.master,bg="lightgray",fg="black", textvariable=self.nameOneVar )
        self.nameOneEntry.pack()
        self.nameTwoLabel = tk.Label(self.master, text = "Name two: ").pack()
        self.nameTwoEntry = tk.Entry(self.master, bg="lightgray",fg="black", textvariable=self.nameTwoVar)
        self.nameTwoEntry.pack()

        self.calculateButton = tk.Button(self.master, text="Calculate", command=self.calculateFlames).pack()
        
        self.resultLabel = tk.Label(self.master, text=f"")
        self.resultLabel.pack()

    # calling this calculate ethods which calls the logc class.
    def calculateFlames(self):

        name1 = self.nameOneEntry.get()
        name2 = self.nameTwoEntry.get()

        if not name1 or not name2:
                self.resultLabel.config(text="Please enter both names.")

        result = FlamesLogic(name1, name2).calculate()
        self.resultLabel.config(text=f"result is {result}")

#### FLAMES LOGICS CLASS ####
class FlamesLogic:
    def __init__(self, fistName, secondName):
       
       #clean the names
       self.nameOne = list(fistName.lower().replace(" ",""))
       self.nameTwo = list(secondName.lower().replace(" ",""))


    # this method doe sthe calculating part of the flames calculator.
    def calculate(self):
        
        # it picks each letters 
        for i in self.nameOne[:]:
            if i in self.nameTwo:
                self.nameOne.remove(i)
                self.nameTwo.remove(i)

        totalLetters = len(self.nameOne) + len(self.nameTwo)

        if totalLetters == 0:
            return "Both name have no uncommon letters."


        self.flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        remainder = totalLetters % len(self.flames)
        print(totalLetters)
        print(remainder)
        return self.flames[remainder - 1]

# this is the main part of the code which runs the application.
if __name__ == "__main__":
    root = tk.Tk()
    app = flamesWindow(root)
    root.mainloop()
    