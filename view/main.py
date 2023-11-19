import pygame
import sys
# Create the built Classes
from classes.Button import Button
from classes.TextOnlyBox import TextOnlyBox
from classes.OptionBox import OptionBox

pygame.init()

# Screen initialization
screenSize = [1280, 720]
screen = pygame.display.set_mode(screenSize)

backgroundStartScreen = pygame.image.load("assets/backgrounds/startingScreen.jpg")

# Executable customizations
pygame.display.set_caption("Escape Alive")
pygame.display.set_icon(pygame.image.load("assets/logo.png"))

questions_background = pygame.image.load("assets/backgrounds/questionBackGround.jpg")


# Return the Roboto loaded pygame font for a giving size
def get_font(font_size, font_style):
    return pygame.font.Font(f"assets/fonts/Roboto-{font_style}.ttf", font_size)


# The function that loads the starting menu
def main_menu():
    start_button_background = pygame.image.load("assets/buttons/startButton.png")
    start_game_button = Button(
        background_image=start_button_background,
        center_coordinates_pair=[
            (screenSize[0]/2),
            (screenSize[1]/2)+(start_button_background.get_height()*2)
        ],
        text_input='Start',
        text_color="White",
        font=get_font(50, 'Thin'),
        text_hovering_color="Gray",
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
                    return game_introduction()

        # Show the changes
        pygame.display.flip()


def game_introduction():
    instructions_text = "Despiertas de golpe en un lugar oscuro, sin recordar cómo llegaste ahí y con la impresión de no haber comido en días. Intentas salir por la puerta pero está cerrada con llave."
    instructions_background = pygame.image.load("assets/backgrounds/textBoxDot.png")

    instructions_container = TextOnlyBox(
        background_image=instructions_background,
        center_coordinates_pair=[screenSize[0]/2, screenSize[1]/2],
        text_input=instructions_text,
        text_color="White",
        font=get_font(25, 'Thin'),
    )

    while True:
        screen.blit(questions_background, (0, 0))
        instructions_container.multiline_text_render(screen, 0)

        # Show the changes
        pygame.display.flip()

        # Check for user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if instructions_container.check_mouse_hover(mouse_position):
                    return prompt_choices()


def prompt_choices():
    choices_background_container = pygame.image.load("assets/backgrounds/choicesContainer.png")
    single_choice_background = pygame.image.load("assets/backgrounds/choiceBox.png")

    choices = []
    choices_data = [
        [pygame.image.load("assets/backgrounds/choiceWindow.png"), "Salir por la ventana", "opt_1"],
        [pygame.image.load("assets/backgrounds/choiceDoor.png"), "Esconderte entre los arbustos", "opt_2"],
        [pygame.image.load("assets/backgrounds/choiceBed.png"), "Tomar una pala cercana como arma", "opt_3"]
    ]

    # 199 x 242 -> OptionBox size
    # 734 x 391 -> Choices container bg
    # TODO: Function for retrieving button functions

    # Feed the choices array to later render each one of them
    for image_iterator in range(0, len(choices_data)):
        new_choice = OptionBox(
            background_image=single_choice_background,
            center_coordinates_pair=[(screenSize[0]/3)-10+(220*image_iterator), (screenSize[1]/2)+25],
            text_input=choices_data[image_iterator][1],
            text_color="White",
            font=get_font(19, 'Thin'),
            choice_image=choices_data[image_iterator][0],
            uuid=choices_data[image_iterator][2]
        )
        choices.append(new_choice)

    choices_container = TextOnlyBox(
        background_image=choices_background_container,
        center_coordinates_pair=[screenSize[0]/2, screenSize[1]/2],
        text_input="¿Qué haces?",
        text_color="White",
        font=get_font(45, 'Thin')
    )

    while True:
        screen.blit(questions_background, (0, 0))
        choices_container.choice_statement_single_line(screen)

        for single_choice in choices:
            single_choice.multiline_text_render(screen, 125)

        # Show the changes
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main_menu()

pygame.quit()
