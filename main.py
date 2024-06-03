def on_a_pressed():
    global Meteorite
    if info.score() >= 3:
        Meteorite = sprites.create_projectile_from_sprite(assets.image("""
            Projectile
        """), mySprite, 65, 0)
        animation.run_image_animation(Meteorite,
            assets.animation("""
                Projectile_Animation
            """),
            100,
            True)
        info.change_score_by(-3)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    if statusbar.value >= 10:
        mySprite.vy = -100
        mySprite.vx = -50
        statusbar.value += -8
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite2, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_score():
    carnival.on_game_over_expanded(carnival.WinTypes.TIMED)
info.on_score(100, on_on_score)

def on_right_pressed():
    if statusbar.value >= 10:
        mySprite.vy = -100
        mySprite.vx = 50
        statusbar.value += -8
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.spray, 200)
    sprites.destroy(sprite, effects.spray, 100)
    info.change_score_by(5)
    music.play(music.create_sound_effect(WaveShape.NOISE,
            3300,
            1400,
            255,
            0,
            150,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    statusbar.value += 10
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

Bat: Sprite = None
Meteorite: Sprite = None
mySprite: Sprite = None
statusbar: StatusBarSprite = None
carnival.start_timer()
statusbar = statusbars.create(120, 4, StatusBarKind.energy)
statusbar.position_direction(CollisionDirection.BOTTOM)
Dificulty = 1840
scene.set_background_image(assets.image("""
    BackGround
"""))
mySprite = sprites.create(assets.image("""
    Player
"""), SpriteKind.player)
animation.run_image_animation(mySprite,
    assets.animation("""
        Player_Animation
    """),
    100,
    True)
mySprite.set_position(80, 60)
mySprite.ay = 320
mySprite.set_stay_in_screen((0) <= (30))
info.set_score(0)
music.play(music.string_playable("A F E F D G E F ", 120),
    music.PlaybackMode.IN_BACKGROUND)

def on_update_interval():
    info.change_score_by(1)
game.on_update_interval(1000, on_update_interval)

def on_forever():
    global Bat, Dificulty
    Bat = sprites.create_projectile_from_side(assets.image("""
        Enemy
    """), -65, 0)
    animation.run_image_animation(Bat,
        assets.animation("""
            Enemy_Animation
        """),
        100,
        True)
    Bat.y = randint(15, 100)
    Bat.set_kind(SpriteKind.enemy)
    pause(Dificulty)
    if Dificulty > 800:
        Dificulty += -80
forever(on_forever)

def on_forever2():
    if statusbar.value <= 8:
        statusbar.set_color(12, 11)
    if statusbar.value > 8 and statusbar.value <= 33:
        statusbar.set_color(2, 11)
    if statusbar.value > 33 and statusbar.value <= 66:
        statusbar.set_color(4, 11)
    if statusbar.value > 66:
        statusbar.set_color(5, 11)
forever(on_forever2)

def on_update_interval2():
    statusbar.value += 1
game.on_update_interval(100, on_update_interval2)
