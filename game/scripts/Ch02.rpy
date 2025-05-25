label chapter2_1:
    scene black
    "최도현 사건으로부터 8년 후"
    "나와 종식이 형은 그 사건을 마무리 짓기위해 \n화재가 진압 된 후 끝까지 조사하여 쫓아봤지만"
    "하얀 재가 되버린 폐허 안에서는 마땅 할 증거는 찾아 볼 수 없었고"
    "최도현의 행방마저 불에 탄 듯이 없어졌기에 \n우리는 최도현을 화재로 인한 사망으로 처리를 할 수 밖에 없었다."
    show chapter2_1bg with fade
    show hajun_determind at left_bottom_offset
    python:
        typewriter_effect_who(hajun, "......", cps=30)
    hide hajun_determind

    show hajun_determind at right_bottom_offset
    jungsik "......"
    hide hajun_determind

    show hajun_angry at left_bottom_offset
    hajun ".....!"
    hide hajun_angry
    return