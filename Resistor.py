from tkinter import *
from tkinter import ttk

class Resistor:
    def __init__(self, root):
        self.root = root
        self.root.title("Resistor Colour Code Calculator")
        self.root.geometry("1352x652+0+0")
        self.root.configure(background="powder blue")

        mainFrame = Frame(self.root)
        mainFrame.grid()

        TitleFrame = Frame(mainFrame, bd = 10, width = 1350, padx = 20, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        self.lblTitle = Label(TitleFrame, font = ('arial', 50, 'bold'), text = "Resistor Colour Code Calculator", padx = 100)
        self.lblTitle.grid()

        ResistorFrame = Frame(mainFrame, bd = 10, width = 1350, padx = 20, relief = RIDGE)
        ResistorFrame.grid(row = 1, column = 0)

        labels = ["1st Band", "2nd Band", "Multiplier", "Tolerance"]
        colors = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Gray", "White", "Gold", "Silver", "None"]
        multipliers = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 0.1, "", ""]
        tolerances = ["", "", "", "", "", "", "", "", "", "", "5%", "10%", "20%"]

        for col, label in enumerate(labels):
            self.lblTitle = Label(ResistorFrame, font = ('arial', 13, 'bold'), text = label)
            self.lblTitle.grid(row = 0, column = col)

        for row, color in enumerate(colors, start=1):
            for col, value in enumerate([color, str(row % 10), str(multipliers[row - 1]), tolerances[row - 1]]):
                if color == "None":
                    color = "White"

                textColor = "black"
                if color == "Black":
                    textColor = "white"

                button = Button(ResistorFrame, width = 13, font = ('arial', 14, 'bold'), text = value, fg = textColor, bg = color)
                button.grid(row = row, column = col)

if __name__ == '__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()
