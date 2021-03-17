import tkinter as tk
from tkinter import ttk as ttk
import truthtable as TT
import data_generation as dg

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

        ''' To Infix Notation '''
        def convToInf(expr):
            red = []
            new = expr[:1]
            p = []
            previous_char = None
            
            for char in expr:
                if previous_char == "¬":
                    p.pop()
                    p.append("TT.zx(" + char + ")")
                else:
                    p.append(char)
                previous_char = char
            
            expr = p
            previous_char = None
            colName = []
            for char in expr:
                if char != "∧" and char != "∨" and char != "→" and char != "↔":
                    colName.append(char)
                    red.append(char)
                if previous_char == "∧":
                    new = "TT.wo(" + new + "," + char + ")"
                    red = []
                elif previous_char == "∨":
                    new = "TT.ow(" + new + "," + char + ")"
                    red = []
                elif previous_char == "→":
                    new = "TT.kl(" + new + "," + char + ")"
                    red = []
                elif previous_char == "↔":
                    new = "TT.xz(" + new + "," + char + ")"
                    red = []
                previous_char = char
            
            
            return new, colName
        
        def displayTable(s, colNames):
            tableWindow = tk.Toplevel(self.parent)
            heading = tk.Label(tableWindow, text="Truth Table for " + expr.get(), font=("Arial", 30)).grid(row=0, columnspan=3)
            listBox = ttk.Treeview(tableWindow, columns=colNames, show='headings')
            for col in colNames:
                listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)

            my_dict = {}
            
            data = TT.create(num=len(colNames) - 1)
            unpacked = TT.unpack(data)

            i = 0
            for cn in colNames[:-1]:
                my_dict[cn] = unpacked[i]
                i += 1

            key = None
            for (key) in my_dict.keys():
                s = s.replace(key, str(my_dict.get(key)))
            
            
            result = eval(s)
            vals = TT.print_result(data, result)
            for c in vals:
                listBox.insert("", "end", values=(c))


        def workOut(expr):
            s, colName = convToInf(expr)
            colName.append(expr)
            displayTable(s, tuple(colName))


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

        # LBRACKET AND RBRACKET / Haven't implemented this yet
        #lbracketButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(row=3, column=0)
        #rbracketButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(row=3, column=1)
        
        # VARIABLES
        pVarButton = tk.Button(buttonFrame, text="P", width=10, height=3, command=lambda: updateExpr("P")).grid(row=4, column=0)
        qVarButton = tk.Button(buttonFrame, text="Q", width=10, height=3, command=lambda: updateExpr("Q")).grid(row=4, column=1)
        rVarButton = tk.Button(buttonFrame, text="R", width=10, height=3, command=lambda: updateExpr("R")).grid(row=4, column=2)
        sVarButton = tk.Button(buttonFrame, text="S", width=10, height=3, command=lambda: updateExpr("S")).grid(row=4, column=3)
        xVarButton = tk.Button(buttonFrame, text="X", width=10, height=3, command=lambda: updateExpr("X")).grid(row=4, column=4)
        uVarButton = tk.Button(buttonFrame, text="U", width=10, height=3, command=lambda: updateExpr("U")).grid(row=4, column=5)
        
        # SECONADRY VARIABLES
        aVarButton = tk.Button(buttonFrame, text="A", width=10, height=3, command=lambda: updateExpr("A")).grid(row=5, column=0)
        bVarButton = tk.Button(buttonFrame, text="B", width=10, height=3, command=lambda: updateExpr("B")).grid(row=5, column=1)
        cVarButton = tk.Button(buttonFrame, text="C", width=10, height=3, command=lambda: updateExpr("C")).grid(row=5, column=2)
        dVarButton = tk.Button(buttonFrame, text="D", width=10, height=3, command=lambda: updateExpr("D")).grid(row=5, column=3)
        eVarButton = tk.Button(buttonFrame, text="E", width=10, height=3, command=lambda: updateExpr("E")).grid(row=5, column=4)
        fVarButton = tk.Button(buttonFrame, text="F", width=10, height=3, command=lambda: updateExpr("F")).grid(row=5, column=5)

        submitButton = tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: workOut(expr.get())).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()


    def practiceMenu(self):
        def updateExpr(value):
            expr.set(expr.get() + str(value))
        
        def clearExpr():
            expr.set("")
        
        def delExpr():
            expr.set(expr.get()[:-1])

        expr = tk.StringVar()
        expr.set("")
        self.CalculatorMenuFrame = tk.Frame(self.parent)
        
        prop_formula = dg.get_prop_formula()

        HLabel = tk.Label(self.CalculatorMenuFrame, text="Practice Menu: Enter correct").grid(row=0, column=0)
        prop_label = tk.Label(self.CalculatorMenuFrame, text=prop_formula).grid(row=0, column=1)
        Entry = tk.Entry(self.CalculatorMenuFrame, state="readonly", width=80, textvariable=expr).grid(row=1, column=1)
        delButton = tk.Button(self.CalculatorMenuFrame, text="DEL", command=lambda: delExpr()).grid(row=1, column=2)
        clearButton = tk.Button(self.CalculatorMenuFrame, text="CLEAR", command=lambda: clearExpr()).grid(row=1, column=3)

        buttonFrame = tk.Frame(self.parent)
        
        andButton = tk.Button(buttonFrame, text="&", width=10, height=3, command=lambda: updateExpr("&")).grid(row=2, column=1)
        orButton = tk.Button(buttonFrame, text="|", width=10, height=3, command=lambda: updateExpr("|")).grid(row=2, column=2)
        
        # SECONADRY VARIABLES
        aVarButton = tk.Button(buttonFrame, text="A", width=10, height=3, command=lambda: updateExpr("A")).grid(row=5, column=0)
        bVarButton = tk.Button(buttonFrame, text="B", width=10, height=3, command=lambda: updateExpr("B")).grid(row=5, column=1)
        cVarButton = tk.Button(buttonFrame, text="C", width=10, height=3, command=lambda: updateExpr("C")).grid(row=5, column=2)
        notaVarButton = tk.Button(buttonFrame, text="~A", width=10, height=3, command=lambda: updateExpr("~A")).grid(row=6, column=0)
        notbVarButton = tk.Button(buttonFrame, text="~B", width=10, height=3, command=lambda: updateExpr("~B")).grid(row=6, column=1)
        notcVarButton = tk.Button(buttonFrame, text="~C", width=10, height=3, command=lambda: updateExpr("~C")).grid(row=6, column=2)


        def isDNF():
            if dg.check_if_dnf(prop_formula,expr.get()) == False:
                popup = tk.Tk()
                popup.wm_title("Incorrect")
                label = ttk.Label(popup, text="The formula you entered was not the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
                B1.pack()
                popup.mainloop()
            else:
                popup = tk.Tk()
                popup.wm_title("Correct")
                label = ttk.Label(popup, text="you have successfully entered the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
                B1.pack()
                popup.mainloop()


        submitButton = tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: isDNF()).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()

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

    




