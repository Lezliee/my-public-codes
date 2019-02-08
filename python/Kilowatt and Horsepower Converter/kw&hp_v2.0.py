from tkinter import *


root = Tk()

val_hp = StringVar()
val_kw = StringVar()
output1 = StringVar()
output2 = StringVar()

output1.set("The result will appear here...")
output2.set("The result will appear here...")

topFrame = Frame(root)
topFrame.pack()
bottomFrame1 = Frame(root)
bottomFrame1.pack(side=BOTTOM)
bottomFrame2 = Frame(root)
bottomFrame2.pack(side=BOTTOM)
bottomFrame3 = Frame(root)
bottomFrame3.pack(side=BOTTOM)

entry_hp2 = Entry(bottomFrame2, textvariable=val_hp)
entry_kw1 = Entry(topFrame, textvariable=val_kw)


def quickMaths1():
    output1.set((int(val_kw.get()) * 1.3596216173))


def quickMaths2():
    output2.set((int(val_hp.get()) * 0.73549875))


button1 = Button(bottomFrame1, text="Go!", fg="red", command=quickMaths2)
button1.grid(row=0, column=2)

button2 = Button(bottomFrame3, text="Go!", fg="red", command=quickMaths1)
button2.grid(row=0, column=2)

label1 = Label(
    bottomFrame1, text="Kilowatt ans Horsepower converter by:Lezliee")
label1.grid(row=1, column=2)

label2 = Label(
    topFrame, text="Kw to Hp")
label3 = Label(
    bottomFrame2, text="Hp to Kw")

label2.grid(row=0, column=0)
label3.grid(row=0, column=0)


label_kw1 = Label(topFrame, text="Kw:")
label_hp1 = Label(topFrame, text="Hp:")
label4 = Label(topFrame, text="to")
output_result1 = Entry(topFrame, textvariable=output1)


label_kw1.grid(row=1, column=0)
entry_kw1.grid(row=1, column=1)
label4.grid(row=1, column=2)
label_hp1.grid(row=1, column=3)
output_result1.grid(row=1, column=4)


label_kw2 = Label(bottomFrame2, text="Kw:")
label_hp2 = Label(bottomFrame2, text="Hp:")
label5 = Label(bottomFrame2, text="to")
output_result2 = Entry(bottomFrame2, textvariable=output2)


label_kw2.grid(row=1, column=3)
output_result2.grid(row=1, column=4)
label5.grid(row=1, column=2)
label_hp2.grid(row=1, column=0)
entry_hp2.grid(row=1, column=1)


root.mainloop()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                Code by: Lezliee
#                                                          (https://github.com/Lezliee)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
