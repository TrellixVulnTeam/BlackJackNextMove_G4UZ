from tkinter import *

root = Tk()
root.title("Blackjack Move Calculator")
root.geometry('600x300')

# Player and dealer cards chosen from Radiobutton.
pc1 = IntVar()
pc2 = IntVar()
dc1 = IntVar()

intro_Label = Label(root, text='Blackjack Move Calculator - Giving you the best move for your cards')
card1_Label = Label(root, text='Whats your first card?')

intro_Label.place(relx=0.5, rely=0, anchor="n")
card1_Label.place(relx=0.5, rely=0.1, anchor="n")


Radiobutton(root, text="A", variable=pc1, value=1).place(relx=0.05, rely=0.2, anchor="w")
Radiobutton(root, text="2", variable=pc1, value=2).place(relx=0.12, rely=0.2, anchor="w")
Radiobutton(root, text="3", variable=pc1, value=3).place(relx=0.19, rely=0.2, anchor="w")
Radiobutton(root, text="4", variable=pc1, value=4).place(relx=0.26, rely=0.2, anchor="w")
Radiobutton(root, text="5", variable=pc1, value=5).place(relx=0.33, rely=0.2, anchor="w")
Radiobutton(root, text="6", variable=pc1, value=6).place(relx=0.40, rely=0.2, anchor="w")
Radiobutton(root, text="7", variable=pc1, value=7).place(relx=0.47, rely=0.2, anchor="w")
Radiobutton(root, text="8", variable=pc1, value=8).place(relx=0.54, rely=0.2, anchor="w")
Radiobutton(root, text="9", variable=pc1, value=9).place(relx=0.61, rely=0.2, anchor="w")
Radiobutton(root, text="10", variable=pc1, value=10).place(relx=0.68, rely=0.2, anchor="w")
Radiobutton(root, text="J", variable=pc1, value=11).place(relx=0.75, rely=0.2, anchor="w")
Radiobutton(root, text="Q", variable=pc1, value=12).place(relx=0.82, rely=0.2, anchor="w")
Radiobutton(root, text="K", variable=pc1, value=13).place(relx=0.89, rely=0.2, anchor="w")

print(pc1.get())
#labelPrint = Label(root, text=pc1.get()).place(relx=.05, rely=0.5)

#pc1 = tkinter.StringVar()



#tkinter.Label(frame1, text="Blackjack Move Calculator - Giving you the best move for your cards", padx=150, pady=5)\
 #   .pack()

#tkinter.Label(frame1, text="Whats your first card?").pack()

#rad1 = tkinter.Radiobutton(root, frame3, text="A", variable=pc1, value=1).pack(side=TOP)
#rad2 = tkinter.Radiobutton(root, frame4, text="2", variable=pc1, value=2).pack()
#rad3 = tkinter.Radiobutton(root, frame5, text="3", variable=pc1, value=3).pack()
#rad4 = tkinter.Radiobutton(root, frame6, text="4", variable=pc1, value=4).pack()
#rad5 = tkinter.Radiobutton(root, frame7, text="4", variable=pc1, value=5).pack()

root.mainloop()

#print(pc1.get())