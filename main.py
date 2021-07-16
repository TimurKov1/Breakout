from tkinter import *
import time
from setting import *
from game_1 import *
from flask import Flask
from game import Breakout_Ball, Breakout_Board, Breakout_Score
import random

window = Tk()
window.title(NAME)
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)

canva = Canvas(window, width=WIDTH, height=HEIGHT, highlightthickness=0, bg='gray')
canva.pack()
window.update()

board = Breakout_Board(canva, COLOR_BOARD)
score = Breakout_Score(canva, COLOR_SCORE)
ball = Breakout_Ball(canva, board, score, COLOR_BALL)
game = Game(ball, canva)

while not game.hit_bottom:
    if game.start:
        ball.move(COLOR_TEXT)
        board.move()
        game.check(ball, canva)
        

    window.update_idletasks()
    window.update()
    if score.ball_score <= 5:
        time.sleep(0.00005)

    elif score.ball_score <= 10:
        time.sleep(0.01)

    elif score.ball_score > 10:
        time.sleep(0)

    if score.ball_score == 5:
        text = ball.canva.create_text(TEXT_PLACE, TEXT_PLACE, text='Вы набрали 5 очков', font=('Helvetica', 25), fill=COLOR_TEXT)
    
    if score.ball_score > 5:
        canva.delete(text)



time.sleep(5)
