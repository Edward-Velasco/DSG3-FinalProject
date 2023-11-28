from .ImageContainer import ImageContainer
from unidecode import unidecode


class TextContainer(ImageContainer):
    def __init__(self, background_image, center_coordinates_pair, text_input, text_color, font):
        super().__init__(background_image, center_coordinates_pair)

        # Text options
        self.text_input = text_input
        self.text_color = text_color
        self.font = font

    def character_label_render(self, screen):
        screen.blit(self.background, self.rect)

        text_font = self.font.render(self.text_input, True, self.text_color)
        text_rect = text_font.get_rect(left=self.x_coord-(164/1.8) ,centery=self.y_coord)

        screen.blit(text_font, text_rect)

    def multiline_text_render(self, screen, y_axis_offset):
        screen.blit(self.background, self.rect)

        words_per_line = []

        accent_free = unidecode(self.text_input, "utf-8")

        # Separate the text_input by lines
        for text_line in accent_free.splitlines():
            words_per_line.append(text_line.split(' '))

        # Define the boundaries for the text
        max_width = self.rect.width
        # TODO: I should add a height limit eventually
        max_height = self.rect.height
        space_size = self.font.size(' ')[0]

        # The starting position of the word
        word_x_coord = self.rect.left + 30
        word_y_coord = self.rect.top + 30 + y_axis_offset

        # Iterate per each line and word
        for line in words_per_line:
            for word in line:
                word_surface = self.font.render(word, True, self.text_color)
                word_width, word_height = word_surface.get_size()

                # Adjust the word if needed
                if word_x_coord + word_width >= max_width + self.rect.left - 30:
                    word_x_coord = self.rect.left + 30
                    word_y_coord += word_height
                screen.blit(word_surface, (word_x_coord, word_y_coord))
                word_x_coord += word_width + space_size

            # New line settings
            word_x_coord = self.rect.left + 30
            word_y_coord += word_height
