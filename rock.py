import random
from tkinter import *
import tkinter.messagebox as tmsg

chances = 5
score = 0
cscore = 0
def update_score():
    mee2.config(text=f"Chances = {chances}       Score  computer = {cscore}      player ={score} ")

def click(event):
    global chances, score,cscore
    text = event.widget.cget("text")
    #print(text)
    list1 = ["Rock", "Paper", "Scissor","Fire","Water"]
    c = random.choice(list1)

    if chances == 0:
        if(score>cscore): win="player"
        else: win="computer"
        tmsg.showinfo("Game Over", f"final winer = {win} \nNo more chances! Game Over.")
        root.destroy()
        return

    if text == c:
        mes = "It's a tie"
    elif text == "Rock" :
        if c == "Scissor" or c == "Water":
            mes = "Player wins"
            score += 1
        else:
            mes = "Computer wins"
            cscore += 1
    elif text == "Paper":
        if c == "Rock" or c == "Water":
            mes = "Player wins"
            score += 1
        else:
            mes = "Computer wins"
            cscore += 1
    elif text == "Scissor":
        if c == "Paper" or c == "Water":
            mes = "Player wins"
            score += 1
        else:
            mes = "Computer wins"
            cscore += 1
    elif text == "Water":
        if c == "Fire":
            mes = "Player wins"
            score += 1
        else:
            mes = "Computer wins"
            cscore += 1
    elif text == "Fire":
        if c == "Paper" or c == "Rock" or c == "Scissor":
            mes = "Player wins"
            score += 1
        else:
            mes = "Computer wins"
            cscore += 1

    chances -= 1
    update_score()

    mee.config(text=f"Computer choice = {c}")
    mee1.config(text=f"Player choice = {text}")

    tmsg.showinfo("Winner", mes)

    if chances == 0:
        if(score>cscore): win="player"
        else: win="computer"
        tmsg.showinfo("Game Over", f"final winer = {win} \nNo more chances! Game Over.")
        root.destroy()

root = Tk()
root.geometry("870x450",)
root.title("Rock Paper Scissors")
root.iconbitmap("icon1.ico")
root.configure(bg='hotpink')
f1 = Frame(root, bg="gray")
b1 = Button(f1, text="Rock", font="lucida 25 bold",bg="darkorchid1")
b1.pack(side=LEFT, padx=18, pady=12)
b1.bind("<Button-1>", click)
b2 = Button(f1, text="Paper", font="lucida 25 bold",bg="cyan")
b2.pack(side=LEFT, padx=18, pady=12)
b2.bind("<Button-1>", click)
b3 = Button(f1, text="Scissor", font="lucida 25 bold",bg="darksalmon")
b3.pack(side=LEFT, padx=18, pady=12)
b3.bind("<Button-1>", click)
b4 = Button(f1, text="Fire", font="lucida 25 bold",bg="brown1")
b4.pack(side=LEFT, padx=18, pady=12)
b4.bind("<Button-1>", click)
b5 = Button(f1, text="Water", font="lucida 25 bold",bg="orange")
b5.pack(side=LEFT, padx=18, pady=12)
b5.bind("<Button-1>", click)
f1.pack()
f2 = Frame(root, bg="violetred")

mee1 = Label(f2,text="Player",bg="violetred",fg="yellow",font="lucida 20 bold")
mee1.pack(padx=18,pady=12)
mee = Label(f2,text="Computer",bg="violetred",fg="yellow",font="lucida 20 bold")
mee.pack(padx=18,pady=12)

mee2 = Label(text=f"Chances = {chances}         Score  computer = {cscore}      player ={score}  ",bg="hotpink",fg="blue",font="lucida 20 bold")
mee2.pack()
f2.pack(pady=12)
root.mainloop()
