# This learniing tool assists with learning a new language.The game automatically starts with a french word
# and you have three seconds to indicate if you know the word or not. If you click the correct tick, then the word
# is actually removed as its a word that you know already. Subsequent games will not have those words.
# This game was built using the TKinter module



from tkinter import *
import time
import math
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except:
    df = pd.read_csv("./data/french_words.csv")
finally:
    word_dict = df.to_dict('records')

selected_word = ''



def remove_word():
    global selected_word

    print(len(word_dict))
    word_dict.remove(selected_word)

    words_to_learn_df= pd.DataFrame(word_dict)
    words_to_learn_df.to_csv('./data/words_to_learn.csv',index = False)




#Button Functions
def get_word():


    global selected_word, flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(word_dict)


    canvas.itemconfig(title_text, text='French', fill = "Black")
    canvas.itemconfig(word_text, text=selected_word["French"],fill = "Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)




def wrong_click():
    get_word()
    pass

def right_click():
    remove_word()
    get_word()
    pass

def flip_card():
    canvas.itemconfig(title_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, text = selected_word["English"],fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer= window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,263,image = card_front_img)

title_text = canvas.create_text(400,150, text = "", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263, text = "", font=("Ariel", 60, "bold"))
canvas.grid(column = 0,row = 0, columnspan= 2)
my_image = PhotoImage(file="./images/wrong.png")

wrong_btn = Button(image = my_image, command =wrong_click,  highlightthickness=0 )
wrong_btn.grid (column = 0, row = 1 )

my_image2 = PhotoImage(file="./images/right.png")

right_btn = Button(image = my_image2, command =right_click,  highlightthickness=0 )
right_btn.grid (column = 1, row = 1 )

get_word()

window.mainloop()


