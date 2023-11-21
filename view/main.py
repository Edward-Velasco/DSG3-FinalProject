import pygame
import sys
# Create the built Classes
from view.classes.Button import Button
from view.classes.TextOnlyBox import TextOnlyBox
from view.classes.OptionBox import OptionBox

# Import utility functions
from view.utils import get_font

pygame.init()

# Screen initialization
screenSize = [1280, 720]
screen = pygame.display.set_mode(screenSize)

backgroundStartScreen = pygame.image.load("view/assets/backgrounds/start_menu_bg.png")

# Executable customizations
pygame.display.set_caption("Infinity Deadpool")
pygame.display.set_icon(pygame.image.load("view/assets/misc/logo.png"))

# The function that loads the starting menu
def start_gui():
    start_button_background = pygame.image.load("view/assets/buttons/start_button.png")
    start_game_button = Button(
        background_image=start_button_background,
        center_coordinates_pair=[
            (screenSize[0]/2),
            (screenSize[1]/2)+(start_button_background.get_height()*2.5)
        ],
        text_input=None,
        text_color="White",
        font=get_font(50),
        text_hovering_color="White",
        uuid="123"
    )

    # Cycle to run per frame
    while True:
        # Render the background into the screen
        screen.blit(backgroundStartScreen, (0, 0))

        mouse_position = pygame.mouse.get_pos()

        # Interaction functions for the start button
        start_game_button.change_color(mouse_position)
        start_game_button.screen_render(screen)

        # Check for user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button.check_mouse_hover(mouse_position):
                    load_introduction()

        # Show the changes
        pygame.display.flip()

# Function that displays the series of introductory cutscenes
def load_introduction():
    cutscenes_iterator = 1
    cutscene_path = f"view/assets/backgrounds/introduction/cutscene_{cutscenes_iterator}.png"

    active_cutscene_bg = pygame.image.load(cutscene_path)

    # Cycle to run per frame
    while True:
        # Render the background into the screen
        screen.blit(active_cutscene_bg, (0, 0))

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
                cutscene_path = f"view/assets/backgrounds/introduction/cutscene_{cutscenes_iterator}.png"
                active_cutscene_bg = pygame.image.load(cutscene_path)

        # Show the changes
        pygame.display.flip()

start_gui()

pygame.quit()