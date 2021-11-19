import wrap


def changecostume(sprite, costume):
    spritebotom = wrap.sprite.get_bottom(sprite)
    wrap.sprite.set_costume(sprite, costume)
    wrap.sprite.move_bottom_to(sprite, spritebotom)


def speeddow(sprite, speed, ground, costume):
    groundup = wrap.sprite.get_top(ground)
    spritebotom = wrap.sprite.get_bottom(sprite)
    wrap.sprite.move(sprite, 0, speed)
    if spritebotom != groundup:
        speed += 0.1
        if wrap.sprite.is_collide_sprite(sprite, ground):
            speed = 0
            wrap.sprite.move_bottom_to(sprite, groundup)
            changecostume(sprite, costume)
    return speed


def walk(p):
    cos2 = wrap.sprite.get_costume(p)
    if cos2 == 'stand':
        changecostume(p, 'walk1')
    elif cos2 == 'walk1':
        changecostume(p, 'walk2')
    elif cos2 == 'walk2':
        changecostume(p, 'walk3')
    elif cos2 == 'walk3':
        changecostume(p, 'walk1')


def hodba(p, storona, stena):
    wrap.sprite.move(p, storona, 0)
    walk(p)
    if wrap.sprite.is_collide_sprite(stena, p):
        wrap.sprite.move(stena,storona,0)

    if storona < 0:
        wrap.sprite.set_reverse_x(p, True)
    if storona > 0:
        wrap.sprite.set_reverse_x(p, False)
