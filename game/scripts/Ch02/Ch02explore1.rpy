
default checked_explore_livingroom = False
default checked_explore_studyroom = False
default checked_explore_toilet = False
default checked_check_all_rooms = False
default checked_livingroom_시신 = False
default checked_livingroom_TV = False
default checked_livingroom_창문 = False
default checked_studyroom_책 = False
default checked_studyroom_일기 = False
default checked_studyroom_침대 = False

default is_object_locked = False

default visited_livingroom = False

default visited_studyroom = False

default show_hint = False

screen my_screen():
    if show_hint:
        text "여기를 조사할 수 있습니다."  xpos 821 ypos 920 color "#FFFFFF" size 30


screen 조사_종료():
    frame:
        align (0.5, 0.5)
        padding (10, 10)
        background "#0008"
        textbutton "조사를 마쳤다면 이 버튼을 누르세요":
            style "end_button"
            action Jump("chapter2_3")


screen screen_livingroom():
    tag menu
    if not is_object_locked:
        if not checked_livingroom_시신:
            imagebutton:
                xpos 800
                ypos 820
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_시신", True), Jump("livingroom_시신")]
        if not checked_livingroom_TV:
            imagebutton:
                xpos 1310
                ypos 500
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_TV", True), Jump("livingroom_TV")]
        if not checked_livingroom_창문:
            imagebutton:
                xpos 1000
                ypos 300
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_창문", True), Jump("livingroom_창문")]
        if checked_livingroom_TV or checked_livingroom_시신 or checked_livingroom_창문:
            use 조사_종료

screen screen_studyroom():
    tag menu
    if not is_object_locked:
        if not checked_studyroom_책:
            imagebutton:
                xpos 530
                ypos 320
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_책", True), Jump("studyroom_책")]

        if not checked_studyroom_일기:
            imagebutton:
                xpos 810
                ypos 610
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_일기", True), Jump("studyroom_일기")]

        if not checked_studyroom_침대:
            imagebutton:
                xpos 1400
                ypos 500
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_침대", True), Jump("studyroom_침대")]

        if checked_studyroom_일기 or checked_studyroom_책 or checked_studyroom_침대:
            use 조사_종료


label chapter2_3_explore_livingroom:
    $ visited_livingroom = True
    scene chapter2_3_1bg
    "거실을 조사합니다. 클릭하여 수사를 진행하세요."
    window hide
    call screen screen_livingroom
    jump chpater2_3


label chapter2_3_explore_studyroom:
    $ visited_studyroom = True
    scene chapter2_3_2bg
    "서재를 조사합니다. 클릭하여 수사를 진행하세요."
    window hide
    call screen screen_studyroom
    jump chapter2_3


label livingroom_시신:
    play sound "sfx_ch2_investigation.mp3"
    show hajun at left_bottom_offset onlayer master
    hajun "죽은지 며칠 된듯해. 부패상태를 봐서는 3~4일은 된거 같군. \n사인은 수많은 자상때문에 생긴 과다출혈로 인한 쇼크사로 추측 해볼 수 있어."
    hide hajun
    show hajun at left_bottom_offset onlayer master
    hajun "하지만 이상해. 사람을 죽일거였으면,\n급소를 찔러 한번에 죽여야 할 것인데, 어째서?"
    hide hajun
    show hajun_serious at left_bottom_offset onlayer master
    hajun "고문을 행한 것처럼 의자에 앉혀서 천천히 죽여갔다는 것인데…."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "마치 8년전 고문실에서 봤던 매듭법이랑 비슷해."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "그러고 보니 거기에도 바닥에 피가 고여서 마른 느낌이 아니라 \n난도질 당한 듯 주위로 마구 튄 느낌이었지."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "지금 여기 처럼…."
    hide hajun_serious
    show hajun at left_bottom_offset
    hajun "일단 시신 조사는 여기까지 하고, 다른 곳을 찾아보자."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_livingroom


label livingroom_TV:
    play sound "sfx_ch2_investigation.mp3"
    show hajun at left_bottom_offset
    hajun "집도 크더니, TV도 되게 크네."
    hide hajun
    show hajun at left_bottom_offset
    hajun "얼마나 심하게 칼로 긋고 상처냈는지, TV에도 피가 묻어있어."
    hide hajun
    show hajun at left_bottom_offset
    hajun "피해자는 자신이 즐겨보던 TV에 자신의 피가 묻어있을거라곤 상상했었을까?"
    hide hajun
    show hajun at left_bottom_offset
    hajun "하지만 그거랑은 별개로, TV는 이 사건과 관련이 없어보여."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_livingroom


label livingroom_창문:
    play sound "sfx_ch2_investigation.mp3"
    show hajun at left_bottom_offset
    hajun "창문이다. 되게 큰 통유리야."
    hide hajun
    show hajun at left_bottom_offset
    hajun "창문에는 피해자의 혈흔이 묻어있어.\n얼마나 많은 피를 흘렸는지 눈감고도 알 정도야."
    hide hajun
    show hajun at left_bottom_offset
    hajun "하지만, 피해자의 혈흔 말고는 달리 눈에 띄는 건 없네,\n조사하는덴 큰 도움이 없을 거 같아."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_livingroom


label studyroom_책:
    play sound "sfx_ch2_investigation.mp3"
    show hajun at left_bottom_offset
    hajun "책이다. 가죽으로 재단되있는 것 같군. 아무래도 성경인거같아."
    hide hajun
    show hajun at left_bottom_offset
    hajun "잠시만.. 이거 본적있어.."
    hide hajun
    show hajun_serious at left_bottom_offset
    hajun "분명히 이건 8년전 지하실 서재에 있던 그 책이야."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "거기있던 책들은 모두 타버렸을텐데, 어떻게?"
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "최도현은 죽었는데 아직 종교는 건재하다 이건가?"
    hide hajun_serious
    show hajun at left_bottom_offset
    hajun "역시 종교는 종교야. 믿을게 사라졌다해도 없어지지는 않는군."
    hide hajun
    show hajun_serious at left_bottom_offset
    hajun "그렇다면… 제 2의 최도현이 나올 수 도 있다는 말도 되지않나..?"
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "나중에 따로 조사해봐야겠어. 그걸 왜 생각 못했지?\n일단 다른 것들부터 탐색 해보자."
    hide hajun_serious
    $ is_object_locked = False 
    jump chapter2_3_explore_studyroom


label studyroom_일기:
    play sound "sfx_ch2_investigation.mp3"
    show hajun at left_bottom_offset
    hajun "일기다. 아마도 이 살인사건에 관한 이야기를 적어 두지 않았을까?"
    hajun "보자…"
    hide hajun
    play sound "sfx_ch2_flippage.mp3"
    book "{i}'오늘은 아이스크림을 먹었다. 맛있었다. 또먹고싶다...'{/i}"
    play sound "sfx_ch2_flippage.mp3"
    book "{i}'길 가다가 귀여운 강아지를 봤다.\n한번쓰다듬어 보고 싶었지만 강아지가 도망쳤다.'{/i}"
    hide hajun
    show hajun at left_bottom_offset
    hajun "이게… 성인남성의 일기장..?\n사는 곳과 나이에 안맞게 굉장히 순수한 사람이였군…."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_studyroom


label studyroom_침대:
    play sound "sfx_ch2_investigation.mp3" 
    show hajun at left_bottom_offset
    hajun "침대다. 푹신해 보이네."
    hajun "아마도 피해자는 자신이 죽을 날이 다가올지도 모른채 여기서 자고 일어났겠지.."
    hide hajun
    show hajun at left_bottom_offset
    hajun "대체 무슨 이유로 죽인걸까?"
    hide hajun
    show hajun at left_bottom_offset
    hajun "꼭 범인을 찾고 말겠어."
    hide hajun
    show hajun at left_bottom_offset
    hajun "다른 것도 마저 조사해 보자."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_studyroom