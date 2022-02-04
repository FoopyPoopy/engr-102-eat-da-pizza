@namespace
class SpriteKind:
    Stair = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    tiles.set_tilemap(tilemap("""
        level2
    """))
    mySprite.set_position(8, 8)
    Ladder.set_position(246, 8)
sprites.on_overlap(SpriteKind.player, SpriteKind.Stair, on_on_overlap)

def on_countdown_end():
    pass
info.on_countdown_end(on_countdown_end)

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
        info.start_countdown(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

Ladder: Sprite = None
mySprite: Sprite = None
PIZZA: Sprite = None
tiles.set_tilemap(tilemap("""
    Level1
"""))
PIZZA = sprites.create(assets.image("""
    Pizza
"""), SpriteKind.food)
mySprite = sprites.create(assets.image("""
    Player
"""), SpriteKind.player)
Ladder = sprites.create(assets.image("""
    Ladder
"""), SpriteKind.Stair)
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
tiles.place_on_random_tile(mySprite, assets.tile("""
    transparency16
"""))
scene.camera_follow_sprite(mySprite)
tiles.place_on_random_tile(Ladder, sprites.dungeon.dark_ground_north_west0)
info.set_life(3)