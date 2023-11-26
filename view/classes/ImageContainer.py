import pygame

class ImageContainer:
    def __init__(self, background_image, center_coordinates_pair):
        self.background = pygame.image.load(background_image)

        # Decompose the coordinates duple into each property (Coords to the center of the button)
        self.x_coord = center_coordinates_pair[0]
        self.y_coord = center_coordinates_pair[1]

        self.rect = self.background.get_rect(center=(self.x_coord, self.y_coord))

    # Render the background image of the image
    def image_only_render(self, screen):
        screen.blit(self.background, self.rect)

    def check_mouse_hover(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            return True
        return False
