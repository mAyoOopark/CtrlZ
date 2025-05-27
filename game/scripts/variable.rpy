# 배경
image chapter1_1bg = "chapter1_1.png"
image chapter1_2bg = "chapter1_2.png"
image chapter1_3bg = "chapter1_3.png"
image chapter1_4bg = "chapter1_4.png"
image chapter1_4_1bg = "chapter1_4_1.png"
image chapter1_4_1_2bg = "chapter1_4_1_2.png"
image chapter1_4_2bg = "chapter1_4_2.png"
image chapter1_4_2_Abg = "chapter1_4_2_A.png"
image chapter1_4_3bg = "chapter1_4_3.png"
image chapter1_4_3_1bg = "chapter1_4_3_1.png"
image chapter1_5bg = "chapter1_5.png"
image chapter1_5_1bg = "chapter1_5_1.png"
image chapter1_5_2bg = "chapter1_5_2.png"
image chapter1_5_3bg = "chapter1_5_3.png"
image chapter1_5_4bg = "chapter1_5_4.png"
image chapter1_5_5bg = "chapter1_5_5.png"
image chapter1_6bg = "chapter1_6.png"
image chapter1_7bg = "chapter1_7.png"
image chapter1_8bg = "chapter1_8.png"
image chapter1_9bg = "chapter1_9.png"

image chapter2_1bg = "chapter2_1.png"
image chapter2_1_1bg = "chapter2_1_1.png"
image chapter2_2bg = "chapter2_2.png"
image chapter2_2_1bg = "chapter2_2_1.png"
image chapter2_2_2bg = "chapter2_2_2.png"

image chapter3_1bg = "chapter3_1.png"
image chapter3_1_1bg = "chapter3_1_1.png"
image chapter3_1_1_ibg = "chapter3_1_1_i.png"
image chapter3_2_1bg = "chapter3_2_1.png"
image chapter3_2_2bg = "chapter3_2_2.png"
image chapter3_3bg = "chapter3_3.png"
image chapter4_1bg = "chapter4_1.png"
image chapter4_1_1bg = "chapter4_1_1.png"
image chapter4_1_3bg = "chapter4_1_3.png"
image chapter4_1_3_1bg = "chapter4_1_3_1.png"
image chapter4_1_4bg = "chapter4_1_4.png"



# 이미지
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
image hajun_laugh = "hajun_laugh.png"
image hajun_frown = "hajun_frown.png"
image hajun_sigh = "hajun_sigh.png"


image jungsik = "jungsik.png"
image jungsik_angry = "jungsik_angry.png"
image jungsik_consider = "jungsik_consider.png"
image jungsik_despair = "jungsik_despair.png"
image jungsik_puzzled = "jungsik_puzzled.png"
image jungsik_surprised = "jungsik_surprised.png"
image jungsik_sad = "jungsik_sad.png"
image jungsik_smile = "jungsik_smile.png"
image jungsik_sigh = "jungsik_sigh.png"

image dohyeon_asd = "dohyeon_asd.png"
image dohyeon_angry = "dohyeon_angry.png"
image dohyeon_frown = "dohyeon_frown.png"
image dohyeon_surprised = "dohyeon_surprised.png"
image dohyeon_hammer = "dohyeon_hammer.png"

image parents = "parents.png"

image babyfarmer = "babyfarmer.png"
image babyfarmer_flustered = "babyfarmer_flustered.png"
image babyfarmer_low = "babyfarmer_low.png"

image haram = "haram.png"
image haram_flustered = "haram_flustered.png"
image haram_low = "haram_low.png"
image haram_teeth = "haram_teeth.png"
image haram_angry = "haram_angry.png"

image minjae = "minjae.png"

# 캐릭터
define hajun = Character("박하준")
define jungsik = Character("남종식")
define dohyeon = Character("최도현")
define asd = Character("???")
define parents = Character("아이들 부모")
define babyfarmer = Character("보육원장")
define haram = Character("최하람")
define minjae = Character("최민재")
# 오디오


# 화면효과
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
    xpos 50
    ypos 1.0
    xanchor 0.0
    yanchor 1.0

transform right_bottom_offset:     # 캐릭터를 오른쪽 아래에 위치
    xpos 1600
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

transform center_image:
    xalign 0.5
    yalign 0.4