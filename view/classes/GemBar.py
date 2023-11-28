from .ImageContainer import ImageContainer


class ItemBar(ImageContainer):
    def __init__(self, background_image, center_coordinates_pair, max_items):
        super().__init__(background_image, center_coordinates_pair)

        self.max_items = max_items

        self.items_coordinates = []

        for iterator in range(0, max_items):
            self.items_coordinates.append(iterator*(self.rect.height/max_items))

    def get_item_coordinates(self, position):
        if position is None:
            print(self.items_coordinates)
        else:
            print(self.items_coordinates[position])