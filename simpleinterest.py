from tkinter import *
window=Tk()

window.title('SimpleInterest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_simpleinterest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)
    result_label.destroy()

    output_message=Label(result_frame,text="Interest on rs"+ str(p)+" at rate "+ str(r)+ " for "+str(t)+" years is rs "+str(interest),bg="lightcyan",font=("Calibri",12),width=42)
    output_message.place(x=20,y=40)
    output_message.pack()


app_label=Label(window, text="SimpleInterest Calculator", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window,text="Principle",fg="black",bg="lightcyan",font=("Calibri",12),bd=2)
principle_label.place(x=20,y=120)

principle=Entry(window,text="",bd=2,width=20)
principle.place(x=150,y=122)

rate_label=Label(window,text="Rate",fg="black",bg="lightcyan",font=("Calibri",12),bd=2)
rate_label.place(x=20,y=165)

rate=Entry(window,text="",bd=2,width=20)
rate.place(x=150,y=167)

time_label=Label(window,text="Years",fg="black",bg="lightcyan",font=("Calibri",12),bd=2)
time_label.place(x=20,y=200)

time=Entry(window,text="",bd=2,width=20)
time.place(x=150,y=202)

calculate=Button(window,text="CALCULATE",fg="black",bg="cyan",bd=4,command=calculate_simpleinterest)
calculate.place(x=20,y=250)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()