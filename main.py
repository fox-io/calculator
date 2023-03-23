import pygame

# Initialize Pygame
pygame.init()


# Calculator Class
class Calculator:
    # Debugging Flag
    debug = True

    # Define Variables
    left_value = "0"
    right_value = "0"
    operator = None
    result = "0"

    window = pygame.display.set_mode((300, 475))
    display = {}

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

    def __init__(self):
        pygame.display.set_caption("Calculator")
        self.window.fill(self.colors['white'])

        self.make_display()
        self.make_buttons()

        pygame.display.flip()

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
        self.update_display()

    def update_display(self):
        # Fill and update the display area to erase the previous value
        self.window.fill(self.colors['white'], (1, 1, 299, 99))
        pygame.display.update(self.display['display'])

        # Render the new value
        self.display['text'] = self.font.render(self.right_value, True, self.colors['black'])
        self.window.blit(self.display['text'],
                         self.display['text'].get_rect(right=self.display['display'].right - 10,
                                                       centery=self.display['display'].centery))
        pygame.display.update(self.display['display'])

    def clear(self):
        self.left_value = "0"
        self.right_value = "0"
        self.operator = None
        # If the result was an error, display "E", but continue clearing everything else.
        if self.result == "E":
            self.right_value = "E"
            self.update_display()
            self.right_value = "0"
            self.result = "0"
        else:
            self.result = "0"
            self.update_display()

    def evaluate(self):
        # Evaluate the expression
        if self.operator == "+":
            self.result = str(float(self.left_value) + float(self.right_value))
        elif self.operator == "-":
            self.result = str(float(self.left_value) - float(self.right_value))
        elif self.operator == "*":
            self.result = str(float(self.left_value) * float(self.right_value))
        elif self.operator == "/":
            if self.right_value == "0":
                self.result = "E"
            else:
                self.result = str(float(self.left_value) / float(self.right_value))
        if self.result == "E":
            self.clear()
        else:
            self.left_value = self.result
            # Temporarily set the right value to the result so that it will be displayed
            self.right_value = self.result
            self.update_display()
            # Clear the right value so that the next number will be appended
            self.right_value = "0"
            # Clear the operator so that the next button push will be treated as the first value of a new expression
            self.operator = None

    def button_handler(self, pushed_button):
        # Handles button pushes.
        if pushed_button == "C":
            self.clear()
            return 0
        elif pushed_button == "=":
            self.evaluate()
            return 0
        elif pushed_button == "+" or pushed_button == "-" or pushed_button == "*" or pushed_button == "/":
            # If an operator is already set, evaluate the expression first.
            if self.operator is not None:
                self.evaluate()
            else:
                self.left_value = self.right_value
                # Update display before clearing the right value
                self.update_display()
                self.right_value = "0"
                self.operator = pushed_button
            return 0
        elif pushed_button == ".":
            if "." not in self.right_value:
                self.right_value += pushed_button
            self.update_display()
            return 0
        else:
            if self.right_value == "0":
                self.right_value = pushed_button
            else:
                self.right_value += pushed_button
            self.update_display()
            return 0

    def click_handler(self, clicked_position):
        # Translates clicks into button pushes if the click happened inside a button.
        for button in self.buttons:
            if self.buttons[button]['button'].collidepoint(clicked_position):
                self.button_handler(self.buttons[button]['code'])

    def key_handler(self, pressed_key_code):
        # Translates key presses into button pushes if the key is a valid button.
        for key_code, key_text in self.key_codes.items():
            if pressed_key_code == key_code:
                self.button_handler(key_text)


# Create Calculator
app = Calculator()

# Main Loop
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
