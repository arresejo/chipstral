
class Display:
    def __init__(self, pixels=None):
        self.width = 64
        self.height = 32
        if pixels is None:
            self.pixels = [[0] * self.width for _ in range(self.height)]
        else:
            self.pixels = pixels

    def clear(self):
        self.pixels = [[0] * self.width for _ in range(self.height)]

    def get_pixel(self, x, y):
        x %= self.width
        y %= self.height
        return self.pixels[y][x]

    def set_pixel(self, x, y, value):
        x %= self.width
        y %= self.height
        self.pixels[y][x] = value
