import pygame


def init_main_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.set_caption('123')
    show_start_menu(screen)


def show_start_menu(screen):
    global button_start
    global button_setup
    global sprites
    image_bg_menu = pygame.image.load('Images/menu background 2.png').convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    button_start = MenuButton('start')
    sprites.add(button_start)
    sprites.draw(screen)
    button_setup = MenuButton('setup')
    sprites.add(button_setup)
    screen.blit(button_start, button_start.rect_center())
    screen.blit(button_setup, button_setup.rect_center())
    sprites.draw(screen)


def process_event(screen):
    global running
    global present_screen
    global button_start
    global button_setup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if present_screen == 'Menu':
                if button_start.collidepoint(event.pos):
                    game_start()
                if button_setup.collidepoint(event.pos):
                    open_settings()
            if present_screen == 'Game':
                pass


def game_start():
    global screen
    global present_screen
    global button_start
    global button_setup
    button_start.kill()
    button_setup.kill()
    present_screen = 'Game'


def open_settings():
    global screen
    global present_screen
    present_screen = 'Settings'


class MenuButton(pygame.sprite.Sprite):
    def __init__(self, bt_name):
        self.bt_name = bt_name
        super().__init__()
        if bt_name == 'start':
            self.image = pygame.image.load('Images/start button 3.png').convert()
        else:
            self.image = pygame.image.load('Images/setup button 4.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def rect_center(self):
        global screen
        if self.bt_name == 'start':
            return (0.3 * screen.get_size()[0] + self.image.get_size()[0] // 2,
                    0.4 * screen.get_size()[1] + self.image.get_size()[1] // 2)
        else:
            return (0.6 * screen.get_size()[0] + self.image.get_size()[0] // 2,
                    0.4 * screen.get_size()[1] + self.image.get_size()[1] // 2)


if __name__ == '__main__':
    pygame.init()
    running = True
    present_screen = 'Menu'
    button_start = None
    button_setup = None
    sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    init_main_screen(screen)
    while running:
        process_event(screen)
        pygame.display.flip()
    pygame.quit()
