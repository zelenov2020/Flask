import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i = (y - self.top) // self.cell_size + 1
        j = (x - self.left) // self.cell_size + 1

        if 1 <= i <= self.height and 1 <= j <= self.width:
            return j - 1, i - 1
        else:
            return None

    def on_click(self, cell):
        print(cell)



# поле 5 на 7
if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()