#!/bin/python3

import pygame, sys
import save_menu
from grid import Grid


SQR_SZ = 20
unsaved_states = None

def main(canvas_x, canvas_y, data_name=None, refill_states=None):

    SCREEN_WIDTH = SQR_SZ * canvas_x
    SCREEN_WIDTH = SQR_SZ * canvas_y

    pygame.init()

    FPS = 60
    FramePerSec = pygame.time.Clock()

    surf = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
    pygame.display.set_caption('click squares, enter to save')
    # surf.fill(WHITE)

    grid = Grid(surf, canvas_x, canvas_y, SQR_SZ, unsaved_states)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if(left):
                    grid.left_is_clicked = True
                if(right):
                    grid.right_is_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                grid.left_is_clicked = False
                grid.right_is_clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    grid.h_flip()
                elif event.key == pygame.K_v:
                    grid.v_flip()
                elif event.key == pygame.K_s:
                    print('UNSAVED:\n')
                    grid.print()
                    pygame.quit()
                    return grid.states()

        grid.draw()
        grid.update()

        if grid.left_is_clicked:
            grid.selected.click()
        elif grid.right_is_clicked:
            grid.selected.unclick()

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    data_name, canvas_x, canvas_y = save_menu.start()
    is_running = True
    while is_running:
        unsaved_states = main(canvas_x, canvas_y, data_name, unsaved_states)
        if save_menu.save(unsaved_states, canvas_x, data_name):
            is_running = False