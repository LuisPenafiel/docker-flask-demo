from flask import Flask, render_template
import threading
import pygame
import random
import os

# Disable Pygame audio to prevent ALSA errors
os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ['SDL_VIDEODRIVER'] = 'dummy'  # For headless environments

app = Flask(__name__)

class Cube:
    def __init__(self, start, rows, dirnx=0, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.rows = rows
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def draw(self, surface, eyes=False):
        size = surface.get_width() // self.rows
        i, j = self.pos
        pygame.draw.rect(surface, self.color, (i*size+1, j*size+1, size-2, size-2))
        if eyes:
            centre = size // 2
            radius = 3
            eye1 = (i*size + centre - radius, j*size + 8)
            eye2 = (i*size + size - radius*2, j*size + 8)
            pygame.draw.circle(surface, (0,0,0), eye1, radius)
            pygame.draw.circle(surface, (0,0,0), eye2, radius)

class Snake:
    def __init__(self, color, pos, rows):
        self.color = color
        self.rows = rows
        self.head = Cube(pos, self.rows, color=color)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.dirnx != 1:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_RIGHT] and self.dirnx != -1:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_UP] and self.dirny != 1:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_DOWN] and self.dirny != -1:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, cube in enumerate(self.body):
            p = cube.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.dirnx, cube.dirny = turn
                if i == len(self.body)-1:
                    self.turns.pop(p)
            cube.pos = (
                (cube.pos[0] + cube.dirnx) % self.rows,
                (cube.pos[1] + cube.dirny) % self.rows
            )

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        new_pos = (tail.pos[0] - dx, tail.pos[1] - dy)
        new_cube = Cube(new_pos, self.rows, dx, dy, self.color)
        self.body.append(new_cube)

    def reset(self, pos):
        self.body = []
        self.head = Cube(pos, self.rows, color=self.color)
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            cube.draw(surface, eyes=(i == 0))

def randomSnack(rows, snake):
    while True:
        x = random.randrange(1, rows-1)
        y = random.randrange(1, rows-1)
        if all((x, y) != cube.pos for cube in snake.body):
            return (x, y)

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for _ in range(rows):
        x += sizeBtwn
        y += sizeBtwn
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

@app.route('/')
def home():
    return render_template('game.html', game_content="<div id='game-frame'>Game loading...</div>")

def run_pygame():
    width = 500
    rows = 20
    pygame.init()
    
    # Try to create window, fallback to dummy mode if needed
    try:
        win = pygame.display.set_mode((width, width))
    except pygame.error:
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        win = pygame.display.set_mode((1, 1))  # Minimal window
        
    pygame.display.set_caption("Snake Game")
    s = Snake((255,0,0), (10,10), rows)
    snack = randomSnack(rows, s)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        pygame.time.delay(50)
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        s.move()
        
        if s.head.pos == snack:
            s.addCube()
            snack = randomSnack(rows, s)

        for cube in s.body[1:]:
            if cube.pos == s.head.pos:
                s.reset((10,10))
                break

        if win.get_size() != (1, 1):  # Only draw if we have a real window
            win.fill((0,0,0))
            drawGrid(width, rows, win)
            s.draw(win)
            pygame.draw.rect(win, (0,255,0), 
                           (snack[0]*(width//rows)+1, 
                            snack[1]*(width//rows)+1,
                            (width//rows)-2, 
                            (width//rows)-2))
            pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    # Start Pygame in main thread
    pygame_thread = threading.Thread(target=run_pygame)
    pygame_thread.daemon = True
    pygame_thread.start()
    
    # Start Flask
    app.run(host='0.0.0.0', port=5000, use_reloader=False)