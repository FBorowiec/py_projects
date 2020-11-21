from tkinter import *

class Window:
    def __init__(self):
        self.window = Tk()

        self.add_labels()
        self.add_entries()
        self.add_list_with_scrollbar()
        self.add_buttons()

        self.window.mainloop()

    def add_labels(self):
        l1 = Label(self.window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(self.window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(self.window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(self.window, text="ISBN")
        l4.grid(row=1, column=2)

    def add_entries(self):
        title_text = StringVar()
        e1 = Entry(self.window, textvariable=title_text)
        e1.grid(row=0, column=1)

        author_text = StringVar()
        e2 = Entry(self.window, textvariable=author_text)
        e2.grid(row=0, column=3)

        year_text = StringVar()
        e3 = Entry(self.window, textvariable=year_text)
        e3.grid(row=1, column=1)

        isbn_text = StringVar()
        e4 = Entry(self.window, textvariable=isbn_text)
        e4.grid(row=1, column=3)

    def add_list_with_scrollbar(self):
        list1 = Listbox(self.window, height=6, width=35)
        list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(self.window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview())

    def add_buttons(self):
        b1 = Button(self.window, text="View all", width=12)
        b1.grid(row=2, column=3)

        b2 = Button(self.window, text="Search entry", width=12)
        b2.grid(row=3, column=3)

        b3 = Button(self.window, text="Add entry", width=12)
        b3.grid(row=4, column=3)

        b4 = Button(self.window, text="Update selected", width=12)
        b4.grid(row=5, column=3)

        b5 = Button(self.window, text="Delete selected", width=12)
        b5.grid(row=6, column=3)

        b6 = Button(self.window, text="Close", width=12)
        b6.grid(row=7, column=3)
