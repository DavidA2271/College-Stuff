from tkinter import Frame, Button


class ButtonFrame(Frame):
    """ Base class used to helpme make frames with many buttons """

    def __init__(self, master, btn_per_row: int):
        super().__init__(master=master)
        self.btn_per_row = btn_per_row

        self.buttons: dict[int, Button] = {}

    def make_button_grid(self, count: int, btn_text: list):
        """ instantiates buttons and saves them in a dict """

        text = []
        for item in btn_text:
            text.append(str(item))

        for i in range(count):
            row = int(i/self.btn_per_row) + 1
            col = i % self.btn_per_row

            btn = Button(self, text=text[i], command=lambda j=i: self.on_btn_click(j))
            btn.grid(row=row, column=col, sticky='ew', padx=20, pady=20)
            self.buttons[i] = btn
            self.grid_columnconfigure(col, weight=1)

    def on_btn_click(self, btn_index: int):
        """ called when button is clicked. meant to be implemented by child classes """

        raise NotImplementedError

    def update_button(self, btn_index: int, text: str):
        """ updates text and positioning of the button """

        if self.buttons.keys().__contains__(btn_index):
            self.buttons[btn_index].config(text=text)
        else:
            self.buttons[btn_index] = Button(self, text=text,
                                             command=lambda: self.on_btn_click(btn_index))
            row = int((len(self.buttons) - 1) / self.btn_per_row) + 1
            col = (len(self.buttons) - 1) % self.btn_per_row
            self.buttons[btn_index].grid(row=row, column=col, sticky='ew', padx=20, pady=20)
            self.grid_columnconfigure(col, weight=1)
