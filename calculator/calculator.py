#Imports
import math
import tkinter

def calculator():
    operator = operator_entry.get() 
    #numbers are set as decimals
    try:
        number1 = float(number1_entry.get())
        number2 = float(number2_entry.get())
    #in case of error
    except:
        ans_lable.config(text="Invalid number! please enter again")
    else:
        #operators
        if operator == "+":
            Addition= number1 + number2
            ans_lable.config(text=f"{Addition}")
        elif operator == "-":
            Subtraction = number1 - number2
            ans_lable.config(text=f"{Subtraction}")
        elif operator == "/":
            if number2 == 0 :
                ans_lable.config(text="Error")
                return
            Division = number1 / number2
            ans_lable.config(text=f"{Division}")
        elif operator == "*":
             Multiplication = number1 * number2
             ans_lable.config(text=f"{Multiplication}")
        elif operator == "**":
            powe = math.pow(number1, number2)
            ans_lable.config(text=f"{powe}")
        elif operator == "log":
            if (number2 == 0) or (number1 == 0) :
                ans_lable.config(text="Error")
                return
            logarithm = math.log(number1, number2)
            ans_lable.config(text=f"{logarithm}")

window = tkinter.Tk()
window.title("calculator")

calcul_lable = tkinter.Label(text="number 1: ")
calcul_lable.grid(row=0, column=0, padx=(20, 10), pady=10)

number1_entry = tkinter.Entry(width=30)
number1_entry.grid(row=0, column=1, padx=(20, 10), pady=10)

calcul4_lable = tkinter.Label(text="operator:")
calcul4_lable.grid(row=1, column=0, padx=(20, 10), pady=10)

operator_entry = tkinter.Entry(width=30)
operator_entry.grid(row=1, column=1, padx=(20, 10), pady=10)

calcul3_lable = tkinter.Label(text="number 2: ")
calcul3_lable.grid(row=2, column=0, padx=(20, 10), pady=10)

number2_entry = tkinter.Entry(width=30)
number2_entry.grid(row=2, column=1, padx=(20, 10), pady=10)

ans_lable = tkinter.Label(text="Answer")
ans_lable.grid(row=3, column=1, padx=(20, 10), pady=10)

calculator_button = tkinter.Button(text="calculat!", bg="blue", command=calculator)
calculator_button.grid(row=4, column=11)

window.mainloop()
