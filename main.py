import pygame
import csv
import sqlite3


def init_main_screen(screen):
    global bt_close
    screen.fill((0, 0, 0))
    bt_close = Button(r'Images\close button 2.png', 0.93, 0.03)
    sprites.add(bt_close)
    show_game(screen, present_screen)


def init_game_screen(screen):
    global present_screen
    global sprites
    screen.fill((0, 0, 0))
    show_game(screen, present_screen)


def show_game(screen, present_screen):
    global sprites
    global bt1
    global bt2
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute(f"""SELECT * FROM Backs
        WHERE screen_id = {present_screen}""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[2]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    bt1 = cur.execute(f"""SELECT * FROM Buttons
            WHERE screen_id = {present_screen}""").fetchone()
    sprites.draw(screen)
    if bt1:
        bt1 = Button(bt1[2], bt1[3], bt1[4])
        sprites.add(bt1)
        bt2 = cur.execute(f"""SELECT * FROM Buttons
                    WHERE screen_id = {present_screen}""").fetchall()[1]
        bt2 = Button(bt2[2], bt2[3], bt2[4])
        sprites.add(bt2)
        sprites.draw(screen)
    else:
        texts = cur.execute(f"""SELECT * FROM Texts
                    WHERE screen_id = {present_screen}""").fetchall()
        texts.sort(key=lambda i: i[2])
        for i in texts:
            im = Button(i[3], 0.5, 0.1)
            sprites.add(im)
            sprites.draw(screen)
            clock = pygame.time.Clock()
            clock.tick(1000)
            im.kill()
            im.remove()


def process_event(screen):
    global running
    global present_screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if present_screen == 1:
                if bt1.rect.collidepoint(event.pos):
                    game_start()
                if bt2.rect.collidepoint(event.pos):
                    open_settings()
            if bt_close.rect.collidepoint(event.pos):
                running = False


def game_start():
    global screen
    global present_screen
    global bt1
    global bt2
    bt1.kill()
    bt1.remove()
    bt2.kill()
    bt2.remove()
    present_screen = saved_screen
    show_game(screen, present_screen)


def open_settings():
    global screen
    global present_screen


class Button(pygame.sprite.Sprite):
    def __init__(self, bt_name, cen_x, cen_y):
        super().__init__()
        self.cen_x = cen_x
        self.cen_y = cen_y
        self.image = pygame.image.load(bt_name).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect_center())

    def rect_center(self):
        global screen
        return (self.cen_x * screen.get_size()[0] + self.image.get_size()[0] // 2,
                self.cen_y * screen.get_size()[1] + self.image.get_size()[1] // 2)


if __name__ == '__main__':
    pygame.init()
    running = True
    with open('present screen.csv') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        saved_screen = int(list(reader)[0][0])
    bt1 = None
    bt2 = None
    bt_close = None
    first_character = None
    second_character = None
    present_screen = 1
    sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    init_main_screen(screen)
    while running:
        process_event(screen)
        pygame.display.flip()
    with open('present screen.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        writer.writerow([str(present_screen) if present_screen != 1 else saved_screen])
    pygame.quit()
