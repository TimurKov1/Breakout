import random
from setting import *

class Breakout_Ball:
    def __init__(self, canva, board, score, color):
        self.canva = canva
        self.board = board
        self.score = score
        self.color = color

        self.id = canva.create_oval(BALL_WIDTH, BALL_WIDTH, BALL_HEIGHT, BALL_HEIGHT, fill=self.color)
        self.canva.move(self.id, BALL_PLACE_WIDTH, BALL_PLACE_HEIGHT)

        start_position = START_POSITION
        random.shuffle(start_position)

        self.x = start_position[0]
        self.y = -2

        self.ball_height = self.canva.winfo_height()
        self.ball_width = self.canva.winfo_width()
        self.hit_bottom = False

    def hit_board(self, position):
        board_position = self.canva.coords(self.board.id)

        if position[2] >= board_position[0] and position[0] <= board_position[2]:
            if position[3] >= board_position[1] and position[3] <= board_position[3]:

                self.score.point()
                return True

        return False

    def move(self, color):
        self.canva.move(self.id, self.x, self.y)
        self.position = self.canva.coords(self.id)

        if self.position[1] <= 0:
            self.y = 2

        if self.position[3] >= self.ball_height:
            self.hit_bottom = True
            self.canva.create_text(TEXT_PLACE, TEXT_PLACE, text='Вы проиграли', font=('Helvetica', 25), fill=color)

        if self.hit_board(self.position) == True:
            self.y = -2

        if self.position[0] <= 0:
            self.x = 2

        if self.position[2] >= self.ball_width:
            self.x = -2

class Breakout_Board:
    def __init__(self, canva, color):
        self.canva = canva
        self.id = canva.create_rectangle(0, 0, BOARD_WIDTH, BOARD_HEIGHT, fill=color)

        start_1_position = START_1_POSITION
        random.shuffle(start_1_position)

        self.x = start_1_position[0]

        self.canva.move(self.id, self.x, BOARD_PLACE)

        self.x_position = 0
        self.board_width = self.canva.winfo_width()
        self.canva.bind_all('<KeyPress-Right>', self.move_right)
        self.canva.bind_all('<KeyPress-Left>', self.move_left)

    def move_right(self, event):
        self.x_position = 2

    def move_left(self, event):
        self.x_position = -2

    def move(self):
        self.canva.move(self.id, self.x_position, 0)
        position = self.canva.coords(self.id)

        if position[0] <= 0:
            self.x_position = 0

        if position[2] >= self.board_width:
            self.x_position = 0

class Breakout_Score:
    def __init__(self, canva, color):
        self.ball_score = 0
        self.canva = canva
        self.id = canva.create_text(SCORE_PLACE_WIDTH, SCORE_PLACE_HEIGHT, text=self.ball_score, font=('Helvetica', 20), fill=color)

    def point(self):
        self.ball_score += 1
        self.canva.itemconfig(self.id, text=self.ball_score)