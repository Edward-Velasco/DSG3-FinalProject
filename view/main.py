import pygame
import sys
# Create the built Classes
from view.classes.Button import Button
from view.classes.TextOnlyBox import TextOnlyBox
from view.classes.OptionBox import OptionBox

# Import utility functions
from view.utils import get_font

class GameInterface:
    def __init__(self):
        pygame.init()

        # Screen initialization
        self.display_size = [1280, 720]
        self.screen = pygame.display.set_mode(self.display_size)

        # Executable customizations
        pygame.display.set_caption("Infinity Deadpool")
        pygame.display.set_icon(pygame.image.load("view/assets/misc/logo.png"))

    # Update the screen's background given an image route
    def set_background(self, image_route: str):
        new_background = pygame.image.load(image_route)
        self.screen.blit(new_background, (0, 0))

    # The function that loads the starting menu
    def start_gui(self):
        start_game_button = Button(
            background_image="view/assets/buttons/start_button.png",
            center_coordinates_pair=[
                (self.display_size[0]/2),
                (self.display_size[1]/2)+183
            ],
            text_input=None,
            text_color="White",
            font=get_font(50),
            text_hovering_color="White",
            uuid="123"
        )

        # Cycle to run per frame
        while True:
            self.set_background("view/assets/backgrounds/start_menu_bg.png")

            start_game_button.display_button_update(self.screen)

            # Check for user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_game_button.check_mouse_hover(pygame.mouse.get_pos()):
                        self.load_introduction()

            # Show the changes
            pygame.display.flip()

        # Function that displays the series of introductory cutscenes
    def load_introduction(self):
        cutscenes_iterator = 1

        # Cycle to run per frame
        while True:
            self.set_background(f"view/assets/backgrounds/introduction/cutscene_{cutscenes_iterator}.png")

            # Check for user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if cutscenes_iterator == 4:
                        # When the last intro image is reached, move to whatever is next
                        return
                    cutscenes_iterator += 1

            # Show the changes
            pygame.display.flip()