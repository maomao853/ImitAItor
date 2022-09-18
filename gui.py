import nlp
import random
import time
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

### Code
submittedP1 = False
submittedP2 = False
answeredP1 = False
answeredP2 = False
submissionP1 = 0
submissionP2 = 0
correctP1 = False
correctP2 = False

newPrompt = nlp.getPrompt()
sentences = []
winning = 0
resetFlag = False

def updateWinner():
    global correctP1, correctP2, resetFlag
    p1 = correctP1
    p2 = correctP2
    print(f"1{p1}")
    print(f"2{p2}")
    if p1 == p2:
        winner = "Winner: Tie"
    elif p1 == True and p2 == False:
        winner = "Winner: Player 1"
    elif p1 == False and p2 == True:
        winner = "Winner: Player 2"

    canvas.itemconfig(win, text=winner)

def buttonClick(but, player):
    global answeredP1, answeredP2, submittedP1, submittedP2, correctP1, correctP2, resetFlag
    
    print(f"button{but} pressed")
    print(correctP1)
    print(correctP2)
    if player == 1:
        if but == ai:
            correctP1 = True
        else:
            correctP1 = False
        answeredP1 = True
    elif player == 2:
        if but == ai:
            correctP2 = True
        else:
            correctP2 = False
        answeredP2 = True

    print("final " + str(correctP1))
    print("final " + str(correctP2))
    if answeredP1 and answeredP2:
        updateWinner()
        


def genText():
    global ai
    textAI = nlp.getSentences(newPrompt)

    sentences.append(textAI)
    random.shuffle(sentences)

    temp = []

    for i, text in enumerate(sentences):
        print(f"{i} {text}")
        temp.append(text)
        if text == textAI:
            ai = i+1
            print(f"ai{ai}")

    
    entry_3.insert(END, temp[0])
    entry_2.insert(END, temp[1])
    entry_4.insert(END, temp[2])

    

def playerSubmission(txt):
    global submittedP1, submittedP2, submissionP1, submissionP2
    wrong = txt.get()
    sentences.append(wrong)
    txt.delete(0, "end")
    print(wrong)
    if not submittedP1:
        submissionP1 = findMatch(wrong)
        submittedP1 = True
    elif not submittedP2:
        submissionP2 = findMatch(wrong)
        submittedP2 = True
        genText()


def findMatch(match):
    for i, text in enumerate(sentences):
        if text == match:
            return(i)
        else:
            return(-1)

###
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1299x843")
window.configure(bg="#FFFFFF")

canvas = Canvas(window,
                bg="#FFFFFF",
                height=843,
                width=1299,
                bd=0,
                highlightthickness=0,
                relief="ridge")

canvas.place(x=0, y=0)
canvas.create_rectangle(0.0,
                        0.0,
                        1299.0,
                        843.6627197265625,
                        fill="#F0F0F0",
                        outline="")

canvas.create_rectangle(340.2142639160156,
                        42.097198486328125,
                        958.7857360839844,
                        115.98211669921875,
                        fill="#D3D3D3",
                        outline="")

canvas.create_text(548.2559509277344,
                   52.695404052734375,
                   anchor="nw",
                   text="ImitAItor",
                   fill="#000000",
                   font=("Consolas", 41 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(649.5, 672.6963958740234, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", highlightthickness=0)
entry_1.place(x=217.359130859375,
              y=642.626953125,
              width=864.28173828125,
              height=58.138885498046875)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(649.5, 431.2817077636719, image=entry_image_2)
entry_2 = Text(bd=0, bg="#D9D9D9", highlightthickness=0, font="montserrat 16")
entry_2.place(x=176.98016357421875,
              y=376.2975769042969,
              width=945.0396728515625,
              height=107.96826171875)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(649.5, 310.144832611084, image=entry_image_3)
entry_3 = Text(bd=0, bg="#D9D9D9", highlightthickness=0, font="montserrat 16")
entry_3.place(x=176.98016357421875,
              y=255.16070556640625,
              width=945.0396728515625,
              height=107.96825408935547)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(649.5, 552.4186706542969, image=entry_image_4)
entry_4 = Text(bd=0, bg="#D9D9D9", highlightthickness=0, font="montserrat 16")
entry_4.place(x=176.98016357421875,
              y=497.4345397949219,
              width=945.0396728515625,
              height=107.96826171875)

prompt = canvas.create_text(350.9365234375,
                            130.5872802734375,
                            anchor="nw",
                            text=newPrompt + "...  [Finish the sentence]",
                            fill="#000",
                            font=("MontserratRoman Regular", 27 * -1))

win = canvas.create_text(219.9365234375,
                         189.86705017089844,
                         anchor="nw",
                         text="Winner: ",
                         fill="#000000",
                         font=("MontserratRoman Regular", 27 * -1))

### Buttons (by number)
"""
L   R
2   1
5   4
6   3
"""

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(1, 2),
                  relief="flat")
button_1.place(x=1169.2718505859375,
               y=280.07537841796875,
               width=60.138916015625,
               height=60.138893127441406)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: playerSubmission(entry_1),
                  relief="flat")
button_2.place(x=460.4920654296875,
               y=745.7222900390625,
               width=378.015869140625,
               height=54.984130859375)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(1, 1),
                  relief="flat")
button_3.place(x=69.58929443359375,
               y=280.07537841796875,
               width=60.138885498046875,
               height=60.138893127441406)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(3, 2),
                  relief="flat")
button_4.place(x=1169.2718505859375,
               y=522.3491821289062,
               width=60.138916015625,
               height=60.138885498046875)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(2, 2),
                  relief="flat")
button_5.place(x=1169.2718505859375,
               y=401.2123107910156,
               width=60.138916015625,
               height=60.138885498046875)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(2, 1),
                  relief="flat")
button_6.place(x=69.58929443359375,
               y=401.2123107910156,
               width=60.138885498046875,
               height=60.138885498046875)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: buttonClick(3, 1),
                  relief="flat")
button_7.place(x=69.58929443359375,
               y=522.3491821289062,
               width=60.138885498046875,
               height=60.138885498046875)

canvas.create_text(35.02032470703125,
                   220.5917510986328,
                   anchor="nw",
                   text="PLAYER 1",
                   fill="#000000",
                   font=("MontserratRoman Regular", 27 * -1))

canvas.create_text(1139.202392578125,
                   220.5917510986328,
                   anchor="nw",
                   text="PLAYER 2",
                   fill="#000000",
                   font=("MontserratRoman Regular", 27 * -1))

window.resizable(False, False)
window.mainloop()
