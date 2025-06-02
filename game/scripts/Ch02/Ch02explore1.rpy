
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
default checked_toilet_배수구 = False
default checked_toilet_락스 = False
default checked_toilet_물때_ = False

default is_object_locked = False

default visited_livingroom = False

default visited_studyroom = False

default visited_toilet = False

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
            action Jump("chapter2_3")

screen screen_livingroom():
    tag menu
    if not is_object_locked:
        if not checked_livingroom_시신:
                button:
                    xpos 713
                    ypos 821
                    xsize 600
                    ysize 200
                    background "#0000"  # 붉은 계열 반투명
                    # text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_시신", True), Jump("livingroom_시신")]
        if not checked_livingroom_TV:
                button:
                    xpos 1260
                    ypos 457
                    xsize 300
                    ysize 220
                    background "#0000"  # 붉은 계열 반투명
                    # text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_TV", True), Jump("livingroom_TV")] 
        if not checked_livingroom_창문:
                button:
                    xpos 682
                    ypos 186
                    xsize 650
                    ysize 558
                    background "#0000"  # 붉은 계열 반투명
                    # text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_livingroom_창문", True), Jump("livingroom_창문")]
        if checked_livingroom_TV or checked_livingroom_시신 or checked_livingroom_창문 :
            use 조사_종료

screen screen_studyroom():
    tag menu
    if not is_object_locked:
        if not checked_studyroom_책:
                button:
                    xpos 571
                    ypos 323
                    xsize 20
                    ysize 76
                    background "#0000"  # 붉은 계열 반투명
                    # text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_책", True), Jump("studyroom_책")]
        if not checked_studyroom_일기:
                button:
                    xpos 800
                    ypos 661
                    xsize 200
                    ysize 40
                    background "#0000"  # 붉은 계열 반투명
                    #text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_일기", True), Jump("studyroom_일기")]
        if not checked_studyroom_침대:
                button:
                    xpos 1250
                    ypos 500
                    xsize 330
                    ysize 300
                    background "#0000"  # 붉은 계열 반투명
                    #text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_studyroom_침대", True), Jump("studyroom_침대")]
        if checked_studyroom_일기 or checked_studyroom_책 or checked_studyroom_침대 :
            use 조사_종료
    
screen screen_toilet():
    tag menu
    if not is_object_locked:
        if not checked_toilet_배수구:
             button:
                    xpos 821
                    ypos 975
                    xsize 130
                    ysize 80
                    background "#0000"
                    hovered SetVariable("show_hint", True)
                    unhovered SetVariable("show_hint", False)
                    #background "#f008"  # 붉은 계열 반투명
                    #style_prefix None
                    #text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_toilet_배수구", True), Jump("toilet_배수구")]
        if not checked_toilet_락스:
                button:
                    xpos 1027
                    ypos 692
                    xsize 100
                    ysize 192
                    background "#0000"
                    #background "#f008"  # 붉은 계열 반투명
                    #style_prefix None
                    #text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_toilet_락스", True), Jump("toilet_락스")]
        if not checked_toilet_물때_:
                button:
                    xpos 180
                    ypos 370
                    xsize 70
                    ysize 70
                    background "#0000"
                    #background "#f008"  # 붉은 계열 반투명
                    #style_prefix None
                    #text "여기!" color "#fff"
                    action [SetVariable("is_object_locked", True), SetVariable("checked_toilet_물때", True), Jump("toilet_물때")]
        if checked_toilet_배수구 or checked_toilet_락스 or checked_toilet_물때_ :
            use 조사_종료

label chapter2_3_explore_livingroom:
    $ visited_livingroom = True
    scene chapter2_3_1bg
    "이 장소를 조사합니다. 필요한 오브젝트를 클릭하세요."
    window hide
    call screen screen_livingroom
    jump chpater2_3


label chapter2_3_explore_studyroom:
    $ visited_studyroom = True
    scene chapter2_3_2bg
    "이 장소를 조사합니다. 필요한 오브젝트를 클릭하세요."
    window hide
    call screen screen_studyroom
    jump chapter2_3


label chapter2_3_explore_toilet:
    $ visited_toilet = True
    scene chapter2_3_3bg
    "이 장소를 조사합니다. 필요한 오브젝트를 클릭하세요."
    window hide
    call screen screen_toilet
    jump chapter2_3

label livingroom_시신:
    show hajun at left_bottom_offset onlayer master
    hajun "죽은지 며칠 된듯해. 부패상태를 봐서는 3~4일은 된거 같군. \n사인은 수많은 자상때문에 생긴 과다출혈로 인한 쇼크사로 추측 해볼 수 있어."
    hide hajun
    show hajun at left_bottom_offset onlayer master
    hajun "하지만 이상해. 사람을 죽일거였으면, 급소를 찔러 한번에 죽여야 할 것인데, 어째서?"
    hide hajun
    show hajun_serious at left_bottom_offset onlayer master
    hajun "고문을 행한 것처럼 의자에 앉혀서 천천히 죽여갔다는 것인데…."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "마치 8년전 고문실에서 봤던 매듭법이랑 비슷해."
    hide hajun_serious
    show hajun_serious at left_bottom_offset
    hajun "그러고 보니 거기에도 바닥에 피가 고여서 마른 느낌이 아니라 피가 주위로 마구 튄 느낌이었지."
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
    show hajun at left_bottom_offset
    hajun "창문이다. 되게 큰 통유리야."
    hide hajun
    show hajun at left_bottom_offset
    hajun "창문에는 피해자의 혈흔이 묻어있어. 얼마나 많은 피를 흘렸는지 눈감고도 알 정도야."
    hide hajun
    show hajun at left_bottom_offset
    hajun "하지만, 피해자의 혈흔 말고는 달리 눈에 띄는 건 없네, 조사하는덴 큰 도움이 없을 거 같아."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_livingroom


label studyroom_책:
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
    hajun "나중에 따로 조사해봐야겠어. 그걸 왜 생각 못했지? 일단 다른 거부터 탐색 해보자."
    hide hajun_serious
    $ is_object_locked = False 
    jump chapter2_3_explore_studyroom


label studyroom_일기:
    show hajun at left_bottom_offset
    hajun "일기다. 아마도 이 살인사건에 관한 이야기를 적어 두지 않았을까?"
    hide hajun
    show hajun at left_bottom_offset
    hajun "보자…'오늘은 아이스크림을 먹었다. 맛있었다. 또먹고싶다'…."
    hide hajun
    show hajun at left_bottom_offset
    hajun "'길 가다가 귀여운 강아지를 봤다. 한번쓰다듬어 보고 싶었지만 강아지가 도망쳤다.'"
    hide hajun
    show hajun at left_bottom_offset
    hajun "이게… 성인남성의 일기장..? 사는 곳과 나이에 안맞게 굉장히 순수한 사람이였군…."
    hide hajun
    show hajun at left_bottom_offset
    hajun "침대다. 푹신해 보이네."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_studyroom


label studyroom_침대:
    show hajun at left_bottom_offset
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


label toilet_배수구:
    show hajun at left_bottom_offset
    hajun "배수구네. 혹시 용의자의 체모가 여기에 걸려있지않을까?"
    hide hajun
    show hajun at left_bottom_offset
    hajun "깨끗하네… 아무것도 없어.."
    hide hajun
    show hajun at left_bottom_offset
    hajun "조사에 도움이 안될거 같아."
    $ is_object_locked = False
    hide hajun
    jump chapter2_3_explore_toilet


label toilet_락스:
    show hajun at left_bottom_offset
    hajun "락스네. 혹시 피를 지우기 위해 사용 하려 했지 않을까?"
    hide hajun
    show hajun at left_bottom_offset
    hajun "새 거네.. 아직 열려있지 않아."
    hide hajun
    show hajun at left_bottom_offset
    hajun "그렇다면 용의자와 관련이 있어보이지 않아."
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_toilet


label toilet_물때:
    show hajun at left_bottom_offset
    hajun "물때다…"
    hide hajun
    show hajun at left_bottom_offset
    hajun "….."
    hide hajun
    show hajun at left_bottom_offset
    hajun "전혀 조사와 상관이 없잖아. 난 왜 본거지?"
    hide hajun
    $ is_object_locked = False
    jump chapter2_3_explore_toilet