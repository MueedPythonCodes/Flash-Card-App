import tkinter
from tkinter import Canvas, PhotoImage
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
displaying_card = {}
words_dic = {}


try:
    words = pandas.read_csv("data/learning_words.csv")
except FileNotFoundError:
    real_data = pandas.read_csv("data/french_words.csv")
    words_dic = real_data.to_dict(orient="records")

else:
    words_dic = words.to_dict(orient="records")
    # print(words_dic)


def new_card():
    global displaying_card, timer
    window.after_cancel(timer)
    displaying_card = random.choice(words_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=displaying_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=fr_img)
    timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=displaying_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)


def known():
    words_dic.remove(displaying_card)
    # print(len(words_dic))
    data = pandas.DataFrame(words_dic)
    data.to_csv("data/learning_words.csv", index=False)
    new_card()


window = tkinter.Tk()
window.title("Flash Car App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(5000, func=flip_card)


canvas = Canvas(width=650, height=500)
fr_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(325, 250, image=fr_img)
card_title = canvas.create_text(325, 150, font=("Arial", 30, "bold"))
card_word = canvas.create_text(325, 250, font=("Arial", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_img_btn = tkinter.Button(image=wrong_img, command=new_card)
wrong_img_btn.grid(row=1, column=0)


right_img = PhotoImage(file="images/right.png")
right_img_btn = tkinter.Button(image=right_img, command=known)
right_img_btn.grid(row=1, column=1)


new_card()

window.mainloop()
