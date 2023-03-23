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

    key_codes = {pygame.K_ESCAPE: "C", pygame.K_KP_DIVIDE: "/", pygame.K_SLASH: "/", pygame.K_KP_MULTIPLY: "*",
                 pygame.K_ASTERISK: "*", pygame.K_KP_MINUS: "-", pygame.K_MINUS: "-", pygame.K_KP_PLUS: "+",
                 pygame.K_PLUS: "+", pygame.K_KP_ENTER: "=", pygame.K_RETURN: "=", pygame.K_KP0: "0",
                 pygame.K_0: "0", pygame.K_KP1: "1", pygame.K_1: "1", pygame.K_KP2: "2", pygame.K_2: "2",
                 pygame.K_KP3: "3", pygame.K_3: "3", pygame.K_KP4: "4", pygame.K_4: "4", pygame.K_KP5: "5",
                 pygame.K_5: "5", pygame.K_KP6: "6", pygame.K_6: "6", pygame.K_KP7: "7", pygame.K_7: "7",
                 pygame.K_KP8: "8", pygame.K_8: "8", pygame.K_KP9: "9", pygame.K_9: "9", pygame.K_KP_PERIOD: ".",
                 pygame.K_PERIOD: "."}
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
            button['code'] = label
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

    def button_handler(self, pushed_button):
        if self.debug:
            print("Button Pressed: " + pushed_button)
        return 0

    def is_clicked(self, pos):
        # Check if a button is clicked
        for button in self.buttons:
            if self.buttons[button]['button'].collidepoint(pos):
                return self.buttons[button]['code']
        # If no button is clicked, return None
        return None

    def is_valid_key(self, key):
        # Check if a key is valid
        for key_code, key_text in self.key_codes.items():
            if event.key == key_code:
                return key_text
        # If no key is valid, return None
        return None

    def click_handler(self, pos):
        button_clicked = self.is_clicked(pos)
        if button_clicked:
            self.button_handler(button_clicked)

    def key_handler(self, key):
        valid_key = self.is_valid_key(event.key)
        if valid_key:
            self.button_handler(valid_key)


# Main Loop
app = Calculator()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            app.click_handler(event.pos)
        elif event.type == pygame.KEYDOWN:
            app.key_handler(event.key)


pygame.quit()
