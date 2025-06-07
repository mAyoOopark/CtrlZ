default checked_villa_livingroom_칼 = False 
default checked_villa_livingroom_시신 = False 
default checked_villa_livingroom_머리카락 = False 
default checked_villa_livingroom_피글자 = False 
default checked_villa_room_주사기 = False
default checked_villa_room_교리서적 = False
default checked_villa_room_핸드폰 = False
default checked_villa_room_일기 = False

default visited_villa_livingroom = False
default visited_villa_room = True

screen 빌라조사_종료():
    frame:
        align (0.5, 0.5)
        padding (10, 10)
        background "#0008"
        textbutton "조사를 마쳤다면 이 버튼을 누르세요":
            action Jump("chapter2_5")

screen screen_villa_livingroom():
    tag menu
    if not is_object_locked:
        if not checked_villa_livingroom_시신:
            imagebutton:
                xpos 1300
                ypos 800
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_livingroom_시신", True), Jump("villa_livingroom_시신")]

        if not checked_villa_livingroom_칼:
            imagebutton:
                xpos 737
                ypos 915
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_livingroom_칼", True), Jump("villa_livingroom_칼")]

        if not checked_villa_livingroom_머리카락:
            imagebutton:
                xpos 1050
                ypos 850
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_livingroom_머리카락", True), Jump("villa_livingroom_머리카락")]

        if not checked_villa_livingroom_피글자:
            imagebutton:
                xpos 650
                ypos 200
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_livingroom_피글자", True), Jump("villa_livingroom_피글자")]

        if checked_villa_livingroom_칼 and checked_villa_livingroom_피글자 and checked_villa_livingroom_시신 and checked_villa_livingroom_머리카락:
            use 빌라조사_종료

screen screen_villa_room():
    tag menu
    if not is_object_locked:
        if not checked_villa_room_주사기:
            imagebutton:
                xpos 420
                ypos 480
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_room_주사기", True), Jump("villa_room_주사기")]

        if not checked_villa_room_교리서적:
            imagebutton:
                xpos 1300
                ypos 500
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_room_교리서적", True), Jump("villa_room_교리서적")]

        if not checked_villa_room_일기:
            imagebutton:
                xpos 1200
                ypos 480
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_room_일기", True), Jump("villa_room_일기")]

        if not checked_villa_room_핸드폰:
            imagebutton:
                xpos 1100
                ypos 470
                idle "gui/btn_idle.png"
                hover "gui/btn_hover.png"
                action [SetVariable("is_object_locked", True), SetVariable("checked_villa_room_핸드폰", True), Jump("villa_room_핸드폰")]

        if checked_villa_room_주사기 and checked_villa_room_교리서적 and checked_villa_room_일기 and checked_villa_room_핸드폰:
            use 빌라조사_종료



label chapter2_5_explore_villa_livingroom:
    $ visited_villa_livingroom = True
    if checked_villa_livingroom_칼 and checked_villa_livingroom_피글자 and checked_villa_livingroom_시신 and checked_villa_livingroom_머리카락 and checked_villa_room_주사기 and checked_villa_room_교리서적 and checked_villa_room_일기 and checked_villa_room_핸드폰 :
        jump chapter2_6
    if checked_villa_livingroom_칼 and checked_villa_livingroom_피글자 and checked_villa_livingroom_시신 and checked_villa_livingroom_머리카락 :
        "당신은 여기서 필요한 조사를 모두 마쳤습니다"
        jump chapter2_5
    scene chapter2_5_1bg
    "거실을 조사합니다. 필요한 오브젝트를 클릭하세요."
    window hide
    call screen screen_villa_livingroom
    jump chpater2_5

label chapter2_5_explore_villa_room:
    $ visited_villa_room = True
    if checked_villa_livingroom_칼 and checked_villa_livingroom_피글자 and checked_villa_livingroom_시신 and checked_villa_livingroom_머리카락 and checked_villa_room_주사기 and checked_villa_room_교리서적 and checked_villa_room_일기 and checked_villa_room_핸드폰 :
        jump chapter2_6
    if checked_villa_room_주사기 and checked_villa_room_교리서적 and checked_villa_room_일기 and checked_villa_room_핸드폰 :
        "당신은 여기서 필요한 조사를 모두 마쳤습니다"
        jump chapter2_5
    scene chapter2_5_2bg
    "침실을 조사합니다. 필요한 오브젝트를 클릭하세요."
    window hide
    call screen screen_villa_room
    jump chpater2_5

label villa_livingroom_칼:
    show hajun_serious at left_bottom_offset
    hajun "이건 분명히 살인 범행 도구겠지."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "칼에는 피가 낭자하게 묻어있어. 대체 이걸로 몇번이나 찌르고 벤 건지..."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "분명히 증거품으로 사용 될거야. 국과수로 넘기자.."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_livingroom


label villa_livingroom_시신:
    show hajun_serious at left_bottom_offset
    hajun "피해자의 시신이야. 정말 끔찍하군…"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "피해자의 신상으로는 이 집에 사는 주인이며 18살 여자로 보여.\n이 어린 나이에 무슨 죄가 있다고…"
    hide hajun_serious

    show hajun_surprised at left_bottom_offset
    hajun "잠시만.. 이 시체도.. 며칠 전 사건과 같이 의자에 묶인 상태에서\n수십 번을 찌르고 베어서 죽었어."
    hide hajun_surprised

    show hajun_serious at left_bottom_offset
    hajun "범행 수법이 같다는 것은.. 범인도 같다는 것."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "이것도 중요한 증거가 될 거 같아."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_livingroom


label villa_livingroom_머리카락:
    show hajun at left_bottom_offset
    hajun "시신 밑에 뭔가 떨어져 있어..."
    hide hajun

    show hajun at left_bottom_offset
    hajun "이건… 머리카락..?"
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "피해자의 머리카락 길이랑 비교해 봤을 때, \n이건 피해자의 머리 길이랑 같지 않아."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "이건 용의자의 머리카락임이 분명해. 이것도 국과수에 넘기자."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_livingroom


label villa_livingroom_피글자:
    show hajun_serious at left_bottom_offset
    hajun "뭐야, 이게..."
    extend "{i}'주께선 너를 아셨으나, 네가 주를 부인하였도다.'{\i}?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "혹시, 이거 피로 그린거야?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "진짜… 엄청나네… 대체 왜 이런 짓을…"
    hide hajun_serious

    show hajun_consider at left_bottom_offset
    hajun "이 살인이, 종교와 관련이 있는 것 같아.."
    hide hajun_consider

    show hajun_serious at left_bottom_offset
    hajun "이것도 범인을 찾는 데 중요한 단서가 되겠지."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_livingroom

label villa_room_주사기:
    show hajun_curious at left_bottom_offset
    hajun "웬 주사기? 그것도 이렇게나 많이..."
    hide hajun_curious

    show hajun_frown at left_bottom_offset
    hajun "혹시 이거… 마약이야..?"
    hide hajun_frown

    show hajun_serious at left_bottom_offset
    hajun "아니야 혹시 몰라.  "
    extend "피해자의 지병 때문에 처방받은 약일지 몰라.\n인슐린처럼 말이지."
    extend "일단 섣불리 생각하진 말자."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "이것도 성분 조사를 요청해야겠어."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_room


label villa_room_핸드폰:
    show hajun at left_bottom_offset
    hajun "핸드폰이네. 아마도 피해자의 핸드폰인 거 같아."
    hide hajun

    show hajun at left_bottom_offset
    hajun "뭐야..? 뭐 이렇게 문자가 많이 와있어?"
    hide hajun

    show hajun at left_bottom_offset
    hajun "잠시만… 모두 뭔가를 구매 요청을 하기 위한 문자야."
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "대체… 무엇을? 이렇게 많은 사람이?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "일단.. 다른 것도 살펴보자."
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_room


label villa_room_일기:
    show hajun at left_bottom_offset
    hajun "이거는.. 일기잖아? 피해자의 이름이 적혀있는 걸 봐선 피해자의 것으로 보여."
    hide hajun

    show hajun at left_bottom_offset
    hajun "이 사건과 관련이 있을지도 몰라. 일단 한번 살펴볼까?"
    hide hajun

    show hajun at left_bottom_offset
    hajun "『오늘, 청소 중에 마약이 보관되어있는 곳을 봐버린 것 같다. 여기 있기도 지긋지긋한데.. 저거 가지고 나가서 돈이라도 벌어봐?』"
    hide hajun

    show hajun at left_bottom_offset
    hajun "『들고 나왔다! 그리고 하루 만에 거래도 성공했어! 벌써 수중에 이만한 돈이… 일단 숨을 만한 집을 사야겠어. 이정도 돈이면 충분해!』"
    hide hajun

    show hajun at left_bottom_offset
    hajun "『요즘, 거래를 하러 밖에 나가다 보면 이상한 사람들과 자주 마주치는 것 같다. 왠지 나를 쳐다보는 사람들도 있는 거 같고.. 피해망상일까? 혹시 그 사람들은 아니겠지..?』"
    hide hajun

    show hajun at left_bottom_offset
    hajun "『요즘 집에 계속 모르는 사람이 문을 두드려.. 대체 누군거야?? 혹시 여기에 있는 걸 알아차린건가? 어떡하지??』"
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "….."
    hide hajun_serious

    show hajun at left_bottom_offset
    hajun "여기까지가 끝이다."
    hajun "피해자도 좋은 사람은 아니었지만, 결코 죽을 이유는 없어."
    hajun "대체 여기서 말하는 그 사람들은 누구일까? 그리고 마약이 있던 곳은 어디고?"
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "어떤 사람들과 엮인 거야..?"
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_room


label villa_room_교리서적:
    show hajun at left_bottom_offset
    hajun "이건…잠시만…"
    hide hajun

    show hajun_surprised at left_bottom_offset
    hajun "분명… 얼마 전 그 주택에서도 있었는데…!"
    hide hajun_surprised

    show hajun_serious at left_bottom_offset
    hajun "그럼… 이 사건의 피해자는 그 사건과 연관이 있는 거야…?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "그리고…. 대체 이 책이 어떻게 아직까지 있는 건데?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "무슨 일이… 무슨 일이 벌어지고 있는 거야…"
    hide hajun_serious

    $ is_object_locked = False
    jump chapter2_5_explore_villa_room

