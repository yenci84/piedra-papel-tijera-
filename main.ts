input.onGesture(Gesture.Shake, function () {
    if (randint(1, 3) == 1) {
        basic.showLeds(`
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        music.playMelody("C D E F G A B C5 ", 120)
    } else if (randint(1, 3) == 2) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
        music.playMelody("C5 A B G A F G E ", 120)
    } else if (randint(1, 3) == 3) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . # . .
            . # . # .
            # # . # #
            `)
        music.playMelody("G B A G C5 B A B ", 120)
    } else {
    	
    }
})
