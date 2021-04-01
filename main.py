'''
Important!
pip3 install sympy
pip3 install pandas
pip3 install Pillow
'''
import tkinter as tk
from tkinter import ttk as ttk
from truthtable import create, unpack, print_result, wo, ow, zx, xz, kl
from PIL import Image, ImageTk
import data_generation as dg
from sympy import sympify, srepr, pretty
from sympy.logic import simplify_logic
from sympy.logic.boolalg import to_dnf, to_cnf
import random
varList = ['A', 'B', 'C', 'D', 'E', 'F', 'P', 'Q', 'R', 'S', 'X', 'U']

class Question():
    def __init__(self):
        questionType = ["toCNF", "inCNFtoDNF", "toDNF", "inDNFtoCNF"]
        x = random.randint(0, len(questionType) - 1)
        self.type = questionType[x]
        f = dg.get_prop_formula()
        if x == 0:
            self.question = "What is " + pretty(f) + " in CNF?"
            self.answer = to_cnf(f)
        elif x == 1:
            f = to_cnf(f)
            self.question = pretty(f) + " is in CNF,convert it to DNF"
            self.answer = to_dnf(f)
        if x == 2:
            self.question = "What is " + pretty(f) + " in DNF?"
            self.answer = to_dnf(f)
        elif x == 3:
            f = to_dnf(f)
            self.question = pretty(f) + " is in CNF,convert it to DNF"
            self.answer = to_cnf(f)
        
        self.userinput = ""
    
    def checkIfCorrect(self):
        return simplify_logic(self.answer) == simplify_logic(self.userinput.replace(" ", ""))
    

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mainMenu()

    def mainMenu(self):
        ''' Main Menu '''
        #1000, 500
        self.canvas = tk.Canvas(self.parent, width=1200, height=719)
        self.canvas.pack()

        self.MenuFrame = tk.Frame(self.canvas)
        

        #self.fn = tk.PhotoImage(file=r"pics/blank background.png")
        self.fn = ImageTk.PhotoImage(Image.open("pics/home.png").resize((1200, 719), Image.ANTIALIAS))
        self.canvas.background = self.fn
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.fn)
        
        # 62:height  515:width  // Buttons:  610:width  168:height
        # 239:height 2031:width // New Buttons: 549:width 161:height

        
        # 1200x719
        # 1080x647 
        #self.CalculatorMenuLogo = ImageTk.PhotoImage(Image.open("pics/CalculatorMenuLogo.png").resize((439, 128), Image.ANTIALIAS))
        self.CalculatorMenuLogo = tk.PhotoImage(file=r"pics/CalculatorMenuLogo.png")
        self.PracticeMenuLogo = tk.PhotoImage(file=r"pics/PracticeMenuLogo.png")
        self.LearnMenuLogo = tk.PhotoImage(file=r"pics/LearnMenuLogo.png")
        self.TestMenuLogo = tk.PhotoImage(file=r"pics/TestMenuLogo.png")

        tk.Button(self.MenuFrame, text="Calculator", image=self.CalculatorMenuLogo,
                  command=lambda: self.goto_x_Menu(1)).grid(row=2, column=0)
        tk.Button(self.MenuFrame, text="Practice", image=self.PracticeMenuLogo,
                  command=lambda: self.goto_x_Menu(2)).grid(row=2, column=1)
        tk.Button(self.MenuFrame, text="Learn", image=self.LearnMenuLogo,
                  command=lambda: self.goto_x_Menu(3)).grid(row=3, column=0)
        tk.Button(self.MenuFrame, text="Test", image=self.TestMenuLogo,
                  command=lambda: self.goto_x_Menu(11)).grid(row=3, column=1)

        #self.MenuFrame.pack()
        button_window = self.canvas.create_window(300, 250, anchor=tk.NW, window=self.MenuFrame)

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
            self.PracticeSubMenu()
        elif x == 3:
            self.learnMenu()
        elif x == 5:
            self.EnglishTranslationActivity()
        elif x==6:
            self.practiceDNF()
        elif x == 7:
            self.practiceCNF()
        elif x == 11:
            self.TestSubMenu()
        
    def calculatorMenu(self):
        def updateExpr(value):
            if value == "↔":
                exprView.set("Equivalent(" + exprView.get() + ", ")
            else:
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
            print("Infix_expr:", exprr)

            exprr = exprr.replace("And", "wo")
            exprr = exprr.replace("Or", "ow")
            exprr = exprr.replace("Not", "zx")
            exprr = exprr.replace("Equivalent", "xz")
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
            CNFanswer.set("CNF Form: " + str(to_cnf(expr)))
            DNFanswer.set("     DNF Form: " + str(to_dnf(expr)))
            s, colName = toInfix(expr)
            displayTable(s, tuple(colName))

        
        exprView = tk.StringVar(value="")

        self.canvas = tk.Canvas(self.parent, width=1200, height=719)
        self.canvas.pack()
        BgColor = '#ded9e2'

        self.CalculatorMenuFrame = tk.Frame(self.canvas, bg=BgColor)
        

        #self.fn = tk.PhotoImage(file=r"pics/blank background.png")
        self.fn = ImageTk.PhotoImage(Image.open("pics/background-with-penguin.png").resize((1200, 719), Image.ANTIALIAS))
        self.canvas.background = self.fn
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.fn)

        tk.Label(self.CalculatorMenuFrame, text="Welcome to calculator menu", bg=BgColor).grid(row=0, column=0)
        tk.Entry(self.CalculatorMenuFrame, state="readonly", width=80, textvariable=exprView, highlightbackground=BgColor).grid(row=1, column=1)
        tk.Button(self.CalculatorMenuFrame, text="DEL", command=lambda: delExpr(), highlightbackground=BgColor).grid(row=1, column=2)
        tk.Button(self.CalculatorMenuFrame, text="CLEAR", command=lambda: clearExpr(), highlightbackground=BgColor).grid(row=1, column=3)

        dnfcnfFrame = tk.Frame(self.canvas, bg=BgColor)
        buttonFrame = tk.Frame(self.canvas, bg=BgColor)

        tk.Button(buttonFrame, text="¬", width=10, height=3, command=lambda: updateExpr("~")).grid(row=2,
                                                                                                   column=0)
        tk.Button(buttonFrame, text="∧", width=10, height=3, command=lambda: updateExpr("&")).grid(row=2,
                                                                                                   column=1)
        tk.Button(buttonFrame, text="∨", width=10, height=3, command=lambda: updateExpr("|")).grid(row=2,
                                                                                                   column=2)
        tk.Button(buttonFrame, text="→", width=10, height=3, command=lambda: updateExpr(">>")).grid(
            row=2, column=3)
        tk.Button(buttonFrame, text="↔", width=10, height=3, command=lambda: updateExpr("↔")).grid(
            row=2, column=4)


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


        tk.Button(self.CalculatorMenuFrame, text="SUBMIT", command=lambda: workOut(exprView.get()), highlightbackground=BgColor).grid(
            row=6, column=1)
        
        CNFanswer = tk.StringVar(value="CNF Form: ")
        DNFanswer = tk.StringVar(value="DNF Form: ")
        tk.Label(dnfcnfFrame, textvariable=CNFanswer, bg=BgColor).grid(row=1, column=0)
        tk.Label(dnfcnfFrame, textvariable=DNFanswer, bg=BgColor).grid(row=1, column=3)

        self.BackLogo = ImageTk.PhotoImage(Image.open("pics/back.png").resize((100, 60), Image.ANTIALIAS))

        tk.Button(self.CalculatorMenuFrame, text="Go Back", image=self.BackLogo,
                  command=lambda: self.goto_x_Menu(0)).grid(row=9, column=0)

        
        self.canvas.create_window(80, 100, anchor=tk.NW, window=self.CalculatorMenuFrame)
        self.canvas.create_window(350, 200, anchor=tk.NW, window=dnfcnfFrame)
        self.canvas.create_window(350, 250, anchor=tk.NW, window=buttonFrame)

        def convertToCNF(expr):
            answer1 = "CNF form of ", expr,"  is  ", to_cnf(expr)
            cnfWindow = tk.Tk()
            cnfWindow.wm_title("CNF form")
            label = ttk.Label(cnfWindow, text=answer1)
            label.pack(side="top", fill="x", pady=10)
            Button1 = ttk.Button(cnfWindow, text="Done", command=cnfWindow.destroy)
            Button1.pack()
            cnfWindow.mainloop()

        def convertToDNF(expr):
            answer2 = "DNF form of ",expr,"  is  ", to_dnf(expr)
            dnfWindow = tk.Tk()
            dnfWindow.wm_title("DNF form")
            label = ttk.Label(dnfWindow, text = answer2)
            label.pack(side="top", fill="x", pady=10)
            Button2 = ttk.Button(dnfWindow, text="Done", command=dnfWindow.destroy)
            Button2.pack()
            dnfWindow.mainloop()
    
    def PracticeSubMenu(self):
        self.PracticeSubMenuFrame = tk.Frame(self.parent)
        DNFButton = tk.Button(self.PracticeSubMenuFrame,command=lambda:self.goto_x_Menu(6), text="practice converting Propositional formula to CNF").grid(row=1, column=0)
        CNFButton = tk.Button(self.PracticeSubMenuFrame,command=lambda:self.goto_x_Menu(7), text="practice converting Propositional formula to DNF").grid(row=2, column=0)
        EnglishButton = tk.Button(self.PracticeSubMenuFrame,command=lambda:self.goto_x_Menu(5),text="practice converting Propositional formula to English sentence").grid(row=3, column=0)
        self.PracticeSubMenuFrame.pack()        

    def EnglishTranslationActivity(self):
        def getQuestionAndAnswers():
            import pandas as pd
            df = pd.read_csv('QandA.csv')
            questions = df['QUESTION'].to_list()
            answer1 = df['ANSWER1'].to_list()
            answer2 = df['ANSWER2'].to_list()
            answer3 = df['ANSWER3'].to_list()
            correct = df['CORRECT'].to_list()
            return questions, answer1, answer2, answer3, correct
        def getQuestion():
            import random 
            rand_index = random.randint(0,len(getQuestionAndAnswers()[0])-1)
            question = getQuestionAndAnswers()[0][rand_index]
            answer1 = getQuestionAndAnswers()[1][rand_index]
            answer2 = getQuestionAndAnswers()[2][rand_index]
            answer3 = getQuestionAndAnswers()[3][rand_index]
            correct = getQuestionAndAnswers()[4][rand_index]
            return question, answer1,answer2,answer3,correct
        def displayMessage(_str):
            popup = tk.Tk()
            label = ttk.Label(popup, text=_str)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Try again", command=(popup.destroy))
            B1.pack()
            popup.mainloop()
        def correct():
            popup = tk.Tk()
            label = ttk.Label(popup, text="Correct! \n you will now go onto another question")
            label.pack(side="top", fill="x", pady=10)
            self.goto_x_Menu(5)
            popup.mainloop()

            

        self.EnglishFrame = tk.Frame(self.parent)
        question = getQuestion()
        label = tk.Label(self.EnglishFrame,text=question[0]).grid(row=0, column=0)
        import random
        ycoordinates = random.sample(range(1, 5), 4)
        answer1Button = tk.Button(self.EnglishFrame,command=lambda:displayMessage("Incorrect"), text=question[1]).grid(row=ycoordinates[0], column=0)
        answer2Button = tk.Button(self.EnglishFrame,command=lambda:displayMessage("Incorrect"), text=question[2]).grid(row=ycoordinates[1], column=0)
        answer3Button = tk.Button(self.EnglishFrame,command=lambda:displayMessage("Incorrect"),text=question[3]).grid(row=ycoordinates[2], column=0)
        correctButton = tk.Button(self.EnglishFrame,command=lambda:correct(), text=question[4]).grid(row=ycoordinates[3], column=0)
        tk.Button(self.EnglishFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=7, column=2)
        self.EnglishFrame.pack()
 
    def practiceDNF(self):
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
        lparenButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(
            row=6, column=3)
        rparenButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(
            row=6, column=4)


        def isDNF(prop_formula):
            if dg.check_if_dnf(simplify_logic(prop_formula), simplify_logic(expr.get())) == False:
                popup = tk.Tk()
                popup.wm_title("Incorrect")
                label = ttk.Label(popup, text="The formula you entered was not the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
                B1.pack()
                popup.mainloop()
            else:
                popup = tk.Tk()
                #popup.wm_title("Correct")
                label = ttk.Label(popup, text="you have successfully entered the correct DNF")
                label.pack(side="top", fill="x", pady=10)
                self.goto_x_Menu(6)
                popup.mainloop()
                

        submitButton = tk.Button(self.CalculatorMenuFrame, text="Submit", command=lambda: isDNF(prop_formula)).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(
            row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()

    def practiceCNF(self):
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
        lparenButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(
            row=6, column=3)
        rparenButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(
            row=6, column=4)


        def isCNF(prop_formula):
            if dg.check_if_cnf(simplify_logic(prop_formula), simplify_logic(expr.get())) == False:
                popup = tk.Tk()
                popup.wm_title("Incorrect")
                label = ttk.Label(popup, text="The formula you entered was not the correct CNF")
                label.pack(side="top", fill="x", pady=10)
                B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
                B1.pack()
                popup.mainloop()
            else:
                popup = tk.Tk()
                label = ttk.Label(popup, text="you have successfully entered the correct CNF")
                label.pack(side="top", fill="x", pady=10)
                B1.pack()
                self.goto_x_Menu(7)
                popup.mainloop()
                
        submitButton = tk.Button(self.CalculatorMenuFrame, text="Submit", command=lambda: isCNF(prop_formula)).grid(row=6, column=1)
        goBackButton = tk.Button(self.CalculatorMenuFrame, text="Go Back", command=lambda: self.goto_x_Menu(0)).grid(row=6, column=0)
        self.CalculatorMenuFrame.pack()
        buttonFrame.pack()

    def learnMenu(self):
        '''
        def nextSlide(var, counter, slides, button):
            var.set(var.get() + "\n\n" + slides[counter.get()])
            counter.set(counter.get() + 1)
            if counter.get() == len(slides):
                button['state'] = tk.DISABLED
        '''

        def nextSlide(lessonLabel, lesson, lessonp1, lessonb, lessonf):
            if lessonLabel.image == lesson:
                lessonLabel.configure(image=lessonp1)
                lessonLabel.image = lessonp1
                lessonb.config(state='normal')
                lessonf.config(state='disabled')
            else:
                lessonLabel.configure(image=lesson)
                lessonLabel.image = lesson
                lessonb.config(state='disabled')
                lessonf.config(state='normal')

        self.LearnMenuFrame = tk.Frame(self.parent)
        learnFrame = tk.LabelFrame(self.parent, text="Topics")
        tabs = ttk.Notebook(learnFrame)

        self.BackLogo = ImageTk.PhotoImage(Image.open("pics/back.png").resize((100, 60), Image.ANTIALIAS))
        self.ForwardLogo = ImageTk.PhotoImage(Image.open("pics/forward.png").resize((100, 60), Image.ANTIALIAS))

        tab1 = ttk.Frame(tabs)
        lesson1 = ImageTk.PhotoImage(Image.open("pics/lesson 1.0.png").resize((1090, 622), Image.ANTIALIAS))
        lesson1p1 = ImageTk.PhotoImage(Image.open("pics/lesson 1.1.png").resize((1090, 622), Image.ANTIALIAS))
        lesson1Label = tk.Label(tab1, image=lesson1)
        lesson1Label.image = lesson1
        lesson1Label.grid(row=0, column=0)
        l1b = tk.Button(tab1, text="Previous", image=self.BackLogo, command=lambda: nextSlide(lesson1Label, lesson1, lesson1p1, l1b, l1f), state="disabled")
        l1b.place(x=10, y=550)
        l1f = tk.Button(tab1, text="Next", image=self.ForwardLogo, command=lambda: nextSlide(lesson1Label, lesson1, lesson1p1, l1b, l1f))
        l1f.place(x=970, y=550)


        tab2 = ttk.Frame(tabs)
        lesson2 = ImageTk.PhotoImage(Image.open("pics/lesson 2.0.png").resize((1090, 622), Image.ANTIALIAS))
        lesson2p2 = ImageTk.PhotoImage(Image.open("pics/lesson 2.1.png").resize((1090, 622), Image.ANTIALIAS))
        lesson2Label = tk.Label(tab2, image=lesson2)
        lesson2Label.image = lesson2
        lesson2Label.grid(row=0, column=0)
        l2b = tk.Button(tab2, text="Previous", image=self.BackLogo, command=lambda: nextSlide(lesson2Label, lesson2, lesson2p2, l2b, l2f), state="disabled")
        l2b.place(x=10, y=550)
        l2f = tk.Button(tab2, text="Next", image=self.ForwardLogo, command=lambda: nextSlide(lesson2Label, lesson2, lesson2p2, l2b, l2f))
        l2f.place(x=970, y=550)

        tab3 = ttk.Frame(tabs)
        lesson3 = ImageTk.PhotoImage(Image.open("pics/lesson 3.1.png").resize((1090, 622), Image.ANTIALIAS))
        lesson3Label = tk.Label(tab3, image=lesson3)
        lesson3Label.image = lesson3
        lesson3Label.grid(row=0, column=0)

        tab4 = ttk.Frame(tabs)
        lesson4 = ImageTk.PhotoImage(Image.open("pics/lesson 4.0.png").resize((1090, 622), Image.ANTIALIAS))
        lesson4p4 = ImageTk.PhotoImage(Image.open("pics/lesson 4.1.png").resize((1090, 622), Image.ANTIALIAS))
        lesson4Label = tk.Label(tab4, image=lesson4)
        lesson4Label.image = lesson4
        lesson4Label.grid(row=0, column=0)
        l4b = tk.Button(tab4, text="Previous", image=self.BackLogo, command=lambda: nextSlide(lesson4Label, lesson4, lesson4p4, l4b, l4f), state="disabled")
        l4b.place(x=10, y=550)
        l4f = tk.Button(tab4, text="Next", image=self.ForwardLogo, command=lambda: nextSlide(lesson4Label, lesson4, lesson4p4, l4b, l4f))
        l4f.place(x=970, y=550)
        
        
        tabs.add(tab1, text="Introduction")
        tabs.add(tab2, text="Syntax of formulas")
        tabs.add(tab3, text="Translating English to propositional logic")
        tabs.add(tab4, text="Valuations")
        tabs.pack(expand=1, fill="both")
        learnFrame.pack(fill="both", expand=True)

        goBackButton = tk.Button(self.LearnMenuFrame, text="Go Back To Main Menu",
                                 command=lambda: self.goto_x_Menu(0)).grid(row=1, column=0)
        self.LearnMenuFrame.pack()
    

    def TestSubMenu(self):
        self.TestSubMenuFrame = tk.Frame(self.parent)
        tk.Label(self.TestSubMenuFrame, text="You will be given 10 randomised questions related to propositional logic. \n You will have 15 minutes to answer them. \n Click begin once you are ready to start and GOOD LUCK!!").grid(row=0, column=0)
        s = tk.Button(self.TestSubMenuFrame,command=lambda:self.beginTest(10, 15), text="BEGIN")
        s.grid(row=2, column=0)
        self.TestSubMenuFrame.pack()
    
    def beginTest(self, numOfQ, timeLim):
        useranswer = tk.StringVar("")
        self.clearwin()
        qFrame = tk.Frame(self.parent)
        Score = 0

        QList = self.generateQuestions(numOfQ)
        CurrentQuestion = tk.IntVar(0)
        timeTaken = tk.IntVar(0)
        currentTime = tk.Label(qFrame, text="Time Taken: 0")
        currentTime.grid(row=0, column=0)

        def updateTimer():
            if timeTaken.get() < 6000:
                timeTaken.set(timeTaken.get() + 1)
                currentTime.configure(text="Time Taken: "+str(timeTaken.get()))
                self.parent.after(1000, updateTimer)
            else:
                result = tk.Toplevel(self.parent)
                tk.Label(result, text="Your didn't answer the questions in time: ").pack()
                tk.Label(result, text="You have FAILED!").pack()
                tk.Button(result, text="Continue", command=lambda: self.goto_x_Menu(11)).pack()


        def showNextQ():
            previousButton.config(state='normal') 
            QList[CurrentQuestion.get()].userinput = useranswer.get()
            CurrentQuestion.set(CurrentQuestion.get() + 1)
            if QList[CurrentQuestion.get()].userinput != "":
                useranswer.set(QList[CurrentQuestion.get()].userinput)
            elif QList[CurrentQuestion.get()].userinput == "":
                clearExpr()
            questionNumber.configure(text="Question No: " + str(CurrentQuestion.get())) 
            question.configure(text=QList[CurrentQuestion.get()].question)
            if CurrentQuestion.get() == len(QList) - 1:
                nextButton.config(state='disabled') 
                submitButton.config(state='normal')
        
        def showPrevQ():
            nextButton.config(state='normal')
            QList[CurrentQuestion.get()].userinput = useranswer.get()
            CurrentQuestion.set(CurrentQuestion.get() - 1)
            if QList[CurrentQuestion.get()].userinput != "":
                useranswer.set(QList[CurrentQuestion.get()].userinput)
            questionNumber.configure(text="Question No: " + str(CurrentQuestion.get()))
            question.configure(text=QList[CurrentQuestion.get()].question)
            
            if CurrentQuestion.get() == 0:
                previousButton.config(state='disabled') 
        
        def submit():
            QList[CurrentQuestion.get()].userinput = useranswer.get()
            score = 0
            didntanswer = 0
            for q in QList:
                try:
                    if q.checkIfCorrect():
                        score += 1
                except:
                    pass
                if q.userinput == "":
                    didntanswer += 1
            
            percentage = score / len(QList) * 100
            result = tk.Toplevel(self.parent)
            tk.Label(result, text="Your total score is: " + str(score)).pack()
            tk.Label(result, text="You did not answer " + str(didntanswer) + " questions").pack()
            tk.Label(result, text="Your percentage for this test was: " + str(percentage)).pack()
            if percentage > 50:
                tk.Label(result, text="Your have PASSED!: ").pack()
            else:
                tk.Label(result, text="You have FAILED!: ").pack()

            tk.Button(result, text="Continue", command=lambda: self.goto_x_Menu(11)).pack()
            
                
            

        def updateExpr(value):
            useranswer.set(useranswer.get() + str(value))

        def clearExpr():
            useranswer.set("")

        def delExpr():
            useranswer.set(useranswer.get()[:-1])
        
        questionNumber = tk.Label(qFrame, text="Question No: " + str(CurrentQuestion.get()))
        questionNumber.grid(row=0, column=1)

        question = tk.Label(qFrame, text=QList[CurrentQuestion.get()].question)
        question.grid(row=1, column=0)
        tk.Entry(qFrame, textvariable=useranswer).grid(row=2, column=0)
        
        buttonFrame = tk.Frame(self.parent)
        andButton = tk.Button(buttonFrame, text="&", width=10, height=3, command=lambda: updateExpr("&")).grid(row=3,
                                                                                                               column=1)
        orButton = tk.Button(buttonFrame, text="|", width=10, height=3, command=lambda: updateExpr("|")).grid(row=3,
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
        lparenButton = tk.Button(buttonFrame, text="(", width=10, height=3, command=lambda: updateExpr("(")).grid(
            row=4, column=1)
        rparenButton = tk.Button(buttonFrame, text=")", width=10, height=3, command=lambda: updateExpr(")")).grid(
            row=4, column=2)

        
        previousButton = tk.Button(buttonFrame, text="Previous Q", state='disabled', command=lambda: showPrevQ())
        previousButton.grid(row=7, column=0)
        nextButton = tk.Button(buttonFrame, text="Next Q", command=lambda: showNextQ())
        nextButton.grid(row=7, column=2)
        submitButton = tk.Button(buttonFrame, text="FINISH TEST", state='disabled', command=lambda: submit())
        submitButton.grid(row=8, column=1)
        updateTimer()
        qFrame.pack()
        buttonFrame.pack()

    def generateQuestions(self, amount):
        QList = []
        for _ in range(0, amount):
            Q = Question()
            QList.append(Q)
        return QList


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('{}x{}'.format(1200, 719))
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()