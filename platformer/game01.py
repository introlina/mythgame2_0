import pygame, sys

pygame.font.init()


class Koschei(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.time_counter = 0
        self.koschei1 = pygame.image.load('koschei.png').convert_alpha()
        self.koschei1 = pygame.transform.scale(self.koschei1, (player_size[0], player_size[1]))
        self.koschei2 = pygame.image.load('koschei2.png').convert_alpha()
        self.koschei2 = pygame.transform.scale(self.koschei2, (player_size[0], player_size[1]))
        self.images = [self.koschei1, self.koschei2]
        self.koschei_pic = self.images[0]
        self.rect = self.koschei_pic.get_rect(center=(pos))
        self.koschei_coordx = self.rect.x
        self.koschei_coordy = self.rect.y

    def animate_koschei(self):
        self.image = self.images[int(self.time_counter % 2)]
        self.koschei_coordx, self.koschei_coordy = self.rect.x, self.rect.y
        if abs(self.koschei_coordx - self.player_coordx) <= 2 * tile_size and \
                abs(self.koschei_coordy - self.player_coordy) < tile_size:
            pass

    def get_input(self):
        global text_object, time1, k_koschei
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            if abs(self.player_coordx - self.koschei_coordx) < tile_size * 2 and \
                    abs(self.player_coordy - self.koschei_coordy) < tile_size:
                text_object = 'koschei'
                time1 = pygame.time.get_ticks() // 1000
                game_active = False
                Texts(text_object)
                k_koschei += 1

    def update(self, x_shift, player_coords):
        self.player_coordx, self.player_coordy = player_coords[0], player_coords[1]
        self.get_input()
        self.time_counter += 0.05
        self.rect.x += x_shift
        self.animate_koschei()


class Kikimora(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.time_counter = 0
        self.kikimora_sad = pygame.image.load('kikimora_sad.png').convert_alpha()
        self.kikimora_sad = pygame.transform.scale(self.kikimora_sad, (player_size[0], player_size[1]))
        self.kikimora_stand = pygame.image.load('kikimora1.png').convert_alpha()
        self.kikimora_stand = pygame.transform.scale(self.kikimora_stand, (player_size[0], player_size[1]))
        self.kikimora_crying = pygame.image.load('kikimora_crying.png').convert_alpha()
        self.kikimora_crying = pygame.transform.scale(self.kikimora_crying, (player_size[0] * 1.1, player_size[1]))
        self.images = [self.kikimora_crying, self.kikimora_sad, self.kikimora_sad, self.kikimora_sad, self.kikimora_stand]
        self.kikimora_pic = self.images[0]
        self.rect = self.kikimora_pic.get_rect(center=(pos))
        self.kikimora_coordx = self.rect.x
        self.kikimora_coordy = self.rect.y

    def animate_kikimora(self):
        self.image = self.images[int(self.time_counter % 5)]
        self.kikimora_coordx, self.kikimora_coordy = self.rect.x, self.rect.y

    def get_input(self):
        global text_object, time1, k_kikimora
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            if abs(self.player_coordx - self.kikimora_coordx) < tile_size * 2 and \
                    abs(self.player_coordy - self.kikimora_coordy) < tile_size:
                text_object = 'kikimora'
                time1 = pygame.time.get_ticks() // 1000
                game_active = False
                Texts(text_object)
                k_kikimora += 1

    def update(self, x_shift, player_coords):
        self.player_coordx, self.player_coordy = player_coords[0], player_coords[1]
        self.get_input()
        self.time_counter += 0.05
        self.rect.x += x_shift
        self.animate_kikimora()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, object_letter):
        super().__init__()
        self.time_counter = 0
        if object_letter == 'Z':
            self.image = pygame.Surface((size, size))
            self.image = pygame.image.load('ground1.JPEG').convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
            self.rect = self.image.get_rect(topleft=(pos))
            self.object = 'tile'
        elif object_letter == 'X':
            self.image = pygame.Surface((size, size))
            self.image.fill((29, 36, 17))
            self.rect = self.image.get_rect(topleft=(pos))
        elif object_letter == 'W':
            self.image = pygame.Surface((size, size))
            self.image.fill((20, 42, 30))
            self.rect = self.image.get_rect(topleft=(pos))
            self.object = 'swamp'

    def update(self, x_shift, player_coords):
        global kik_coords
        self.player_coordx, self.player_coordy = player_coords[0], player_coords[1]
        self.time_counter += 0.05
        self.rect.x += x_shift


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.player_walk1_image = pygame.image.load('playerwalk1.png').convert_alpha()
        self.player_walk1_image = pygame.transform.scale(self.player_walk1_image, (player_size[0], player_size[1]))
        self.player_walk2_image = pygame.image.load('playerwalk2.png').convert_alpha()
        self.player_walk2_image = pygame.transform.scale(self.player_walk2_image, (player_size[0], player_size[1]))
        self.player_walk1_2_image = pygame.transform.flip(
            self.player_walk1_image, True, False)
        self.player_walk_images = [self.player_walk1_image, self.player_walk2_image]
        self.player_jump_image = pygame.image.load('player_jump.png').convert_alpha()
        self.player_jump_image = pygame.transform.scale(self.player_jump_image, (player_size[0], player_size[1]))
        self.player_jump2_image = pygame.transform.flip(
            self.player_jump_image, True, False)
        self.player_stand_image = pygame.image.load('playerstand1.png')
        self.player_stand_image = pygame.transform.scale(self.player_stand_image, (player_size[0], player_size[1]))
        self.player_walk_index = 0
        self.image = self.player_walk_images[self.player_walk_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -18

    def get_input(self):
        if game_active and pygame.time.get_ticks() // 1000 > 10:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_SPACE]:
                self.player_jump()
            else:
                self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def player_jump(self):
        if self.direction.y == 0:
            self.direction.y = self.jump_speed

    def update(self):
        if game_active:
            self.get_input()
            self.rect.x += self.direction.x * self.speed
        napr_x = self.direction.x
        napr_y = self.direction.y
        if napr_x > 0:
            self.image = self.player_walk1_image
        elif napr_x < 0:
            self.image = self.player_walk1_2_image
        self.player_animation(napr_x, napr_y)

    def player_animation(self, naprx, napry):
        self.player_walk_index += 0.1
        if naprx > 0:
            self.image = self.player_walk_images[int(self.player_walk_index % 2)]
        elif naprx < 0:
            self.image = pygame.transform.flip(
                self.player_walk_images[int(self.player_walk_index % 2)], True, False)
        elif naprx == 0 and napry >= 0:
            self.image = self.player_stand_image
        if napry < 0:
            if naprx >= 0: self.image = self.player_jump_image
            if naprx < 0: self.image = self.player_jump2_image


class Texts:
    def __init__(self, text_object0):
        global game_active, time1, koschei_texts1, text_object, text_before_quests
        global vvodn_text_koschei, kikimora_texts1, vvodn_text_kikimora, counter_texts
        self.time = time1
        self.hero = text_object
        game_active = False
        try:
            if text_object == 'koschei':
                if k_koschei == 0:
                    text = vvodn_text_koschei
                else:
                    text = koschei_texts1[k_koschei - 1]
            if text_object == 'kikimora':
                if k_kikimora == 0:
                    text = vvodn_text_kikimora
                else:
                    text = kikimora_texts1[k_kikimora - 1]
        except:
            if text_object == 'koschei':
                text = ['Кощею больше нечего рассказать:(']
            if text_object == 'kikimora':
                text = ['Кикиморе больше нечего рассказать:(']
        self.image1 = pygame.image.load('svitok.png').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (screen_width * 0.8, screen_height * 0.8))
        self.rect1 = self.image1.get_rect(topleft=((screen_width // 10, screen_height // 10)))
        self.image2 = pygame.Surface((screen_width * 0.5, screen_height * 0.6))
        self.rect2 = self.image2.get_rect(topleft=((screen_width // 8, screen_height // 8)))
        test_font = pygame.font.SysFont('serif', font_size)
        self.blit_text(self.image1, text, (screen_width // 10, screen_height // 10), test_font)
        screen.blit(self.image1, self.rect1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True

    def blit_text(self, surf, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text]
        space = font.size(' ')[0]
        max_width, max_height = surf.get_size()
        x, y = pos
        for line in words:
            for word in line:
                if '\n' in word:
                    word = word[:-1]
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surf.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height


class Start_and_Bottom_Board:
    def __init__(self, iferror=False):
        global game_active
        try:
            phrases_1 = ['Ищите обитателей леса!', 'Чтобы поговорить жмите 0. Чтобы повторить диалоги нажмите [Esc]']
            phrases_2 = ['Им есть что вам рассказать:)', 'Игра начнётся прямо сейчас!']
            test_font = pygame.font.SysFont('serif', font_size)
            time_game = int(pygame.time.get_ticks() // 1000) - 9
            time_all = int(pygame.time.get_ticks() // 1000)
            if pygame.time.get_ticks() // 1000 < 9: time_game = 0
            score_surf1 = test_font.render('', False, 'white')
            score_surf2 = test_font.render('', False, 'white')
            if 1 < time_all < 5:
                score_surf1 = test_font.render(phrases_1[0], False, 'white')
            if 3 < time_all < 6:
                score_surf2 = test_font.render(phrases_2[0], False, 'white')
            if 5 < time_all < 10:
                score_surf1 = test_font.render(phrases_1[1], False, 'white')
            if 6 < time_all < 10:
                score_surf2 = test_font.render(phrases_2[1], False, 'white')
            score_rect1 = score_surf1.get_rect(topleft=(screen_width / 20, screen_height * 6 / 20))
            score_rect2 = score_surf2.get_rect(topleft=(screen_width / 20, screen_height * 8 / 20))
            screen.blit(score_surf1, score_rect1)
            screen.blit(score_surf2, score_rect2)
            screen_time_surf = test_font.render(self.convert_time(int(time_game)),
                                                False, (128, 22, 82))
            screen_time_rect = screen_time_surf.get_rect(topleft=(screen_width / 20 * 18, screen_height * 19 / 20))
            screen.blit(screen_time_surf, screen_time_rect)
        except: pass

    def convert_time(self, sec):
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        return "%02d:%02d:%02d" % (hour, min, sec)


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.kikimora = pygame.sprite.GroupSingle()
        self.koschei = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x, y = col_index * tile_size, row_index * tile_size
                if col == 'X':
                    tile = Tile((x, y), tile_size, 'X')
                    self.tiles.add(tile)
                if col == 'Z':
                    tile = Tile((x, y), tile_size, 'Z')
                    self.tiles.add(tile)
                if col == 'P':
                    player_spr = Player((x, y))
                    self.player.add(player_spr)
                if col == 'K':
                    kikimora_spr = Kikimora((x, y))
                    self.kikimora.add(kikimora_spr)
                if col == 'W':
                    koschei_spr = Koschei((x, y))
                    self.koschei.add(koschei_spr)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 3 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width * 2 / 3 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 4

    def horizontal_colls(self):
        if game_active:
            player = self.player.sprite
            player.rect.x += player.direction.x * player.speed

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def vertical_colls(self):
        if game_active:
            player = self.player.sprite
            player.apply_gravity()

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                    if player.rect.top == sprite.rect.bottom:
                        player.direction.y = 0

    def check_button_kikimora_talk(self, mouse_pos):
        pass

    def run(self):
        player = self.player.sprite
        self.tiles.update(self.world_shift, (player.rect.x, player.rect.y))
        self.tiles.draw(self.display_surface)
        self.kikimora.update(self.world_shift, (player.rect.x, player.rect.y))
        self.kikimora.draw(self.display_surface)
        self.koschei.update(self.world_shift, (player.rect.x, player.rect.y))
        self.koschei.draw(self.display_surface)
        self.scroll_x()

        if game_active:
            self.player.update()
            self.horizontal_colls()
            self.vertical_colls()
            self.player.draw(self.display_surface)
            Start_and_Bottom_Board(self)


level1_map = [
    'XXXXXXXXZ                                                                                        ZXXXXXXXXXXZ',
    'XXXXXXXXZ                                                                                        ZXXXXXXXXXXZ',
    'XXXXXXXXZ             ZZZZZZZ         Z                     ZZ                                   ZXXXXXXXXXXZ',
    'XXXXXZXXX                         Z                                                              ZXXXXXXXXXXZ',
    'XXXXXXXXZ     ZZZZZZ               ZZZZ                                               ZZZZZ      ZXXXXXXXXXXZ',
    'XXXXXXXXZ                 W         ZZZ                                          ZZZZZ           ZXXXXXXXXXXZ',
    'XXXXXXXXX P            ZZZZZ                                                                     ZXXXXXXXXXXZ',
    'ZXXXXXXXXZZ                                                                Z                     ZXXXXXXXXXXZ',
    'XXXZZXXXXXXZZZZ                    ZZZZ    ZZ                K   ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ    ZXXXXXXXXXXZ',
    'XXXXXXXXXXXXXXXZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZXXXXXXXXXXZ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXXZ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXXZ', ]

screen_width = 1200
screen_height = screen_width // 10 * 6
tile_size = 62
player_size = (screen_height / 7.8, screen_width / 10)
font_size = (screen_height + screen_width) // 80
fps = 60

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background_surf1 = pygame.image.load('forest_background1.JPEG')
background_surf2 = pygame.image.load('forest_background2.JPEG')
background_surf3 = pygame.image.load('forest_background3.JPEG')
background_surfs = [background_surf1, background_surf2, background_surf3, background_surf1, background_surf2]
clock = pygame.time.Clock()
level = Level(level1_map, screen)
time_counter = 0
text_object = ''
game_active = True
k = 0
kikimora_texts = []
koschei_texts = []
koschei_texts1 = []
kikimora_texts1 = []
sp = []
vvodn_text_koschei = ['Вы решили поговорить с Кощеем!']
vvodn_text_kikimora = ['Вы решили поговорить с Кикиморой!']
alls = [koschei_texts, kikimora_texts]
k = 0
koschei_questions = []
kikimora_questions = []
helper_sp = []
k_koschei = 0
k_kikimora = 0
counter_texts = 0

# работа с текстовым файлом
with open("texts.txt", 'r', encoding='utf-8') as all_texts:
    for line in all_texts:
        if len(line) == 1:
            k += 1
        alls[k % 2].append(line)
for i in koschei_texts:
    if i == '\n':
        koschei_texts1.append(sp)
        sp = []
    else:
        sp.append(i)
koschei_texts1.append(sp)
sp = []
for i in kikimora_texts:
    if i == '\n' or i == []:
        kikimora_texts1.append(sp)
        sp = []
    else:
        sp.append(i)
kikimora_texts1.append(sp)
kikimora_texts1 = kikimora_texts1[1::]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                k_kikimora = 0; k_koschei = 0
    if game_active is False:
        Texts(text_object)
    time_counter += 0.1
    if game_active:
        screen.fill('black')
        screen.blit(background_surfs[int(time_counter % 5)], (0, 0))
        level.run()

    pygame.display.update()
    clock.tick(fps)