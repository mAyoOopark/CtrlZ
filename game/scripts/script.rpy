
#배경
image chapter1_1 = "chapter1_1.png"
image chapter1_2 = "chapter1_2.png"
image chapter1_3 = "chapter1_3.png"
image chapter1_4 = "chapter1_4.png"
image chapter1_4_1 = "chapter1_4_1.png"
image chapter1_4_1_2 = "chapter1_4_1_2.png"
image chapter1_4_2 = "chapter1_4_2.png"
image chapter1_4_2_A = "chapter1_4_2_A.png"
image chapter1_4_3 = "chapter1_4_3.png"
image chapter1_4_3_1 = "chapter1_4_3_1.png"
image chapter1_5 = "chapter1_5.png"
image chapter1_5_1 = "chapter1_5_1.png"
image chapter1_5_2 = "chapter1_5_2.png"
image chapter1_5_3 = "chapter1_5_3.png"

#이미지
image hajun = "hajun.png"
image hajun_angry = "hajun_angry.png"
image hajun_surprised = "hajun_surprised.png"
image hajun_consider = "hajun_consider.png"
image hajun_despair = "hajun_despair.png"
image hajun_puzzled = "hajun_puzzled.png"
image hajun_sad = "hajun_sad.png"
image hajun_determind = "hajun_determind.png"
image hajun_smile = "hajun_smile.png"
image hajun_cough = "hajun_cough.png"

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

default visited_chapel = False
default visited_dining = False
default visited_bathroom = False
default checked_tools = False
default checked_menu = False
default checked_table = False
default visited_chapter1_5_2 = False
default visited_chapter1_5_3 = False
default visited_chapter1_5_4 = False
default visited_chapter1_5_5 = False


label start:
    scene chapter1_1 with fade # 기본 제공 배경 or "bg_restaurant.jpg"로 교체
    show screen life_display

    "20xx년  xx월 xx일 늦은 밤. 나와 남종식 선배는 한 사이비 종교단체의 불법적인 행각이 벌어지고 있다는 신고를 받고 xx에 위치한 xx로 출동했다."
    "그 날은 비가 많이 오고 있던 아침이였다."
    
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

            if knock_count >= 5:
                jump bad_end1
            else:
                jump break_door_choice

        "문을 부순다":
            jump chapter1_3

label bad_end1:
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
    
    "증거를 가지고 다시 찾아갔을 땐 모든 것이 불에 타고 있었다."
    "모든 증거가 사라지고, 최도현 또한 사라지고 없었다."
    
    with Pause(2.0)
    
    "선택지로 다시 되돌아갑니다."
    
    jump knock_door_event
    
    return

label chapter1_3:
    show chapter1_2 at shake
    scene chapter1_3 with fade

    show dohyeon_asd at right_bottom_offset
    asd "어서오세요 자매님들 잘 찾아오셨습니다."
    hide dohyeon_asd

    "박하준과 남종식은 검은색 망토를 뒤집어 쓴 남자를 보고있다."
    
    show dohyeon_asd at right_bottom_offset
    asd "자매님들 조금만 더 밖에서 기다려 주시겠어요?"
    hide dohyeon_asd
    
    "???는 자리를 도망치듯 빠르게 말하며 달려갔다."
    
    show jungsik_consider at right_bottom_offset
    jungsik "야 하준아 저 사람 뭔가 이상하지 않냐?"
    hide jungsik_consider
    
    show hajun_puzzled at left_bottom_offset
    hajun "선배도 그렇게 생각하시죠?"
    hide hajun_puzzled

    show jungsik_puzzled at right_bottom_offset
    jungsik "자리에서 벗어날려고 하는 느낌이 들었는데?"
    hide jungsik_puzzled

    show hajun_determind at left_bottom_offset
    hajun "선배 그러면 한번 쫓아가 볼까요?"
    hide hajun_determind

    show jungsik at right_bottom_offset
    jungsik "하준아 우리 둘이 같이 가는 것 보단 찢어져서 한번 찾아보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "예 선배님. 제가 1층을 살펴보고 오겠습니다!"
    hajun "선배님이 2층을 살펴주세요!"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래 찾으면 바로 무전하는걸로 하자"
    hide jungsik

    show hajun at left_bottom_offset
    hajun "넵!"
    hide hajun

    jump chapter1_4

label chapter1_4:
    scene chapter1_4 with fade

    show hajun_consider at left_bottom_offset
    hajun "숨겨진 방? 여긴 뭐가 있는거지?"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "어디서부터 확인해볼까?"
    hide hajun

    "예배실과 식당, 화장실을 살펴보고 숨겨진 방으로 다시 와야한다."

    jump location_select

# ✅ 장소 선택 메뉴
label location_select:

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
    
    show hajun at left_bottom_offset
    hajun "여긴 신도들이 예배를 드리는 곳인가... 안으로 더 들어가볼까?"
    hide hajun

    scene chapter1_4_1 with fade

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
            " '빨리 돈을 다 챙겨!' 라는 키워드를 발견했다."

            show hajun_consider at left_bottom_offset
            hajun "돈을 다 챙기라는건 무슨 의미일까?"
            hide hajun_consider

            show hajun at left_bottom_offset
            hajun "다시 돌아가자"
            hide hajun

            scene chapter1_4 with fade

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

    " 식당으로 들어가니 각종 조리도구가 많이 걸려있다. "

    show hajun at left_bottom_offset
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
            scene chapter1_4_2_A
            show chapter1_4_2_A at shake
           
            " 메뉴판에 문구가 생성되었다."

            jump chapter1_4_2_2
        "식탁":
            $ checked_table = True
            "음식을 가지고 와서 앉아서 먹는 곳이다."
            jump chapter1_4_2_check
label chapter1_4_2_2:
    show hajun_surprised at left_bottom_offset
    hajun "??시??분 까지 가야한다고?"
    hajun "어디를 간다는거지?"
    hide hajun_surprised

    jump chapter1_4_2_check

label chapter1_4_2_check:
        if checked_tools and checked_menu and checked_table:
            "여기서 더 할일은 없을 것 같아."
            scene chapter1_4 with fade
            jump location_select
        else:
            jump chapter1_4_2_1

label chapter1_4_3:
    $ visited_bathroom = True
    scene chapter1_4_3 with fade

    show hajun at left_bottom_offset
    hajun "화장실이군... 남자 화장실과 여자 화장실이 있어. 한번 살펴보자."
    hide hajun

    jump location_select

# ✅ 숨겨진 방: 조건 미달 시
label room_secret_locked:

    show hajun at left_bottom_offset
    hajun "이상한 문이 하나 있다... 다른 곳을 다 살펴보고 와야겠다."
    hide hajun

    jump location_select

# ✅ 숨겨진 방: 조건 만족 시
label chapter1_4_4:
    
    "3곳을 전부 확인했다."

    show hajun_consider at left_bottom_offset
    hajun "3곳에서 얻은건 어디로 몇시까지 돈을 가지고 간다는건데..."
    hide hajun_consider

    show hajun_surprised at left_bottom_offset
    hajun "설마 최도현은 몇시까지 어디로 돈을 가지고 도망을 가려고 생각하는건가?"
    hide hajun_surprised

    menu:
        "내려가자":
            show hajun_determind at left_bottom_offset
            hajun "빠르게 숨겨진 문으로 내려가보자."
            hide hajun_determind

            show hajun at left_bottom_offset
            hajun "선배님 1층 조사하는 중에 최도현의 행동이 너무 수상해서 지하실로 가보겠습니다."
            hide hajun

            show jungsik at right_bottom_offset
            jungsik "야 그래도 혼자는 위험해 같이가자."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "알겠어요 그럼 조심히 찾아볼게요"
            hide hajun

            show jungsik_angry at right_bottom_offset
            jungsik "야 그래도 혼자는 위험해 같이가자"
            hide jungsik

            jump chapter1_5
        "아직 좀 더 찾아보자":
            jump location_select
label chapter1_5:
    scene chapter1_5 with fade
    
    show hajun_surprised at left_bottom_offset
    hajun "와.. 이 건물 밑에 이런 곳이 숨겨져있다니.."
    hide hajun_surprised

    show hajun_consider at left_bottom_offset
    hajun "대체.. 이런 곳에서 무슨 일이 있었던거야?"
    hajun "방도 여러 개 있네."
    hajun "그럼 하나씩 조사해보자"
    hide hajun_consider

    show hajun_smile at left_bottom_offset
    hajun "종식 선배가 조심하라 했지만, 뭔 일 나겠어?"
    hide hajun_smile
    
    jump chapter1_5_1

label chapter1_5_1:
    scene chapter1_5_1 with fade
    with Pause(1.0)
    "총 방이 4개가 있다."
    "각 방 안에는 열쇠 조각과 본드가 들어있다."
    "각각의 방을 둘러보고 아이템을 획득하게 되면 보일러실 열쇠가 완성된다."
    "열쇠를 완성한 후 보일러실에 진입할 수 있다."

    jump chapter1_5_1location

label chapter1_5_1location:
        menu:
            "서재":
                jump chapter1_5_2
            "창고":
                jump chapter1_5_3


label chapter1_5_2:
    $ visited_chapter1_5_2 = True
    scene chapter1_5_2 with fade

    show hajun at left_bottom_offset
    hajun "이 방은.. 서재인가?"
    hajun "많은 책들이 있어. 전부 교리 서적이군."
    hide hajun

    show hajun_cough at left_bottom_offset
    hajun "콜록콜록.."
    hajun "먼지가 잔뜩 쌓였구만.."
    hide hajun_cough

    show hajun at left_bottom_offset
    hajun "여기에도 최도현은 보이지 않아"
    hide hajun
    menu:
        "책에 튀어나온 것을 살펴본다.":
            show hajun at left_bottom_offset
            hajun "이건 뭐지..? 무슨 조각 같은데?"
            hajun "일단 가지고 있자."
            hide hajun
            
            scene chapter1_5_1 with fade
            jump chapter1_5_1location

label chapter1_5_3:
    $ visited_chapter1_5_3 = True
    scene chapter1_5_3 with fade

    show hajun at left_bottom_offset
    hajun "여기는.. 창고인 것 같네"
    hajun "여러 기구들이 있어."
    hide hajun

    show hajun_consider at left_bottom_offset
    hajun "뼈톱? 인두기?"
    hajun "이런것 들이 여기에 왜 있는거지..?"
    hide hajun_consider
    
    show hajun at left_bottom_offset
    hajun "대체 여기서 무슨 일이 벌어졌던거야?"
    hajun "바닥에 왜 본드가 떨어져있지?"
    hide hajun

    menu:
        "바닥에 떨어진 본드를 살펴본다.":
            show hajun at left_bottom_offset
            hajun "본드...."
            hajun "뭔가 맞출 수 있을 것 같아"
            hajun "일단 가져가자"
            hide hajun

            scene chapter1_5_1 with fade
            jump chapter1_5_1location

    return
