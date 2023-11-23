import pygame

# Return the loaded pygame font for a given size
def get_font(font_size):
    return pygame.font.Font(f"view/assets/fonts/Webcomic.ttf", font_size)

# Check the base ongoing pygame events for user inputs
def event_read(button_items):
    # Close the game if prompted by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Determine whether the user pressed a button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_items:
                button.check_mouse_hover(pygame.mouse.get_pos())
            # TODO: Retrieve the node stuff over here