"""Define functions for different states"""


from ui_element import UIElement, GameState, UIElementImage
import pygame
import constants
import images
from  sprite_set import Sprite

def title_screen(screen):

    font = pygame.font.Font('../pygame_test/learning_curve_alt_G_bold_ot_tt.ttf', 64)
 
    # create a text surface object,
    text = font.render('Farm-to-Table', True, constants.BLACK)
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (constants.X // 2 +2, constants.Y // 3)
    
    # create ui elements
    korn = UIElementImage(
        center_position=(constants.X/4, 500),
        img='../pygame_test/images/Corn_S.png',
        size=(192,110),
        action=GameState.KORN
    )
    milk = UIElementImage(
        center_position=(2 * (constants.X/4), 500),
        img='../pygame_test/images/Milk_S.png',
        size=(200,200),
        action=GameState.MILK
    )
    eggs = UIElementImage(
        center_position=(3* (constants.X/4), 500),
        img='../pygame_test/images/Egg_S.png',
        size=(192,110),
        action=GameState.EGGS
    )
    quit_btn = UIElement(
        center_position=(50, 25),
        font_size=30,
        text_rgb=constants.BLACK,
        text="Quit",
        action=GameState.QUIT,
    )
    question_mark = UIElementImage(
        center_position = (750, 25),
        img = '../pygame_test/images/icons8-question-mark-48.png',
        size=(100,100),
        action=GameState.QUESTION
    )
    

    
    
    buttons = [milk, eggs, korn, quit_btn, question_mark]
 


    while True:
        mouse_up = False
        bg_1 = pygame.image.load("../pygame_test/images/Farm-to-Table StartScreen.png")
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
       
       

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
    
    
    
def korn(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    tractor = UIElementImage(
        center_position=(725,70),
        img="../pygame_test/images/John Deere Tractor.png",
        size=(100,100),
        action=GameState.TRACTOR
    )
    buttons = [return_btn, tractor]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
        
def milk(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
        
def eggs(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
        
        
def question_mark(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    font = pygame.font.Font('../pygame_test/learning_curve_alt_G_bold_ot_tt.ttf', 64)
    text = font.render('Farm-to-Table', True, constants.BLACK)
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (constants.X // 2 +2, constants.Y // 3)
    while True:
        mouse_up = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
        
        
# def tractor(screen):
    
#     while True:
#         mouse_up = False
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#                 mouse_up = True
#         bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
#         screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))

#         ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
#         if ui_action is not None:
#             return ui_action
#         return_btn.draw(screen)

#         pygame.display.flip()