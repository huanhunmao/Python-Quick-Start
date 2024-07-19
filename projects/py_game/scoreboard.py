import pygame.font


class Scoreboard:
    def __init__(self, ai_game):
        self.score_rect = None
        self.score_image = None
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 47)

        self.prep_score()

    def prep_score(self):
        # format score
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # 展示在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # 画出来
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)