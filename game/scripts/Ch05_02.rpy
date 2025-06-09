label chapter5_2:
    show screen life_display
    scene chapter5_1bg with fade

    show hajun_hard at left_bottom_offset
    hajun "헉.. 헉.."
    hajun "대체 어디로 간거야..?"
    hide hajun_hard

    show hajun at left_bottom_offset
    hajun "형님한테 지원 요청을 해야겠어.."
    #통화 연결음 시간에 따라서 아래 퍼즈 조정하면 될 것 같아용
    pause(1.0)
    hide hajun

    show hajun_wtf at left_bottom_offset
    hajun "뭐야.. 왜 전화를 안받는거야?"
    hide hajun_wtf

    show hajun_curious at left_bottom_offset
    hajun "형님인가?"
    hide hajun_curious

    show hajun at left_bottom_offset
    hajun "형님! 어디세요, 왜 이렇게 전화를 안받아요?"
    hide hajun

    show police_1 at right_bottom_offset
    police "여기는 XX경찰서입니다. 남종식 형사님이 전화를 안받으셔서 이쪽으로 전화를 드립니다."
    hide police_1

    show hajun_consider at left_bottom_offset
    hajun "그쪽에서 무슨 일이시죠?"
    hide hajun_consider

    show police1 at right_bottom_offset
    police "다름이 아니라 두 분께서 조사하신 살인 사건 있지 않습니까."
    police "그 사건이랑 매우 유사한 살인 사건이 갑자기 여러 건 신고가 접수 되었습니다."
    police "혹시 뭔가 아시는 게 있으신가 해서요"
    hide police1

    show dohyeon_asd at center
    show chapter5_1bg at shake
    asd "{b}{size=40}{color=#803232}으아아아악!!{/b}{/size}{/color}"
    hide dohyeon_asd

    show hajun_surprised at left_bottom_offset
    hajun "잠시만, 갑자기 형님의 비명 소리가..!!"
    hajun "죄송해요! 나중에 다시 전화드릴게요!"
    hide hajun_surprised

    scene black with fade

    "나는 갑자기 들려온 충격적인 소식과 소름끼치는 비명에 심장이 뒤집어 질 듯이 소리가 들려온 쪽으로 뛰었다."
    "나는 온갖 생각이 스쳐갔다."
    "{i}{size=40}형님이 잘못된게 아닐까..?{/i}{/size}"
    "{i}{size=40}내가 놓친 최민재에게 당한 게 아닐까..?{/i}{/size}"
    "그 장면을 본 나는 무너져 내릴 수 밖에 없었다."
    "{i}{color=#803232}{size=40}등이 칼에 찔려{/color}{/size} 벽에 기대어 있었고, {color=#803232}{size=40}등에서 뿜어져 나오는 피{/color}{/size}가 벽에 묻어 마치 날개 처럼 보이는 듯 했다.{/i}"
    "형님은 숨소리보다 작은 소리로 속삭이며 최민재의 이름을 말했고, 내가 예상한 일들이 정말로 벌어진 것이었다."
    "그렇게 {color=#803232}{b}과다 출혈{/color}{/b}로 인한 쇼크로 인해 남종식 형님은 장례를 치루게 되었고, 최하람을 제외한 모두를 놓치게 되었다."
    "그 일 이후로 나는 다른 부서로 이동하였지만, 그 날 남종식 형님이 쓰러져있는 장면이 계속해서 눈 앞을 가리게 되어 일이 손에 잡히지 않았다."
    "그렇게 나는 사직서를 내고 집에서 백수로 지내게 되었으며, 그 장면을 보지 않기 위하여 매일 음주를 하며 잠에 들었다."

    pause(1.0)

    scene black with fade

    pause(1.0)

    $ renpy.full_restart()
    