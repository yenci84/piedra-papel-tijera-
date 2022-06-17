def on_gesture_shake():
    if randint(1, 3) == 1:
        basic.show_leds("""
            . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
                        . # # # .
        """)
        music.play_melody("C D E F G A B C5 ", 120)
    elif randint(1, 3) == 2:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . # . .
        """)
        music.play_melody("C5 A B G A F G E ", 120)
    elif randint(1, 3) == 3:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . # . .
                        . # . # .
                        # # . # #
        """)
        music.play_melody("G B A G C5 B A B ", 120)
    else:
        pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
