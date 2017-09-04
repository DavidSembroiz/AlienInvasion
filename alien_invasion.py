import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    #Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Make a play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship.
    ship = Ship(ai_settings, screen)
    #Make a group of bullets.
    bullets = Group()
    #Make an alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Set background color.
    bg_color = (230, 230, 230)

    #Start the main loop of the game.
    while True:
        gf.check_events(ai_settings, stats, screen, sb, play_button, ship,
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, screen, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens,
                bullets)
        gf.update_screen(ai_settings, stats, screen, sb, ship, aliens,
            bullets, play_button)

run_game()