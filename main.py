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
    if first_character:
        first_character.kill()
        second_character.kill()
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


def init_death_or_win_screen(screen):
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
    if first_character:
        first_character.kill()
        second_character.kill()
    bt1.kill()
    bt1.remove()
    bt2.kill()
    bt2.remove()
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
    global image_bg_menu
    global rect
    if first_character:
        first_character.kill()
        second_character.kill()
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
    now_text = texts.copy()
    for i in texts:
        im = Rectangle(i[3], 0.3, 0.05)
        sprites.add(im)
        sprites.draw(screen)
        pygame.display.flip()
        if i[4]:
            bt1 = cur.execute(f"""SELECT * FROM Buttons
                        WHERE bg_id = {present_screen}""").fetchone()
            bt1 = Rectangle(bt1[2], bt1[3], bt1[4])
            sprites.add(bt1)
            bt2 = cur.execute(f"""SELECT * FROM Buttons
                                WHERE bg_id = {present_screen}""").fetchall()[1]
            bt2 = Rectangle(bt2[2], bt2[3], bt2[4])
            sprites.add(bt2)
            sprites.draw(screen)
            im.kill()
            im.remove()
            del now_text[now_text.index(i)]
            break
        else:
            sleep(5)
            im.kill()
            im.remove()
            if texts.index(i) != len(texts) - 1:
                screen.blit(image_bg_menu, rect)
                pygame.display.update()
            del now_text[now_text.index(i)]

    if present_screen == 2:
        present_screen = 3
        show_game(screen)
    if present_screen == 5:
        present_screen = 10
        init_death_or_win_screen(screen)
    if present_screen == 7:
        dt = cur.execute(f"""SELECT death FROM Buttons
                        WHERE bg_id = 4""").fetchone()
        if dt[0]:
            present_screen = 11
            init_death_or_win_screen(screen)


def continue_texts(screen):
    global now_text
    global sprites
    global image_bg_menu
    global rect
    pygame.display.flip()
    if bt1 and now_text:
        bt1.kill()
        bt1.remove()
        bt2.kill()
        bt2.remove()
    for i in now_text:
        screen.blit(image_bg_menu, rect)
        im = Rectangle(i[3], 0.3, 0.05)
        sprites.add(im)
        sprites.draw(screen)
        pygame.display.flip()
        sleep(5)
        im.kill()
        im.remove()
    pygame.display.flip()
    update_screen()


def process_event(screen):
    global running
    global present_screen
    global saved_screen
    global click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            return
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
                    if 9 <= present_screen <= 12 or present_screen == 14:
                        present_screen = bt[5]
                        update_screen()
                    elif 9 <= bt[5] <= 12 or present_screen == 14:
                        present_screen = bt[5]
                        init_death_or_win_screen(screen)
                        save_progress(2)
                    else:
                        present_screen = bt[5]
                        continue_texts(screen)
                elif bt2.rect.collidepoint(event.pos):
                    bt = cur.execute(f"""SELECT * FROM Buttons
                            WHERE bg_id = {present_screen}""").fetchall()[1]
                    if 9 <= present_screen <= 12 or present_screen == 14:
                        present_screen = 1
                        init_main_screen(screen)
                    elif 9 <= bt[5] <= 12 or present_screen == 14:
                        present_screen = bt[5]
                        init_death_or_win_screen(screen)
                        save_progress(2)
                    else:
                        if present_screen == 4:
                            cur.execute(f'''UPDATE Buttons SET death=1 WHERE bg_id=4''')
                        else:
                            cur.execute(f'''UPDATE Buttons SET death=0 WHERE bg_id=4''')
                        con.commit()
                        present_screen = bt[5]
                        continue_texts(screen)


def save_progress(sc):
    with open('present screen.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        writer.writerow([str(sc)])


def update_screen():
    global screen
    global sprites
    global bt1
    global bt2
    global bt3
    global first_character
    global second_character
    if bt1:
        bt1.kill()
        bt1.remove()
        bt2.kill()
        bt2.remove()
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
    image_bg_menu = None
    rect = None
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
    if 2 <= present_screen <= 8:
        save_progress(present_screen)
    pygame.quit()
