default saw_knife = False
default saw_drug = False
default saw_hair = False


label chapter3:
    show screen life_display
    scene black with fade
    "사건 조사를 끝낸 며칠 뒤"
    "국과수의 감식 결과가 나오게 되었다."
    play amb "amb_office.mp3" volume 0.5 loop
    scene chapter2_1bg with fade

    show jungsik at right_bottom_offset
    jungsik "하준아!"
    hide jungsik

    show jungsik_smile at right_bottom_offset
    jungsik "드디어 감식 결과가 나왔어!"
    hide jungsik_smile

    show hajun_smile at left_bottom_offset
    hajun "오 드디어 나왔대요?"
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

    play music "bgm_ch2_investigation.mp3" volume 2.0 fadein 1.0
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
            jungsik "그러니까, {i}{color=#803232}지문으로 용의자를 추적 할 수 없다{/i}{/color} 는 뜻이지."
            hide jungsik

            show hajun_consider at left_bottom_offset
            hajun "어떻게 지문이 등록되지 않을 수 있죠?"
            hide hajun_consider

            show jungsik_consider at right_bottom_offset
            jungsik "혹시나 하는 생각인데"
            jungsik "{i}{color=#803232}{size=32}어린 아이들{/size}{/color}{/i}   이 저지른 일이 아닐까 생각이 든다."
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
            jungsik "그 집에서 나왔던 주사기 말이야."
            jungsik "그거, 마약 맞는 것 같다. {i}{color=#803232}감식 결과, 모르핀{/color}{/i}이 나왔어."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "…진짜 마약이었던 거군요."
            with dissolve
            hide hajun

            show hajun_consider at left_bottom_offset
            hajun "그렇다면, 스마트폰에 저장된 거래 내역들…"
            hajun "{color=#6A5F55}전부 마약 거래{/color}였던 거네요."
            hide hajun_consider

            show jungsik_consider at right_bottom_offset
            jungsik "그래. 그렇게 봐야겠지."
            hide jungsik_consider

            show hajun_consider at left_bottom_offset
            hajun "그 피해자는 자신이 속해 있던 곳에서 {color=#6A5F55}마약을 빼돌렸고{/color}…"
            hajun "그걸로 {color=#6A5F55}돈을 벌려다{/color} 결국…"
            play sound "sfx_shake.mp3"
            hajun "{color=#803232}들킨 거군요. 조직의 사람들에게.{/color}" with hpunch
            hide hajun_consider

            show hajun_consider at left_bottom_offset
            hajun "그래서… {color=#803232}{cps=10}살해당했다.{/color}"
            hajun "……"
            hajun "점점 복잡해지네요."
            hide hajun_consider

            jump chapter3choice_check
        "머리카락":
            $ saw_hair = True

            show jungsik at right_bottom_offset
            jungsik "머리카락 감식 결과, {color=#6A5F55}일단 피해자의 것은 아니야{/color}."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "그럼, {i}{color=#6A5F55}그 머리카락의 주인{/color}{/i}이 용의자인 확률이 높겠네요."
            hide hajun

            show jungsik at right_bottom_offset
            jungsik "그렇지, 하지만 머리카락의 주인은..."
            hide jungsik

            show jungsik_consider at right_bottom_offset
            jungsik "{color=#803232}{i}{cps=20}아직 사춘기도 오지 않은 여자 아이와 남자 아이의 것이야.{/cps}{/i}{/color}"
            hide jungsik_consider

            show hajun_puzzled at left_bottom_offset
            hajun "{cps=15}네...?{/cps}"
            hajun "설마... {i}어린 아이들이 범인이라고 생각하시는 건가요?{/i}"
            hide hajun_puzzled

            show jungsik_consider at right_bottom_offset
            jungsik "일단은... 그렇게 의심하고 있어."
            hide jungsik_consider

            show hajun_consider at left_bottom_offset
            hajun "하지만 그 집을 예전에 방문한 아이들일 수도 있잖아요."
            hide hajun_consider

            show jungsik at right_bottom_offset
            jungsik "그래, 그래서 단정 지을 수도 없는거지."
            hide jungsik

            show hajun at left_bottom_offset
            hajun "제발... 우리가 생각하는 상황이 벌어지지 않았으면 좋겠네요."
            hide hajun

            show jungsik_consider at right_bottom_offset
            jungsik "...."
            hide jungsik_consider


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
    play sound "sfx_ch2_cctv.mp3"
    scene chapter3_1_1bg with fade

    show hajun_frown at left_bottom_offset
    hajun "흠… 화질을 아무리 개선해도, 얼굴은 또렷하게 안 보이네요..."
    hide hajun_frown

    show chapter3_1_1_ibg at center_image

    show hajun_surprised at left_bottom_offset
    play sound2 "sfx_shake.mp3"
    hajun "어? 잠시만..." with hpunch
    hide hajun_surprised

    show jungsik_sigh at right_bottom_offset
    jungsik "{cps=10}..."
    hide jungsik_sigh

    show hajun at left_bottom_offset
    hajun "{cps=10}..."
    hide hajun

    show hajun_surprised at left_bottom_offset
    hajun "잠시만.. 설마 범행 시각 때 왔다 갔다 했던 게..."
    hajun "{size=40}{i}{color=#803232}진짜 어린 아이들이라구요?{/size}{i}{/color}" with hpunch
    hide hajun_surprised

    show jungsik_sigh at right_bottom_offset
    jungsik "설마설마 했는데.."
    jungsik "진짜 어린 아이들이었을 줄이야.."
    hide jungsik_sigh

    show jungsik_consider at right_bottom_offset
    jungsik "{size=35}{i}{color=#803232}{cps=10}그것도 하나가 아니라 둘이나...{/size}{/i}{/color}"
    hide jungsik_consider

    hide chapter3_1_1_ibg

    show hajun_puzzled at left_bottom_offset
    hajun  "{color=#803232}{i}그럼 지문이 등록되지 않은 이유도,{/i}{/color}"
    extend "\n{color=#803232}{i}그 집에서 어린 아이들의 머리카락이 나온 이유도...{/i}{/color}"
    hide hajun_puzzled

    show jungsik_consider at right_bottom_offset
    jungsik "범인이 어린 아이들이였기 때문이지."
    hide jungsik_consider

    show hajun at left_bottom_offset
    hajun "그럼 우리가 해야 할 일은 이 DNA를 통해 \n아이들을 찾아내는 것이 네요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그렇지.. 일단 이 아이들의 부모가 누군지부터 확인해야겠네."
    stop music fadeout 2.0
    stop amb fadeout 1.0
    scene black with fade    

    play amb "amb_office.mp3" fadein 2.0
    "그렇게 이틀이 지나고, 우리는 DNA대조 기술을 통해\n아이들 부모를 찾아냈다."
    scene chapter2_1bg with fade

    show hajun at left_bottom_offset
    hajun "그럼, 전화 해볼게요."
    hide hajun

    show jungsik at right_bottom_offset
    jungsik "그래."
    hide jungsik
    
    play sound "sfx_calling.mp3"
    pause (2.0)


    hajun "..."
    jungsik "..."

    play sound "sfx_ch2_click_phone.mp3"
    $ renpy.music.set_volume(0.1, channel='amb')
    play music "bgm_ch3_parents.mp3" volume 0.7
    show parents at right_bottom_offset
    parents "여보세요?"
    hide parents

    show hajun at left_bottom_offset
    hajun "네 안녕하세요."
    hajun "저는 달묘 경찰서 강력 1반 박하준입니다."
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
    parents "이혼하면서 애들을 {i}{color=#803232}보육원{/i}{/color}    에 맡겼거든요."
    hide parents

    show hajun at left_bottom_offset
    hajun "보육원이라면 어디 보육원인지 여쭤봐도 될까요?"
    hajun "정말 중요합니다."
    hide hajun

    show parents at right_bottom_offset
    parents "하.."
    parents "{i}{color=#803232}새벽나무 보육원{/i}{/color}    이요."
    parents "저한테는 피해가 안끼치는거죠?"
    parents "이젠 얼굴도 가물가물한 아이들인데.."
    hide parents

    show hajun_consider at left_bottom_offset
    hajun "그건 모르는 일이죠.."
    hajun "혹시 보육원으로 보내신 아이들의 이름이 어떻게 될까요?"
    hide hajun_consider

    show parents at right_bottom_offset
    parents "{cps=5}......"
    parents "{i}{color=#803232}최민재와 최하람이에요.{/i}{/color}"
    parents "이젠 더 이상 물어보실 것 없으시죠?"
    parents "귀찮으니까 전화는 삼가해주세요. 제발"
    hide parents
    play sound "sfx_ch2_click_phone.mp3"

    play sound2 "sfx_shake.mp3"
    show hajun_angry at left_bottom_offset
    hajun "잠시만요! 저기요!" with hpunch
    hide hajun_angry

    show hajun_puzzled at left_bottom_offset
    hajun "끊었네.."
    hide hajun_puzzled

    show jungsik at right_bottom_offset
    jungsik "됐어, 우리가 알아야 될 정보는 이정도면 충분해"
    jungsik "그럼 새벽나무 보육원으로 가보자."
    jungsik "거기에 우리가 필요한 정보가 있을지도 몰라."
    hide jungsik

    show hajun at left_bottom_offset
    hajun "네. 그럼 보육원으로 가시죠."
    hide hajun

    scene black with fade

    play sound "sfx_ch1_man_walk.mp3"
    "그렇게 나와 종식이 형은 아이들의 정보를 얻기 위해\n새벽나무 보육원으로 발걸음을 옮겼다."
    stop music fadeout 2.0
    stop amb fadeout 1.0
    jump chapter3_2

label chapter3_2:
    play music "bgm_ch3_child.mp3" volume 0.7
    play amb "amb_outside.mp3"
    scene chapter3_1 with fade

    show hajun at left_bottom_offset
    hajun "여기가 새벽나무 보육원.."
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
    babyfarmer " {color=#6A5F55}{i}여기를 몰래 나가{/color}{/i} {i}{color=#803232}어디론가 가버렸습니다.{/color}{/i}"
    babyfarmer "경찰에 신고를 해도 여기 주위가 워낙 낡은 동네라서 cctv도 잘 없거든요."
    hide babyfarmer_low

    show hajun_puzzled at left_bottom_offset
    hajun "몰래 여기를 빠져나갔다구요?"
    hide hajun_puzzled

    show hajun at left_bottom_offset
    hajun "{i}{color=#803232}이유는 파악이 되나요?{/color}{/i} "
    hide hajun

    play sound "sfx_shake.mp3" volume 0.2 fadein 0.3
    show babyfarmer_flustered at right_bottom_offset
    babyfarmer "...!" with hpunch
    pause (2.0  )
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
    play sound "sfx_ch2_flippage.mp3"
    window hide
    show chapter3_2_1bg at center_image
    hide babyfarmer
    pause(5.0)
    hide chapter3_2_1bg

    show hajun at left_bottom_offset
    hajun "이 정도면 저희가 원하는 정보는 이게 끝인 것 같습니다."
    hajun "수사에 응해주셔서 감사합니다."
    hide hajun
    
    show babyfarmer at right_bottom_offset
    babyfarmer "별말씀을요."
    babyfarmer "{color=#803232}{i}꼭 아이들을 찾아주세요.{/i}{/color}"
    hide babyfarmer

    show hajun at left_bottom_offset
    hajun "네, 수고하십시오."
    hide hajun
    
    play sound "sfx_ch1_man_walk.mp3"
    stop music fadeout 2.0
    stop amb fadeout 1.0
    scene chapter3_3bg with fade
    play amb "amb_car.mp3" fadein 1.0
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

    show jungsik_puzzled at right_bottom_offset
    play sound "sfx_shake.mp3" volume 0.5
    jungsik "{color=#803232}{i}잠시만 하준아{/i}{/color}" with hpunch
    hide jungsik_puzzled
    play music "bgm_ch3_tension.mp3" volume 0.7 

    show hajun at left_bottom_offset
    hajun "네? 왜요?"
    hide hajun

    show chapter3_2_2bg at center_image    

    play sound2 "sfx_ch2_investigation.mp3"
    show jungsik_surprised at right_bottom_offset
    jungsik "{color=#803232}{i}{cps=10}이거... {cps=20}{size=40}아까 봤던 최하람 아니냐?{/size}{/i}{/color}"
    hide jungsik_surprised
     

    show hajun_surprised at left_bottom_offset
    play sound "sfx_shake.mp3" volume 0.5
    hajun "어? 잠시만" with hpunch
    hajun "여기가 어디죠?"
    hide hajun_surprised
    hide chapter3_2_2bg

    show jungsik_panic at right_bottom_offset
    jungsik "나 여기 어디인지 알아!"
    jungsik "내가 네비 찍을게.   "
    extend "{color=#803232}{i}얼른 이 장소로 가보자!{/i}{/color}"
    hide jungsik_panic

    show hajun at left_bottom_offset
    hajun "네! 바로 가보죠!"
    hide hajun

    play sound "sfx_ch2_car_ignition.ogg"
    scene black with fade

    "그렇게 우리는 실낱같은 정보를 가지고\n{color=#803232}{i}뉴스 속 최하람이 발견된 장소로{/i}{/color}    급하게 차를 타고 이동하였다."
    jump chapter3_3

label chapter3_3:

    scene chapter3_3bg with fade

    show hajun at left_bottom_offset
    hajun "{i}찾았다...{/i}"
    hide hajun

    show hajun_frown at left_bottom_offset
    hajun "{color=#803232}저 자식...{/color}"
    extend "       {i}{color=#803232}사람을 죽여놓고 저렇게 태연하게...{/color}{/i}"
    hajun "{color=#803232}{size=36}웃는 얼굴로 사이비 종교를 전도하고 있다니{/size}{/color}"
    hajun "지금 바로 체포할까요?"
    hide hajun_frown

    play sound "sfx_shake.mp3" volume 0.5
    show jungsik_consider at right_bottom_offset
    jungsik "{i}아니야, 기다려.{/i}" with hpunch
    hide jungsik_consider

    show jungsik_consider at right_bottom_offset
    jungsik "{color=#6A5F55}저 녀석이 진짜 범인이라면{/color}"
    extend "\n얼마 전 사건의 피해자가 마약을 가져온 장소도 알게 될 것 같지 않아?"
    hide jungsik_consider

    show jungsik_consider at right_bottom_offset
    jungsik "{color=#6A5F55}그리고 저 아이 혼자가 아니라 2명 이였다면서{/color}"
    jungsik "{i}그럼 나머지 한 명도 잡을 수 있을 거야.{/i}"
    jungsik "{color=#6A5F55}몰래 미행하는 것도 나쁘지 않을 것 같아.{/color}"
    hide jungsik_consider

    show hajun_consider at left_bottom_offset
    hajun "하긴... 만약에 진짜 {color=#803232}저 녀석이 그 사람을 죽인 범인{/color}이라면\n그 전에 있던 사건의 범인도 알게 되겠죠."
    hajun "그리고 {color=#803232}마약을 유통한 장소까지도{/color}   알게 되겠죠."
    hide hajun_consider

    show hajun at left_bottom_offset
    hajun "하지만 {color=#6A5F55}저희가 헛짚은 거라면요?{/color}"
    hajun "{i}저 녀석이 마약을 유통하던 곳의 사람이 아니라{/i}"
    hajun "{i}{color=#803232}그저 단순한...  {/color}{/i}"
    extend "{i}{color=#803232}{size=36}구매자였다면요?{/size}  {/color}{/i}"
    hide hajun

    show jungsik_consider at right_bottom_offset
    jungsik "그것도 그렇긴 하지... {color=#6A5F55}어떻게 해야 할까?{/color}"
    hide jungsik_consider

    menu:
        "체포한다":
            jump chapter4_1
        "미행한다":
            jump chapter4_2
