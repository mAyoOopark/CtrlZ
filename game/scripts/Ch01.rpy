default visited_chapel = False
default visited_dining = False
default checked_tools = False
default checked_menu = False
default checked_table = False
default visited_chapter1_5_2 = False
default visited_chapter1_5_3 = False
default visited_chapter1_5_4 = False
default visited_chapter1_5_5 = False

default qte_answers = ["dodge", "dodge", "punch", "dodge", "punch"]
default current_qte = 0
default success = 0
default asdf = 0

default checked_message = False

label start:
    show screen life_display onlayer screens zorder 100
    scene chapter1_1bg with fade
    show expression Solid("#0000004D") as dark_overlay
    
    play amb "amb_rain.mp3" volume 0.5 fadein 1.0 loop
    play music "bgm_ch1.mp3" volume 0.7
    pro "20xx년  xx월 xx일 늦은 밤."
    pro "나와 남종식 선배는 한 사이비 종교단체의 불법 행각 신고에\n xx에 위치한 xx로 출동했다."
    pro "그 날은 유독 비가 많이 오는 아침이었다."
    hide window with None
    hide dark_overlay
    scene black
    
    slow_c "{cps=20}이 게임은 픽션입니다. 여기에서 등장하는 소재는\n 실존하는 모든 지명, 인물, 사건, 단체, 기관과는 무관합니다."

    scene chapter1_1bg with fade
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
                play sound "sfx_ch1_knock_door.ogg"
                "당신은 문을 두드렸다... (현재 [knock_count]회)"

                if knock_count >= 3:
                    jump break_door_choice
                else:
                    jump knock_loop

label break_door_choice:
    "당신은 문 앞에서 고민한다."
    "문을 여러번 두드릴 시, 최도현이 틈을 타 도망갈 수도 있지 않을까?"

    menu: 
        "문을 계속 두드릴까, 부술까?"

        "문을 계속 두드린다":
            play sound "sfx_ch1_knock_door.ogg"
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
    hajun "분명 맞는데... 제보의 위치와 일치하는데..."
    hajun "……이상하네요. 돌아가서 다시 확인해보죠."
    hide hajun_consider

    show jungsik_sad at right_bottom_offset
    jungsik "하... 이게 뭐냐 진짜."
    jungsik "너 때문에 완전히 헛탕쳤네."
    hide jungsik_sad
    
    stop music fadeout 1.0
    stop amb fadeout 1.0
    scene black with fade
    pause(1.0)

    play sound "sfx_ch1_wind.mp3"
    "며칠 뒤, 다시 그 장소를 찾았을 땐—"
    "남아 있던 건 까맣게 타버린 잔해뿐이었다."

    pause(1.0)

    play amb "sfx_ch1_fire_crackle.mp3" volume 0.7
    "그 안에 있던 모든 증거, 그리고 최도현까지..."
    "그 흔적마저 연기처럼 사라져 있었다."

    scene black with fade
    pause(1.5)

    play sound "sfx_gameover.mp3"
    pro "\n{size=40}Bad End : 시작조차 못한 수사.{/size}"
    stop amb fadeout 2.0
    stop sound fadeout 2.0
    
    with Pause(2.0)
    
    "선택지로 다시 되돌아갑니다."

    play amb "amb_rain.mp3" volume 0.8 fadein 0.8 loop
    play music "bgm_ch1.mp3" volume 0.7
    jump knock_door_event
    
    return

label chapter1_3:
    show chapter1_2bg at shake
    play sound "sfx_ch1_break_door.mp3"
    play amb "amb_church.mp3" volume 0.8 fadein 0.8 loop
    scene chapter1_3bg with fade

    show dohyeon_asd at right_bottom_offset
    asd "어서오세요 자매님들 잘 찾아오셨습니다."
    hide dohyeon_asd

    "박하준과 남종식은 검은색 망토를 뒤집어 쓴 남자를 보고있다."
    
    show dohyeon_asd at right_bottom_offset
    asd "자매님들 조금만 더 밖에서 기다려 주시겠어요?"
    hide dohyeon_asd
    
    play sound "sfx_ch1_runaway.mp3" volume 5.0
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
    play sound "sfx_run_man.mp3"
    jump chapter1_4

label chapter1_4:
    scene chapter1_4bg with fade

    show hajun_consider at left_bottom_offset
    hajun "숨겨진 방? 여긴 뭐가 있는거지?"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "어디서부터 확인해볼까?"
    hide hajun

    "예배실과 식당을 살펴보고 숨겨진 방으로 다시 와야한다."

    jump location_select

define check_mg_restaurant = False

# ✅ 장소 선택 메뉴
label location_select:
    scene chapter1_4 with fade
    if checked_tools and checked_menu and checked_table and not check_mg_restaurant:
        "식당에서 중요한 단어를 얻었다"
        $check_mg_restaurant = True
            
    menu:
        "어디로 이동할까?"

        "예배실":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            jump chapter1_4_1

        "식당":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            play sound2 "sfx_ch1_man_walk.mp3"
            jump chapter1_4_2

        "숨겨진 방":
            if visited_chapel and visited_dining:
                jump chapter1_4_4
            else:
                jump room_secret_locked

# ✅ 각 장소별 라벨

label chapter1_4_1:
    $ visited_chapel = True
    
    show hajun at left_bottom_offset
    hajun "여긴 신도들이 예배를 드리는 곳인가... 안으로 더 들어가볼까?"
    hide hajun
    play sound "sfx_ch1_man_walk.mp3"

    scene chapter1_4_1bg with fade

    "예배실 안으로 들어가니 앞에는 예수님 동상이 있고"
    extend "\n많은 의자들이 있었다."

    show hajun_surprised at left_bottom_offset
    hajun "최도현 이 새끼 왜 이렇게 잘 꾸며둔거야.. 진짜 교회인거 같잖아.."
    hide hajun_surprised

    show hajun_consider at left_bottom_offset
    hajun "어디를 먼저 조사해볼까?"
    hide hajun_consider
    jump chapter1_4_1_1

label chapter1_4_1_1:
    menu:
        "예수님 동상":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            "예수님 팔에 이상한 문양이 새겨져있다. 그 외에는 중요한 건 없는 것 같다."
            jump chapter1_4_1_1
        "의자":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            "각각 의자마다 뒤에 번호가 새겨져있다. 어디에 쓰이려나?"
            jump chapter1_4_1_1
        "예수님 동상 뒤의 문":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            "동상 뒤를 자세히 살펴보니 작은 문이 있는 것 같다."
            "한 번 가보자."
            play sound "sfx_ch1_man_walk.mp3"
            jump chapter1_4_1_2

label chapter1_4_1_2:
    $ right_door_check = 0
    scene chapter1_4_1_2bg with fade
    "2가지의 문이 나왔다."
    jump chapter1_4_1_2_1

label chapter1_4_1_2_1:
    
    menu:
        "왼쪽 문":
            play sound "sfx_ch1_open_door.mp3"
            pause(0.2)
            "안쪽으로 희미한 불빛이 비춰온다."
            "들어가볼까?"
            menu:
                "들어가본다":
                    play sound "sfx_ch2_investigation.mp3" volume 0.5
                    play sound2 "sfx_ch1_man_walk.mp3"
                    jump chapter1_4_1_2_1_leftdoor
        "오른쪽 문":
            call check_fail from _call_check_fail
            play sound "sfx_ch1_open_door.mp3"
            pause(0.2)
            if right_door_check >= 1:
                show hajun at left_bottom_offset
                hajun "이곳은 이미 확인했다. 왼쪽 문을 확인해보자."
                hide hajun
                
                jump chapter1_4_1_2_1
            $ wrong_count += 1
            show chapter1_4_1_2 at shake
            play sound "sfx_life_minus.mp3"
            play voice "sfx_punch.mp3"
            "잘못된 선택으로 라이프가 1 감소했다."
            $ right_door_check += 1
            $ life += 3
            call check_fail from _call_check_fail_1
            jump chapter1_4_1_2_1

label chapter1_4_1_2_1_leftdoor:
    scene chapter1_4_1_leftdoorbg with fade
    show hajun_frown at left_bottom_offset
    hajun "여긴 왜 이렇게 으스스하지 뭔가 튀어 나올 거 같은 느낌인데...?"
    hajun "벽에 먼지가 너무 많은걸? 좀 털어 볼까?"
    hide hajun_frown
    menu: 
        "벽의 먼지를 턴다.":
            play sound "sfx_ch1_sweep_dust.mp3"
            pause(1.5)
            jump chapter1_4_1_2_1_keyword

label chapter1_4_1_2_1_keyword:
    scene chapter1_4_1_leftdoor_keywordbg at shake
    play sound2 "sfx_shake.mp3"
    show hajun_surprised at left_bottom_offset
    hajun " 저...저게 뭐야....!!"
    hide hajun_surprised
    "벽에는 피로 묻은 글씨가 적혀 있다."
    "{i}왜 우리만 빼 놓고...  {color=#803232}{size=40}빨리 돈을 다 챙겨!!{/size}{/color} 라고 말씀 하시는거지...{/i}"
    show hajun_surprised at left_bottom_offset
    hajun "{i}{color=#803232}{size=40}빨리 돈을 다 챙기라고...?{/i}{/size}{/color}   저게 무슨 의미지..."
    hide hajun_surprised
    pause (1.0)
    "박하준은 생각에 잠기며 방을 나왔다."
    play sound "sfx_ch1_close_door.mp3"
    play sound2 "sfx_ch1_man_walk.mp3"
    jump location_select

label chapter1_4_2:
    $ visited_dining = True
    scene chapter1_4_2bg with fade

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
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            play audio "sfx_punch.mp3"
            play sound2 "sfx_life_minus.mp3"
            show chapter1_4_2bg at shake
            "날카로운 칼에 긁혀서 상처가 생겼다."
            "잘못된 선택으로 라이프가 1 감소했다."
            with Pause(1.0)
            jump chapter1_4_2_check
        "메뉴판":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            $ checked_menu = True
            scene chapter1_4_2_Abg
            play sound "sfx_shake.mp3" volume 0.8
            show chapter1_4_2_Abg at shake
           
            " 메뉴판에 문구가 생성되었다."

            "'??시까지 가야해...' 라는 문구가 써있다"
            jump chapter1_4_2_2
        "식탁":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
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
        if checked_menu and checked_table:
            "식당에서는 더 이상 할게 없는 것 같다"
            play sound2 "sfx_ch1_man_walk.mp3"
            jump location_select
        else:
            jump chapter1_4_2_1

# ✅ 숨겨진 방: 조건 미달 시
label room_secret_locked:

    show hajun at left_bottom_offset
    hajun "이상한 문이 하나 있다... 다른 곳을 다 살펴보고 와야겠다."
    hide hajun

    jump location_select

# ✅ 숨겨진 방: 조건 만족 시
label chapter1_4_4:
    
    "2곳을 전부 확인했다."

    show hajun_consider at left_bottom_offset
    hajun "2곳에서 얻은건 어디로 몇시까지 돈을 가지고 간다는건데..."
    hide hajun_consider

    show hajun_surprised at left_bottom_offset
    hajun "설마 최도현은 몇시까지 어디로 돈을 가지고 도망을 가려고 생각하는건가?"
    hide hajun_surprised

    menu:
        "내려가자" :
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            play sound2 "sfx_ch1_man_walk.mp3"
            show hajun_determind at left_bottom_offset
            hajun "빠르게 숨겨진 문으로 내려가보자."
            hide hajun_determind

            show hajun at left_bottom_offset
            hajun "선배님 1층 조사하는 중에 최도현의 행동이 너무 수상해서\n지하실로 가보겠습니다."
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
    scene chapter1_5bg with fade
    
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
    stop music fadeout 2.0
    jump chapter1_5_1

label chapter1_5_1:
    scene chapter1_5_1bg with fade
    play music "bgm_ch1_trace.mp3" fadein 2.0 
    with Pause(1.0)
    "총 방이 4개가 있다."
    "각 방 안에는 열쇠 조각과 본드가 들어있다."
    "각각의 방을 둘러보고 아이템을 획득하게 되면 보일러실 열쇠가 완성된다."
    "열쇠를 완성한 후 보일러실에 진입할 수 있다."

    jump chapter1_5_1location

label chapter1_5_1location:
        menu:
            "서재":
                play sound "sfx_ch2_investigation.mp3" volume 0.5
                play sound2 "sfx_ch1_man_walk.mp3"
                jump chapter1_5_2
            "창고":
                play sound "sfx_ch2_investigation.mp3" volume 0.5
                play sound2 "sfx_ch1_man_walk.mp3"
                jump chapter1_5_3
            "고문실":
                play sound "sfx_ch2_investigation.mp3" volume 0.5
                play sound2 "sfx_ch1_man_walk.mp3"
                jump chapter1_5_4
            "감옥":
                play sound "sfx_ch2_investigation.mp3" volume 0.5
                play sound2 "sfx_ch1_man_walk.mp3"
                jump chapter1_5_5

label chapter1_5_1_check :
    if visited_chapter1_5_2 and visited_chapter1_5_3 and visited_chapter1_5_4 and visited_chapter1_5_5:
        jump chapter1_5_6
    else :
        jump chapter1_5_1location


label chapter1_5_2:
    $ visited_chapter1_5_2 = True
    scene chapter1_5_2bg with fade

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
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "이건 뭐지..? 무슨 조각 같은데?"
            play sound2 "sfx_item.mp3"
            hajun "일단 가지고 있자."
            hide hajun

            play sound2 "sfx_ch1_man_walk.mp3"
            scene chapter1_5_1 with fade
            jump chapter1_5_1_check

label chapter1_5_3:
    $ visited_chapter1_5_3 = True
    scene chapter1_5_3bg with fade

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
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "본드...."
            hajun "뭔가 맞출 수 있을 것 같아"
            play sound2 "sfx_item.mp3"
            hajun "일단 가져가자"
            hide hajun
            play sound2 "sfx_ch1_man_walk.mp3"
            scene chapter1_5_1 with fade
            jump chapter1_5_1_check

label chapter1_5_4:
    scene chapter1_5_4bg with fade
    $ visited_chapter1_5_4 = True
    show hajun_cough at left_bottom_offset
    hajun "윽.."
    hajun "이상한 냄새가 진동을 하네... 피비린내?"
    hide hajun_cough

    show hajun_surprised at left_bottom_offset
    hajun "잠시만... 여기는 고문실인가?"
    hide hajun_surprised

    show hajun_angry at left_bottom_offset
    hajun "이 의자에 포박당한 자국도 있군..."
    hajun "최도현 이새끼..."
    hide hajun_angry

    show hajun at left_bottom_offset
    hajun "잠깐만, 의자 밑에 이건 뭐지?"
    hajun "쇳조각이군..."
    hide hajun

    menu:
        "바닥에 떨어진 쇳조각을 살펴본다":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "쇳조각..."
            hajun "뭔가 맞출 수 있는 게 있지 않을까?"
            play sound2 "sfx_item.mp3"
            hajun "가져가자"
            hide hajun

            play sound2 "sfx_ch1_man_walk.mp3"
            scene chapter1_5_1bg with fade
            jump chapter1_5_1_check

label chapter1_5_5:
    scene chapter1_5_5bg with fade
    $ visited_chapter1_5_5 = True

    show hajun at left_bottom_offset
    hajun "여기에 왜 쇠창살이...?"
    hajun "잠시만... 이건 감옥이잖아?"
    hajun "진짜 온통 알 수 없는 것들만 있어"
    hide hajun

    show hajun_consider at left_bottom_offset
    hajun "누굴 가두며 있던거야?"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "최도현을 꼭 잡아서 물어봐야겠어"
    hajun "바닥에 반짝이는게 있어, 이건 뭐지?"    
    hide hajun

    menu:
        "바닥에 떨어진 반짝이는 것을 살펴본다":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "퍼즐처럼 쪼개진 듯한 쇳조각..."
            hajun "나중에 뭔가 할 수 있을지도 몰라"
            play sound2 "sfx_item.mp3"
            hajun "가져가자"
            hide hajun
            play sound2 "sfx_ch1_man_walk.mp3"
            pause (2.0)
            scene chapter1_5_1bg with fade
            jump chapter1_5_1_check

label chapter1_5_6:
    show hajun at left_bottom_offset
    hajun "잠시만... 이 조각들... 다 맞춰지잖아?"
    hajun "내가 주워온 것들로 다시 맞출 수 있을 것 같아."
    hajun "맞춰볼까?"
    hide hajun
    menu:
        "맞춰본다":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "맞춰보자"
            hide hajun

            jump chapter1_5_7

label chapter1_5_7:  
    play sound "sfx_shake.mp3"
    scene chapter1_5_1bg at short_shake
    show hajun_surprised at left_bottom_offset, short_shake
    hajun "이건... 열쇠잖아?" 
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "이걸로 저 끝에 있는 방을 열 수 있지 않을까?"
    hajun "저기에 분명히 최도현이 있을거야"
    hajun "들어갈까?"
    hide hajun
    
    menu:
        "들어간다":
            play sound "sfx_ch2_investigation.mp3" volume 0.5
            show hajun at left_bottom_offset
            hajun "들어가자"
            play sound2 "sfx_ch1_man_walk.mp3"
            hide hajun

            jump chapter1_6

label chapter1_6:
    scene black with fade

    show hajun at left_bottom_offset
    hajun "여기 왜 이렇게 어두워..?"
    hajun "여기.."
    hajun "이게 전등 스위치인가?"
    play sound "sfx_ch1_light_on.mp3"
    hide hajun

    scene chapter1_6bg with fade

    stop music fadeout 2.0
    "불이 켜지며 보일러실 비밀통로로 빠져나가려고 하는 최도현을 발견했다."
    play music "bgm_ch1_battle.mp3" volume 0.7 fadein 1.0
    show hajun_angry at left_bottom_offset, shake
    play  sound "sfx_shake.mp3" volume 0.5
    hajun "{size=40}야!!!!!!{/size}"
    show hajun_angry at left_bottom_offset, short_shake
    play  sound "sfx_shake.mp3" volume 0.5
    extend "  {size=60}최{/size}"
    show hajun_angry at left_bottom_offset, short_shake
    play  sound "sfx_shake.mp3" volume 0.7
    extend "{size=60}도{/size}"
    show hajun_angry at left_bottom_offset, short_shake
    play  sound "sfx_shake.mp3" volume 1.0
    extend "{size=60}현!!{/size}"
    hide hajun_angry

    show hajun_frown at left_bottom_offset
    hajun "내가 여기까지 오면서 살펴봤는데,"
    extend "여기 정상적인 곳은 아니더라?"
    hide hajun_frown

    show hajun_frown at left_bottom_offset
    hajun "대체 무슨 일을 벌이고 있는거냐?"
    hide hajun_frown

    show dohyeon_frown at right_bottom_offset
    dohyeon "형제님... 여긴 들어오시면 안되죠.."
    dohyeon "왜..."
    dohyeon "저의 뜻을 이해하시지 못하시는거죠?"
    dohyeon "돌아가주시죠.. 모든 것을 잊고.."
    hide dohyeon_frown

    show hajun_laugh at left_bottom_offset
    hajun "그건 안되겠는걸?"
    hide hajun_laugh

    show hajun at left_bottom_offset
    hajun "여기까지 오면서 봐 온게 많아서..."
    hajun "너한테 여기에 있었던 이야기 좀 들어봐야겠다 이 새끼야."
    hide hajun

    show dohyeon_angry at right_bottom_offset, shake
    play sound "sfx_shake.mp3"
    dohyeon "이놈이고 저놈이고.."
    hide dohyeon_angry

    show dohyeon_unpleasant at right_bottom_offset
    dohyeon "왜 이렇게 날 방해하는거지?"
    hide dohyeon_unpleasant

    show dohyeon_hammer at right_bottom_offset
    dohyeon "그냥 못본 척 하고 돌아가면 안되냐?"
    dohyeon "알 필요 없잖아."
    hide dohyeon_hammer

    show hajun_determind at left_bottom_offset
    hajun "너는 내가 못본 척 하고 돌아갈 것 같으냐?"
    hajun "일단 서에 가서 이야기 좀 들어보자"
    hajun "너에 대해서 들을 말이 많아"
    hide hajun_determind

    scene chapter1_6bg at shake
    show dohyeon_angry at right_bottom_offset, shake
    play  sound "sfx_big_shake.mp3" volume 0.7
    dohyeon "{color=#803232}{size=40}아{/size}{size=50}아{/size}{size=60}아!{/size}{/color}"

    show dohyeon_angry at right_bottom_offset, shake
    dohyeon "{color=#803232}{size=50}망할 사탄새끼가!!!!{/size}{/color}"

    scene chapter1_6bg at crazy_shake
    show dohyeon_angry at right_bottom_offset, crazy_shake
    play  sound "sfx_big_shake.mp3" volume 0.7
    dohyeon "{color=#803232}{size=40}그냥{/size} {size=50}여기서{/size} {size=60} 죽여주마!!!{/size}{/color}"
    hide dohyeon_angry

    scene chapter1_6bg with fade
    show hajun_laugh at left_bottom_offset
    hajun "그럼 널 때려눕히고 데려가야겠다"
    hide hajun_laugh
    "3번 틀린 선택 시 다시 선택지로 돌아옵니다."
    "옳은 선택지를 3초 안에 골라주세요."

    scene black with fade

    jump chapter1_qte_event

label chapter1_qte_event:
    scene chapter1_6bg with fade
    if success >=5:
        jump chapter1_7
    if current_qte >= len(qte_answers):
        $ current_qte = 0
    
    
    $ action_texts = [
        "최도현이 배트를 휘둘렀다!",
        "최도현이 주먹을 휘둘렀다!",
        "최도현이 빈틈을 보였다!",
        "최도현이 빠르게 돌진해온다!",
        "최도현이 가드를 내렸다!",
    ]

    $ correct_answer = qte_answers[current_qte]
    $ current_action = action_texts[current_qte]

    dohyeon "[current_action]"

    call screen qte_choice

    if _return == correct_answer:
        $ success += 1
        show hajun_laugh at left_bottom_offset
        show dohyeon_hurts at right_bottom_offset, shake
        play sound "sfx_punch.mp3"
        hajun "하! 이거지!"
        hajun "좋았어.. 좀만 더!"
        hide dohyeon_hurts
        hide hajun_laugh
        
    else:
        $ wrong_count += 1
        show hajun_hurts at left_bottom_offset, shake
        show dohyeon_angry at right_bottom_offset
        play sound "sfx_punch.mp3"
        play sound2 "sfx_life_minus.mp3"
        hajun "윽... 이새끼가..."
        hajun "큭.. 똑바로 해야겠어..."
        hide hajun_frown
        hide dohyeon_angry
        if wrong_count >= 3:
            stop music fadeout 1.0
            stop sound fadeout 1.0
            play sound "sfx_gameover.mp3"
            "라이프가 모두 소진되었습니다."
            pause 1.0
            jump chapter1_6_fail

    $ current_qte += 1
    jump chapter1_qte_event
screen qte_choice():
    timer 3.0 action Return("fail")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        padding (30, 30)
        background "#0008"
        has vbox
        spacing 20
        text "3초 안에 선택지를 고르세요." size 40 xalign 0.5

        textbutton "피하기":
            action Return("dodge")
            xsize 300
            xalign 0.5
            padding (10, 10)
            background "#444"
            hover_background "#666"
            text_color "#000000"  # ← 검정 글씨로 바꾸기

        textbutton "때리기":
            action Return("punch")
            xsize 300
            xalign 0.5
            padding (10, 10)
            background "#444"
            hover_background "#666"
            text_color "#000000"  # ← 검정 글씨로 바꾸기

label chapter1_6_fail:
    scene black with fade
    pause 1.0
    "최도현은 제압하지 못한 박하준은 바닥에 쓰러졌다."
    "박하준은 의식을 잃어가며, 최도현이 도망가는 소리가 들렸다."
    pause 1.0
    $ life = 3
    $ current_qte = 0
    $ success = 0
    $ wrong_count = 0
    "3번 틀린 선택 시 다시 선택지로 돌아옵니다."
    "옳은 선택지를 3초 안에 골라주세요."
    play music "bgm_ch1_battle.mp3" fadein 1.0
    play amb "amb_church.mp3"
    jump chapter1_qte_event

label chapter1_7 :
    show hajun_frown at left_bottom_offset
    hajun "윽!"
    hide hajun_frown

    show dohyeon_angry at right_bottom_offset, shake
    dohyeon "지옥으로 가라!!!"
    dohyeon "사탄 새끼야!!"
    hide dohyeon_angry

    play sound "sfx_ch1_run_dh.mp3" volume 1.5
    show jungsik_angry at right_bottom_offset
    jungsik "위험해!!!"
    hide jungsik_angry

    "내가 최도현에게 당하기 전에 남종식 선배가 나를 도와줬다."
    "하지만 나를 도와주던 과정, 뒤에 있던 가스통에 기스가 났다."

    show hajun_surprised at left_bottom_offset
    hajun "선배!!"
    hide hajun_surprised

    show jungsik_consider at right_bottom_offset
    jungsik "야이 새끼야 내가 위험하다고 했잖아!"
    hide jungsik_consider

    show hajun_cough at left_bottom_offset
    hajun "그래도 덕분에 잘 잡아놨잖아요.."
    hide hajun_cough

    show dohyeon_angry at right_bottom_offset, shake
    dohyeon "또야 또.."
    dohyeon "날 방해하는 사탄의 자식이 또 왔네?"
    show dohyeon_angry at right_bottom_offset, crazy_shake
    dohyeon "둘 다 여기서 죽여주마!"
    hide dohyeon_angry

    play sound "sfx_ch1_swing.mp3" 
    "그때 최도현의 해머가 천장의 가스파이프를 한번 더 가격하며\n튀어나온 불똥이 튀었다."
    play amb "sfx_ch1_fire_crackle.mp3" volume 0.3
    "가스통에서 새어나온 가스에 불이 붙어 폭발이 일어났다."
    show chapter1_6bg at shake
    stop music fadeout 2.0
    scene black with fade
    play music "bgm_escape.mp3" fadein 1.0
    "폭발의 영향으로 잠시 기절했다 깨어난 후 주변을 둘러보자\n방이 불에 휩싸여있었다."
    "또한, 최도현은 보이지 않았다."
    scene chapter1_7bg with fade

    show hajun_frown at left_bottom_offset
    hajun "으윽.."
    hide hajun_frown

    show hajun_surprised at left_bottom_offset
    hajun "종식 선배!!"
    hide hajun_surprised

    show hajun_cough at left_bottom_offset
    hajun "최도현은..?"
    hide hajun_cough

    show hajun_frown at left_bottom_offset
    hajun "일단 선배를 데리고 불길을 빠져나가자.."
    hajun "최대한 이 불을 피할 수 있는데로 가야겠어.."
    hajun "불이 번지지 않을 곳으로.."    
    hide hajun_frown

    jump chapter1_8

label chapter1_8:
    scene chapter1_8bg with fade
    $ success = 0
    $ correct_path = ["왼쪽", "오른쪽", "오른쪽"]
    $ current_index = 0

    if asdf < 1:
        $ asdf += 1
        "앞에 세 갈래 길이 있다."
        "옳은 길을 골라 빠르게 대피해야 한다."
        "잘못된 길을 고를 시 라이프가 1 감소합니다."
        "이번 선택은 고정된 순서로 진행됩니다."

    while success < 3 and wrong_count < 3:
        $ current_correct = correct_path[current_index]
        $ result = renpy.display_menu([
            ("왼쪽", "왼쪽"),
            ("직진", "직진"),
            ("오른쪽", "오른쪽"),
        ])

        $ current_index = success

        if result == current_correct:
            play sound "sfx_ch1_run_straight.mp3" volume 3.0
            $ success += 1
            $ current_index += 1
            show hajun at left_bottom_offset
            hajun "여기가 맞는 길이야."
            hajun "좋았어... 이대로만 계속 가면 돼."
            hide hajun
        else:
            $ wrong_count += 1
            play sound "sfx_punch.mp3"
            play sound2 "sfx_life_minus.mp3"
            show chapter1_8 at shake
            show hajun_surprised at left_bottom_offset
            hajun "으악! 불이 온 몸을 덮을 뻔 했잖아!"
            hajun "틀렸어, 여기로 갔다간 통구이가 되고 말 거야."
            hide hajun_surprised

        if success == 3:
            jump chapter1_9
        elif wrong_count >= 3:
            scene black with fade
            $ wrong_count = 0
            $ asdf = 0
            "잘못된 선택지를 세 번 골랐습니다."
            "라이프가 모두 소진되었습니다."
            "다시 선택지로 되돌아갑니다."
            pause 1.0
            jump chapter1_8


label chapter1_9:
    scene chapter1_9bg with fade
    
    show hajun_consider at left_bottom_offset
    hajun "뭐야.. 입구에도 불이 번졌잖아?"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "어떻게 뚫을 순 없을까?"
    hide hajun

    menu:
        "불을 뚫고 정문으로 들어간다":
            show hajun at left_bottom_offset
            hajun "이 정도 불길이면 뚫고 들어갈 수 있을 것 같아."
            hajun "선배 꽉 잡으세요!"
            hide hajun

            play sound "sfx_ch1_run_straight.mp3" volume 3.0 
            "하준과 종식은 불길로 뛰어들었다."

            play sound "sfx_big_shake.mp3"
            scene chapter1_9bg at shake
            show hajun_puzzled at left_bottom_offset, crazy_shake
            hajun "으아아악! 살려줘!"
            hide hajun_puzzled

            "그렇게 나와 선배는 불 속에서 불을 키우는 장작이 되어버렸다."

            pause 1.0
            pro "\n{size=40}Bad End2 : 무모한 돌파{/size}"

            scene black with fade

            pause 1.0
            "다시 선택지로 돌아갑니다."

            pause 1.0

            jump chapter1_9
        "불을 피할 수 있는 장소를 찾아본다.":
            jump chapter1_10

label chapter1_10:
    show hajun at left_bottom_offset
    hajun "아니야, 이건 위험해."
    hajun "차라리 불을 피해 신고 할 수 있는 곳을 찾아보자."
    hajun "그래, 화장실 같은"
    hide hajun

    play sound "sfx_ch1_run_straight.mp3" volume 3.0 
    stop music fadeout 5.0
    scene chapter1_4_3_1bg with fade
    $ renpy.music.set_volume(0.3, channel='amb')
    play voice "amb_toilet.mp3" loop
    play music "bgm_fail.mp3" fadein 1.0
    show hajun at left_bottom_offset
    hajun "여기 화장실에 숨어 있어야겠어."
    hajun "물이 충분하니까 불을 피하기엔 좋을거야."
    hide hajun

    show hajun_consider at left_bottom_offset
    hajun "남종식 선배! 정신차려요!"
    hide hajun_consider

    show jungsik_despair at right_bottom_offset
    jungsik "으윽.. 무슨 일이 있었던 거야"
    hide jungsik_despair

    show hajun at left_bottom_offset
    hajun "모르겠어요, 갑자기 폭발이 일어났고, 거기서 화재가 일어났어요."
    hajun "일단 119에 신고부터 할게요."
    hide hajun

    show jungsik_despair at right_bottom_offset
    jungsik "으윽.. 잠시만.."
    jungsik "최도현은..?"
    hide jungsik_despair

    show hajun_sad at left_bottom_offset
    hajun "{cps=1}..."
    hajun "{cps=10}모르겠어요..."
    hide hajun_sad

    play sound "sfx_calling.mp3"
    pause 2.0
    stop sound
    scene black with fade

    "신고를 받고 온 119는 화재를 진압했고 우리를 구해주었다."
    "나는 어깨에 작은 화상을 입은 것 말고는 다친 곳은 없었으며\n다행히 선배도 멀쩡했다."
    "하지만 불타버린 교회 안에서 최도현의 흔적은 끝내 발견되지 않았다."
    "잔해 속에서 그의 시신은 찾을 수 없었지만, 수사당국은 그가 화재로 \n사망한 것으로 결론지었다."
    "그렇게 사이비 종교 사건은 일단락되었고, 사건은 종결 처리되었다."
    "…그러나 나는 아직도 가끔 생각한다.\n"
    extend "{i}{size=32}정말로,   {/i}{/size}" 
    extend "{i}{color=#803232}{size=32}그가 그 안에서 죽은 게 맞을까?{/i}{/color}{/size}"

    stop music fadeout 2.0
    stop amb fadeout 1.0
    pause 1.0
    jump chapter2_1
