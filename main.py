import pygame
import csv
import sqlite3


def init_main_screen(screen):
    screen.fill((0, 0, 0))
    show_start_menu(screen)


def init_game_screen(screen):
    global present_screen
    screen.fill((0, 0, 0))
    show_game(screen, present_screen)


def show_start_menu(screen):
    global button_start
    global button_setup
    global sprites
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute("""SELECT * FROM Images
    WHERE screen_id = 1 and type = 'bg'""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[2]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    bt1 = cur.execute("""SELECT * FROM Images
        WHERE screen_id = 1 and type = 'bt1'""").fetchone()
    button_start = Button(bt1[2], 'bt1')
    sprites.add(button_start)
    bt2 = cur.execute("""SELECT * FROM Images
            WHERE screen_id = 1 and type = 'bt2'""").fetchone()
    button_setup = Button(bt2[2], 'bt2')
    sprites.add(button_setup)
    sprites.draw(screen)


def show_game(screen, present_screen):
    global sprites
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute(f"""SELECT * FROM Images
        WHERE screen_id = {present_screen} and type = 'bg'""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[2]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    bt1 = cur.execute(f"""SELECT * FROM Images
            WHERE screen_id = {present_screen} and type = 'bt1'""").fetchone()
    if bt1:
        button_start = Button(bt1[2], 'bt1')
        sprites.add(button_start)
        bt2 = cur.execute(f"""SELECT * FROM Images
                    WHERE screen_id = {present_screen} and type = 'bt2'""").fetchone()
        button_setup = Button(bt2[2], 'bt2')
        sprites.add(button_setup)
        sprites.draw(screen)
    else:
        clock = pygame.time.Clock()
        clock.tick(1000)
        print('++++++')


def process_event(screen):
    global running
    global present_screen
    global button_start
    global button_setup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('present screen.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';', quotechar='"')
                writer.writerow([str(present_screen) if present_screen != 1 else saved_screen])
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if present_screen == 1:
                if button_start.rect.collidepoint(event.pos):
                    game_start()
                if button_setup.rect.collidepoint(event.pos):
                    open_settings()
            else:
                pass


def game_start():
    global screen
    global present_screen
    global button_start
    global button_setup
    button_start.kill()
    button_start.remove()
    button_setup.kill()
    button_setup.remove()
    present_screen = saved_screen
    show_game(screen, present_screen)


def open_settings():
    global screen
    global present_screen


class Button(pygame.sprite.Sprite):
    def __init__(self, bt_name, num):
        super().__init__()
        self.num = num
        self.image = pygame.image.load(bt_name).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect_center())

    def rect_center(self):
        global screen
        if self.num == 'bt1':
            return (0.3 * screen.get_size()[0] + self.image.get_size()[0] // 2,
                    0.4 * screen.get_size()[1] + self.image.get_size()[1] // 2)
        else:
            return (0.6 * screen.get_size()[0] + self.image.get_size()[0] // 2,
                    0.4 * screen.get_size()[1] + self.image.get_size()[1] // 2)


if __name__ == '__main__':
    pygame.init()
    running = True
    with open('present screen.csv') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        saved_screen = int(list(reader)[0][0])
    button_start = None
    button_setup = None
    first_character = None
    second_character = None
    present_screen = 1
    sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    init_main_screen(screen)
    while running:
        process_event(screen)
        pygame.display.flip()
    pygame.quit()
