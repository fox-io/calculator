import pygame

# Initialize Pygame
pygame.init()


# Calculator Class
class Calculator:
    # Debugging Flag
    debug = True

    # Define Variables
    left_value = 0
    right_value = 0
    operator = None
    result = 0

    display = {}
    window = pygame.display.set_mode((300, 475))
    pygame.display.set_caption("Calculator")

    font = pygame.font.SysFont("Consolas", 20)
    button_setup = {"C": (0, 100, 75, 75), "/": (75, 100, 75, 75), "*": (150, 100, 75, 75), "-": (225, 100, 75, 75),
                    "+": (225, 175, 75, 150), "=": (225, 325, 75, 150), "0": (0, 400, 150, 75), "1": (0, 325, 75, 75),
                    "2": (75, 325, 75, 75), "3": (150, 325, 75, 75), "4": (0, 250, 75, 75), "5": (75, 250, 75, 75),
                    "6": (150, 250, 75, 75), "7": (0, 175, 75, 75), "8": (75, 175, 75, 75), "9": (150, 175, 75, 75),
                    ".": (150, 400, 75, 75)}
    colors = {'black': (0, 0, 0), 'grey': (128, 128, 128), 'light_grey': (192, 192, 192), 'white': (255, 255, 255)}
    buttons = {}

    def make_buttons(self):
        for label, bounds in self.button_setup.items():
            button = {}
            button['button'] = pygame.Rect(bounds)
            button['surface'] = pygame.draw.rect(self.window, self.colors['light_grey'], button['button'])
            button['border'] = pygame.draw.rect(self.window, self.colors['grey'], button['button'], 1)
            button['text'] = self.font.render(label, True, self.colors['black'])
            self.window.blit(button['text'], button['text'].get_rect(center=button['button'].center))
            self.buttons[label] = button

    def make_display(self):
        self.display['display'] = pygame.Rect(0, 0, 300, 100)
        self.display['surface'] = pygame.draw.rect(self.window, self.colors['white'], self.display['display'])
        self.display['border'] = pygame.draw.rect(self.window, self.colors['grey'], self.display['display'], 1)
        self.display['text'] = self.font.render("0", True, self.colors['black'])
        self.window.blit(self.display['text'],
                         self.display['text'].get_rect(right=self.display['display'].right - 10,
                                                       centery=self.display['display'].centery))

    def __init__(self):
        self.window.fill(self.colors['white'])

        self.make_display()
        self.make_buttons()

        pygame.display.flip()

    def button_handler(self, x):
        if x == "C":
            self.left_value = 0
            self.right_value = 0
            self.operator = None
            self.result = 0
        if self.debug:
            print(x)
        return 0


# Main Loop
app = Calculator()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if button_c.collidepoint(event.pos):
        #         button_handler("C")
        #     elif button_div.collidepoint(event.pos):
        #         button_handler("/")
        #     elif button_mul.collidepoint(event.pos):
        #         button_handler("*")
        #     elif button_sub.collidepoint(event.pos):
        #         button_handler("-")
        #     elif button_add.collidepoint(event.pos):
        #         button_handler("+")
        #     elif button_eq.collidepoint(event.pos):
        #         button_handler("=")
        #     elif button_0.collidepoint(event.pos):
        #         button_handler("0")
        #     elif button_1.collidepoint(event.pos):
        #         button_handler("1")
        #     elif button_2.collidepoint(event.pos):
        #         button_handler("2")
        #     elif button_3.collidepoint(event.pos):
        #         button_handler("3")
        #     elif button_4.collidepoint(event.pos):
        #         button_handler("4")
        #     elif button_5.collidepoint(event.pos):
        #         button_handler("5")
        #     elif button_6.collidepoint(event.pos):
        #         button_handler("6")
        #     elif button_7.collidepoint(event.pos):
        #         button_handler("7")
        #     elif button_8.collidepoint(event.pos):
        #         button_handler("8")
        #     elif button_9.collidepoint(event.pos):
        #         button_handler("9")
        #     elif button_dot.collidepoint(event.pos):
        #         button_handler(".")
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         button_handler("C")
        #     elif event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
        #         button_handler("/")
        #     elif event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK:
        #         button_handler("*")
        #     elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
        #         button_handler("-")
        #     elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
        #         button_handler("+")
        #     elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
        #         button_handler("=")
        #     elif event.key == pygame.K_KP0 or event.key == pygame.K_0:
        #         button_handler("0")
        #     elif event.key == pygame.K_KP1 or event.key == pygame.K_1:
        #         button_handler("1")
        #     elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
        #         button_handler("2")
        #     elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
        #         button_handler("3")
        #     elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
        #         button_handler("4")
        #     elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
        #         button_handler("5")
        #     elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
        #         button_handler("6")
        #     elif event.key == pygame.K_KP7 or event.key == pygame.K_7:
        #         button_handler("7")
        #     elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
        #         button_handler("8")
        #     elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
        #         button_handler("9")
        #     elif event.key == pygame.K_KP_PERIOD or event.key == pygame.K_PERIOD:
        #         button_handler(".")

pygame.quit()
