@namespace
class SpriteKind:
    Stair = SpriteKind.create()

# Variables
BOSS: Sprite = None
projectile: Sprite = None
Direction = 0
Ladder: Sprite = None
Stage = 1
mySprite: Sprite = None
PIZZA: Sprite = None

# Set Up Work
PIZZA = sprites.create(assets.image("""
    Pizza
"""), SpriteKind.food)
mySprite = sprites.create(assets.image("""
    Player
"""), SpriteKind.player)
animation.run_image_animation(mySprite,
    [img("""
            . . . . . . . . . . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . f f f 2 2 f f f . . . . .
                . . f f f 2 2 2 2 f f f . . . .
                . f f f e e e e e e f f f . . .
                . f f e 2 2 2 2 2 2 e e f . . .
                . f e 2 f f f f f f 2 e f . . .
                . f f f f e e e e f f f f . . .
                f f e f b f 4 4 f b f e f f . .
                f e e 4 1 f d d f 1 4 e e f . .
                . f f f f d d d d d e e f . . .
                f d d d d f 4 4 4 e e f . . . .
                f b b b b f 2 2 2 2 f 4 e . . .
                f b b b b f 2 2 2 2 f d 4 . . .
                . f c c f 4 5 5 4 4 f 4 4 . . .
                . . f f f f f f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                f d f e e d d d d d 4 e f f . .
                f b f f e e 4 4 4 e d d 4 e . .
                f b f 4 f 2 2 2 2 e d d e . . .
                f c f . f 2 2 c c c e e . . . .
                . f f . f 4 4 c d c 4 f . . . .
                . . . . f f f d d c f f . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . f f . . . . . . .
                . . . . . f f 2 2 f f . . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f 2 2 2 2 2 2 f f f . .
                . . f f f 2 2 2 2 2 2 f f f . .
                . . f e e e e e e e e e e f f .
                . f f e 2 2 2 2 2 2 2 2 e f f .
                . f f f f f e e e e f f f f f .
                f d f e f b f 4 4 f b f e f f .
                f b f e 4 1 f d d f 1 4 e f . .
                f b f f e 4 d d d d 4 e f e . .
                f c f e f 2 2 2 2 2 f 4 e . . .
                . f f 4 f 4 4 5 5 4 f 4 e . . .
                . . . . f f f f f f d d e . . .
        """),
        img("""
            . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 d d d d d d 4 e e f .
                f d f e e d d d d d 4 e e f f e
                f b f f e e 4 4 4 4 e e 4 f d d
                f b f 4 f 2 2 2 2 2 2 f 1 e d d
                f c f . f 2 2 2 2 2 2 f 4 4 e e
                . f f . f 4 4 5 5 4 4 f . . . .
                . . . . f f f f f f f f . . . .
        """)],
    500,
    True)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
info.set_life(3)
SetStage()

# Methods & Event Handling
def on_up_pressed():
    global Direction
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        500,
        True)
    Direction = 180
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    global Stage
    Stage += 1
    SetStage()
sprites.on_overlap(SpriteKind.player, SpriteKind.Stair, on_on_overlap)

def StageOne():
    tiles.set_tilemap(tilemap("""
        Level1
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
    """))

def on_a_pressed():
    global projectile
    if Direction == 270:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Arrow2
        """), mySprite, -50, 0)
    elif Direction == 90:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Arrow1
        """), mySprite, 50, 0)
    elif Direction == 180:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Arrow0
        """), mySprite, 0, -50)
    else:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            Arrow
        """), mySprite, 0, 50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global Direction
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . . f 2 f e e e e f f . . 
                        . . . . f 2 2 2 f e e e e f f . 
                        c . . . f e e e e f f e e e f . 
                        d c . f e 2 2 2 2 e e f f f f . 
                        d d c f 2 e f f f f 2 2 2 e f . 
                        c d d c f f e e e f f f f f f f 
                        . c d d c e 4 4 f b e 4 4 e f f 
                        . . c d c e d d f 1 4 d 4 e e f 
                        . . c c c d e d d d 4 e e e f . 
                        . . . e d d 4 e 4 4 e e f f . . 
                        . . . . e e 4 4 2 2 2 2 f . . . 
                        . . . . . f 2 e 2 2 2 2 f . . . 
                        . . . . . f 5 5 4 4 4 4 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . . f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f . . . . . . . 
                        . . . . . f 2 f f f f f . . . . 
                        . . . f f 2 2 e e e e e f f . . 
                        . . f f 2 2 2 e e e e e e f f . 
                        . . f e e e e f f f e e e e f . 
                        . f e 2 2 2 2 e e e f f f f f . 
                        . f 2 e f f f f f 2 2 2 e f f f 
                        . f f f e e e f f f f f f f f f 
                        . f e e 4 4 f b b e 4 4 e f e f 
                        . . f e d d f b b 4 d 4 e e f . 
                        c e e f d d d d d 4 e e e f . . 
                        c d d e e 2 2 2 2 2 2 2 f . . . 
                        c d d 4 4 e 5 4 4 4 4 4 f . . . 
                        . e e e e f f f f f f f f . . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . . f f . . . . . . . 
                        . . . . . f f 2 f f f f . . . . 
                        . . . . f f 2 f e e e e f f . . 
                        . . . f f 2 2 f e e e e e f f . 
                        . . . f e e e e f f e e e e f . 
                        . . f e 2 2 2 2 e e f f f f f . 
                        . . f 2 e f f f f 2 2 2 e f f f 
                        . . f f f e e e f f f f f f f f 
                        . . f e e 4 4 f b e 4 4 e f e f 
                        . . . f e d d f b 4 d 4 e e f . 
                        . . c . e e d d d 4 e e e f . . 
                        c c c e d d e e 2 2 2 2 f . . . 
                        d d c e d d 4 4 e 4 4 4 f . . . 
                        c c c . e e e e f f f f f . . . 
                        . . c . . . f f f f f f f f . . 
                        . . . . . . . f f . . f f f . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . . f 2 f e e e e f f . . 
                        . . . . f 2 2 2 f e e e e f f . 
                        . . . . f e e e e f f e e e f . 
                        . . . f e 2 2 2 2 e e f f f f . 
                        . . . f 2 e f f f f 2 2 2 e f . 
                        . . . f f f e e e f f f f f f f 
                        . . . f e e 4 4 f b e 4 4 e f f 
                        . . . . f e d d f 1 4 d 4 e e f 
                        . . . . . f d d d d 4 e e e f . 
                        . . . . . f e 4 4 4 e d d f . . 
                        . . . . . c c c 2 2 e d d f . . 
                        . . . . . c d c 2 2 f e e . . . 
                        . . . . c d d c 4 4 3 4 f . . . 
                        . . . c d d c f f f f f . . . . 
                        . . c d d c . . f f f . . . . .
            """)],
        500,
        True)
    Direction = 270
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    info.change_life_by(-1)
    info.start_countdown(15)
info.on_countdown_end(on_countdown_end)

def StageThree():
    global BOSS
    tiles.set_tilemap(tilemap("""
        level3
    """))
    Ladder.destroy()
    BOSS = sprites.create(assets.image("""
        Boss
    """), SpriteKind.enemy)
    info.set_life(3)
def StageTwo():
    tiles.set_tilemap(tilemap("""
        level2
    """))
    mySprite.set_position(8, 8)
    Ladder.set_position(246, 8)

def on_right_pressed():
    global Direction
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . f f e e e e f 2 f . . . . . 
                        . f f e e e e f 2 2 2 f . . . . 
                        . f e e e f f e e e e f . . . c 
                        . f f f f e e 2 2 2 2 e f . c d 
                        . f e 2 2 2 f f f f e 2 f c d d 
                        f f f f f f f e e e f f c d d c 
                        f f e 4 4 e b f 4 4 e c d d c . 
                        f e e 4 d 4 1 f d d e c d c . . 
                        . f e e e 4 d d d e d c c c . . 
                        . . f f e e 4 4 e 4 d d e . . . 
                        . . . f 2 2 2 2 4 4 e e . . . . 
                        . . . f 2 2 2 2 e 2 f . . . . . 
                        . . . f 4 4 4 4 5 5 f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . f f f . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . f f f f f 2 f . . . . . 
                        . . f f e e e e e 2 2 f f . . . 
                        . f f e e e e e e 2 2 2 f f . . 
                        . f e e e e f f f e e e e f . . 
                        . f f f f f e e e 2 2 2 2 e f . 
                        f f f e 2 2 2 f f f f f e 2 f . 
                        f f f f f f f f f e e e f f f . 
                        f e f e 4 4 e b b f 4 4 e e f . 
                        . f e e 4 d 4 b b f d d e f . . 
                        . . f e e e 4 d d d d d f e e c 
                        . . . f 2 2 2 2 2 2 2 e e d d c 
                        . . . f 4 4 4 4 4 5 e 4 4 d d c 
                        . . . f f f f f f f f e e e e . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . . . . f f . . . . . . . 
                        . . . . f f f f 2 f f . . . . . 
                        . . f f e e e e f 2 f f . . . . 
                        . f f e e e e e f 2 2 f f . . . 
                        . f e e e e f f e e e e f . . . 
                        . f f f f f e e 2 2 2 2 e f . . 
                        f f f e 2 2 2 f f f f e 2 f . . 
                        f f f f f f f f e e e f f f . . 
                        f e f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 b f d d e f . . . 
                        . . f e e e 4 d d d e e . c . . 
                        . . . f 2 2 2 2 e e d d e c c c 
                        . . . f 4 4 4 e 4 4 d d e c d d 
                        . . . f f f f f e e e e . c c c 
                        . . f f f f f f f f . . . c . . 
                        . . f f f . . f f . . . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . f f e e e e f 2 f . . . . . 
                        . f f e e e e f 2 2 2 f . . . . 
                        . f e e e f f e e e e f . . . . 
                        . f f f f e e 2 2 2 2 e f . . . 
                        . f e 2 2 2 f f f f e 2 f . . . 
                        f f f f f f f e e e f f f . . . 
                        f f e 4 4 e b f 4 4 e e f . . . 
                        f e e 4 d 4 1 f d d e f . . . . 
                        . f e e e 4 d d d d f . . . . . 
                        . . f d d e 4 4 4 e f . . . . . 
                        . . f d d e 2 2 c c c . . . . . 
                        . . . e e f 2 2 c d c . . . . . 
                        . . . f 4 3 4 4 c d d c . . . . 
                        . . . . f f f f f c d d c . . . 
                        . . . . . f f f . . c d d c . .
            """)],
        500,
        True)
    Direction = 90
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    global Direction
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f f 2 2 f f f . . . . . 
                        . . f f f 2 2 2 2 f f f . . . . 
                        . f f f e e e e e e f f f . . . 
                        . f f e 2 2 2 2 2 2 e e f . . . 
                        . f e 2 f f f f f f 2 e f . . . 
                        . f f f f e e e e f f f f . . . 
                        f f e f b f 4 4 f b f e f f . . 
                        f e e 4 1 f d d f 1 4 e e f . . 
                        . f f f f d d d d d e e f . . . 
                        f d d d d f 4 4 4 e e f . . . . 
                        f b b b b f 2 2 2 2 f 4 e . . . 
                        f b b b b f 2 2 2 2 f d 4 . . . 
                        . f c c f 4 5 5 4 4 f 4 4 . . . 
                        . . f f f f f f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        f d f e e d d d d d 4 e f f . . 
                        f b f f e e 4 4 4 e d d 4 e . . 
                        f b f 4 f 2 2 2 2 e d d e . . . 
                        f c f . f 2 2 c c c e e . . . . 
                        . f f . f 4 4 c d c 4 f . . . . 
                        . . . . f f f d d c f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . f f . . . . . . . 
                        . . . . . f f 2 2 f f . . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f 2 2 2 2 2 2 f f f . . 
                        . . f f f 2 2 2 2 2 2 f f f . . 
                        . . f e e e e e e e e e e f f . 
                        . f f e 2 2 2 2 2 2 2 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        f d f e f b f 4 4 f b f e f f . 
                        f b f e 4 1 f d d f 1 4 e f . . 
                        f b f f e 4 d d d d 4 e f e . . 
                        f c f e f 2 2 2 2 2 f 4 e . . . 
                        . f f 4 f 4 4 5 5 4 f 4 e . . . 
                        . . . . f f f f f f d d e . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 d d d d d d 4 e e f . 
                        f d f e e d d d d d 4 e e f f e 
                        f b f f e e 4 4 4 4 e e 4 f d d 
                        f b f 4 f 2 2 2 2 2 2 f 1 e d d 
                        f c f . f 2 2 2 2 2 2 f 4 4 e e 
                        . f f . f 4 4 5 5 4 4 f . . . . 
                        . . . . f f f f f f f f . . . .
            """)],
        500,
        True)
    Direction = 0
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.over(False)
    info.stop_countdown()
    info.set_score(info.score())
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    if True:
        music.power_up.play()
        info.change_score_by(1)
        PIZZA.set_position(randint(0, 160), randint(0, 120))
        info.start_countdown(20)
        if info.life() < 3:
            info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def SetStage():
    if Stage == 1:
        StageOne()
    elif Stage == 2:
        StageTwo()
    else:
        StageThree()

def on_on_overlap3(sprite3, otherSprite3):
    otherSprite3.destroy()
    game.over(True)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)


# Game Loop
while True:
    pause(100)
    if info.score() == 25:
        Ladder = sprites.create(assets.image("""
            Ladder
        """), SpriteKind.Stair)
        tiles.place_on_random_tile(Ladder, sprites.dungeon.dark_ground_north_west0)
        break