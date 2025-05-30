default chapter4_2_a1 = False
default chapter4_2_b1 = False
default chapter4_2_c1 = False


label chapter4_2:

    show hajun at left_bottom_offset
    hajun "결정했어요. 미행을 해봅시다."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래, 한번 가보자고."
    hide jungsik

    scene black with fade
    "끝까지 최하람을 미행한 결과 밤이 되었고, 마침내 사이비교단 본거지를 찾게되었다."

    scene chapter2_4bg with fade

    show hajun_consider at left_bottom_offset
    hajun "여기는…그 얼마전 살인사건이 일어났던 빌라 주위네요..."
    hide hajun_consider

    show jungsik_consider at right_bottom_offset
    jungsik "설마 이렇게 가까운 곳에 범인들이 지내고있었을 줄이야.."
    jungsik "그리고 이렇게 구석진 곳에 있으니까 발자취도 찾을 수 없었던 것이였겠지…"
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "늦은 밤인데도 아직 불이 켜져있는 방이 있네요.."
    hajun "조심히 잠입 해서 정보를 알아봐야겠어요…"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래… 한번 들어가서 쓸만한 정보를 얻어보자고.."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네, 출발해보죠."
    hide hajun
    
    scene chapter4_2bg with fade

    show hajun at left_bottom_offset
    hajun "실내는 좀 많이 어둡네요.. 방도 많고.."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "여기 사람도 좀 있는거 같아. 조심히 뒤져보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네. 수사를 시작해볼까요?"
    hide hajun

    jump chapter4_2_m
label chapter4_2_m:
    pause(1.0)
    if  chapter4_2_a1 and chapter4_2_b1 and chapter4_2_c1:
        jump chapter4_2_1
    else:
        menu:
            "숙소":
                jump chapter4_2_a

            "샤워실":
                jump chapter4_2_b

            "예배당":
                jump chapter4_2_c

label chapter4_2_a:
    $ chapter4_2_a1 = True 
    scene chapter4_2_abg with fade

    show jungsik_consider at right_bottom_offset
    jungsik "여기가 숙소인거같은데…"
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "냄새가… 사람사는 곳에서 이런 냄새가 날 수 있는건가?"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그러니까, 불도 꺼져있고."
    jungsik "잠시만 쉿, 여기 사람이 있는데..?"
    jungsik "하나가 아니고 여럿인거 같아."
    hide jungsik

    show hajun_surprised at left_bottom_offset
    hajun "근데 우리가 여기를 들어온걸 눈치를 못챘다구요..?"
    hide hajun_surprised

    show jungsik_surprised at right_bottom_offset
    jungsik "저기. 주사기 보여?"
    hide jungsik_surprised

    show hajun_surprised at left_bottom_offset
    hajun "혹시..저건.."
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "마약 아닌가요?"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그런거 같아. 아마도 여기 있는 인원들은 모두 저걸 맞고 뻗어있는게 아닐까?"
    hide jungsik

    show hajun_consider at left_bottom_offset
    hajun "그러면 두번째 피해자가 마약을 들고 온 곳이 여기가 확실하네요.."
    hajun "그리고 이 벽에 아무렇게나 칠해져있는 글자들…"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "그 빌라에서 본거랑 비슷해요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "여기서 더 지체하면 큰일날거 같아. 이제 슬슬 나가자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네, 다른 곳도 둘러보죠."
    hide hajun

    scene chapter4_2bg with fade

    jump chapter4_2_m
    
label chapter4_2_b:

    $ chapter4_2_b1 = True
    scene chapter4_2_bbg with fade

    show jungsik_disgust at right_bottom_offset
    jungsik "와…곰팡이 냄새…"
    hide jungsik_disgust

    show hajun at left_bottom_offset
    hajun "여기 아무래도 샤워실같아요."
    hide hajun

    show hajun_disgust at left_bottom_offset
    hajun "더러운 물때에 곰팡이 그리고 하수도 썩은 내…."
    hide hajun_disgust

    show hajun_surprised at left_bottom_offset
    hajun "그리고 온수도 안나오는 듯 하네요."
    hide hajun_surprised

    show jungsik_surprised at right_bottom_offset
    jungsik "샤워호스도 제대로 안 꽂혀서 그냥 그런대로 쓰고 있네."
    hide jungsik_surprised

    show hajun_surprised at left_bottom_offset
    hajun "진짜 여기서 제대로 살 수 있을까요…"
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "그 어린 친구들이 여기서 지낸다니…"
    hajun "뭔가 단단히 잘못됐어요. 어린 나이에는 좋은 곳에서 잘 씻고자라야하는데.."
    hide hajun

    show jungsik_angry at right_bottom_offset
    jungsik "대체 이런 곳으로 애들을 데려와서 방치하는 놈들은 누굴까?"
    hide jungsik_angry

    show hajun at left_bottom_offset
    hajun "살인사건의 범인을 찾기도 하고, 이렇게 방치해두는 놈도 찾아야겠네요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래 꼭 그래야지. 여기도 다 둘러본거 같으니 딴 곳도 둘러보자."
    hide jungsik

    scene chapter4_2bg with fade

    jump chapter4_2_m

label chapter4_2_c:

    $ chapter4_2_c1 = True
    scene chapter4_2_cbg with fade

    show hajun at left_bottom_offset
    hajun "여기가 예배당인 것 같네요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "생각보다 규모는 작네."
    jungsik "그리고 난방이 안되서그런지 서늘해."
    hide jungsik

    show hajun_consider at left_bottom_offset
    hajun "여기 왜 의자에 구속구들이 달려있는 걸까요?"
    hajun "혹시 예배를 드리다가 도망치는 아이들을 잡기 위해서..?"
    hide hajun_consider

    show jungsik_surprised at right_bottom_offset
    jungsik "그럴리가…"
    hide jungsik_surprised

    show jungsik at right_bottom_offset
    jungsik "대체 여기서는 사람을 어떤 식으로 대하고 생각하는거야.."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "인간이라기 보다는 짐승 취급을 하고 있는 거 같네요."
    hide hajun

    show hajun_angry at left_bottom_offset
    hajun "그렇지 않고서야 이런식으로 대할 수가..."
    hide hajun_angry

    show jungsik at right_bottom_offset
    jungsik "여기 구속구에는 피가 묻어있어."
    jungsik "아마도 구속구를 끊고 도망치려다 실패한게 아닐까?"
    hide jungsik

    show hajun_angry at left_bottom_offset
    hajun "진짜 도저히 용서 할 수가없네요."
    hajun "아이들을 살인하게 시키고, 마약을 주며, 구속하여 짐승처럼 살게하다니"
    hide hajun_angry

    show hajun at left_bottom_offset
    hajun "진짜 흑막은 따로 있었어요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "꼭 그래야만해."
    jungsik "일단 나머지 곳도 살펴보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "그러죠. 일단 나갑시다."
    hide hajun

    scene chapter4_2bg with fade
    jump chapter4_2_m

label chapter4_2_1:
    
    show jungsik at right_bottom_offset
    jungsik "일단 여기서 조사해볼만 한 것들은 모두 본거 같아."
    jungsik "그럼 밖을 나가서 내일 최하람과 만나서 이야기를 해보자."
    hide jungsik

    show jungsik_consider at right_bottom_offset
    jungsik "설득을 하면 공범을 찾을 수 있고, 여기 교단을 무너뜨릴만한 것들을 알 수 있지 않을까?"
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "그럽시다. 그럼 조용히…."
    hide hajun

    "우리는 나갈려던 찰나, 어두운 시야 때문에 보이지 않는 주사기를 밟고 생각보다 큰 소음에 신도들이 눈치를 채고 밖으로 한 둘 씩 나왔다."

    show dohyeon_asd at right_bottom_offset
    cultist "거기!! 누구야!!"
    hide dohyeon_asd

    show jungsik_surprised at right_bottom_offset
    jungsik "아이씨 큰일났다, 튀어!!"
    hide jungsik_surprised

    show hajun_surprised at left_bottom_offset
    hajun "하필 지금!!"
    hide hajun_surprised

    jump chapter4_2_run
label chapter4_2_run:
    scene chapter4_2_1bg with fade

    $ success = 0

    while success < 5 and wrong_count < 3:

        $ from random import shuffle
        $ correctness = [True, False]
        $ shuffle(correctness)
        $ choices = [
            {"name": "왼쪽", "correct": correctness[0]},
            {"name": "오른쪽", "correct": correctness[1]}
        ]

        "앞에 양갈래 길이 있다."
        "옳은 길을 골라 빠르게 대피해야한다."
        "잘못된 길을 고를 시 라이프가 1 감소합니다."
        "옳은 선택은 랜덤입니다."

        $ result = renpy.display_menu([
            (choices[0]["name"], 0),
            (choices[1]["name"], 1)
        ])

        if choices[result]["correct"]:
            $ success += 1
            show hajun_wtf at left_bottom_offset
            hajun "형님 여기에요!"
            hide hajun_wtf

            show jungsik at right_bottom_offset
            jungsik "오케이! 계속 쭉쭉 가!"
            hide jungsik
            
        else:
            $ wrong_count += 1
            show chapter4_2_1bg at shake
            show hajun_surprised at left_bottom_offset
            hajun "형님 이 길이 아닌가봐요!"
            hide hajun_surprised

            show jungsik at right_bottom_offset
            jungsik "일단 다른 길을 찾아봐!"
            hide jungsik

    if success >= 5:
        jump chapter4_2_2
    elif wrong_count >= 3:
        scene black with fade
        $ wrong_count = 0
        "라이프가 모두 소진되었습니다."
        pause (1.0)

        jump chapter4_2_run

    
label chapter4_2_2:
    scene chapter4_2_2bg with fade
    show jungsik_panic at right_bottom_offset
    jungsik "헉..헉.."
    jungsik "더 이상 안 쫓아오지?"
    hide jungsik_panic

    show hajun_sigh at left_bottom_offset
    hajun "네, 더 이상 오진 않네요."
    hide hajun_sigh

    show hajun at left_bottom_offset
    hajun "확실히 이상한 곳이였어요. 오늘 얻은 정보로 한번 최하람을 구슬려 봐야겠네요."
    hide hajun

    scene black with fade
    "우리는 다음날 처음으로 최하람을 발견했던 곳으로 향했다."
    scene chapter4_1bg with fade

    show hajun at left_bottom_offset
    hajun "역시나 여기에서 또 전도 중이네요."
    hajun "일단 저 친구에게 경계받지 않고 다가갈려면 전도받는 입장이 되야겠죠?"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "아무래도 그래야겠지, 늙은 나보다는 젊은 네가 가서 이야기를 걸어보는게 좋지 않을까?"
    hide jungsik

    show hajun at left_bottom_offset
    hajun "알았어요, 제가 한번 말을 걸어볼게요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래 무슨 일 있으면 문자하고 난 멀리서 지켜볼게."
    hide jungsik

    show hajun_happy at left_bottom_offset
    hajun "네, 그럼 한번 가볼게요."
    hide hajun_happy

    show haram_happy at right_bottom_offset
    haram "안녕하세요~ 저희 천계교 믿고 천국 가지 않으실래요?"
    hide haram_happy

    show hajun_happy at left_bottom_offset
    hajun "천계교가 뭐죠?"
    hide hajun_happy

    show haram_happy at right_bottom_offset
    haram "아 저희 천계교에 관심이 있으시구나, 그럼 저기 카페에서 커피하나 마시면서 이야기 해볼 수 있을까요?"
    hide haram_happy

    show hajun_consider at left_bottom_offset
    hajun "(진짜 사이비 종교니까 도를 아세요느낌으로 다가오는구나..)"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "네 저도 요즘 뭔가 일이 잘 안풀려서요. 한번 이야기를 들어보고싶네요."
    hide hajun

    show haram_happy at right_bottom_offset
    haram "좋습니다! 좋은 이야기 많이 해드릴게요!"
    hide haram_happy
    
    scene black with fade
   
    "나와 최하람은 카페로 향해서 커피를 시키고 자리를 잡았다."

    jump chapter4_2_3

label chapter4_2_3:

    
    scene chapter4_2_3bg with fade
    
    show haram_happy at right_bottom_offset
    haram "저희 천계교는요, 하늘의 아버지가 처음으로 만드신 인간이있는데요."
    haram "그 인간이 아버지께서 하지 말라는 짓을 하셨대요."
    haram "하지만 그 하지말라는 짓은 자신이 창조한 피조물이 자신보다 완벽해지는 것을 질투한 나머지 누명을 씌운거래요."
    haram "그렇게 억울하게 불에 타게 되었는데요."
    haram "지은 죄가 없으니 그 불에서 살아남았으나, 그 불에 의해서 피부가 모두 녹아내렸어요."
    haram "그런 큰 불에도 살아 남아서 사람들은 하늘의 아버지를 외면하고 그 분을 숭배하기 시작했는데요, 그게 저희 종교의 시초에요."
    hide haram_happy

    show hajun at left_bottom_offset
    hajun "(진짜 사이비 종교같은 느낌이네.)"
    hajun "(이런 어린 아이들만 믿을 만한 이야기들이야.)"
    hide hajun

    show haram_surprised at right_bottom_offset
    haram "(벨 울리는 소리) 어? 커피가 나왔네요."
    hide haram_surprised

    show haram_happy at right_bottom_offset
    haram "제가 들고 올게요!"
    hide haram_happy

    show hajun_curious at left_bottom_offset
    hajun "커피 하나에 저렇게 기뻐하는 아이인데 왜 그런 곳에서 지내는 걸까.."
    hajun "그리고 왜 그런 짓을 벌인 걸까.."
    hide hajun_curious

    show hajun at left_bottom_offset
    hajun "이제 한번 알아봐야할거 같아."
    hide hajun

    show haram_happy at right_bottom_offset
    haram "자 일단 커피 드시고요!"
    haram "마저 이야기를 이어서 하자면…"
    hide haram_happy

    show hajun at left_bottom_offset
    hajun "잠시만, 내가 할말이 있어."
    hide hajun

    show haram_surprised at right_bottom_offset
    haram "네…?"
    hide haram_surprised

    show hajun at left_bottom_offset
    hajun "얼마전에 낡은 빌라에서 살인 사건이 일어났어."
    hajun "그것뿐만 아니야, 그 전 주택가에서도 일어났었지."
    hajun "거기서 나온 증거품을 조사해본결과 네가 범인인게 나왔어."
    hide hajun

    show hajun_frown at left_bottom_offset
    hajun "너 맞지?"
    hide hajun_frown

    show haram_surprised at right_bottom_offset
    haram "그게 무슨..?"
    hide haram_surprised

    show hajun at left_bottom_offset
    hajun "그리고 너 뿐만이 아니야."
    hajun "한 명 더 있었지"
    hide hajun 

    show hajun_frown at left_bottom_offset
    hajun "바로 네 오빠 최민재야"
    hide hajun_frown

    show haram_surprised at right_bottom_offset
    haram "사.. 사람 잘못 보신 것 같아요"
    haram "저 이만 가볼게요. 커피 잘 마셨어요."
    hide haram_surprised

    show hajun at left_bottom_offset
    hajun "잠시만, 나는 지금 너를 체포하러 온 게 아니야"
    hajun "일단 내 이야기를 들어줘"
    hide hajun

    jump chapter4_2_select

label chapter4_2_select:
    scene chapter4_2_3bg with fade
    pause(1.0)
    menu:
        "왜 그런곳에서 사는거야? 나 같으면 열심히 돈을 벌어서 그런 곳에서 안 살겠다.":
            show hajun at left_bottom_offset
            hajun "왜 그런곳에서 사는거야? 나 같으면 열심히 돈을 벌어서 그런 곳에서 안 살겠다."
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select2
        "네가 사는 곳을 봤어.. 그런 곳에서 사는 건 힘들지 않니?":
            show hajun at left_bottom_offset
            hajun "네가 사는 곳을 봤어.. 그런 곳에서 사는 건 힘들지 않니?"
            hide hajun

            show haram at right_bottom_offset
            haram "...!"
            hide haram

            show hajun at left_bottom_offset
            hajun "(좋았어, 잘 말한 것 같아.)"
            hide hajun

            jump chapter4_2_select2
        "너 거지야?":

            show hajun_frown at left_bottom_offset
            hajun "너 거지야?"
            hide hajun_frown

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select2

label chapter4_2_select2:
    pause(1.0)
    menu:
        "네 꼴을 좀 봐라, 밥좀 잘 챙겨먹고 다녀라":
            show hajun at left_bottom_offset
            hajun "네 꼴을 좀 봐라, 밥 좀 잘 챙겨먹고 다녀라"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select3
        "힘들지 않니? 밥을 잘 챙겨먹고 있어? 어릴때는 잘 먹고 다녀야해..":
            show hajun at left_bottom_offset
            hajun "힘들지 않니? 밥을 잘 챙겨먹고 있어? 어릴때는 잘 먹고 다녀야해"
            hide hajun

            show haram at right_bottom_offset
            haram "...!"
            hide haram

            show hajun at left_bottom_offset
            hajun "(좋았어, 잘 말한 것 같아.)"
            hide hajun

            jump chapter4_2_select3
        "커피도 잘 먹고 있네, 밥도 그렇게 잘 먹니?":
            show hajun at left_bottom_offset
            hajun "커피도 잘 먹고 있네, 밥도 그렇게 잘 먹니?"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select3
label chapter4_2_select3:
    pause(1.0)
    menu:
        "잘 씻고 다녀라, 냄새나니까":
            show hajun at left_bottom_offset
            hajun "잘 씻고 다녀라, 냄새나니까"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select4
        "네가 사는 곳을 조사해봤어, 따뜻한 물도 안나오고 시설도 부실하던데.. 힘들지 않니?":
            show hajun at left_bottom_offset
            hajun "네가 사는 곳을 조사해봤어, 따뜻한 물도 안나오고 시설도 부실하던데.."
            hajun "힘들지 않니?"
            hide hajun

            show haram at right_bottom_offset
            haram "...!"
            hide haram

            show hajun at left_bottom_offset
            hajun "(좋았어, 잘 말한 것 같아.)"
            hide hajun

            jump chapter4_2_select4
        "집에서 물도 안나와? 대체 어디서 지내는거야?":
            show hajun at left_bottom_offset
            hajun "집에서 물도 안나와? 대체 어디서 지내는거야?"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select4

label chapter4_2_select4:
    pause(1.0)
    menu:
        "항상 웃고 다니는 것 보니 보기는 좋네":
            show hajun_smile at left_bottom_offset
            hajun "항상 웃고 다니는 것 보니 보기는 좋네"
            hide hajun_smile

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select5
        "넌 웃고있지만, 속으로는 힘들어보여. 힘들지만 항상 웃으면서 전도하는 모습이 별로 좋아보이지 않아. 괜찮은 것 맞지?":
            show hajun at left_bottom_offset
            hajun "넌 웃고있지만, 속으로는 힘들어보여."
            hajun "힘들지만 항상 웃으면서 전도하는 모습이 별로 좋아보이지 않아. 괜찮은 것 맞지?"
            hide hajun

            show haram at right_bottom_offset
            haram "...!"
            hide haram

            show hajun at left_bottom_offset
            hajun "(좋았어, 잘 말한 것 같아.)"
            hide hajun

            jump chapter4_2_select5
        "힘들다면 힘들다고 말해.":
            show hajun at left_bottom_offset
            hajun "힘들다면 힘들다고 말해"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_select5

label chapter4_2_select5:
    pause(1.0)
    menu:
        "네 또래 애들과 맞게 행동해. 이게 뭐하는 짓이야.":
            show hajun at left_bottom_offset
            hajun "네 또래 애들과 맞게 행동해. 이게 뭐하는 짓이야"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_4
        "네 또래 애들은 공부하면서 뛰어 놀 때, 이러고 있으면 속상하지 않니?":
            show hajun at left_bottom_offset
            hajun "네 또래 애들은 공부하면서 뛰어 놀 때, 이러고 있으면 속상하지 않니?"
            hide hajun

            show haram at right_bottom_offset
            haram "...!"
            hide haram

            show hajun at left_bottom_offset
            hajun "(좋았어, 잘 말한 것 같아.)"
            hide hajun

            jump chapter4_2_4
        "네 또래 아이들은 지금 다들 미래를 생각하고 있는데 여기서 뭐하는거니?":
            show hajun at left_bottom_offset
            hajun "네 또래 아이들은 지금 다들 미래를 생각하고 있는데 여기서 뭐하는거니?"
            hide hajun

            show hajun at left_bottom_offset
            hajun "네 또래 애들과 맞게 행동해. 이게 뭐하는 짓이야"
            hide hajun

            show haram at right_bottom_offset
            haram "..."
            hide haram

            show hajun at left_bottom_offset
            hajun "(아차, 내가 잘못 말했나?)"
            hide hajun
            show chapter4_2_3bg at shake
            $ wrong_count += 1
            
            if wrong_count >= 3:
                scene black with fade
                $ wrong_count = 0
                "라이프가 모두 소진되었습니다."
                "다시 선택지로 이동합니다."
                jump chapter4_2_select
            jump chapter4_2_4
            

label chapter4_2_4:

    show haram_flustered at right_bottom_offset
    haram "저에게…"
    haram "저에게… 뭘 원하시는거에요?"
    haram "그냥 체포 해주시면 안되나요? 제가 이렇게 불면 전 죽을지도 몰라요.."
    hide haram_flustered

    "최하람은 겁을 먹은 듯 몸을 떨기 시작했다."

    show hajun_surprised at left_bottom_offset
    hajun "(대체… 어린 아이를 어떻게 대했으면 이럴 수 가 있는거지..?)"
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "하람아 날 봐봐."
    hajun "난 경찰이야. 너를 충분히 지켜 줄 수 있어."
    hajun "그리고 너를 이렇게 만든 사람도 잡아 줄 수있어."
    hajun "네가 잘못한 건 맞고 마땅한 벌을 받아야 하나 그거를 이런 식으로 대해지는건 옳지않아."
    hajun "나에게 다 털어줘. 네가 너와 거기있는 아이들을 구해줄게."
    hide hajun

    show haram_low at right_bottom_offset
    haram "알았어요. 그럼 왜 이렇게 되었는지 처음부터 천천히 설명해드릴게요."
    hide haram_low
    
    show haram at right_bottom_offset
    haram "일단 경찰관님이 아시는 것 처럼 저와 제 오빠 그리고 엄마와 아빠 넷이서 잘 살고있었어요."
    haram "하지만 어느 날 아빠가 하던 사업이 부도가 났고, 이혼을 하며 저와 제 오빠는 보육원에 맡겨지게 됐어요."
    haram "그렇게 보육원에서 지내는데, 보육원 선생님들이 저희를 폭행하기 시작했어요."
    haram "온갖 잡일을 시키면서 제대로 하지도 않냐고…"
    hide haram

    show hajun_consider at left_bottom_offset
    hajun "(보육원에서 이런 뒷 이야기가 있을 줄이야..)"
    hajun "(그래서 최하람과 최민재의 이름을 꺼내니 흠칫 놀란 이유가 있던거였어.)"
    hide hajun_consider
    
    show hajun at left_bottom_offset
    hajun "응..그래서..?"
    hide hajun

    show haram at right_bottom_offset
    haram "그래서 오빠는 참지 못하고 저한테 보육원을 탈출하자고 했어요."
    haram "여기서 계속 지내다가 맞아 죽겠다면서요."
    haram "저는 나가기 무서웠지만 오빠가 저를 지켜주겠다는 말에 몰래 밤에 나가게 됐어요."
    haram "하지만 삶은 고생과 고난의 연속이랬죠. 보육원을 나온 저희는 마땅한 보금자리도 찾지 못했고 거리를 떠돌게 되었어요."
    haram "아무 주차장에서 노숙을 하며 음식물쓰레기통도 뒤져봤구요, 소매치기도 했었고, 빵집의 빵도 훔치게 되었어요."
    haram "하지만 이런 일들이 계속 되면 걸리기 마련이죠."
    haram "그렇게 저희가 편의점에서 먹을 거리를 훔쳐서 걸린 찰나, 그 사람이 왔어요."
    haram "자신이 잘못 가르쳤다고, 이 물건의 값을 지불 한다고 말이에요."
    haram "그때부터 그 사람과 악연의 시작이였어요."
    haram "오빠가 어느날 기쁜 얼굴로 뛰어와 저에게 말하는거에요. 이제 여기서 안 살아도 된다고, 돈을 벌 곳이 생겼다고."
    hide haram

    show haram_low at right_bottom_offset
    haram "너를 지켜주겠다고…"
    hide haram_low

    show haram at right_bottom_offset
    haram "그렇게 간 곳이 경찰관님이 보신 그 건물일거에요."
    hide haram

    show hajun at left_bottom_offset
    hajun "잠시만, 그럼 너희를 구해주고 그곳으로 데려간 사람의 이름은 알아?"
    hide hajun

    show haram at right_bottom_offset
    haram "아마도 제 기억대로라면…'최도현'일꺼에요."
    hide haram

    show hajun_consider at left_bottom_offset
    hajun "(최도현이라고? 그 화재에서 죽은게 아니였나? 살아서 지금도 그런 짓을 벌이고있다고?)"
    hajun "(그때 내가 최도현을 어떻게 해서라도 잡았더라면 이런 일은 벌어지지 않았을텐데….!)"
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "알았어… 계속 이야기해줘…."
    hide hajun

    show haram at right_bottom_offset
    haram "그렇게 우리는 그곳에 가서 종교적으로 세뇌를 받았고, 돈을 받기 위해서는 일을 해야한다면서 온갖 불법적인 일을 시켰어요."
    haram "저는 뭔가 이상함을 느끼고 나갈 기회를 노리고 오빠에게 말했는데, 오빠는 저를 지키기 위해서 이런 짓을 하는데 너는 내가 이상해보이냐며..."
    hide haram

    show haram_low at right_bottom_offset
    haram "제가 오빠에게 부담만 안줬어도…"
    hide haram_low

    show haram at right_bottom_offset
    haram "저희 오빠와 거기에 있는 사람들을 구해주세요."
    haram "사실 경찰관님이 그 살인 사건때문에 조사하고 돌아다니는 거 최도현은 이미 알고 있어요."
    haram "경찰관님이 생각하는 것 보다 최도현의 정보망은 넓어요."
    haram "그래서 이 사건이 잠잠해질때까지 해외에서 지낼 생각이래요."
    hide haram

    show hajun_surprised at left_bottom_offset
    hajun "잠시만, 넌 이 이야기를 어떻게 들은거야?"
    hide hajun_surprised

    show haram at right_bottom_offset
    haram "아까 말했다시피 나갈 기회를 찾기 위해 여기저기 뒤지던 중 의도치 않게 들었어요."
    haram "아무튼 이야기를 이어서 하자면 2시간 뒤에 신도들을 태운 밀항선이 출발한대요."
    haram "그리고 30분 뒤에는 신도들을 태우러 차가 저희 본거지 앞에 도착 할거에요. 그 안에 구출해야해요."
    hide haram

    show hajun_wtf at left_bottom_offset
    hajun "혹시 밀항선이 출발하는 항구는 여기서 얼마나 걸려?"
    hide hajun_wtf

    show haram at right_bottom_offset
    haram "2시간 가까이 걸려요.. 하지만 밟으면 그것보단 빨리 도착 할 거에요."
    hide haram

    show hajun_consider at left_bottom_offset
    hajun "(최도현에게 먼저 가면 아이들도 못 구하고, 최도현도 놓칠 수도 있어.)"
    hajun "(하지만 아이들을 먼저 구하면 확실하게 아이들을 구출 할 수 있겠지만, 최도현을 놓치게 되겠지.)"
    hajun "(어떻게 하는게 좋을까…?)"
    hide hajun_consider
    
    menu:
        "아이들에게 먼저 간다":
            jump chapter5_3
        "최도현에게 먼저 간다":
            jump chapter5_4
    
    return
