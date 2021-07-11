import random
from tkinter import *

# Constantes
LOWER_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

# open tkinter window
root = Tk()
root.title('Password Generator')
root.iconbitmap('./lock.ico')
root.geometry("600x550")
root['background'] = '#3D3C3F'

# create label for text
heading = Label(root, text='Password Generator', font="Helvetica 16", pady=15, bg='#3D3C3F', fg='#f5ffff')
heading.grid(row=0, column=0)
root.grid_columnconfigure(0, weight=1)  # to center the heading

# create checkboxes
frame_1 = LabelFrame(root, padx=30, pady=0, bg='#3D3C3F', borderwidth=0, highlightthickness=0)
frame_1.grid(row=1, column=0, sticky='W')
include_upper = IntVar()
include_lower = IntVar()
include_numbers = IntVar()
include_symbols = IntVar()
uppercase_letters = Checkbutton(frame_1, text="Would you like to include uppercase letters?", variable=include_upper,
                                font="Helvetica 10 bold", bg='#3D3C3F', fg='#E8E8E9')
lowercase_letters = Checkbutton(frame_1, text="Would you like to include lowercase letters?", variable=include_lower,
                                font="Helvetica 10 bold", bg='#3D3C3F', fg='#E8E8E9')
numbers = Checkbutton(frame_1, text="Would you like to include numbers?", variable=include_numbers,
                      font="Helvetica 10 bold", bg='#3D3C3F', fg='#E8E8E9')
symbols = Checkbutton(frame_1, text="Would you like to include symbols?", variable=include_symbols,
                      font="Helvetica 10 bold", bg='#3D3C3F', fg='#E8E8E9')
# display chechboxes
uppercase_letters.grid(row=0, column=0, pady=20, sticky='W')
lowercase_letters.grid(row=1, column=0, sticky='W')
numbers.grid(row=2, column=0, pady=20, sticky='W')
symbols.grid(row=3, column=0, sticky='W')

# create frame2
frame_2 = LabelFrame(root, padx=30, pady=0, bg='#3D3C3F', borderwidth=0, highlightthickness=0)
frame_2.grid(row=2, column=0, sticky='W')
#       create a line to separate between frames
my_canvas = Canvas(frame_2, width=530, height=0, bg="#86848D", borderwidth=1, highlightthickness=0)
my_canvas.grid(row=0, column=0, pady=30)
#       create input field and display it
input_box = Entry(frame_2, width=30, bg='#3D3C3F', fg='#E8E8E9', font="Helvetica 11", borderwidth=1,
                  highlightthickness=1)
input_box.config(highlightbackground="#86848D", highlightcolor="#eeeeee")
input_box.insert(0, "Enter the length of your password: ")
input_box.grid(row=1, column=0, columnspan=3, padx=0, pady=5, ipady=10, sticky='W')


# copy password to clipboard
def copy_clipboard(psswd):
    root.clipboard_clear()
    # text to clipboard
    root.clipboard_append(psswd)
    # text from clipboard
    clip_psswd = root.clipboard_get()
    print(clip_psswd)


psswd_btns = []  # to keep track of older psswd and don't display them


# generate password and display it
def generate():
    psswd_len = int(input_box.get())
    psswd = ""
    choices = []

    if include_lower.get():
        choices.append(LOWER_LETTERS)
    if include_upper.get():
        choices.append(UPPER_LETTERS)
    if include_numbers.get():
        choices.append(NUMBERS)
    if include_symbols.get():
        choices.append(SYMBOLS)

    for i in range(psswd_len):
        rnd_choice = random.randint(0, len(choices) - 1)
        index = random.randint(0, len(choices[rnd_choice]) - 1)
        psswd += choices[rnd_choice][index]

    input_box.delete(0, 'end')
    myLabel = Label(frame_2, text="Click at your password to copy it into the clipboard", bg='#3D3C3F', fg='#E8E8E9',
                    font="Helvetica 10")
    myLabel.grid(row=3, column=0, padx=0, pady=8)
    frame_2.grid_columnconfigure(0, weight=1)  # to center the label + password
    copy_btn = Button(frame_2, text=psswd, fg="#f4f4f4", bg="#313133", command=lambda: copy_clipboard(psswd))
    copy_btn.grid(row=4, column=0, ipadx=7, ipady=8, pady=4)
    psswd_btns.append(copy_btn)
    if len(psswd_btns) > 1:
        for i in range(0, len(psswd_btns) - 1):
            psswd_btns[i].grid_forget()


generate_psswd_btn = Button(frame_2, text="Generate Your Password", font="Helvetica 9", fg="#f4f4f4", bg="#313133",
                            borderwidth=1, highlightthickness=7, command=generate)
generate_psswd_btn.config(highlightbackground="#575499", highlightcolor="#575499")
generate_psswd_btn.grid(row=2, column=0, padx=0, pady=15, sticky='W')

root.mainloop()
