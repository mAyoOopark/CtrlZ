label chapter5_2:
    show screen life_display
    scene chapter5_1bg with fade
    stop music fadeout 1.0   
    stop amb fadeout 1.0
    play music "bgm_ch5_2.mp3" fadeout 1.0 volume 2.0   
    play amb "amb_city.mp3" fadein 1.0 volume 0.1
    show hajun_hard at left_bottom_offset
    hajun "헉.. 헉.."
    hajun "대체 어디로 간거야..?"
    hide hajun_hard

    play sound2 "sfx_calling.mp3" volume 0.7   
    show hajun at left_bottom_offset
    hajun "형님한테 지원 요청을 해야겠어.."
    #통화 연결음 시간에 따라서 아래 퍼즈 조정하면 될 것 같아용
    hide hajun

    pause (2.0)
    show hajun_wtf at left_bottom_offset
    hajun "뭐야.. 왜 전화를 안받는거야?"
    stop sound2
    # play sound2 "sfx_ch2_click_phone.mp3"
    hide hajun_wtf

    play sound "sfx_ch2_cellphone_ring.ogg"
    show hajun_curious at left_bottom_offset
    hajun "형님인가?"
    hide hajun_curious
    pause (2.0)

    play sound "sfx_ch2_click_phone.mp3"
    show hajun at left_bottom_offset
    hajun "형님! 어디세요, 왜 이렇게 전화를 안받아요?"
    hide hajun

    $ renpy.music.set_volume(0.08, channel='amb')
    show police_1 at right_bottom_offset
    police "여기는 XX경찰서입니다."
    extend "\n남종식 형사님이 전화를 안받으셔서 이쪽으로 전화를 드립니다."
    hide police_1

    show hajun_consider at left_bottom_offset
    hajun "그쪽에서 무슨 일이시죠?"
    hide hajun_consider

    show police1 at right_bottom_offset
    police "다름이 아니라 두 분께서 조사하신 살인 사건 있지 않습니까."
    police "그 사건이랑 매우 유사한 살인 사건이 \n갑자기 여러 건 신고가 접수 되었습니다."
    police "혹시 뭔가 아시는 게 있으신가 해서요"
    hide police1

    show dohyeon_asd at center
    show chapter5_1bg at shake
    play sound "sfx_big_shake.mp3"
    asd "{b}{size=40}{color=#803232}으아아아악!!{/b}{/size}{/color}"
    hide dohyeon_asd

    show hajun_surprised at left_bottom_offset
    hajun "잠시만, 갑자기 비명 소리가..!!" with hpunch
    hajun "죄송해요! 나중에 다시 전화드릴게요!" with hpunch
    play sound "sfx_ch2_click_phone.mp3"
    hide hajun_surprised

    scene black with fade

    play sound2 "sfx_hb.mp3" loop
    play sound "sfx_run_man.mp3"
    "나는 갑자기 들려온 신고 전화와 소름끼치는 비명에\n심장이 뒤집어 질 듯이 소리가 들려온 쪽으로 뛰었다."
    "나는 온갖 생각이 스쳐갔다."
    "{i}{color=#803232}{size=40}형님이 잘못된게 아닐까..?{/i}{/color}{/size}"
    "{i}{size=40}{color=#803232}내가 놓친 최민재에게 당한 게 아닐까..?{/i}{/size}{/color}"
    "그 장면을 본 나는 무너져 내릴 수 밖에 없었다."
    "{i}{color=#803232}{size=40}등이 칼에 찔려{/color}{/size} 벽에 기대어 있는 그의 모습"
    "{i}{color=#803232}{size=40}등에서 뿜어져 나오는 피{/color}{/size}는 벽을 타고 번지며,\n마치 붉은 날개처럼 펼쳐져 있었다.{/i}"
    "형님은 숨소리보다 작은 소리로 속삭이며 최민재의 이름을 말했고,"
    extend "\n내가 예상한 일들이 정말로 벌어진 것이었다."
    "그렇게 {color=#803232}{b}과다 출혈{/color}{/b}로 인한 쇼크로 인해"
    extend "\n남종식 형님은 끝내 세상을 떠났고,"
    "최하람을 제외한 나머지 모두를 놓치고 말았다."
    "그 일이 있고 난 뒤, 나는 다른 부서로 발령받았지만"
    "형님이 피를 흘리며 쓰러져 있던 그 장면이 머릿속을 떠나지 않아\n일에 집중할 수 없었다."

    "결국 사직서를 제출하고 백수 생활을 시작했으며,"
    "그 장면을 떠올리지 않기 위해 매일 술에 의지한 채 잠들곤 했다."

    pause(1.0)
    
    scene black with fade
    pro "\nBad End2 : Reached the Rock Bottom"
    stop music fadeout 1.0   
    stop amb fadeout 1.0
    pause(1.0)

    $ renpy.full_restart()
    