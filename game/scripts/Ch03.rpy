default saw_knife = False
default saw_drug = False
default saw_hair = False


label chapter3:
    scene black with fade
    "사건 조사를 끝낸 며칠 뒤"
    "국과수의 감식 결과가 나오게 되었다."

    scene chapter2_1bg with fade

    show jungsik at right_bottom_offset
    jungsik "하준아!"
    hide jungsik

    show jungsik_smile at right_bottom_offset
    jungsik "드디어 감식 결과가 나왔어!"
    hide jungsik_smile

    show hajun_smile at left_bottom_offset
    hajun "오 드디어 나왔데요?"
    hide hajun_smile
    
    show hajun at left_bottom_offset
    hajun "CCTV 화질 개선 요청했던 것도 나왔어요?"
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "물론이지."
    jungsik "하나씩 확인해보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "넵!"
    hide hajun

    jump chapter3choice

label chapter3choice:
    pause(1.0)
    menu:
        "칼":
            $ saw_knife = True
            show jungsik at right_bottom_offset
            jungsik "칼에 묻은 지문을 감식한 결과 등록되지 않은 지문이였어."
            hide jungsik

            show hajun_consider at left_bottom_offset
            hajun "그게... 무슨 의미죠?"
            hide hajun_consider 

            show jungsik at right_bottom_offset
            jungsik "그러니까, 지문으로 용의자를 추적 할 수 없다는 뜻이지."
            hide jungsik

            show hajun_consider at left_bottom_offset
            hajun "어떻게 지문이 등록되지 않을 수 있죠?"
            hide hajun_consider

            show jungsik_consider at right_bottom_offset
            jungsik "혹시나 하는 생각인데"
            jungsik "어린 아이들이 저지른 일이 아닐까 생각이 든다."
            hide jungsik

            show hajun_puzzled at left_bottom_offset
            hajun "에이 설마요, 외국인이지 않을까요?"
            hajun "불법체류자 같은.."
            hide hajun_puzzled

            show jungsik_consider at right_bottom_offset
            jungsik "그래.. 그게 맞겠지?"
            hide jungsik_consider

            jump chapter3choice_check
        "마약":
            $ saw_drug = True
            
            show jungsik at right_bottom_offset
            jungsik "그 집에 있었던 주사기 말이야."
            jungsik "그거 마약 맞는 것 같다. 감식 결과 모르핀이네."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "진짜 마약이 맞았던거군요.."
            hide hajun

            show jungsik at right_bottom_offset
            jungsik "그래, 마약 종류는 모르핀이였어."
            hide jungsik

            show hajun_consider at left_bottom_offset
            hajun "그럼.. 스마트폰에 있었던 거래 내용들은 전부 마약 거래가 맞았네요."
            hide hajun_consider

            show jungsik_consider at right_bottom_offset
            jungsik "그렇지.."
            hide jungsik_consider

            show hajun_consider at left_bottom_offset
            hajun "그 피해자는 진짜로 마약을 자신이 속해있던 곳에서 빼왔던 것이고, 그걸로 금전벌이를 했으며.."
            hajun "..."
            hajun "빼온게 들키자 피해자가 속해있던 곳의 인원들에게 살해당했다.."
            hide hajun_consider

            show hajun_consider at left_bottom_offset
            hajun "뭔가 복잡해지네.."
            hide hajun_consider

            jump chapter3choice_check
        "머리카락":
            $ saw_hair = True
            show jungsik at right_bottom_offset
            jungsik "머리카락 감식 결과, 일단 피해자의 것은 아니야"
            hide jungsik

            show hajun at left_bottom_offset
            hajun "그럼, 그 머리카락의 주인이 용의자인 확률이 높겠네요."
            hide hajun

            show jungsik at right_bottom_offset
            jungsik "그렇지, 하지만 머리카락의 주인은.."
            hide jungsik

            show jungsik_consider at right_bottom_offset
            jungsik "아직 사춘기도 오지 않은 여자 아이와 남자 아이의 것이야."
            hide jungsik_consider

            show hajun_puzzled at left_bottom_offset
            hajun "네..?"
            hajun "설마.. 어린 아이들이 범인이라고 생각하시는 건가요?"
            hide hajun_puzzled

            show jungsik_consider at right_bottom_offset
            jungsik "일단은.. 그렇게 의심하고 있어."
            hide jungsik_consider

            show hajun_consider at left_bottom_offset
            hajun "하지만 그 집을 예전에 방문한 아이들일 수도 있잖아요."
            hide hajun_consider

            show jungsik at right_bottom_offset
            jungsik "그래, 그래서 단정 지을 수도 없는거지."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "제발.. 우리가 생각하는 상황이 벌어지지 않았으면 좋겠네요."
            hide hajun

            show jungsik at right_bottom_offset
            jungsik "...."
            hide jungsik

            jump chapter3choice_check


label chapter3choice_check:
    if saw_knife and saw_hair and saw_drug:
        jump chapter3_1
    else:
        jump chapter3choice

label chapter3_1:
    show jungsik at right_bottom_offset
    jungsik "그럼 이제, cctv 영상을 확인해보자."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네 그럼 그놈들 낯짝 한번 보죠"
    hide hajun

    scene chapter3_1_1bg with fade

    show hajun_frown at left_bottom_offset
    hajun "흠.. 화질 개선을 했다 해도 얼굴은 잘 보이지 않네요.."
    hide hajun_frown

    show chapter3_1_1_ibg at center_image

    show hajun_surprised at left_bottom_offset
    hajun "어? 잠시만.."
    hide hajun_surprised

    show jungsik_sigh at right_bottom_offset
    jungsik "..."
    hide jungsik_sigh

    show hajun at left_bottom_offset
    hajun "..."
    hide hajun

    show hajun_surprised at left_bottom_offset
    hajun "잠시만.. 설마 범행 시각 때 왔다 갔다 한 이..."
    hajun "어린 아이들이라구요?"
    hide hajun_surprised

    show jungsik_sigh at right_bottom_offset
    jungsik "설마설마 했는데.."
    jungsik "진짜 어린 아이들이였을 줄이야.."
    hide jungsik_sigh

    show jungsik_consider at right_bottom_offset
    jungsik "그것도 하나가 아니라 둘이나.."
    hide jungsik_consider

    hide chapter3_1_1_ibg

    show hajun_puzzled at left_bottom_offset
    hajun "그럼 지문이 등록되지 않은 이유도,\n그 집에서 어린 아이들의 머리카락이 나온 이유도..."
    hide hajun_puzzled

    show jungsik_consider at right_bottom_offset
    jungsik "범인이 어린 아이들이였기 때문이지."
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "그럼 우리가 해야 할 일은 이 dna로 부모를 추적해서 \n그 아이들이 누군지 알아야겠네요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그렇지.. 일단 이 아이들의 부모가 누군지부터 확인해야겠네."

    scene black with fade

    "그렇게 이틀이 지나고, 그 아이들의 부모의 신상을 확인하여 전화를 해보기로 한다. "
    
    scene chapter2_1bg with fade

    show hajun at left_bottom_offset
    hajun "그럼, 전화 해볼게요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래."
    hide jungsik

    hajun "..."
    jungsik "..."

    show parents at right_bottom_offset
    parents "여보세요?"
    hide parents

    show hajun at left_bottom_offset
    hajun "네 안녕하세요."
    hajun "저는 xx 경찰서 강력 1반 박하준입니다."
    hajun "몇가지 여쭤볼게 있어서요."
    hide hajun

    show parents at right_bottom_offset
    parents "보이스 피싱 할거면 다른 곳에 전화하세요."
    hide parents

    show hajun_surprised at left_bottom_offset
    hajun "잠시만요!! 진짜 하나만 여쭙겠습니다."
    hide hajun_surprised

    show hajun at left_bottom_offset
    hajun "지금.. 자녀분과 같이 게시나요..?"
    hide hajun

    show parents at right_bottom_offset
    parents "저희 집에는 아이가 없습니다."
    parents "이혼하면서 애들을 보육원에 맡겼거든요."
    hide parents

    show hajun at left_bottom_offset
    hajun "보육원이라면 어디 보육원인지 여쭤봐도 될까요?"
    hajun "정말 중요합니다."
    hide hajun

    show parents at right_bottom_offset
    parents "하.."
    parents "xx 보육원이요."
    parents "저한테는 피해가 안끼치는거죠?"
    parents "이젠 얼굴도 가물가물한 아이들인데.."
    hide parents

    show hajun_consider at left_bottom_offset
    hajun "그건 모르는 일이죠.."
    hajun "혹시 보육원으로 보내신 아이들의 이름이 어떻게 될까요?"
    hide hajun_consider

    show parents at right_bottom_offset
    parents "{cps=5}......"
    parents "최민재와 최하람이에요."
    parents "이젠 더 이상 물어보실 것 없으시죠?"
    parents "귀찮으니까 전화는 삼가해주세요. 제발"
    hide parents

    show hajun_angry at left_bottom_offset
    hajun "잠시만요! 저기요!"
    hide hajun_angry

    show hajun_puzzled at left_bottom_offset
    hajun "끊었네.."
    hide hajun_puzzled

    show jungsik at right_bottom_offset
    jungsik "됐어, 우리가 알아야 될 정보는 이정도면 충분해"
    jungsik "그럼 xx 보육원으로 가보자."
    jungsik "거기에 우리가 필요한 정보가 있을지도 몰라."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네. 그럼 보육원으로 가시죠."
    hide hajun

    scene black with fade

    "그렇게 나와 종식이 형은 xx 보육원으로 아이들의 정보를 얻기 위하여 발걸음을 옮겼다."
    jump chapter3_2

label chapter3_2:

    scene chapter3_1 with fade

    show hajun at left_bottom_offset
    hajun "여기가 xx 보육원.."
    hajun "낡았네요.. 건물이.."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "내가 오면서 미리 전화했거든?"
    jungsik "아마도 정문에서 기다리고 계실거야."
    hide jungsik

    show babyfarmer at right_bottom_offset
    babyfarmer "오셨네요." 
    babyfarmer "민재와 하람이 때문에 오셨다고.."
    hide babyfarmer

    show hajun at left_bottom_offset
    hajun "네, 혹시 그 아이들이 여기에 있을까요?"
    hide hajun

    show babyfarmer_flustered at right_bottom_offset
    babyfarmer "아뇨.. 그 아이들은.."
    hide babyfarmer_flustered

    show babyfarmer_low at right_bottom_offset
    babyfarmer "여기를 몰래 나가 어디론가 가버렸습니다."
    babyfarmer "경찰에 신고를 해도 여기 주위가 워낙 낡은 동네라서 cctv도 잘 없거든요."
    hide babyfarmer_low

    show hajun_puzzled at left_bottom_offset
    hajun "몰래 여기를 빠져나갔다구요?"
    hide hajun_puzzled

    show hajun at left_bottom_offset
    hajun "이유는 파악이 되나요?"
    hide hajun

    show babyfarmer_flustered at right_bottom_offset
    babyfarmer "...!"
    hide babyfarmer_flustered

    show babyfarmer_low at right_bottom_offset
    babyfarmer "그거는 저도 잘 모르겠네요.."
    hide babyfarmer_low

    show hajun at left_bottom_offset
    hajun "그럼.."
    hajun "아이들 얼굴이라도 알 수 있을까요?"
    hide hajun

    show babyfarmer at right_bottom_offset
    babyfarmer "그럼요."

    show babyfarmer at right_bottom_offset
    babyfarmer "이 사진을 보시면 되실거예요"
    show chapter3_2_1bg at center_image
    hide babyfarmer
    pause(3.0)
    hide chapter3_2_1bg

    show hajun at left_bottom_offset
    hajun "이 정도면 저희가 원하는 정보는 이게 끝인 것 같습니다."
    hajun "수사에 응해주셔서 감사합니다."
    hide hajun
    
    show babyfarmer at right_bottom_offset
    babyfarmer "별말씀을요."
    babyfarmer "꼭 아이들을 찾아주세요."
    hide babyfarmer

    show hajun at left_bottom_offset
    hajun "네, 수고하십시오."
    hide hajun
    
    scene chapter3_3bg with fade

    show jungsik_sigh at right_bottom_offset
    jungsik "이 넓고 낡은 동네에서 어떻게 찾냐.."
    hide jungsik_sigh

    show hajun_consider at left_bottom_offset
    hajun "그러게요.."
    hajun "숨을 곳도 많은데 cctv도 설치 되어있지 않은 곳이라니.."
    hajun "어떻게 찾죠..?"
    hide hajun_consider

    show jungsik_sigh at right_bottom_offset
    jungsik "몰라.. 머리 아프다.."
    hide jungsik_sigh

    show hajun_sigh at left_bottom_offset
    hajun "하.. 복잡하네.."
    hide hajun_sigh

    show jungsik at right_bottom_offset
    jungsik "..."
    hide jungsik

    show jungsik_consider at right_bottom_offset
    jungsik "잠시만 하준아"
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "네? 왜요?"
    hide hajun

    show chapter3_2_2bg at center_image    

    show jungsik_surprised at right_bottom_offset
    jungsik "이거... 아까 봤던 최하람 아니냐?"
    hide jungsik_surprised
     

    show hajun_surprised at left_bottom_offset
    hajun "어? 잠시만"
    hide chapter3_2_2bg
    hajun "여기가 어디죠?"
    hide hajun_surprised

    show jungsik at right_bottom_offset
    jungsik "나 여기 어디인지 알아!"
    jungsik "내가 네비 찍을게. 얼른 이 장소로 가보자!"
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네! 바로 가보죠!"
    hide hajun

    scene black with fade

    "그렇게 우리는 실낱같은 정보를 가지고 뉴스에서 최하람이 찍힌 장소로 급하게 차를 타고 이동하였다."
    jump chapter3_3

label chapter3_3:

    scene chapter3_3bg with fade

    show hajun at left_bottom_offset
    hajun "찾았다.."
    hide hajun

    show hajun_frown at left_bottom_offset
    hajun "저 자식.. 사람을 죽여놓고 저렇게 태연하게.."
    hajun "웃는 얼굴로 사이비 종교를 전도하고 있다니"
    hajun "지금 바로 체포할까요?"
    hide hajun_frown

    show jungsik at right_bottom_offset
    jungsik "아니야, 기다려."
    hide jungsik

    show jungsik_consider at right_bottom_offset
    jungsik "저 녀석이 진짜 범인이라면 얼마 전 사건의 피해자가 마약을 가져온 장소도 알게 될 것 같지 않아?"
    hide jungsik_consider

    show jungsik at right_bottom_offset
    jungsik "그리고 쟤 혼자가 아니라 2명 이였다면서"
    jungsik "그럼 나머지 한 명도 잡을 수 있을거야."
    jungsik "몰래 미행하는 것도 나쁘지 않을 것 같아."
    hide jungsik

    show hajun_consider at left_bottom_offset
    hajun "하긴.. 만약에 진짜 저 녀석이 그 사람을 죽인 범인이라면 \n그 전에 있던 사건의 범인도 알게 되겠죠"
    hajun "그리고 사람을 아무렇지 않게 죽이고, 마약을 유통하는 곳도 알게 되겠죠."
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "하지만 저희가 헛짚은 거라면요?"
    hajun "저 녀석이 마약을 유통하던 곳의 사람이 아니라 그냥 구매자였다면요?"
    hide hajun
    
    show jungsik_consider at right_bottom_offset
    jungsik "그것도 그렇긴 하지.. 어떻게 해야할까?"
    hide jungsik_consider

    menu:
        "체포한다":
            jump chapter4_1
        "미행한다":
            jump chapter4_2
    