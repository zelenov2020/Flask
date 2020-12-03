import pygame

size = 350, 450
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255),
                                 (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)
                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell_x = mouse_pos[0] // self.cell_size - 1
        cell_y = mouse_pos[1] // self.cell_size - 1
        if (cell_x >= 0) and cell_y >= 0 and cell_x < self.width and cell_y < self.height:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if j == cell_x or i == cell_y:
                        if self.board[i][j] == 0:
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] = 0


board = Board(5, 7)
board.set_view(50, 50, 50)
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
