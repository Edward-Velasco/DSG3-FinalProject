class TextContainer:
    def __init__(self, background_image, center_coordinates_pair, text_input, text_color, font):
        self.background = background_image

        # Decompose the coordinates duple into each property (Coords to the center of the button)
        self.x_coord = center_coordinates_pair[0]
        self.y_coord = center_coordinates_pair[1]

        # Text options
        self.text_input = text_input
        self.text_color = text_color
        self.font = font

        self.rect = self.background.get_rect(center=(self.x_coord, self.y_coord))

    def check_mouse_hover(self, mouse_position):
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def multiline_text_render(self, screen, y_axis_offset):
        screen.blit(self.background, self.rect)

        words_per_line = []

        # Separate the text_input by lines
        for text_line in self.text_input.splitlines():
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
