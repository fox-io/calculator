import pygame

# Initialize Pygame
pygame.init()

# Variables
left_value = 0
right_value = 0
operator = None
result = 0

# Make Window
window_size = (300, 475)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Calculator")

# Define Colors
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (192, 192, 192)
white = (255, 255, 255)

# Define Fonts
font = pygame.font.SysFont("Consolas", 20)

# Define UI Components
display = pygame.Rect(0, 0, 300, 100)
button_c = pygame.Rect(0, 100, 75, 75)
button_div = pygame.Rect(75, 100, 75, 75)
button_mul = pygame.Rect(150, 100, 75, 75)
button_sub = pygame.Rect(225, 100, 75, 75)
button_add = pygame.Rect(225, 175, 75, 150)
button_eq = pygame.Rect(225, 325, 75, 150)
button_0 = pygame.Rect(0, 400, 150, 75)
button_1 = pygame.Rect(0, 325, 75, 75)
button_2 = pygame.Rect(75, 325, 75, 75)
button_3 = pygame.Rect(150, 325, 75, 75)
button_4 = pygame.Rect(0, 250, 75, 75)
button_5 = pygame.Rect(75, 250, 75, 75)
button_6 = pygame.Rect(150, 250, 75, 75)
button_7 = pygame.Rect(0, 175, 75, 75)
button_8 = pygame.Rect(75, 175, 75, 75)
button_9 = pygame.Rect(150, 175, 75, 75)
button_dot = pygame.Rect(150, 400, 75, 75)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_c.collidepoint(event.pos):
                print("C")
            elif button_div.collidepoint(event.pos):
                print("/")
            elif button_mul.collidepoint(event.pos):
                print("*")
            elif button_sub.collidepoint(event.pos):
                print("-")
            elif button_add.collidepoint(event.pos):
                print("+")
            elif button_eq.collidepoint(event.pos):
                print("=")
            elif button_0.collidepoint(event.pos):
                print("0")
            elif button_1.collidepoint(event.pos):
                print("1")
            elif button_2.collidepoint(event.pos):
                print("2")
            elif button_3.collidepoint(event.pos):
                print("3")
            elif button_4.collidepoint(event.pos):
                print("4")
            elif button_5.collidepoint(event.pos):
                print("5")
            elif button_6.collidepoint(event.pos):
                print("6")
            elif button_7.collidepoint(event.pos):
                print("7")
            elif button_8.collidepoint(event.pos):
                print("8")
            elif button_9.collidepoint(event.pos):
                print("9")
            elif button_dot.collidepoint(event.pos):
                print(".")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("C")
            elif event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                print("/")
            elif event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK:
                print("*")
            elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                print("-")
            elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                print("+")
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                print("=")
            elif event.key == pygame.K_KP0 or event.key == pygame.K_0:
                print("0")
            elif event.key == pygame.K_KP1 or event.key == pygame.K_1:
                print("1")
            elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                print("2")
            elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                print("3")
            elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                print("4")
            elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                print("5")
            elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                print("6")
            elif event.key == pygame.K_KP7 or event.key == pygame.K_7:
                print("7")
            elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
                print("8")
            elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
                print("9")
            elif event.key == pygame.K_KP_PERIOD or event.key == pygame.K_PERIOD:
                print(".")

    screen.fill(white)

    pygame.draw.rect(screen, white, display)
    pygame.draw.rect(screen, grey, display, 1)
    display_text = font.render("0", True, black)
    screen.blit(display_text, display_text.get_rect(right=display.right - 10, centery=display.centery))
    pygame.draw.rect(screen, light_grey, button_c)
    pygame.draw.rect(screen, grey, button_c, 1)
    button_c_text = font.render("C", True, black)
    screen.blit(button_c_text, button_c_text.get_rect(center=button_c.center))
    pygame.draw.rect(screen, light_grey, button_div)
    pygame.draw.rect(screen, grey, button_div, 1)
    button_div_text = font.render("/", True, black)
    screen.blit(button_div_text, button_div_text.get_rect(center=button_div.center))
    pygame.draw.rect(screen, light_grey, button_mul)
    pygame.draw.rect(screen, grey, button_mul, 1)
    button_mul_text = font.render("*", True, black)
    screen.blit(button_mul_text, button_mul_text.get_rect(center=button_mul.center))
    pygame.draw.rect(screen, light_grey, button_sub)
    pygame.draw.rect(screen, grey, button_sub, 1)
    button_sub_text = font.render("-", True, black)
    screen.blit(button_sub_text, button_sub_text.get_rect(center=button_sub.center))
    pygame.draw.rect(screen, light_grey, button_add)
    pygame.draw.rect(screen, grey, button_add, 1)
    button_add_text = font.render("+", True, black)
    screen.blit(button_add_text, button_add_text.get_rect(center=button_add.center))
    pygame.draw.rect(screen, light_grey, button_eq)
    pygame.draw.rect(screen, grey, button_eq, 1)
    button_eq_text = font.render("=", True, black)
    screen.blit(button_eq_text, button_eq_text.get_rect(center=button_eq.center))
    pygame.draw.rect(screen, light_grey, button_0)
    pygame.draw.rect(screen, grey, button_0, 1)
    button_0_text = font.render("0", True, black)
    screen.blit(button_0_text, button_0_text.get_rect(center=button_0.center))
    pygame.draw.rect(screen, light_grey, button_1)
    pygame.draw.rect(screen, grey, button_1, 1)
    button_1_text = font.render("1", True, black)
    screen.blit(button_1_text, button_1_text.get_rect(center=button_1.center))
    pygame.draw.rect(screen, light_grey, button_2)
    pygame.draw.rect(screen, grey, button_2, 1)
    button_2_text = font.render("2", True, black)
    screen.blit(button_2_text, button_2_text.get_rect(center=button_2.center))
    pygame.draw.rect(screen, light_grey, button_3)
    pygame.draw.rect(screen, grey, button_3, 1)
    button_3_text = font.render("3", True, black)
    screen.blit(button_3_text, button_3_text.get_rect(center=button_3.center))
    pygame.draw.rect(screen, light_grey, button_4)
    pygame.draw.rect(screen, grey, button_4, 1)
    button_4_text = font.render("4", True, black)
    screen.blit(button_4_text, button_4_text.get_rect(center=button_4.center))
    pygame.draw.rect(screen, light_grey, button_5)
    pygame.draw.rect(screen, grey, button_5, 1)
    button_5_text = font.render("5", True, black)
    screen.blit(button_5_text, button_5_text.get_rect(center=button_5.center))
    pygame.draw.rect(screen, light_grey, button_6)
    pygame.draw.rect(screen, grey, button_6, 1)
    button_6_text = font.render("6", True, black)
    screen.blit(button_6_text, button_6_text.get_rect(center=button_6.center))
    pygame.draw.rect(screen, light_grey, button_7)
    pygame.draw.rect(screen, grey, button_7, 1)
    button_7_text = font.render("7", True, black)
    screen.blit(button_7_text, button_7_text.get_rect(center=button_7.center))
    pygame.draw.rect(screen, light_grey, button_8)
    pygame.draw.rect(screen, grey, button_8, 1)
    button_8_text = font.render("8", True, black)
    screen.blit(button_8_text, button_8_text.get_rect(center=button_8.center))
    pygame.draw.rect(screen, light_grey, button_9)
    pygame.draw.rect(screen, grey, button_9, 1)
    button_9_text = font.render("9", True, black)
    screen.blit(button_9_text, button_9_text.get_rect(center=button_9.center))
    pygame.draw.rect(screen, light_grey, button_dot)
    pygame.draw.rect(screen, grey, button_dot, 1)
    button_dot_text = font.render(".", True, black)
    screen.blit(button_dot_text, button_dot_text.get_rect(center=button_dot.center))

    pygame.display.flip()

pygame.quit()
