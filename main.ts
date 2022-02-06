namespace SpriteKind {
    export const Stair = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
    Direction = 180
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Stair, function (sprite, otherSprite) {
    Stage += 1
    SetStage()
})
function StageOne () {
    tiles.setTilemap(tilemap`Level1`)
    tiles.placeOnRandomTile(Ladder, sprites.dungeon.darkGroundNorthWest0)
    tiles.placeOnRandomTile(mySprite, assets.tile`transparency16`)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Direction == 270) {
        projectile = sprites.createProjectileFromSprite(assets.image`Arrow2`, mySprite, -50, 0)
    } else if (Direction == 90) {
        projectile = sprites.createProjectileFromSprite(assets.image`Arrow1`, mySprite, 50, 0)
    } else if (Direction == 180) {
        projectile = sprites.createProjectileFromSprite(assets.image`Arrow0`, mySprite, 0, -50)
    } else {
        projectile = sprites.createProjectileFromSprite(assets.image`Arrow`, mySprite, 0, 50)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
    Direction = 270
})
info.onCountdownEnd(function () {
    info.changeLifeBy(-1)
    info.startCountdown(15)
})
function StageThree () {
    tiles.setTilemap(tilemap`level3`)
    Ladder.destroy()
    BOSS = sprites.create(assets.image`Boss`, SpriteKind.Enemy)
    info.setLife(3)
}
function StageTwo () {
    tiles.setTilemap(tilemap`level2`)
    mySprite.setPosition(8, 8)
    Ladder.setPosition(246, 8)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
    Direction = 90
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
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
    Direction = 0
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
        info.startCountdown(20)
        if (info.life() < 3) {
            info.changeLifeBy(1)
        }
    }
})
function SetStage () {
    if (Stage == 1) {
        StageOne()
    } else if (Stage == 2) {
        StageTwo()
    } else {
        StageThree()
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    game.over(true)
})
let BOSS: Sprite = null
let projectile: Sprite = null
let Direction = 0
let Stage = 0
let Ladder: Sprite = null
let mySprite: Sprite = null
let PIZZA: Sprite = null
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
scene.cameraFollowSprite(mySprite)
info.setLife(3)
Stage = 1
SetStage()
