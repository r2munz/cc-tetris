import pygame

pygame.init()
pygame.display.set_caption('CC TETRIS')
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
obstacle_x = 400
obstacle_y = 400
obstacle_width = 40
obstacle_height = 40
player_x = 200
player_y = 400
player_width = 20
player_height = 20
game_state = "start_menu"

def draw_start_menu():
   screen.fill((0, 0, 0))
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
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('Red Hat Mono', 40)
   font_hint = pygame.font.SysFont('Red Hat Mono', 11)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font_hint.render('Press <r> to Restart', True, (255, 255, 255))
   quit_button = font_hint.render('Press <q> to Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/8 + restart_button.get_height() + 300))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/9 + quit_button.get_height()/2 + 330))
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
   elif game_state == "game_over":
       draw_game_over_screen()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_r]:
           game_state = "start_menu"
       if keys[pygame.K_q]:
           pygame.quit()
           quit()
  
   elif game_state == "game":
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           player_x -= 5
       if keys[pygame.K_RIGHT]:
           player_x += 5
  
       if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
           game_over = True
           game_state = "game_over"
      
       screen.fill((0, 0, 0))
       pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
       pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))
       pygame.display.update()
  
   elif game_over:
       game_state = "game_over"
       game_over = False
 