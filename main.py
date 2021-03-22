'''
Important!
pip3 install sympy
'''
import tkinter as tk
from tkinter import ttk as ttk
from truthtable import create, unpack, print_result, wo, ow, zx, xz, kl
import data_generation as dg
from sympy import sympify, srepr
varList = ['A', 'B', 'C', 'D', 'E', 'F', 'P', 'Q', 'R', 'S', 'X', 'U']
IntroductionSlides = ["• Propositional logic is one of the simplest logics and is in universal usage.",
                      "• Formulas are built up from atomic propositions (factual statements) using logical connectives:",
                      "¬:NOT ∧:AND ∨:OR →:IMPLIES ↔:IF AND ONLY IF",
                      "• Note that ¬ is unary (one argument) while the others are binary (two arguments).",
                      "\n\n Propositions and connectives in English " "• Roughly speaking, propositions are the smallest factual statements in an English sentence.",
                      "• Connectives connect propositions together. \nExamples are “and”, “but”, “or”, “either”, “if”, “unless”...",
                      "• E.g., “If it’s raining I’ll stay in and eat pie”. \nPropositions are “it’s raining”, “I’ll stay in” and “I’ll eat pie”.",
                      "• Not every English sentence can be interpreted this way! \n(Questions, commands, . . . )"]
Lesson2Slides = ["• We assume an infinite set P, Q, R, . . . of proposition letters.",
                 "• Formulas of propositional logic are given by the grammar:", "A ::= P,Q,R... (Proposition)",
                 "    ¬A (Negation)", "    (A ∧ A) (Conjunction)", "    (A ∨ A) (Disjunction)",
                 "    (A → A) (Implication)", "    (A ↔ A) (Equivalence)",
                 "• We can drop outermost parentheses, \ne.g. (P → Q) ∨ R versus ((P → Q) ∨ R).",
                 "• ¬ has greater precedence than other connectives: \n  ¬A ∨ B means (¬A) ∨ B."]
Lesson3Slides = ["• “If it’s raining I will stay and eat pie” \n R→S∧P",
                 "• “You’re getting in if you have a ticket” \nT→G",
                 "• “You’re getting in only if you have a ticket” \nG→T",
                 "• “You’re not getting in unless you have a ticket” \n¬T → ¬G or, equivalently, ¬G ∨ T",
                 "\n“If it’s raining I’ll either stay in and eat pie, or take an Uber to the pub — provided that’s not too expensive, in which case I’ll get the bus there instead” \n R → ((S ∧ P) ∨ ((¬E → U) ∧ (E → B)))"]
Lesson4Slides = ["Reminder: Classical principles",
                 "Law of noncontradiction. Two directly contradictory statements cannot be true at the same time.\n⊢ ¬(A ∧ ¬A)",
                 "Law of excluded middle. Every statement is either true or false. \n ⊢ A ∨ ¬A", "\nValuations",
                 "• Let’s write L for the set of proposition letters in some formula A.",
                 "• I will use values 1 and 0 to stand for “true” and “false” respectively.",
                 "• A valuation v for A is then an interpretation of each letter in L as either true or false, i.e., a function: \n v : L ⟼ {0, 1}",
                 "• Next we explain how a valuation for A determines its overall truth value."]


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mainMenu()

    def mainMenu(self):
        ''' Main Menu '''
        self.MenuFrame = tk.Frame(self.parent)
        tk.Label(self.MenuFrame, text="Select option").grid(row=0, column=1)
        self.CalculatorMenuLogo = tk.PhotoImage(file=r"pics/CalculatorMenuLogo.png")
        self.PracticeMenuLogo = tk.PhotoImage(file=r"pics/PracticeMenuLogo.png")
        self.LearnMenuLogo = tk.PhotoImage(file=r"pics/LearnMenuLogo.png")
        tk.Button(self.MenuFrame, text="Calculator", image=self.CalculatorMenuLogo,
                  command=lambda: self.goto_x_Menu(1)).grid(row=1, column=0)
        tk.Button(self.MenuFrame, text="Practice", image=self.PracticeMenuLogo,
                  command=lambda: self.goto_x_Menu(2)).grid(row=1, column=1)
        tk.Button(self.MenuFrame, text="Learn", image=self.LearnMenuLogo,
                  command=lambda: self.goto_x_Menu(3)).grid(row=1, column=2)
        tk.Button(self.MenuFrame, text="LOAD ACCOUNT", command=lambda: self.goto_x_Menu(4)).grid(
            row=2, column=0)
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
            exprView.set(exprView.get() + str(value))

        def clearExpr():
            exprView.set("")

        def delExpr():
            exprView.set(exprView.get()[:-1])

        ''' To Infix Notation '''
        def toInfix(expr):
            # TT.wo(A,B)
            exprr = srepr(sympify(expr))
            exprr = exprr.replace("Symbol", "")
            exprr = exprr.replace("'", "")
            print(exprr)

            exprr = exprr.replace("And", "wo")
            exprr = exprr.replace("Or", "ow")
            exprr = exprr.replace("Not", "zx")
            exprr = exprr.replace("Equiv", "xz")
            exprr = exprr.replace("Implies", "kl")
            colNames = []
            for char in exprr:
                if char in varList and char not in colNames:
                    colNames.append(char)
            return exprr, colNames

        def displayTable(s, colNames):
            tableWindow = tk.Toplevel(self.parent)
            heading = tk.Label(tableWindow, text="Truth Table for " + exprView.get(), font=("Arial", 30)).grid(row=0,
                                                                                                               columnspan=3)
            cc = list(colNames)
            cc.append(exprView.get())
            listBox = ttk.Treeview(tableWindow, columns=cc, show='headings', height=28)
            for col in cc:
                listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2, rowspan=50)

            my_dict = {}

            data = create(num=len(colNames))
            unpacked = unpack(data)

            i = 0
            for cn in colNames:
                my_dict[cn] = unpacked[i]
                i += 1

            for (key) in my_dict.keys():
                s = s.replace(key, str(my_dict.get(key)))

            result = eval(s)
            vals = print_result(data, result)
            for c in vals:
                listBox.insert("", "end", values=(c))

        def workOut(expr):
            s, colName = toInfix(expr)
            displayTable(s, tuple(colName))

        exprView = tk.StringVar()
        exprView.set("")
        self.CalculatorMenuFrame = tk.Frame(self.parent)

        tk.Label(self.CalculatorMenuFrame, text="Welcome to calculator menu").grid(row=0, column=0)
        tk.Entry(self.CalculatorMenuFrame, state="readonly", width=80, textvariable=exprView).grid(row=1, column=1)
        tk.Button(self.CalculatorMenuFrame, text="DEL", command=lambda: delExpr()).grid(row=1, column=2)
        tk.Button(self.CalculatorMenuFrame, text="CLEAR", command=lambda: clearExpr()).grid(row=1, column=3)

        buttonFrame = tk.Frame(self.parent)

        tk.Button(buttonFrame, text="¬", width=10, height=3, command=lambda: updateExpr("~")).grid(row=2,
                                                                                                   column=0)
        tk.Button(buttonFrame, text="∧", width=10, height=3, command=lambda: updateExpr("&")).grid(row=2,
                                                                                                   column=1)
        tk.Button(buttonFrame, text="∨", width=10, height=3, command=lambda: updateExpr("|")).grid(row=2,
                                                                                                   column=2)
        tk.Button(buttonFrame, text="→", width=10, height=3, command=lambda: updateExpr(">>")).grid(
            row=2, column=3)
        tk.Button(buttonFrame, text="↔", width=10, height=3, command=lambda: updateExpr("↔")).grid(row=2,
                                                                                                   column=4)

        # LBRACKET AND RBRACKET / Haven't implemented this yet
        lbracketButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(
            row=3, column=0)
        rbracketButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(
            row=3, column=1)

        # VARIABLES
        tk.Button(buttonFrame, text="P", width=10, height=3, command=lambda: updateExpr("P")).grid(row=4,
                                                                                                   column=0)
        tk.Button(buttonFrame, text="Q", width=10, height=3, command=lambda: updateExpr("Q")).grid(row=4,
                                                                                                   column=1)
        tk.Button(buttonFrame, text="R", width=10, height=3, command=lambda: updateExpr("R")).grid(row=4,
                                                                                                   column=2)
        tk.Button(buttonFrame, text="X", width=10, height=3, command=lambda: updateExpr("X")).grid(row=4,
                                                                                                   column=3)
        tk.Button(buttonFrame, text="U", width=10, height=3, command=lambda: updateExpr("U")).grid(row=4,
                                                                                                   column=4)

        # SECONADRY VARIABLES
        tk.Button(buttonFrame, text="A", width=10, height=3, command=lambda: updateExpr("A")).grid(row=5,
                                                                                                   column=0)
        tk.Button(buttonFrame, text="B", width=10, height=3, command=lambda: updateExpr("B")).grid(row=5,
                                                                                                   column=1)
        tk.Button(buttonFrame, text="C", width=10, height=3, command=lambda: updateExpr("C")).grid(row=5,
                                                                                                   column=2)
        tk.Button(buttonFrame, text="D", width=10, height=3, command=lambda: updateExpr("D")).grid(row=5,
                                                                                                   column=3)
        tk.Button(buttonFrame, text="E", width=10, height=3, command=lambda: updateExpr("E")).grid(row=5,
                                                                                                   column=4)


        tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: workOut(exprView.get())).grid(
            row=6, column=1)
        tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(
            row=6, column=0)
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
        clearButton = tk.Button(self.CalculatorMenuFrame, text="CLEAR", command=lambda: clearExpr()).grid(row=1,
                                                                                                          column=3)

        buttonFrame = tk.Frame(self.parent)

        andButton = tk.Button(buttonFrame, text="&", width=10, height=3, command=lambda: updateExpr("&")).grid(row=2,
                                                                                                               column=1)
        orButton = tk.Button(buttonFrame, text="|", width=10, height=3, command=lambda: updateExpr("|")).grid(row=2,
                                                                                                              column=2)

        # SECONADRY VARIABLES
        aVarButton = tk.Button(buttonFrame, text="A", width=10, height=3, command=lambda: updateExpr("A")).grid(row=5,
                                                                                                                column=0)
        bVarButton = tk.Button(buttonFrame, text="B", width=10, height=3, command=lambda: updateExpr("B")).grid(row=5,
                                                                                                                column=1)
        cVarButton = tk.Button(buttonFrame, text="C", width=10, height=3, command=lambda: updateExpr("C")).grid(row=5,
                                                                                                                column=2)
        notaVarButton = tk.Button(buttonFrame, text="~A", width=10, height=3, command=lambda: updateExpr("~A")).grid(
            row=6, column=0)
        notbVarButton = tk.Button(buttonFrame, text="~B", width=10, height=3, command=lambda: updateExpr("~B")).grid(
            row=6, column=1)
        notcVarButton = tk.Button(buttonFrame, text="~C", width=10, height=3, command=lambda: updateExpr("~C")).grid(
            row=6, column=2)

        def isDNF():
            if dg.check_if_dnf(prop_formula, expr.get()) == False:
                popup = tk.Tk()
                popup.wm_title("Incorrect")
                label = ttk.Label(popup, text="The formula you entered was not the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
                B1.pack()
                popup.mainloop()
            else:
                popup = tk.Tk()
                popup.wm_title("Correct")
                label = ttk.Label(popup, text="you have successfully entered the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
                B1.pack()
                popup.mainloop()

        submitButton = tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: isDNF()).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(
            row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()

    def learnMenu(self):
        def nextSlide(var, counter, slides, button):
            var.set(var.get() + "\n\n" + slides[counter.get()])
            counter.set(counter.get() + 1)
            if counter.get() == len(slides):
                button['state'] = tk.DISABLED

        self.LearnMenuFrame = tk.Frame(self.parent)
        learnFrame = tk.LabelFrame(self.parent, text="Topics")
        tabs = ttk.Notebook(learnFrame)

        tab1 = ttk.Frame(tabs)
        l1text = tk.StringVar(value="Lesson 1: Introduction \nWhat is propositional logic?")
        l1index = tk.IntVar()
        tk.Label(tab1, textvariable=l1text, bg='#ececec').grid(column=0, row=0)
        nextL1B = tk.Button(tab1, text="NEXT", command=lambda: nextSlide(l1text, l1index, IntroductionSlides, nextL1B))
        nextL1B.grid()

        tab2 = ttk.Frame(tabs)
        l2text = tk.StringVar(value="")
        l2index = tk.IntVar()
        tk.Label(tab2, textvariable=l2text, bg='#ececec').grid(column=0, row=0)
        nextL2B = tk.Button(tab2, text="NEXT", command=lambda: nextSlide(l2text, l2index, Lesson2Slides, nextL2B))
        nextL2B.grid()

        tab3 = ttk.Frame(tabs)
        l3text = tk.StringVar(value="")
        l3index = tk.IntVar()
        tk.Label(tab3, textvariable=l3text, bg='#ececec').grid(column=0, row=0)
        nextL3B = tk.Button(tab3, text="NEXT", command=lambda: nextSlide(l3text, l3index, Lesson3Slides, nextL3B))
        nextL3B.grid()

        tab4 = ttk.Frame(tabs)
        l4text = tk.StringVar(value="")
        l4index = tk.IntVar()
        tk.Label(tab4, textvariable=l4text, bg='#ececec').grid(column=0, row=0)
        nextL4B = tk.Button(tab4, text="NEXT", command=lambda: nextSlide(l4text, l4index, Lesson4Slides, nextL4B))
        nextL4B.grid()

        tabs.add(tab1, text="Introduction")
        tabs.add(tab2, text="Syntax of formulas")
        tabs.add(tab3, text="Translating English to propositional logic")
        tabs.add(tab4, text="Valuations")
        tabs.pack(expand=1, fill="both")
        learnFrame.pack(fill="both", expand=True)

        goBackButton = tk.Button(self.LearnMenuFrame, text="Go Back To Main Menu",
                                 command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)

        self.LearnMenuFrame.pack()

    def loadAccount(self):
        self.LoadAccountFrame = tk.Frame(self.parent)
        Label = tk.Label(self.LoadAccountFrame,
                         text="Here you can load your account and get back where you left off").grid(row=0, column=0)
        goBackButton = tk.Button(self.LoadAccountFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=1,
                                                                                                                  column=0)
        self.LoadAccountFrame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
