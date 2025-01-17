import wrap, player

wrap.add_sprite_dir('2playergame_sprites')

wrap.world.create_world(1920, 1080)
wrap.world.set_title('2 player game')
wrap.world.set_back_color(25, 150, 237)
# ground
ground = wrap.sprite.add('mario-scenery', 500, 10, 'ground')
wrap.sprite.set_size(ground, 1920, 200)
wrap.sprite.move_left_to(ground, 0)
wrap.sprite.move_bottom_to(ground, 1080)
ground1 = ground
ground2 = ground

# ostrowa
ostrowa = []
ostrow = wrap.sprite.add('mario-scenery', 550, 450, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

ostrow = wrap.sprite.add('mario-scenery', 900, 450, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

ostrow = wrap.sprite.add('mario-scenery', 700, 600, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

ostrow = wrap.sprite.add('mario-scenery', 700, 300, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

ostrow = wrap.sprite.add('mario-scenery', 550, 700, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

ostrow = wrap.sprite.add('mario-scenery', 450, 800, 'ground')
wrap.sprite.set_size(ostrow, 200, 20)
ostrowa.append(ostrow)

for o in ostrowa:
    wrap.sprite.set_costume(o, 'block')

groundup = wrap.sprite.get_top(ground)
# bottle
bottle1 = wrap.sprite.add('bottles', 500, 0, 'bottle1')

bottle1_2 = wrap.sprite.add('bottles', 100, 863, 'bottle1')
# player1
player1 = wrap.sprite.add('mario-1-big', 500, 500, 'stand')
ostrowa.append(player1)
speedy1 = -0
# player2
player2 = wrap.sprite.add('mario-2-big', 550, 500, 'stand')
ostrowa.append(player2)
speedy2 = -0
botspeedy = -0


@wrap.on_key_down(wrap.K_DOWN)
def sit2():
    player.changecostume(player2, 'duck')


@wrap.on_key_down(wrap.K_s)
def sit1():
    player.changecostume(player1, 'duck')


@wrap.on_key_up(wrap.K_s)
def set1s():
    player.changecostume(player1, 'stand')


@wrap.on_key_always(wrap.K_UP)
def jump2():
    global speedy2
    player2y = wrap.sprite.get_bottom(player2)
    groundup = wrap.sprite.get_top(ground2)
    if player2y == groundup:
        speedy2 = -4
        player.changecostume(player2, 'jump')


@wrap.on_key_down(wrap.K_w)
def jump1():
    global speedy1
    player1y = wrap.sprite.get_bottom(player1)
    groundup = wrap.sprite.get_top(ground1)
    if player1y == groundup:
        speedy1 = -4
        player.changecostume(player1, 'jump')


@wrap.always(25)
def down(keys):
    global speedy2, speedy1, botspeedy, ground1, ground2
    ground1 = player.semla(player1, ostrowa, ground)
    speedy1 = player.speeddow(player1, speedy1, ground1, 'stand')

    ground2 = player.semla(player2, ostrowa, ground)
    speedy2 = player.speeddow(player2, speedy2, ground2, 'stand')

    groundbotle = player.semla(bottle1, ostrowa, ground)
    botspeedy = player.speeddow(bottle1, botspeedy, groundbotle, 'bottle1')


# hodba2
@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2(keys):
    if wrap.K_RIGHT in keys:
        player.hodba(player2, 6, player1)
    if wrap.K_LEFT in keys:
        player.hodba(player2, -5, player1)


@wrap.on_key_up(wrap.K_RIGHT, wrap.K_LEFT)
def hodba2s():
    player.changecostume(player2, 'stand')


# hodba1
@wrap.on_key_always(wrap.K_d, wrap.K_a)
def hodba1(keys):
    if wrap.K_d in keys:
        player.hodba(player1, 5, player2)

    if wrap.K_a in keys:
        player.hodba(player1, -5, player2)


@wrap.on_key_up(wrap.K_a, wrap.K_d)
def hodba1s():
    player.changecostume(player1, 'stand')

import wrap_py
wrap_py.app.start()