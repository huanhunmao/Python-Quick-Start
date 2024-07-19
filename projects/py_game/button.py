import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        # 初始化按钮属性
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # css
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 构建按钮的矩形对象并将其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮消息只需准备一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # 将msg转换为渲染图像并将文本置于按钮上
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)