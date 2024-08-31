from tkinter import *

# Create main window
m = Tk()
m.title("Body Mass Index")
m.geometry("550x380+0+0")

# Variables to hold weight, height, and result
weight = StringVar()
height = StringVar()
result = StringVar()

# Frame setup
frame1 = Frame(m, pady=10, bd=16)
frame1.grid()

frame2 = Frame(frame1, width=550, height=190, pady=10, bd=16, relief="sunken")
frame2.grid(row=0, column=0)

frame3 = Frame(frame1, width=550, height=190, pady=10, bd=16, relief="sunken")
frame3.grid(row=1, column=0)

# Widgets in frame2
lblwei = Label(frame2, text="Enter your weight", font=('arial', 14, 'bold'), bd=20)
lblwei.grid(row=0, column=0)

entrywei = Entry(frame2, textvariable=weight, font=('arial', 14, 'bold'), bd=20)
entrywei.grid(row=0, column=1)

lblkg = Label(frame2, text="kg", font=('arial', 14, 'bold'), bd=20)
lblkg.grid(row=0, column=2)

lblheig = Label(frame2, text="Enter your height", font=('arial', 14, 'bold'), bd=20)
lblheig.grid(row=1, column=0)

entryheig = Entry(frame2, textvariable=height, font=('arial', 14, 'bold'), bd=20)
entryheig.grid(row=1, column=1)

lblcm = Label(frame2, text="cm", font=('arial', 14, 'bold'), bd=20)
lblcm.grid(row=1, column=2)

lblres = Label(frame2, text="Show Result (BMI)", font=('arial', 14, 'bold'), bd=20)
lblres.grid(row=2, column=0)

entryres = Entry(frame2, textvariable=result, font=('arial', 14, 'bold'), bd=20)
entryres.grid(row=2, column=1)

# Function to calculate BMI
def add():
    try:
        # Get weight and height from entries
        f = float(weight.get())
        s = float(height.get()) / 100  # Convert cm to meters
        a = f / (s * s)  # Calculate BMI
        b = round(a, 2)
        result.set(b)
    except ValueError:
        result.set("Error")

# Function to reset all fields
def Rest():
    weight.set("")
    height.set("")
    result.set("")

# Buttons in frame3
btntotal = Button(frame3, text='Total', font=('arial', 14, 'bold'), bd=12, pady=12, width=8, command=add)
btntotal.grid(row=0, column=0)

btnreset = Button(frame3, text='Reset', font=('arial', 14, 'bold'), bd=12, pady=12, width=8, command=Rest)
btnreset.grid(row=0, column=1)

btnexit = Button(frame3, text='Exit', font=('arial', 14, 'bold'), bd=12, pady=12, width=8, command=m.quit)
btnexit.grid(row=0, column=2)

# Start the main loop
m.mainloop()