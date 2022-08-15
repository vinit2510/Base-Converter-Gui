from tkinter import Tk, Button, Label, StringVar, Entry, Spinbox, IntVar, PhotoImage


def btn_press(event=""):
    num = list(str(num_var.get()).upper())
    fst_base = from_var.get()
    snd_base = to_var.get()

    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    str_nums = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
    int_nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    for i in range(26):
        while alpha[i] in num:
            idx = num.index(alpha[i])
            num[idx] = str_nums[i]

    deci = []

    for i in range(len(num)):
        deci.append(int(num[i])*(fst_base)**(len(num)-i-1))

    decimal = sum(deci)

    bits_lst = []
    bit = ""

    while decimal > 0:
        bits_lst.append(decimal % snd_base)
        decimal = decimal//snd_base
    bits_lst = bits_lst[::-1]

    for i in range(26):
        while int_nums[i] in bits_lst:
            idx = bits_lst.index(int_nums[i])
            bits_lst[idx] = alpha[i]

    bit = ''.join(map(str, bits_lst))

    temp = Label(main_wind, text="              ", font=(
        "Consolas", 15, "bold"), bg="#45464f", borderwidth=3)
    temp.grid(row=5, column=2, pady=25, ipadx=20, ipady=5)

    if len(bit) <= 14:
        ans_lbl = Label(main_wind, text=bit, font=(
            "Consolas", 15, "bold"), relief="solid", borderwidth=3)
        ans_lbl.grid(row=5, column=2, pady=25, ipadx=20, ipady=5)
    elif len(bit) >= 15 and len(bit) <= 17:
        ans_lbl = Label(main_wind, text=bit, font=(
            "Consolas", 12, "bold"), relief="solid", borderwidth=3)
        ans_lbl.grid(row=5, column=2, pady=25, ipadx=20, ipady=5)
    else:
        ans_lbl = Label(main_wind, text=bit, font=(
            "Consolas", 11, "bold"), relief="solid", borderwidth=3)
        ans_lbl.grid(row=5, column=2, pady=25, ipadx=20, ipady=5)

    for i in range(len(num)):
        if int(num[i]) >= fst_base:
            ans_lbl.destroy()
            valid_lbl = Label(main_wind, text="Number is Not Valid", font=(
                "Consolas", 11, "bold"), relief="solid", borderwidth=3)
            valid_lbl.grid(row=5, column=2, pady=25, ipadx=20, ipady=5)


if __name__ == "__main__":

    main_wind = Tk()
    main_wind.title("Base Convertor")
    main_wind.geometry("310x370")
    main_wind.minsize(310, 370)
    main_wind.maxsize(310, 370)
    main_wind.configure(background="#45464f")
    

    num_var = StringVar()
    from_var = IntVar()
    to_var = IntVar()

    lbl1 = Label(main_wind, text='Base Convertor', font=(
        "Consolas", 17, "bold"), relief='ridge', borderwidth=3)
    lbl1.grid(pady=15, row=0, column=2, padx=5)

    lbl2 = Label(main_wind, text='Number', font=(
        "Consolas", 12, "bold"), relief='solid', borderwidth=2)
    lbl2.grid(row=1, column=1)

    num_entry = Entry(main_wind, textvariable=num_var, font=(
        "Consolas", 12, "bold"), insertbackground="red")
    num_entry.grid(row=1, column=2, pady=20)

    lbl3 = Label(main_wind, text='From', font=(
        "Consolas", 12, "bold"), relief='solid', borderwidth=2)
    lbl3.grid(row=2, column=1, ipadx=8)

    from_spin = Spinbox(main_wind, from_=2, to=36, textvariable=from_var, font=(
        "Consolas", 12, "bold"), width=4, insertbackground="red")
    from_spin.grid(row=2, column=2, pady=10)

    lbl4 = Label(main_wind, text='To ', font=(
        "Consolas", 12, "bold"), relief='solid', borderwidth=2)
    lbl4.grid(row=3, column=1, ipadx=12)

    to_spin = Spinbox(main_wind, from_=2, to=36, textvariable=to_var, font=(
        "Consolas", 12, "bold"), width=4, insertbackground="red")
    to_spin.grid(row=3, column=2)

    btn = Button(main_wind, text='Calculate', command=btn_press, font=(
        "Consolas", 12, "bold"), relief="solid", borderwidth=2)
    btn.grid(row=4, column=2, pady=30)

    main_wind.bind('<F9>', btn_press)

    main_wind.mainloop()
