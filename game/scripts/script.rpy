#배경
image chapter1_1 = "chapter1_1.png"
image chapter1_2 = "chapter1_2.png"
image chapter1_3 = "chapter1_3.png"
image chapter1_4 = "chapter1_4.png"
image chapter1_4_1 = "chapter1_4_1.png"
image chapter1_4_1_2 = "chapter1_4_1_2.png"
image chapter1_4_2 = "chapter1_4_2.png"
image chapter1_4_3 = "chapter1_4_3.png"
image chapter1_4_3_1 = "chapter1_4_3_1.png"

#이미지
image hajun = "hajun.png"
image hajun_angry = "hajun_angry.png"
image hajun_surprised = "hajun_surprised.png"
image hajun_consider = "hajun_consider.png"
image hajun_despair = "hajun_despair.png"
image hajun_puzzled = "hajun_puzzled"
image hajun_sad = "hajun_sad.png"
image hajun_determind = "hajun_determind.png"

image jungsik = "jungsik.png"
image jungsik_angry = "jungsik_angry.png"
image jungsik_consider = "jungsik_consider.png"
image jungsik_despair = "jungsik_daspair.png"
image jungsik_puzzled = "jungsik_puzzled.png"
image jungsik_surprised = "jungsik_surprised.png"
image jungsik_sad = "jungsik_sad.png"

image dohyeon_asd = "dohyeon_asd.png"

#캐릭터
define hajun = Character("박하준")
define jungsik = Character("남중식")
define dohyeon = Character("최도현")
define asd = Character("???")

screen life_display():    #라이프
    frame:
        xalign 0.9
        yalign 0.05
        padding (10, 10, 10, 10)
        background "#0008"

        python:
            hearts = "❤️" * (3 - wrong_count) + "🤍" * wrong_count

        text hearts size 30
default wrong_count = 0
default life = 3
  
transform left_bottom_offset: # 캐릭터를 왼쪽 아래에 위치
    xpos 100
    ypos 1.0
    xanchor 0.0
    yanchor 1.0

transform right_bottom_offset:     # 캐릭터를 오른쪽 아래에 위치
    xpos 1820
    ypos 1.0
    xanchor 1.0
    yanchor 1.0

transform shake:         # 화면 흔들림 효과
    linear 0.05 xoffset -20 yoffset -15
    linear 0.05 xoffset 20 yoffset 15
    linear 0.05 xoffset -15 yoffset 20
    linear 0.05 xoffset 15 yoffset -20
    linear 0.05 xoffset 0 yoffset 0

transform sparkle: #반짝임 효과
    linear 0.5 alpha 0.5
    linear 0.5 alpha 1.0
    repeat

screen toilet_message:
    imagebutton:
        idle "obj_sparkle_ch1_01.png"         # 클릭 가능한 이미지
        xpos 1200 ypos 300
        at sparkle
        focus_mask True
        action [Jump("checked_message")]
        sensitive toilet_button_enabled

label checked_message:
    $ checked_message = True
    "거울 옆에 물에 젖은 쪽지를 발견했다. / 쪽지에는 #$@!#!$로 도망가야해...라고 적혀있었다. "
    jump chapter1_4_3

default visited_chapel = False
default visited_dining = False
default visited_bathroom = False
default checked_tools = False
default checked_menu = False
default checked_table = False
default toilet_button_enabled = False
default checked_message = False

label start:
    scene chapter1_1 with fade # 기본 제공 배경 or "bg_restaurant.jpg"로 교체
    show screen life_display

    "20xx년  xx월 xx일 늦은 밤. 나와 남종식 선배는 한 사이비 종교단체의 불법적인 행각이 벌어지고 있다는 신고를 받고 xx에 위치한 xx로 출동했다."
    "그날은 유난히 어두운 밤임에도 구름때문에 달빛하나 비추지 않아 더욱더 어두웠으며 인적이 드문 곳에 위치한 건물이기에 스산한 분위기가 맴돌았다."
    show jungsik at right_bottom_offset
    jungsik "그러니까, 여기라는 거지?"
    hide jungsik

    show hajun at left_bottom_offset
    hajun "예, 여기가 확실해요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "생각보다 멀쩡한 건물이네, 들리는 소문에 비해서는."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "그러게요, 하지만 내부상황도 멀쩡했으면 저희는 여기 오지 않았겠죠."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그렇지. 그럼 들어가보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "예, 제가 한번 문을 두드려 볼게요."
    hide hajun
    jump knock_door_event

label knock_door_event:
    $ knock_count = 0
    scene chapter1_2 with fade
    "하준과 중식은 건물의 문 앞으로 이동했다."
    label knock_loop:

        menu:
            "문을 두드린다":
                $ knock_count += 1
                "당신은 문을 두드렸다... (현재 [knock_count]회)"

                if knock_count >= 3:
                    jump break_door_choice
                else:
                    jump knock_loop

label break_door_choice:
    "당신은 문 앞에서 고민한다."
    "문을 여러번 두드릴 시, 최도현이 도망갈 수 있다."

    menu:
        "문을 계속 두드릴까, 부술까?"

        "문을 계속 두드린다":
            $ knock_count += 1
            "당신은 또 다시 문을 두드렸다... (현재 [knock_count]회)"

            if knock_count >= 10:
                jump bad_end1
            else:
                jump break_door_choice

        "문을 부순다":
            jump chapter1_3

label bad_end1:
    scene chapter1_3 with fade
    show hajun_puzzled at left_bottom_offset
    hajun "아무도 없는 거 같은데요?"
    hide hajun_puzzled

    show jungsik_puzzled at right_bottom_offset
    jungsik "뭐야 너가 여기 맞다면서"
    hide jungsik_puzzled

    show hajun_consider at left_bottom_offset
    hajun "분명 맞는데...."
    hajun "돌아가서 다시 한번 알아보죠."
    hide hajun_consider

    show jungsik_sad at right_bottom_offset
    jungsik "에이씨 이게뭐야"
    jungsik "너때문에 헛발짚었네"
    
    scene black with fade
    
    "박하준과 남중식이 간 곳은 최도현의 아지트가 맞았다."
    "하지만 그들이 노크를 하는 동안, 최도현은 자취를 감췄다."
    
    with Pause(2.0)
    
    "선택지로 다시 되돌아갑니다."
    
    jump knock_door_event
    
    return

label chapter1_3:
    show dohyeon_asd at right_bottom_offset
    asd "어서오세요 자매님들 잘 찾아오셨습니다."
    hide dohyeon_asd

    "최도현은 박하준과 남중식을 한번씩 쳐다보며 급하게 말하였다."
    
    show dohyeon_asd at right_bottom_offset
    asd "자매님들 조금만 더 밖에서 기다려 주시겠어요?"
    hide dohyeon_asd
    
    "최도현은 그 자리를 도망치듯 빠르게 문을 닫고 뒤도 안돌아보고 도망쳤다."
    
    show jungsik_angry at right_bottom_offset
    jungsik "저 개자식이 어딜 도망가려고!!!"
    hide jungsik_angry
    
    "남중식은 문을 열어보려 하지만 열리지 않았다."
    "그 사이 교주로 추정되는 인물의 발걸음 소리는 더욱 멀어지고 있었다."
    
    show hajun_determind at left_bottom_offset
    hajun "선배 나와봐요!!"
    hide hajun_determind
    show chapter1_2 at shake

    with Pause(1.0)
    
    "문이 부숴지며 교회 안으로 진입했다."
    
    scene chapter1_3 with fade

    show jungsik at right_bottom_offset
    jungsik "하준아 우리 둘이 같이 가는 것 보단 찢어져서 최도현을 찾아보자"
    hide jungsik
    
    show hajun at left_bottom_offset
    hajun "예 선배님."
    hajun "그럼 제가 1층을 찾아보겠습니다."
    hajun "선배님이 2층을 찾아봐주세요!"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래 찾으면 바로 무전 하는걸로 하자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "알겠습니다 선배님!"

    jump chapter1_4

label chapter1_4:
    scene chapter1_4 with fade

    show hajun at left_bottom_offset
    hajun "어디서부터 확인해볼까?"
    hide hajun

    jump location_select

# ✅ 장소 선택 메뉴
label location_select:
    scene chapter1_4 with fade
    if checked_tools and checked_menu and checked_table:
        "식당에서 중요한 단어를 얻었다"
    if checked_message :
        show hajun_puzzled at left_bottom_offset
        hajun "쪽지... 앞에는 젖어 있어서 읽을 수 없었다. 도망가야한다는건 무슨 소리지...?"
        hide hajun_puzzled
    if visited_bathroom and visited_chapel and visited_dining :
        "3곳을 모두 확인했다."
        show hajun_puzzled at left_bottom_offset
        # hajun "도망... 돈을 다 챙겨.... ??시 까지..."
        hajun "3곳에서 얻은건 어디로 ??시까지 돈을 가지고 간다는건데..."
        hide hajun_puzzled
        show hajun_despair at left_bottom_offset
        hajun "설마 최도현은 ??시까지 어디로 돈을 가지고 도망을 갈려고 생각하는건가?!"
        menu :
            "내려가자":
                jump chapter1_5

            "아직 좀 더 찾아보자": 
                jump chapter1_4
            
    menu:
        "어디로 이동할까?"

        "예배실":
            jump chapter1_4_1

        "식당":
            jump chapter1_4_2

        "화장실":
            jump chapter1_4_3

        "숨겨진 방":
            if visited_chapel and visited_dining and visited_bathroom:
                jump chapter1_4_4
            else:
                jump room_secret_locked

# ✅ 각 장소별 라벨

label chapter1_4_1:
    $ visited_chapel = True
    scene chapter1_4_1 with fade

    show hajun at left_bottom_offset
    hajun "여긴 신도들이 예배를 드리는 곳인가... 안으로 더 들어가볼까?"
    hide hajun

    "예배실 안으로 들어가니 앞에는 예수님 동상이 있고,많은 의자들이 있었다."

    show hajun_surprised at left_bottom_offset
    hajun "최도현 이 새끼 왜 이렇게 잘 꾸며둔거야 진짜 교회인거 같잖아"
    hide hajun_surprised

    show hajun_consider at left_bottom_offset
    hajun "어디를 먼저 가볼까?"
    hide hajun_consider
    jump chapter1_4_1_1

label chapter1_4_1_1:
    menu:
        "예수님 동상":
            "예수님 팔에 이상한 문양이 새겨져있다. 그 외에는 중요한 건 없는 것 같다."
            jump chapter1_4_1_1
        "의자":
            "각각 의자마다 뒤에 번호가 새겨져있다. 어디에 쓰일려나?"
            jump chapter1_4_1_1
        "예수님 동상 뒤의 문":
            jump chapter1_4_1_2

label chapter1_4_1_2:
    scene chapter1_4_1_2 with fade
    "2가지의 문이 나왔다."
    jump chapter1_4_1_2_1

label chapter1_4_1_2_1:
    menu:
        "왼쪽 문":
            " '보일러실' 이라는 키워드를 얻었다."
            show hajun at left_bottom_offset
            hajun "다시 돌아가자"
            hide hajun

            jump location_select
        "오른쪽 문":
             $ wrong_count += 1
             show chapter1_4_1_2 at shake
             "잘못된 선택으로 라이프가 1 감소했다."
             with Pause(1.0)
             jump chapter1_4_1_2_1


label chapter1_4_2:
    $ visited_dining = True
    scene chapter1_4_2 with fade

    show hajun at left_bottom_offset
    " 식당으로 들어가니 각종 조리도구가 많이 걸려있다. "
    hajun "조리하시는 영양사분이 계신걸까 조리도구가 엄청 많네"
    hajun "조리도구중에 엄청 날카로운 칼도 있으니 조심해야겠어."
    hide hajun

    jump chapter1_4_2_1

label chapter1_4_2_1:
    menu :
        "조리도구":
            $ checked_tools = True
            $ wrong_count += 1
            show chapter1_4_2 at shake
            "날카로운 칼에 긁혀서 상처가 생겼다."
            "잘못된 선택으로 라이프가 1 감소했다."
            with Pause(1.0)
            jump chapter1_4_2_check
        "메뉴판":
            $ checked_menu = True
            "'??시까지 가야해...' 라는 문구가 써있다"
            jump chapter1_4_2_2
        "식탁":
            $ checked_table = True
            "음식을 가지고 와서 앉아서 먹는 곳이다."
            jump chapter1_4_2_check

label chapter1_4_2_2:
    show hajun_surprised at left_bottom_offset
    hajun "??시까지 가야한다고? 어디를 간다는 거지?"
    hide hajun_surprised

    jump chapter1_4_2_checkㄲ

label chapter1_4_2_check:
        if checked_menu and checked_table:
            "식당에서는 더 이상 할게 없는 것 같다"
            jump location_select
        else:
            jump chapter1_4_2_1


label chapter1_4_3:
    $ visited_bathroom = True
    scene chapter1_4_3 with fade
    if checked_message :
        
        show hajun at left_bottom_offset
        hajun "화장실에서는 더 이상 할 수 있는게 없는 거 같다. 돌아가자."
        jump location_select
    show screen toilet_message

    show hajun_consider at left_bottom_offset
    hajun "여자 화장실과 남자 화장실이 있는데 어디를 먼저 가볼까?"
    "여자화장실은 문이 잠겨 있다."
    "큰 거울과 칸 마다 변기들이 있다."
    hide hajun_consider
    $ toilet_button_enabled = True

    if checked_message == False :
        "여기서 무언가를 더 찾아야해"
        jump chapter1_4_3

# ✅ 숨겨진 방: 조건 미달 시
label room_secret_locked:

    show hajun at left_bottom_offset
    hajun "이상한 문이 하나 있다... 다른 곳을 다 살펴보고 와야겠다."
    hide hajun

    jump location_select

# ✅ 숨겨진 방: 조건 만족 시
label chapter1_4_4:
    scene chapter1_4_4 with fade

    show hajun at left_bottom_offset
    hajun "이 문은 뭔가 수상해... 이제야 열 수 있게 된 것 같군."
    hide hajun

    return
