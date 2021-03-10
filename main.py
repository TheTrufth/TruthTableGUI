import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mainMenu()
        
    def mainMenu(self):
        ''' Main Menu '''
        self.MenuFrame = tk.Frame(self.parent)
        Label = tk.Label(self.MenuFrame, text="Select option").grid(row=0, column=1)
        self.CalculatorMenuLogo = tk.PhotoImage(file=r"pics/CalculatorMenuLogo.png")
        self.PracticeMenuLogo = tk.PhotoImage(file=r"pics/PracticeMenuLogo.png")
        self.LearnMenuLogo = tk.PhotoImage(file=r"pics/LearnMenuLogo.png")
        CalculatorMenuButton = tk.Button(self.MenuFrame, text="Calculator", image=self.CalculatorMenuLogo, command=lambda: self.goto_x_Menu(1)).grid(row=1, column=0)
        PracticeMenuButton = tk.Button(self.MenuFrame, text="Practice", image=self.PracticeMenuLogo, command=lambda: self.goto_x_Menu(2)).grid(row=1, column=1)
        LearnMenuButton = tk.Button(self.MenuFrame, text="Learn", image=self.LearnMenuLogo, command=lambda: self.goto_x_Menu(3)).grid(row=1, column=2)
        LoadAccountButton = tk.Button(self.MenuFrame, text="LOAD ACCOUNT", command=lambda: self.goto_x_Menu(4)).grid(row=2, column=0)
        self.MenuFrame.pack()

    def clearwin(self):
        '''Clear the frame f's widgets'''
        for child in self.parent.winfo_children():
            child.destroy()

    def goto_x_Menu(self, x):
        self.clearwin()
        if x == 0:
            self.mainMenu()
        elif x == 1:
            self.calculatorMenu()
        elif x == 2:
            self.practiceMenu()
        elif x == 3:
            self.learnMenu()
        elif x == 4:
            self.loadAccount()
        
    def calculatorMenu(self):
        self.CalculatorMenuFrame = tk.Frame(self.parent)
        Label = tk.Label(self.CalculatorMenuFrame, text="Welcome to calculator menu").grid(row=0, column=0)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)
        self.CalculatorMenuFrame.pack()
    
    def practiceMenu(self):
        self.PracticeMenuFrame = tk.Frame(self.parent)
        Label = tk.Label(self.PracticeMenuFrame, text="Welcome to practice menu").grid(row=0, column=0)
        goBackButton = tk.Button(self.PracticeMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)
        self.PracticeMenuFrame.pack()
    
    def learnMenu(self):
        self.LearnMenuFrame = tk.Frame(self.parent)
        Label = tk.Label(self.LearnMenuFrame, text="Welcome to learn menu").grid(row=0, column=0)
        goBackButton = tk.Button(self.LearnMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)
        self.LearnMenuFrame.pack()
    
    def loadAccount(self):
        self.LoadAccountFrame = tk.Frame(self.parent)
        Label = tk.Label(self.LoadAccountFrame, text="Here you can load your account and get back where you left off").grid(row=0, column=0)
        goBackButton = tk.Button(self.LoadAccountFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)
        self.LoadAccountFrame.pack()



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

    




