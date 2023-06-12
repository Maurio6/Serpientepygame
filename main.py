import pygame
import sys
import time
import random

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 10

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Juego de la serpiente')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game states
game_started = False
game_over = False
show_instructions = False

# Game Over
def show_game_over_screen():
    game_window.fill(black)
    font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)

def show_start_screen():
    game_window.fill(black)
    font = pygame.font.SysFont('times new roman', 60)
    title_surface = font.render('Juego de la Serpiente', True, green)
    title_rect = title_surface.get_rect()
    title_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.blit(title_surface, title_rect)
    font = pygame.font.SysFont('times new roman', 30)
    start_surface = font.render('Press any key to start', True, white)
    start_rect = start_surface.get_rect()
    start_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(start_surface, start_rect)
    pygame.display.flip()

# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)

def reset_game():
    global snake_pos, snake_body, food_pos, food_spawn, direction, change_to, score, game_over, game_started
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    game_over = False
    game_started = False

def show_menu():
    game_window.fill(black)
    menu_font = pygame.font.SysFont('times new roman', 60)
    title_surface = menu_font.render('Juego de la Serpiente', True, green)
    title_rect = title_surface.get_rect()
    title_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(title_surface, title_rect)

    menu_font = pygame.font.SysFont('times new roman', 30)
    start_surface = menu_font.render('Iniciar Juego', True, white)
    start_rect = start_surface.get_rect()
    start_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
    game_window.blit(start_surface, start_rect)

    instructions_surface = menu_font.render('Instrucciones', True, white)
    instructions_rect = instructions_surface.get_rect()
    instructions_rect.midtop = (frame_size_x / 2, frame_size_y / 2 + 50)
    game_window.blit(instructions_surface, instructions_rect)

    quit_surface = menu_font.render('Salir', True, white)
    quit_rect = quit_surface.get_rect()
    quit_rect.midtop = (frame_size_x / 2, frame_size_y / 2 + 100)
    game_window.blit(quit_surface, quit_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    return
                elif instructions_rect.collidepoint(pygame.mouse.get_pos()):
                    show_instructions()
                elif quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

# ...

def show_instructions():
    game_window.fill(black)
    instructions_font = pygame.font.SysFont('times new roman', 30)
    instructions_surface1 = instructions_font.render('Instrucciones del Juego:', True, white)
    instructions_rect1 = instructions_surface1.get_rect()
    instructions_rect1.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(instructions_surface1, instructions_rect1)

    instructions_surface2 = instructions_font.render('Controla la serpiente utilizando las flechas del teclado', True, white)
    instructions_rect2 = instructions_surface2.get_rect()
    instructions_rect2.midtop = (frame_size_x / 2, frame_size_y / 4 + 50)
    game_window.blit(instructions_surface2, instructions_rect2)

    instructions_surface3 = instructions_font.render('Come la comida para crecer y aumentar tu puntaje', True, white)
    instructions_rect3 = instructions_surface3.get_rect()
    instructions_rect3.midtop = (frame_size_x / 2, frame_size_y / 4 + 100)
    game_window.blit(instructions_surface3, instructions_rect3)

    instructions_surface4 = instructions_font.render('Evita chocar con las paredes o tu propio cuerpo', True, white)
    instructions_rect4 = instructions_surface4.get_rect()
    instructions_rect4.midtop = (frame_size_x / 2, frame_size_y / 4 + 150)
    game_window.blit(instructions_surface4, instructions_rect4)

    back_surface = instructions_font.render('Volver al Menú', True, white)
    back_rect = back_surface.get_rect()
    back_rect.midtop = (frame_size_x / 2, frame_size_y / 4 + 250)
    game_window.blit(back_surface, back_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    return show_menu()

# ...


# Main game loop
while True:
    if not game_started:
        show_menu()
        game_started = True
        # show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game_started = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
            game_over = True
        if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            game_over = True
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over = True

        if game_over:
            show_game_over_screen()
            reset_game()

        show_score(1, white, 'consolas', 20)
        pygame.display.update()
        fps_controller.tick(difficulty)
