import sys, pygame, time
from moves import Moves 
from settings import Settings 

class Main:
    def __init__(self):
        pygame.init()
        self.s = Settings()
        self.moves = Moves()
        self.X = self.s.X
        self.Y = self.s.Y

        pygame.display.set_caption("Chance Dance")
        self.disp_text(32, 'How many dance moves?', (self.X//2,self.Y//2))
        self.length = int(self.user_input())
        self.filename = "moves_"+str(time.time())+".txt"

    def draw_stage(self):
        '''Draw stage positions (upstage center etc.)'''
        for i in range(0,self.X,self.X//3):
            for j in range(0,self.Y,self.Y//3):
                pygame.draw.rect(
                    self.s.screen,self.s.red,pygame.Rect((i,j),
                    (self.X//3,self.Y//3)),1
                )

    def disp_text(self, size, string, pos):
        '''Display miscellaneous text'''
        font = pygame.font.SysFont('timesnewroman', size)
        text = font.render(string, True, self.s.white, self.s.black)
        text_rect = text.get_rect()
        text_rect.center = pos
        self.s.screen.blit(text, text_rect)
        pygame.display.flip()


    def user_input(self):
        '''Get numerical user input'''
        runs = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isnumeric():
                        runs += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        runs = runs[:-1]
                    elif event.key == pygame.K_RETURN:
                        return runs
            self.disp_text(16,runs,(self.X//3+32,self.Y//3+128))

    def run(self):
        '''Main game loop'''
        with open(self.filename, "w") as f:
            for i in range(0, self.length):
                self.s.screen.fill(self.s.black)
                self.draw_stage()

                move = self.moves.get_move()
                self.disp_text(16, move, (24,self.Y-16))
                self.moves.show_move(move)
                square = self.moves.walk()
                f.write("Move: " + move + "\r\n")
                f.write("Square: " + square + "\r\n")
                f.write("\r\n")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                pygame.display.flip()
                time.sleep(1)

if __name__ == '__main__':
    game = Main()
    game.run()
