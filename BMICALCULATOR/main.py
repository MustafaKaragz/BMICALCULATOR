import tkinter

screen=tkinter.Tk()
screen.title("BMI CALCULATOR")
screen.config(padx=30,pady=30)


def calculate_bmi():
    height=input_height_entry.get()
    weight=input_weight_entry.get()


    if weight=="" or height=="":
        result_label.config(text="Enter both weight and height!")

    else:
        try:
            bmi=float(weight)/(float(height)/100)**2
            result_string=write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a Valid Number")



def write_result(bmi):
    result_string=f"Your bmi is: {round(bmi,2)}. You are "
    if bmi<=16:
        result_string+="severly thin!"
    elif bmi>16 and bmi<=17:
        result_string+="moderately thin."
    elif bmi>17 and bmi<=18.5:
        result_string+="mild thin."
    elif bmi>18.5 and bmi <=25:
        result_string+="normal."
    elif bmi>25 and bmi <=30:
        result_string+="overweight."
    elif bmi>30 and bmi <=35:
        result_string+="obese class 1."
    elif bmi>35 and bmi<=40:
        result_string+="obese class 2."
    else:
        result_string+="obese class 3."

    return result_string



input_weight_label=tkinter.Label(text="Enter Your Weight (kg)")
input_weight_label.pack()

input_weight_entry=tkinter.Entry(width=10)
input_weight_entry.pack()


input_height_label=tkinter.Label(text="Enter Your Height (cm)")
input_height_label.pack()

input_height_entry=tkinter.Entry(width=10)
input_height_entry.pack()

calculate_button=tkinter.Button(text="Calculate",command=calculate_bmi)
calculate_button.pack()

result_label=tkinter.Label()
result_label.pack()

screen.mainloop()