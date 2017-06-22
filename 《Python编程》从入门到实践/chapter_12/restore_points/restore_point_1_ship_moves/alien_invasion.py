import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化 pygame, settings, 和 screen 对象.
    pygame.init()   # pygame 初始化
    ai_settings = Settings()    # 实例化设置类
    screen = pygame.display.set_mode(   # 取得屏幕参数
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")     # 设置标题
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
