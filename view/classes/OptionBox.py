from .TextContainer import TextContainer


class OptionBox(TextContainer):
    def __init__(self, background_image, center_coordinates_pair, text_input, text_color, font, choice_image, uuid):
        # Obtain the parent class attributes
        super().__init__(background_image, center_coordinates_pair, text_input, text_color, font)

        self.id = uuid
        self.choice_image = choice_image
        self.choice_rect = self.choice_image.get_rect(center=(self.x_coord, self.y_coord-40))

    def multiline_text_render(self, screen, y_axis_offset):
        super().multiline_text_render(screen, y_axis_offset)
        screen.blit(self.choice_image, self.choice_rect)
