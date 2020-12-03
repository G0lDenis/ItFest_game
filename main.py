import pygame


def init_main_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.set_caption('123')
    show_start_menu(screen)


def show_start_menu(screen):
    global st_but
    global set_but
    image = pygame.image.load('Images/menu background 2.png').convert()
    image = pygame.transform.scale(image, screen.get_size())
    rect = image.get_rect()
    rect.center = (image.get_size()[0] // 2,
                   image.get_size()[1] // 2)
    screen.blit(image, rect)
    image = pygame.image.load('Images/start button 3.png').convert()
    image.set_colorkey((255, 255, 255))
    rect = image.get_rect()
    rect.center = (0.3 * screen.get_size()[0] + image.get_size()[0] // 2,
                   0.4 * screen.get_size()[1] + image.get_size()[1] // 2)
    st_but = screen.blit(image, rect)
    image = pygame.image.load('Images/setup button 4.png').convert()
    image.set_colorkey((255, 255, 255))
    rect = image.get_rect()
    rect.center = (0.6 * screen.get_size()[0] + image.get_size()[0] // 2,
                   0.4 * screen.get_size()[1] + image.get_size()[1] // 2)
    set_but = screen.blit(image, rect)


def process_event(screen):
    global running
    global present_screen
    global st_but
    global set_but
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if present_screen == 'Menu':
                if st_but.collidepoint(event.pos):
                    game_start(screen)
                if set_but.collidepoint(event.pos):
                    open_settings(screen)
            if present_screen == 'Game':
                pass


def game_start(screen):
    global present_screen
    present_screen = 'Game'


def open_settings(screen):
    global present_screen
    present_screen = 'Settings'


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    init_main_screen(screen)
    running = False
    present_screen = 'Menu'
    st_but = None
    set_but = None
    while running:
        process_event(screen)
        pygame.display.flip()
    pygame.quit()
