from setting import *

class Game:
    def __init__(self, ball, canvas):
        self.hit_bottom = False
        self.start = False
        canvas.bind_all('<KeyPress-Return>', self.start_update)
        
    def check(self, ball, canva):    
        if ball.position[3] >= ball.ball_height:
            self.hit_bottom = True
            canva.create_text(TEXT_PLACE, TEXT_PLACE, text='Вы проиграли', font=('Helvetica', 25), fill=COLOR_TEXT)

    def start_update(self, event):
        self.start = True