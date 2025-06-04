screen game_over_screen:
    tag menu
    modal True

    add Solid("#000000")
    text "Game Over" xalign 0.5 yalign 0.3 size 60

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.6

        textbutton "다시 시작" action [Hide("game_over_screen"), SetVariable("life", 3)
            , SetVariable("wrong_count", 0), Jump("start")]
        textbutton "타이틀로" action MainMenu()
        textbutton "게임 종료" action Quit(confirm=False)

label check_fail:
    if wrong_count >= 3:
        hide screen choice
        jump gameover
    return

label gameover:
    hide window
    stop music
    play sound "sfx_gameover.mp3"
    show screen game_over_screen
    return