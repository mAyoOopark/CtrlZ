label chapter4_1:
    show screen life_display
    show hajun at left_bottom_offset
    hajun "형 아무래도 잡는게 맞는 거 같아."
    hide hajun
    
    show jungsik_consider at right_bottom_offset
    jungsik "네가 그렇다면야.."
    jungsik "알았어 바로 시작하자."
    hide jungsik_consider

    scene chapter4_1bg with fade

    show hajun_angry at left_bottom_offset
    hajun "거기! 지금 전도하는 너!"
    hajun "연쇄살인사건의 용의자로 체포한다."
    hide hajun_angry

    show haram_flustered at right_bottom_offset
    haram "네..? 저요..?"
    haram "저.. 저는 그런 적 없는데요.."
    hide haram_flustered

    show hajun_puzzled at left_bottom_offset
    hajun "이렇게 발뺌을 한다?"
    show chapter3_1_1_ibg at center_image
    hajun "너 xx 빌라에 들어간 적 있지?"
    hide hajun_puzzled

    show hajun at left_bottom_offset
    hajun "여기 cctv에 너랑 비슷한 나이의 아이들이 들어가더라고."
    hajun "물론 원본 영상 이미지로는 너를 알아보기 힘들었지."
    hajun "하지만 사건 현장에는 {color=#803232}머리카락{/color}이 떨어져 있었고, 그걸로 DNA를 추적했어."
    hajun "그렇게 네 부모님을 찾을 수 있었고, 행적을 쫓은 결과 보육원에서 나왔다는 것 까지 알 수 있었어."
    hide hajun

    hide chapter3_1_1_ibg

    show hajun_laugh at left_bottom_offset
    hajun "어때 이래도 변명할 수 있나?"
    hide hajun_laugh

    show haram_flustered at right_bottom_offset
    haram "....."
    hide haram_flustered

    show hajun at left_bottom_offset
    hajun "그럼 연쇄살인사건의 유력한 용의자로 체포한다."
    hajun "당신은 묵비권을 행사할 수 있고, 당신은 변호인을 선임할 수 있으며 당신이 한 발언은 법정에서 불리하기 작용할 수 있습니다."
    hide hajun

    scene black with fade

    "그렇게 우리는 최하람을 체포항 경찰서로 들어와 심문을 시작했다."

    pause(1.0)

    scene chapter4_1_1bg with fade

    show hajun at left_bottom_offset
    hajun "그래서.. 나머지 한 명 너랑 같이 있던 애 말이야"
    hajun "어디갔어?"
    hajun "너 혼자 독박쓸 거 아니잖아"
    hide hajun

    show haram_low at right_bottom_offset
    haram "누군지 모르겠는데요..."
    haram "처음보는 사람이에요.."
    hide haram_low

    show hajun_laugh at left_bottom_offset
    hajun "또 이렇게 거짓말을 치시겠다?"
    hajun "내가 아까 말했지?"
    hajun "머리카락이 네 것과 하나 더 나왔는데, 나머지 하나는 너보다 1살 많은 남자아이더라고"
    hajun "그리고, 네 {color=#803232}친오빠{/color}인 것 까지 알고 있지."
    hide hajun_laugh

    show hajun at left_bottom_offset
    hajun "이렇게 모든 증거가 너희 둘을 가르키고 있는데, 아직까지 발뺌 할 생각이야?" 
    hide hajun

    show haram_teeth at right_bottom_offset
    haram "...."
    hide haram_teeth

    show hajun_sigh at left_bottom_offset
    hajun "또 말 안하네.."
    hajun "어떻게 해야할까?"
    hide hajun_sigh

    menu:
        "심문한다":
            jump chapter4_1_1

label chapter4_1_1:
    show hajun_despair at left_bottom_offset
    hajun "그래서, 최민재는 어디갔고, 왜 죽였냐니까?"
    hide hajun_despair

    show haram at right_bottom_offset
    haram "....."
    hide haram

    show hajun_sigh at left_bottom_offset
    hajun "어떻게 해야 정보를 얻을 수 있는거지?"
    hide hajun_sigh

    menu:
        "압수한 물품 조사":
            show hajun at left_bottom_offset
            hajun "맞아, 이것도 있었지.."
            hide hajun

            show hajun_consider at left_bottom_offset
            hajun "지갑이 왜 이렇게 볼록해?"
            hajun "돈이 이렇게 많다고?"
            hide hajun_consider

            show hajun_surprised at left_bottom_offset
            hajun "뭐야, 돈이 아니잖아..?"
            hajun "그냥 단순한 종이 뭉치였네"
            hide hajun_surprised

            show hajun at left_bottom_offset
            hajun "혹시 이거.."
            hajun "아까 전도 할 때 주던 종이들인가..?"
            hajun "{i}{b}'나는 하늘의 선택을 받아 하늘의 아버지가 내려주신 시련으로부터 살아 남았고,{w=1}\n그렇기에 나는 하늘에 계신 아버지가 내려주신 메시아다.'{/i}{/b}"
            
            "안에 있는 종이를 모두 펼치니 약도로 보이는 종이가 바닥으로 떨어졌다."

            hajun "이건.. 그 낡은 빌라 주위 건물이잖아..?"
            hajun "혹시 여기서 활동하는건가?"
            hajun "그럼 이걸로 다시 심문해보자."
            jump chapter4_1_2

label chapter4_1_2:
    show hajun at left_bottom_offset
    hajun "여기 그려진 약도, 네가 활동하는 본거지냐?"
    hide hajun

    show haram_flustered at right_bottom_offset
    haram "그.. 그걸 어떻게?"
    hide haram_flustered

    show hajun at left_bottom_offset
    hajun "그리고 너 열심히 전도하는 것 같더라."
    hajun "이렇게 많은 전단지를 들고 다니면서 전도를 하다니."
    hajun "근데 네가 믿는 신도 무심하시지, 여기 건물 엄청 낡았잖아.."
    hide hajun

    show hajun_laugh at left_bottom_offset
    hajun "그런 낡은 건물에 살게 하다니, 신이 오히려 무능하네"
    hajun "불쌍하다. 나라면 그런 신은 믿지 않아."
    hide hajun_laugh

    show haram_teeth at right_bottom_offset
    haram "니가.."
    haram "니가 뭘 알아.."
    hide haram_teeth

    show haram_angry at right_bottom_offset
    show chapter4_1_1bg at shake
    haram "{i}{color=#803232}{size=40}니가 뭘 알아!!{/i}{/color}{/size}"
    haram "나는 충분히 잘 살고 있고, 그분이 내려준 낙원에서 부족한 거 없이 지내고 있는.."
    hide haram_angry

    show haram_flustered at right_bottom_offset
    haram "앗..!"
    hide haram_flustered

    show hajun_smile at left_bottom_offset
    hajun "여기서 살고있는게 맞구나?"
    hide hajun_smile

    show haram_angry at right_bottom_offset
    haram "감히 우리 유일 신을 모욕하고 능욕하다니!!"
    haram "천벌을 받을거야!!"
    hide haram_angry

    show hajun_smile at left_bottom_offset
    hajun "나라면 그런 종교 믿지 않을거야."
    hajun "신이 진짜로 있다면 너한테 살인을 시켰을까?"
    hajun "형님 출발합시다!! 어딘지 알아냈어요."
    hide hajun_smile

    show jungsik_smile at right_bottom_offset
    jungsik "알아냈구나! 알았어 바로 거기로 출발하자."
    hide jungsik_smile

    scene black with fade

    jump chapter4_1_3

label chapter4_1_3:
    scene chapter4_1_3bg with fade
    
    show hajun at left_bottom_offset
    hajun "평범한 상가 같은데.."
    hajun "그 연쇄살인사건의 원흉의 장소라니.."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "머뭇거리지 말고 바로 들어가자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네 바로 들어가죠."
    hide hajun

    scene black with fade

    "그렇게 우리는 사이비 종교의 본거지로 들어갔다."

    scene chapter4_1_3_1bg with fade
    
    show hajun at left_bottom_offset
    hajun "아무래도 여기가 이 건물의 중심부인거 같죠?"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래, 한번 들어가보자."
    hide jungsik

    show hajun_puzzled at left_bottom_offset
    hajun "이게 뭐야.."
    hajun "두번째 피해자의 집에 있던 주사기들과 교리서적.."
    hajun "대체 이거 무슨 종교 집단인거야.."
    hide hajun_puzzled

    show jungsik_sigh at right_bottom_offset
    jungsik "하준아 여기저기 둘러봤는데, 아무도 없어"
    hide jungsik_sigh

    show hajun_sad at left_bottom_offset
    hajun "젠장, 확실한 증거를 잡은 줄 알았는데.."
    hajun "이렇게 또 놓친다고..?"
    hide hajun_sad

    "그 떄, 갑자기 문이 열리고 누군가가 들어왔다."

    show dohyeon_asd at right_bottom_offset
    asd "누구세요?"
    asd "여기가 어딘 줄 알고 들어왔죠?"
    hide dohyeon_asd

    show hajun_surprised at left_bottom_offset
    hajun "너는..!"
    hajun "{size=40}{i}최민재?{/szie}{/i}"
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "드디어 찾았다.."
    hajun "너를 연쇄살인사건의 가해자로 체포하겠다."
    hide hajun 

    show minjae at right_bottom_offset
    minjae "하하.. 사람 잘못 보신 거 같은데요?"
    hide minjae

    show hajun at left_bottom_offset
    hajun "그래? 일단 서에가서 이야기 해볼까?"
    hide hajun

    show minjae at right_bottom_offset
    minjae "이런 씨..."
    hide minjae

    "궁지에 몰린 최민재는 곧장 밖으로 도망갔다."
    
    show hajun_angry at left_bottom_offset
    hajun "거기 서!!"
    hide hajun

    jump chapter4_1_4

label chapter4_1_4:
    scene chapter4_1_4bg with fade
    "미니게임을 통과했을 때와 하지 못했을 때의 진행 스토리가 다릅니다."
    "신중히 플레이해주시길 바랍니다."
    $ success = 0
    $ wrong = 0
    $ max_attempts = 4
    $ attempt = 0
    $ first = 0

    while attempt < max_attempts and wrong < 3:
        $ attempt += 1

        if first < 1:
            $ first += 1
            "앞에 양갈래 길이 있다."
            "옳은 길을 골라 빠르게 대피해야한다."
            "잘못된 길을 고를 시 라이프가 1 감소합니다."
            "옳은 선택은 랜덤입니다."

        $ result = renpy.display_menu([
            ("왼쪽", "왼쪽"),
            ("오른쪽", "오른쪽"),
        ])    
        $ correct = (attempt in [1, 2])  # 원하는 정답 위치로 조정 가능
        $ is_correct = (result == "왼쪽") if correct else (result == "오른쪽")

        if is_correct:
            $ success += 1

            if success == 1:
                show hajun_surprised at left_bottom_offset
                hajun "좋았어. 저기 최민재가 보인다!"
                hide hajun_surprised
            elif success == 2:
                show hajun_surprised at left_bottom_offset
                hajun "이쪽이다. 최민재! 거기 서!"
                hide hajun_surprised
                jump chapter5_1
        else:
            $ wrong += 1
            #$ wrong_count += 1

            if wrong == 1:
                show hajun_surprised at left_bottom_offset, shake
                hajun "틀렸어. 최도현은 여기에 온거 같지 않아." 
                hide hajun_surprised
            elif wrong == 2:
                show hajun_surprised at left_bottom_offset, shake
                hajun "아니야, 이쪽 방향이 아니야."
                hide hajun_surprisedz
                jump chapter5_2

#        if wrong_count >= 3:
#            scene black with fade
#            $ wrong_count = 0
#            $ life = 3
#            "잘못된 선택지를 세 번 골랐습니다."
#            "라이프가 모두 소진되었습니다."
#            pause 1.0

