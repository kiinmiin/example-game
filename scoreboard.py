import pygame.font


class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        """Init scoreboard attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # Score attributes - size color and font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        # Prepare Graphical Score
        self.prepare_score()
        # Prepare Graphical level
        self.prepare_level()
        
        
    def prepare_score(self):
        """Convert score to graphics component"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20
        
    def prepare_level(self):
        """Convert level to graphics component"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_settings.bg_color)
        # Level appears under score value
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10
    
    
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)