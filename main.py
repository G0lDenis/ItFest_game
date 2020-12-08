import pygame
import csv
import sqlite3
from time import sleep


def init_main_screen(screen):
    global bt_close
    global bt1
    global bt2
    global bt3
    global present_screen
    global saved_screen
    screen.fill((0, 0, 0))
    present_screen = 1
    if bt1:
        bt1.kill()
        bt1.remove()
        bt2.kill()
        bt2.remove()
    if bt3:
        bt3.kill()
        bt3.remove()
    bt1, bt2, bt3 = None, None, None
    with open('present screen.csv') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        saved_screen = int(list(reader)[0][0])
    bt_close = Rectangle(r'Images\close button 2.png', 0.93, 0.03)
    sprites.add(bt_close)
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute(f"""SELECT * FROM Backs
            WHERE id = {present_screen}""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[1]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    bt1 = cur.execute(f"""SELECT * FROM Buttons
                            WHERE bg_id = {present_screen}""").fetchone()
    bt1 = Rectangle(bt1[2], bt1[3], bt1[4])
    sprites.add(bt1)
    bt2 = cur.execute(f"""SELECT * FROM Buttons
                                    WHERE bg_id = {present_screen}""").fetchall()[1]
    bt2 = Rectangle(bt2[2], bt2[3], bt2[4])
    sprites.add(bt2)
    sprites.draw(screen)
    pygame.display.flip()
    pygame.mixer.music.load('snd/background_snd_1.mp3')
    pygame.mixer.music.play(-1)


def init_settings_screen(screen):
    global bt1
    global bt2
    global bt3
    global present_screen
    global sprites
    global bt1
    global bt2
    global bt3
    global first_character
    global second_character
    bt1.kill()
    bt1.remove()
    bt2.kill()
    bt2.remove()
    bt1, bt2, bt3 = None, None, None
    present_screen = 13
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute(f"""SELECT * FROM Backs
                WHERE id = {present_screen}""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[1]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    bt1 = cur.execute(f"""SELECT * FROM Buttons
                                WHERE bg_id = {present_screen}""").fetchone()
    bt1 = Rectangle(bt1[2], bt1[3], bt1[4])
    sprites.add(bt1)
    bt2 = cur.execute(f"""SELECT * FROM Buttons
                                        WHERE bg_id = {present_screen}""").fetchall()[1]
    bt2 = Rectangle(bt2[2], bt2[3], bt2[4])
    sprites.add(bt2)
    bt3 = cur.execute(f"""SELECT * FROM Buttons
                                    WHERE bg_id = {present_screen}""").fetchall()
    bt3 = Rectangle(bt3[2][2], bt3[2][3], bt3[2][4])
    sprites.add(bt3)
    sprites.draw(screen)
    pygame.display.flip()


def show_game(screen):
    global sprites
    global bt1
    global bt2
    global bt3
    global ends_texts
    global first_character
    global second_character
    global present_screen
    global now_text
    global running
    con = sqlite3.connect('maps.db')
    cur = con.cursor()
    bg_way = cur.execute(f"""SELECT * FROM Backs
        WHERE id = {present_screen}""").fetchone()
    image_bg_menu = pygame.image.load(bg_way[1]).convert()
    image_bg_menu = pygame.transform.scale(image_bg_menu, screen.get_size())
    rect = image_bg_menu.get_rect()
    rect.center = (image_bg_menu.get_size()[0] // 2,
                   image_bg_menu.get_size()[1] // 2)
    screen.blit(image_bg_menu, rect)
    pygame.display.flip()
    first_character = cur.execute(f"""SELECT * FROM Heroes
            WHERE bg_id = {present_screen}""").fetchall()
    if first_character:
        first_character = first_character[0]
        first_character = Rectangle(first_character[2], first_character[3], first_character[4])
        sprites.add(first_character)
        second_character = cur.execute(f"""SELECT * FROM Heroes
                    WHERE bg_id = {present_screen}""").fetchall()[1]
        second_character = Rectangle(second_character[2], second_character[3], second_character[4])
        sprites.add(second_character)
    sprites.draw(screen)
    texts = cur.execute(f"""SELECT * FROM Texts
                WHERE bg_id = {present_screen}""").fetchall()
    texts.sort(key=lambda i: i[2])
    now_text = texts
    for i in texts:
        im = Rectangle(i[3], 0.3, 0.05)
        sprites.add(im)
        sprites.draw(screen)
        pygame.display.flip()
        if i[4]:
            print(present_screen, i[4])
            bt1 = cur.execute(f"""SELECT * FROM Buttons
                        WHERE bg_id = {present_screen}""").fetchone()
            bt1 = Rectangle(bt1[2], bt1[3], bt1[4])
            sprites.add(bt1)
            bt2 = cur.execute(f"""SELECT * FROM Buttons
                                WHERE bg_id = {present_screen}""").fetchall()[1]
            bt2 = Rectangle(bt2[2], bt2[3], bt2[4])
            sprites.add(bt2)
            bt = cur.execute(f"""SELECT * FROM Buttons
                                WHERE bg_id = {present_screen}""").fetchall()
            if len(bt) > 2:
                bt3 = Rectangle(bt[2][2], bt[2][3], bt[2][4])
                sprites.add(bt3)
            sprites.draw(screen)
            ends_texts = texts.index(i)
        else:
            clock = pygame.time.Clock()
            for t in range(10):
                clock.tick(2)
            im.kill()
            im.remove()
            screen.blit(image_bg_menu, rect)
            pygame.display.update()
    if present_screen == 2:
        present_screen = 3
        show_game(screen)


def continue_texts(screen):
    global now_text
    for i in now_text:
        im = Rectangle(i[3], 0.3, 0.05)
        sprites.add(im)
        sprites.draw(screen)
        sleep(5)
        im.kill()
        im.remove()
    show_game(screen)


def process_event(screen):
    global running
    global present_screen
    global saved_screen
    global click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mixer.Sound.play(click)
            if bt_close.rect.collidepoint(event.pos):
                running = False
                return
            if present_screen == 1:
                if bt1.rect.collidepoint(event.pos):
                    present_screen = saved_screen
                    update_screen()
                if bt2.rect.collidepoint(event.pos):
                    init_settings_screen(screen)
            elif present_screen == 13:
                if bt1.rect.collidepoint(event.pos):
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
                if bt2.rect.collidepoint(event.pos):
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
                if bt3.rect.collidepoint(event.pos):
                    init_main_screen(screen)
            else:
                con = sqlite3.connect('maps.db')
                cur = con.cursor()
                if bt1.rect.collidepoint(event.pos):
                    bt = cur.execute(f"""SELECT * FROM Buttons
                            WHERE bg_id = {present_screen}""").fetchall()[0]
                    present_screen = bt[5]
                    continue_texts(screen)
                elif bt2.rect.collidepoint(event.pos):
                    bt = cur.execute(f"""SELECT * FROM Buttons
                            WHERE bg_id = {present_screen}""").fetchall()[1]
                    present_screen = bt[5]
                    continue_texts(screen)


def update_screen():
    global screen
    global sprites
    global bt1
    global bt2
    global bt3
    global first_character
    global second_character
    bt1.kill()
    bt1.remove()
    bt2.kill()
    bt2.remove()
    bt1, bt2, bt3 = None, None, None
    if bt3:
        bt3.kill()
        bt3.remove()
    if first_character:
        first_character.kill()
        first_character.remove()
        second_character.kill()
        second_character.remove()
    show_game(screen)


class Rectangle(pygame.sprite.Sprite):
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
    bt1 = None
    bt2 = None
    bt3 = None
    bt_close = None
    ends_texts = 0
    first_character = None
    second_character = None
    now_text = []
    saved_screen = 0
    click = pygame.mixer.Sound('snd/click.mp3')
    present_screen = 1
    sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    init_main_screen(screen)
    while running:
        process_event(screen)
        pygame.display.flip()
    with open('present screen.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        writer.writerow([str(present_screen) if present_screen != 1 and present_screen != 13 else str(saved_screen)])
    pygame.quit()
