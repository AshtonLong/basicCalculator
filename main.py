import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the display for the calculator
        self.display = tk.Entry(self, font=("Helvetica", 24), bg="#eee", bd=0, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, pady=10)

        # Create the buttons for the calculator
        buttons = [
            ["C", "CE"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row in buttons:
            for button in row:
                tk.Button(self, text=button, font=("Helvetica", 18), bg="#fff", bd=0, padx=20, pady=10, command=lambda b=button: self.press(b)).grid(row=buttons.index(row)+1, column=row.index(button))

    def press(self, button):
        if button == "=":
            # Evaluate the expression and display the result
            try:
                result = eval(self.display.get())
                self.display.insert(tk.END, " = " + str(result))
            except:
                self.display.insert(tk.END, "Error")
        elif button == "C":
            # Clear the display
            self.display.delete(0, tk.END)
        elif button == "CE":
            # Clear the last character in the display
            self.display.delete(len(self.display.get())-1)
        else:
            # Add the button press to the display
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    app = Calculator()
    app.title("Scientific Calculator")
    app.mainloop()
