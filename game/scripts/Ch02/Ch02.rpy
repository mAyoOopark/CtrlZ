label chapter2_1:
    scene black
    "{cps=20}최도현 사건으로부터 8년 후"
    "{cps=20}나와 종식이 형은 그 사건을 마무리 짓기위해\n화재가 진압 된 후 끝까지 조사하여 쫓아봤지만"
    "{cps=20}하얀 재가 되버린 폐허 안에서는 마땅 할 증거는 찾아 볼 수 없었고"
    "{cps=20}최도현의 행방마저 불에 탄 듯이 없어졌기에\n우리는 최도현을 화재로 인한 사망으로 처리를 할 수 밖에 없었다."
    show chapter2_1bg with fade
    show hajun_determind at left_bottom_offset
    hajun "{cps=20}......"
    hide hajun_determind

    show hajun_determind at right_bottom_offset
    jungsik "{cps=20} ......"
    hide hajun_determind

    show hajun_angry at left_bottom_offset
    hajun "{cps=40}.....!"

    show jungsik_angry at right_bottom_offset
    jungsik "{cps=40} .....!"

    duo "{cps=40}가위... 바위..."
    show chapter2_1bg at shake
    duo "{cps=60}보!" 

    hide jungsik_angry
    hide hajun_angry
    show hajun_happy at left_bottom_offset
    hajun "이야아아아아!! 이겼다!!"
    hajun "형님!! 오늘은 형님이 쏘시는 겁니다!!"
    hide hajun_happy

    show jungsik_sad at right_bottom_offset
    jungsik "야, 나 돈 없어..."
    jungsik "용돈도 쥐꼬리 만큼 받는데, 담에 사줄게 하준아...  {cps=10}알잖아"
    hide jungsik_sad

    show hajun_wtf at left_bottom_offset
    hajun "그런게 어딨어요!!"
    hajun "제가 저번 주부터 전부 져서 제가 점심 다 샀잖아요!!"
    hide hajun_wtf

    show jungsik_sad at right_bottom_offset
    jungsik "알았어 사면 되잖아 {w=0.2} 사면...."
    hide jungsik_sad

    show hajun_happy at left_bottom_offset
    hajun "{cps=30}얼마 만에 얻어먹는 공짜밥이야~\n 형님 오늘은 삼계탕 먹을까요?"
    
    play sound "sfx_ch2_cellphone_ring.ogg" loop
    "전화가 울린다."
    hide hajun_happy

    show jungsik_blue at right_bottom_offset
    jungsik "그건 좀 봐주라"
    jungsik "일단 이 전화만 받고 가자"
    hide jungsik_blue
    $ renpy.pause()
    stop sound
    
    show jungsik at right_bottom_offset
    jungsik "네, xx경찰서 강력1반 남종식입니다."
    jungsik "네, 네"
    hide jungsik

    show jungsik_serious at right_bottom_offset
    jungsik "네, 지금 바로 가보도록 하겠습니다."
    hide jungsik_serious

    show hajun_curious at left_bottom_offset
    hajun "왜요, 형님 무슨 일인데?"
    hide hajun_curious

    show jungsik_serious at right_bottom_offset
    jungsik "가자, 출발이다"
    hide jungsik_serious
    
    show hajun_wtf at left_bottom_offset
    hajun "아니, 이제 내가 얻어먹을려 하니까 이런일이 생기네! 억울하다 억울해."
    hajun "담엔 꼭 사주셔야해요!"
    hide hajun_wtf
    
    show jungsik_gentle at right_bottom_offset
    jungsik "알았다 알았어. \n가자 사건 현장으로"
    hide jungsik_gentle
    
    show hajun_fightingspirit at left_bottom_offset
    hajun "옙! 가보자고요"
    hide hajun_fightingspirit
    
    scene black with fade
    play sound "sfx_ch2_car_ignition.ogg"
    $ renpy.pause()
    jump chapter2_2

label chapter2_2:
    "그렇게 우리는 신고 받은 장소로 도착했다."
    "하지만 입구에서부터 심상치 않은 기운이 흘러나왔다."
    show chapter2_2bg with fade

    show hajun_disgust at left_bottom_offset
    hajun "윽! 이 악취.. 이 냄새는 틀림 없이..!"
    hide hajun_disgust

    show jungsik_serious at right_bottom_offset
    jungsik "그래, 틀림 없는 시체 썩은 냄새지."
    hide jungsik_serious

    show hajun_surprised at left_bottom_offset
    hajun "형님, 여기 대문이 열려있어요! 대체 무슨일이!!"
    hide hajun_surprised

    "나는 살인사건임을 짐작하고 대문을 박차고 들어갔다."

    show jungsik_panic at right_bottom_offset
    jungsik "야! 또 혼자 들어가면 어떡해!!"
    # (탁 탁 탁 사람 뛰는 사운드와 함께 화면 페이드 아웃)
    hide jungsik_panic

    scene chapter2_2_1bg with fade  # 배경 실내로 전환 (페이드 인)

    show hajun_surprised at left_bottom_offset
    hajun "이…이게 무슨.."
    hide hajun_surprised

    show jungsik_disgust at right_bottom_offset
    jungsik "누군진 몰라도, 일을 거하게 벌려놨구만…"
    hide jungsik_disgust

    show hajun_angry at left_bottom_offset
    hajun "사람을 어떻게 이런 식으로 무자비하게...."
    hide hajun_angry

    show hajun at left_bottom_offset
    hajun "후… 일단 여기를 조사해봅시다."
    hide hajun
    jump chapter2_3

label chapter2_3:
    if visited_livingroom and visited_studyroom and visited_toilet:
        jump chapter2_4
    "어디부터 조사해 볼까?"
    menu:
        "거실":
            jump chapter2_3_explore_livingroom
        "서재":
            jump chapter2_3_explore_studyroom
        "화장실":
            jump chapter2_3_explore_toilet
    jump chapter2_3

label chapter2_4:
    scene chapter2_3_1bg with fade

    show hajun_consider at left_bottom_offset
    hajun "전부 조사를 해본 결과, 시신의 문신 그림과 책 이정도가 있군."
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "메모 해놔야겠어."
    hajun "기억이 안날 때마다 한번씩 봐야겠어."
    hajun "일단, 돌아가자. 더 이상 내가 확인 해볼게 없네. 나머지 팀들에게 도움을 청해야겠어."
    hajun "형님, 돌아갑시다. 우리 둘이서 할게 없어요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래. 돌아가자. 더 이상 우리가 할 수 있는 일은 없는 듯 하네."
    hide jungsik

    scene chapter2_1bg with fade
    "그렇게 며칠이 지난 후, 우리는 또 다시 살인사건이 벌어진 곳으로 찾아가게 됐다."
    
    show jungsik_serious at right_bottom_offset
    jungsik "하준아, 가자."
    hide jungsik_serious

    show hajun at left_bottom_offset
    hajun "네? 어디를요?"
    hide hajun

    show jungsik_serious at right_bottom_offset
    jungsik "어디긴 어디야. 사건현장이지."
    hide jungsik_serious

    show hajun at left_bottom_offset
    hajun "무슨 사건인데요?"
    hide hajun

    show jungsik_serious at right_bottom_offset
    jungsik "살인사건."
    hide jungsik_serious

    show hajun_surprised at left_bottom_offset
    hajun "네? 또요?"
    hide hajun_surprised

    show jungsik_serious at right_bottom_offset
    jungsik "게다가, 그때 주택에서 발견된 시신이랑 비슷한 방법으로 죽은거 같아. 한번 찾아가 보자."
    hide jungsik_serious

    show hajun_serious at left_bottom_offset
    hajun "네. 바로 찾아 갑시다."
    hide hajun_serious

    scene chapter2_4bg with fade

    show jungsik_serious at right_bottom_offset
    jungsik "여기다. 동네가 매우 낡아 보이네."
    hide jungsik_serious

    show hajun_consider at left_bottom_offset
    hajun "큰일이네.. 이런 곳일수록 주위의 CCTV가 없어서 조사하기 빡센데…"
    hide hajun_consider

    show jungsik_serious at right_bottom_offset
    jungsik "일단 사건 현장으로 가보자."
    hide jungsik_serious

    show hajun at left_bottom_offset
    hajun "네, 그럽시다."
    hide hajun
    scene chapter2_5_1bg with fade

    show police_1 at center
    police_1 "충성! 오셨습니까!"
    hide police_1

    show jungsik at right_bottom_offset
    jungsik "그래, 상황은?"
    hide jungsik

    show police_1 at center
    police_1 "네, 상황보고 하자면 신고내용으로 4일 전부터 아무런 인기척이 없었으며 갑자기 악취가 났다고 합니다."
    police_1 "그래서 출동 해본 결과 시신은 부패되어있었고, 사인은 수많은 자상으로 인해 과다출혈이 일어나서 쇼크사 한 걸로 보입니다."
    hide police_1

    show hajun_serious at left_bottom_offset
    hajun "이 사람… 죽기 전까지 얼마나 고통스러웠는지 안구 실핏줄이 모두 터져있어..."
    hajun "대체.. 무슨 일이 벌어지고 있는거지..?"
    hajun "그럼… 조사를 시작해보자."
    hide hajun_serious

    jump chapter2_5

label chapter2_5:
    if visited_livingroom and visited_studyroom and visited_toilet:
        jump chapter2_6
    "어디부터 조사해 볼까?"
    menu:
        "거실":
            jump chapter2_5_explore_villa_livingroom
        "방":
            jump chapter2_5_explore_villa_room
    jump chapter2_5

    
