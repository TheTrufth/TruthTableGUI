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
        '''Clear everything on screen'''
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
        def updateExpr(value):
            expr.set(expr.get() + str(value))
        
        def clearExpr():
            expr.set("")
        
        def delExpr():
            expr.set(expr.get()[:-1])

        expr = tk.StringVar()
        expr.set("")
        self.CalculatorMenuFrame = tk.Frame(self.parent)
        
        Label = tk.Label(self.CalculatorMenuFrame, text="Welcome to calculator menu").grid(row=0, column=0)
        Entry = tk.Entry(self.CalculatorMenuFrame, state="readonly", width=80, textvariable=expr).grid(row=1, column=1)
        delButton = tk.Button(self.CalculatorMenuFrame, text="DEL", command=lambda: delExpr()).grid(row=1, column=2)
        clearButton = tk.Button(self.CalculatorMenuFrame, text="CLEAR", command=lambda: clearExpr()).grid(row=1, column=3)

        buttonFrame = tk.Frame(self.parent)
        
        notButton = tk.Button(buttonFrame, text="¬", width=10, height=3, command=lambda: updateExpr("¬")).grid(row=2, column=0)
        andButton = tk.Button(buttonFrame, text="∧", width=10, height=3, command=lambda: updateExpr("∧")).grid(row=2, column=1)
        orButton = tk.Button(buttonFrame, text="∨", width=10, height=3, command=lambda: updateExpr("∨")).grid(row=2, column=2)
        impliesButton = tk.Button(buttonFrame, text="→", width=10, height=3, command=lambda: updateExpr("→")).grid(row=2, column=3)
        equivButton = tk.Button(buttonFrame, text="↔", width=10, height=3, command=lambda: updateExpr("↔")).grid(row=2, column=4)

        # LBRACKET AND RBRACKET
        lbracketButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(row=3, column=0)
        rbracketButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(row=3, column=1)
        
        # VARIABLES
        pVarButton = tk.Button(buttonFrame, text="P", width=10, height=3, command=lambda: updateExpr("P")).grid(row=4, column=0)
        qVarButton = tk.Button(buttonFrame, text="Q", width=10, height=3, command=lambda: updateExpr("Q")).grid(row=4, column=1)
        rVarButton = tk.Button(buttonFrame, text="R", width=10, height=3, command=lambda: updateExpr("R")).grid(row=4, column=2)
        sVarButton = tk.Button(buttonFrame, text="S", width=10, height=3, command=lambda: updateExpr("S")).grid(row=4, column=3)
        tVarButton = tk.Button(buttonFrame, text="T", width=10, height=3, command=lambda: updateExpr("T")).grid(row=4, column=4)
        uVarButton = tk.Button(buttonFrame, text="U", width=10, height=3, command=lambda: updateExpr("U")).grid(row=4, column=5)
        
        # SECONADRY VARIABLES
        aVarButton = tk.Button(buttonFrame, text="A", width=10, height=3, command=lambda: updateExpr("A")).grid(row=5, column=0)
        bVarButton = tk.Button(buttonFrame, text="B", width=10, height=3, command=lambda: updateExpr("B")).grid(row=5, column=1)
        cVarButton = tk.Button(buttonFrame, text="C", width=10, height=3, command=lambda: updateExpr("C")).grid(row=5, column=2)
        dVarButton = tk.Button(buttonFrame, text="D", width=10, height=3, command=lambda: updateExpr("D")).grid(row=5, column=3)
        eVarButton = tk.Button(buttonFrame, text="E", width=10, height=3, command=lambda: updateExpr("E")).grid(row=5, column=4)
        fVarButton = tk.Button(buttonFrame, text="F", width=10, height=3, command=lambda: updateExpr("F")).grid(row=5, column=5)

        submitButton = tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: self.goto_x_Menu(0)).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()

    
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

    




