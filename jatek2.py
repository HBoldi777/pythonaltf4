from n_mygameworld import *
from n_menu_menustage import *
import random


class GameStage(MyStage):

    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pontszam = 0
    betutipus = pygame.font.SysFont(None, 40)
    lastkey = None

    def back(self, pos, btn):
        self.menu.menu_Main()

    def keyuplistener(self, key, mod):
        print("UP")
        self.lastkey = None

    def keydownlistener(self, key, mod, unicode):
        print("DOWN")
        self.lastkey = key

    def pontszam_kirajzolasa(self):
        pontszam_txt = "Pontszám: " + str(self.pontszam)
        pontszam_img = self.betutipus.render(pontszam_txt, True, (100, 50, 255))
        self.screen.blit(pontszam_img, (0, 0))

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.borderbal: MyActor = MyActor("border1.png", pos=(0, 0), anchor=(16, 16))
        self.add_actor(self.borderbal)
        self.borderjobb: MyActor = MyActor("border1.png", pos=(0, 1000), anchor=(16, 16))
        self.add_actor(self.borderjobb)
        self.food: MyActor = MyActor("ama.png", pos=(200, 200), anchor=(16, 16))
        self.add_actor(self.food)
        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)
        self.snake: MyActor = MyActor("kocka.png", pos=(300, 300), anchor=(16, 16))
        self.add_actor(self.snake)

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        if self.lastkey != None:
            if self.lastkey == keys.UP:
                animate(self.snake, pos=(self.snake.pos[0], self.snake.pos[1] - 1000), duration=4)
                self.snake.set_rotation(360)
            if self.lastkey == keys.DOWN:
                animate(self.snake, pos=(self.snake.pos[0], self.snake.pos[1] + 1000), duration=4)
                self.snake.set_rotation(180)
            if self.lastkey == keys.LEFT:
                animate(self.snake, pos=(self.snake.pos[0] - 1000, self.snake.pos[1]), duration=4)
                self.snake.set_rotation(90)
            if self.lastkey == keys.RIGHT:
                animate(self.snake, pos=(self.snake.pos[0] + 1000, self.snake.pos[1]), duration=4)
                self.snake.set_rotation(270)

        if self.food.is_on_stage() and self.food.overlaps_with(self.snake):
            self.pontszam += 1
            print(self.pontszam)
            self.food.set_x(x=random.randint(64, self.screen_width))
            self.food.set_y(y=random.randint(64, self.screen_height))

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderbal):
            self.snake.remove_from_stage()

        if self.snake.is_on_stage() and self.snake.overlaps_with(self.borderjobb):
            self.snake.remove_from_stage()









