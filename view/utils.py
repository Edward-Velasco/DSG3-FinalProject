import pygame

# Return the loaded pygame font for a given size
def get_font(font_size):
    return pygame.font.Font(f"view/assets/fonts/Webcomic.ttf", font_size)

# Check the base ongoing pygame events for user inputs
"""def event_reader(buttons_coordinates_list):
    # Close the game if prompted by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Determine whether the user pressed a button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()"""