import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLACK_SELECT = (0, 0, 180)
WHITE_SELECT = (180, 255, 180)

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0
        self.highlighted = False
        self.rect = None
        self.outline = None

    def click(self):
        self.state = 1
    def unclick(self):
        self.state = 0

class Grid:
    def __init__(self, surface, cols, rows, gridsize=20, refill_states:list=None):
        self.surface = surface
        self.cols = cols
        self.rows = rows
        self.sz = gridsize
        self.squares = [None] * self.cols * self.rows
        self.selected = None
        self.left_is_clicked = False
        self.right_is_clicked = False
        self.fill_grid(refill_states)
    
    def fill_grid(self, refill_states:list=None):
        o = 0
        i = 0
        for r in range(self.rows):
            tmp_str = ''
            for c in range(self.cols):
                x = self.sz * c
                y = self.sz * o
                self.squares[i] = Square(x, y)
                # tmp_str += f'{self.squares[i].x}, {self.squares[i].y}  '
                if refill_states:
                    self.squares[i].state = refill_states[i]
                i += 1
            #print(tmp_str)
            o += 1

    def draw(self):
        for sqr in self.squares:
            if sqr.state: # (filled)
                if sqr.highlighted:
                    sqr.rect = pygame.draw.rect(self.surface, BLACK_SELECT, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 0)
                    sqr.outline = pygame.draw.rect(self.surface, WHITE, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 1)
                else:
                    sqr.rect = pygame.draw.rect(self.surface, BLACK, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 0)
                    sqr.outline = pygame.draw.rect(self.surface, WHITE, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 1)
            else:
                if sqr.highlighted:
                    sqr.rect = pygame.draw.rect(self.surface, WHITE_SELECT, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 0)
                    sqr.outline = pygame.draw.rect(self.surface, WHITE, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 1)
                else:
                    sqr.rect = pygame.draw.rect(self.surface, WHITE, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 0)
                    sqr.outline = pygame.draw.rect(self.surface, BLACK, pygame.Rect(sqr.x, sqr.y, self.sz, self.sz), 1)
    
    def update(self):
        for sqr in self.squares:
            if sqr.rect.collidepoint(pygame.mouse.get_pos()):
                sqr.highlighted = True
                self.selected = sqr
            else:
                sqr.highlighted = False
    
    def print(self):
        buf = ''
        for sqr in self.squares:
            buf += f'{sqr.state}, '
        print(buf)
    
    def states(self):
        ret = []
        for sqr in self.squares:
            ret.append(sqr.state)
        return ret
    
    def h_flip(self):
        out_buf = []
        i = 0
        # go thru each row
        for r in range(self.rows):
            # empty buffer to hold the row
            line_buf = []
            # grab each state in row
            for c in range(self.cols):
                line_buf.append(self.squares[i].state)
                # iterate index
                i += 1
            # reverse each element in the line
            line_buf.reverse()
            # add to out buf
            out_buf.extend(line_buf)

        self.fill_grid(out_buf)
    
    def v_flip(self):
        # list to hold each line. list of lists
        rvrs_buf = []
        i = 0

        for r in range(self.rows):
            # empty buffer to hold the row
            line_buf = []
            # grab each state in row
            for c in range(self.cols):
                line_buf.append(self.squares[i].state)
                # iterate index
                i += 1
            rvrs_buf.append(line_buf)
        # reverse the list of lists (the order of the rows)
        rvrs_buf.reverse()
        # unpack reverse buf into single list
        out_buf = []
        for row in rvrs_buf:
            out_buf.extend(row)
        
        self.fill_grid(out_buf)