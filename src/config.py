import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        #self._add_themes()
        #self.idx = 0
        self.theme = Theme((241, 217, 192), (169, 122, 101), (255, 235, 125), (235, 195, 66), '#C86464', '#C84646')
        #self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('../assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('../assets/sounds/capture.wav'))
