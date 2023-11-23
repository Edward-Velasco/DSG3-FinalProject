from .TextContainer import TextContainer
import pygame

class Button(TextContainer):
    def __init__(self, background_image, center_coordinates_pair, text_input, text_color, font, text_hovering_color, uuid):
        # Obtain the parent class attributes
        super().__init__(background_image, center_coordinates_pair, text_input, text_color, font)

        # The color the text should change to when hovering it
        self.hover_color = text_hovering_color

        # Button Identifier
        self.id = uuid

        # Pygame objects
        self.text = self.font.render(self.text_input, True, self.text_color)

        if self.background is None:
            self.background = self.text

        self.text_rect = self.text.get_rect(center=(self.x_coord, self.y_coord))

    def display_button_update(self, screen):
        # Check if the button is being hovered and update it's color
        if self.check_mouse_hover(pygame.mouse.get_pos()):
            self.text = self.font.render(self.text_input, True, self.hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.text_color)

        # Show the button into the display
        if self.background is not None:
            screen.blit(self.background, self.rect)
        screen.blit(self.text, self.text_rect)
