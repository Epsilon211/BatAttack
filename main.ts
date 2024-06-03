controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (info.score() >= 3) {
        Meteorite = sprites.createProjectileFromSprite(assets.image`Projectile`, mySprite, 70, 0)
        animation.runImageAnimation(
        Meteorite,
        assets.animation`Projectile_Animation`,
        100,
        true
        )
        info.changeScoreBy(-3)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (statusbar.value >= 10) {
        mySprite.vy = -100
        mySprite.vx = -50
        statusbar.value += -8
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    carnival.onGameOverExpanded(carnival.WinTypes.Lose)
})
info.onScore(100, function () {
    carnival.onGameOverExpanded(carnival.WinTypes.Timed)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (statusbar.value >= 10) {
        mySprite.vy = -100
        mySprite.vx = 50
        statusbar.value += -8
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.spray, 200)
    sprites.destroy(sprite, effects.spray, 100)
    info.changeScoreBy(5)
    music.play(music.createSoundEffect(WaveShape.Noise, 3300, 1400, 255, 0, 150, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    statusbar.value += 10
})
let Bat: Sprite = null
let Meteorite: Sprite = null
let mySprite: Sprite = null
let statusbar: StatusBarSprite = null
carnival.startTimer()
statusbar = statusbars.create(120, 4, StatusBarKind.Energy)
statusbar.positionDirection(CollisionDirection.Bottom)
let Dificulty = 1840
scene.setBackgroundImage(assets.image`BackGround`)
mySprite = sprites.create(assets.image`Player`, SpriteKind.Player)
animation.runImageAnimation(
mySprite,
assets.animation`Player_Animation`,
100,
true
)
mySprite.setPosition(80, 60)
mySprite.ay = 320
mySprite.setStayInScreen((0 as any) <= (30 as any))
info.setScore(1)
music.play(music.stringPlayable("A F E F D G E F ", 120), music.PlaybackMode.InBackground)
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(1)
})
forever(function () {
    console.log(statusbar.value)
})
forever(function () {
    Bat = sprites.createProjectileFromSide(assets.image`Enemy`, -65, 0)
    animation.runImageAnimation(
    Bat,
    assets.animation`Enemy_Animation`,
    100,
    true
    )
    Bat.y = randint(15, 110)
    Bat.setKind(SpriteKind.Enemy)
    pause(Dificulty)
    if (Dificulty > 800) {
        Dificulty += -80
    }
})
forever(function () {
    if (statusbar.value <= 8) {
        statusbar.setColor(12, 11)
    }
    if (statusbar.value > 8 && statusbar.value <= 33) {
        statusbar.setColor(2, 11)
    }
    if (statusbar.value > 33 && statusbar.value <= 66) {
        statusbar.setColor(4, 11)
    }
    if (statusbar.value > 66) {
        statusbar.setColor(5, 11)
    }
})
game.onUpdateInterval(100, function () {
    statusbar.value += 1
})
