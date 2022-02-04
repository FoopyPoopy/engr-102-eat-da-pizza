namespace SpriteKind {
    export const Stair = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Stair, function (sprite, otherSprite) {
    tiles.setTilemap(tilemap`level2`)
    mySprite.setPosition(8, 8)
    Ladder.setPosition(246, 8)
})
info.onCountdownEnd(function () {
	
})
info.onLifeZero(function () {
    game.over(false)
    info.stopCountdown()
    info.setScore(info.score())
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    if (true) {
        music.powerUp.play()
        info.changeScoreBy(1)
        PIZZA.setPosition(randint(0, 160), randint(0, 120))
        info.startCountdown(10)
    }
})
let Ladder: Sprite = null
let mySprite: Sprite = null
let PIZZA: Sprite = null
tiles.setTilemap(tilemap`Level1`)
PIZZA = sprites.create(assets.image`Pizza`, SpriteKind.Food)
mySprite = sprites.create(assets.image`Player`, SpriteKind.Player)
Ladder = sprites.create(assets.image`Ladder`, SpriteKind.Stair)
animation.runImageAnimation(
mySprite,
[img`
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
    `,img`
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
    `,img`
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
    `,img`
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
    `],
500,
true
)
controller.moveSprite(mySprite)
tiles.placeOnRandomTile(mySprite, assets.tile`transparency16`)
scene.cameraFollowSprite(mySprite)
tiles.placeOnRandomTile(Ladder, sprites.dungeon.darkGroundNorthWest0)
info.setLife(3)
