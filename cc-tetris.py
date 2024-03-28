import pygame

pygame.init()
pygame.display.set_caption('CC TETRIS')
screen_width = 750
screen_height = 450
#color definition
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
obstacle_x = 400
obstacle_y = 400
obstacle_width = 40
obstacle_height = 40
# Tetris single block dimensions
base_unit_width = 20
base_unit_eight = 20
player_x = 200
player_y = 400
player_width = 20
player_height = 20
game_state = "start_menu"

# Render long text on multiple lines
def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def draw_start_menu():
    screen.fill(black)
    font = pygame.font.SysFont('Red Hat Mono', 40)
    font_hint = pygame.font.SysFont('Red Hat Mono', 11)
    title = font.render('Coding Challenge Tetris', True, (255, 255, 255))
    hint = font_hint.render('Press <space> to Start', True, (255, 255, 255))
    help = font_hint.render('Press <h> for Help', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(hint, (screen_width/2 - hint.get_width()/2, screen_height/10 + hint.get_height()/2 + 300))
    screen.blit(help, (screen_width/2 - help.get_width()/2, screen_height/10 + help.get_height()/2 + 330))
    pygame.display.update()

def draw_game_over_screen():
    screen.fill(black)
    font = pygame.font.SysFont('Red Hat Mono', 40)
    font_hint = pygame.font.SysFont('Red Hat Mono', 11)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font_hint.render('Press <r> to Restart', True, (255, 255, 255))
    quit_button = font_hint.render('Press <q> to Quit', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
    screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/8 + restart_button.get_height() + 300))
    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/9 + quit_button.get_height()/2 + 330))
    screen.blit
    pygame.display.update()

def draw_board_game_screen():
    screen.fill(black)
    font = pygame.font.SysFont('Red Hat Mono', 40)
    font_hint = pygame.font.SysFont('Red Hat Mono', 11)
    title = font.render('Score:', True, (255, 255, 255))
    quit_button = font_hint.render('Press <q> to Quit', True, (255, 255, 255))
    back_button = font_hint.render('Press <b> to go back to Home Screen', True, (255, 255, 255))
    screen.blit(title, ((screen_width / 5 + screen_width / 2) - title.get_width()/2, screen_height/ 4 - title.get_height()/3))
    screen.blit(quit_button, ((screen_width / 5 + screen_width / 2) - quit_button.get_width()/2, screen_height/9 + quit_button.get_height()/2 + 330))
    screen.blit(back_button, ((screen_width / 5 + screen_width / 2) - back_button.get_width()/2, screen_height/9 + back_button.get_height()/2 + 350))
    rect_width = 10  # Adjust the thickness of the frame
    # Tetris Board Frame - should be 20 x 10 Base Units
    pygame.draw.rect(screen, white, (rect_width + 15, rect_width + 15, base_unit_width * 10, base_unit_eight * 20), rect_width)
    pygame.display.update()

def draw_help_screen():
    screen.fill(black)
    font = pygame.font.SysFont('Red Hat Mono', 40)
    font_help = pygame.font.SysFont('Red Hat Mono', 16)
    font_hint = pygame.font.SysFont('Red Hat Mono', 11)
    title = font.render('Help', True, (255, 255, 255))
    help = font_help.render('Combine these pieces into single, horizontal lines and score some points!', True, (255, 255, 255))
    help_text = 'Combine these pieces into single, horizontal lines and score some points!'
    back_button = font_hint.render('Press <b> to go back to Home Screen', True, (255, 255, 255))
    screen.blit(title, ((screen_width / 5 + screen_width / 2) - title.get_width()/2, screen_height/ 4 - title.get_height()/3))
    # screen.blit(help, ((screen_width / 5 + screen_width / 2) - help.get_width()/2, screen_height/ 4 - help.get_height()/2))
    blit_text(screen, help_text, ((screen_width / 3 + screen_width / 2) - help.get_width()/3, ((screen_height / 3) + (screen_height / 4))  - help.get_height()/2), font_help)
    screen.blit(back_button, ((screen_width / 5 + screen_width / 2) - back_button.get_width()/2, screen_height/9 + back_button.get_height()/2 + 330))
    rect_width = 10  # Adjust the thickness of the frame
    # Tetris Board Frame - should be 20 x 10 Base Units
    pygame.draw.rect(screen, white, (rect_width + 15, rect_width + 15, base_unit_width * 10, base_unit_eight * 20), rect_width)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = 200
            player_y = 400
            game_state = "game"
            game_over = False
        if keys[pygame.K_h]:
            game_state = "help_menu"
    elif game_state == "game_over":
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
    elif game_state == "help_menu":
        draw_help_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            game_state = "start_menu"
  
    elif game_state == "game":
        draw_board_game_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if keys[pygame.K_b]:
            game_state = "start_menu"
        if keys[pygame.K_LEFT]:
            player_x -= 1
        if keys[pygame.K_RIGHT]:
            player_x += 1
        if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
            game_over = True
            game_state = "game_over"
        
        pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))
        pygame.display.update()
  
    elif game_over:
        game_state = "game_over"
        game_over = False
 