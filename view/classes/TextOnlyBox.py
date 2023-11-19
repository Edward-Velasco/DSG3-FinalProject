from .TextContainer import TextContainer


class TextOnlyBox(TextContainer):
    def __init__(self, background_image, center_coordinates_pair, text_input, text_color, font):
        # Obtain the parent class attributes
        super().__init__(background_image, center_coordinates_pair, text_input, text_color, font)

    # We use this to render the "what would you do" prompt box text!
    def choice_statement_single_line(self, screen):
        text_to_render = self.font.render(self.text_input, True, self.text_color)
        text_rect = text_to_render.get_rect(center=(self.rect.centerx, self.rect.y+55))
        screen.blit(self.background, self.rect)
        screen.blit(text_to_render, text_rect)
