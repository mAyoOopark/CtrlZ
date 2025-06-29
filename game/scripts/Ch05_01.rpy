label chapter5_1:
    show screen life_display
    scene chapter5_1bg with fade
    stop music fadeout 1.0   
    stop amb fadeout 1.0
    play music "bgm_ch5_1_fades.mp3" fadeout 1.0   
    play amb "amb_city.mp3" fadein 1.0 volume 0.1

    show hajun_angry at left_bottom_offset
    hajun "이대로 도망치기만 하면 너만 손해일 뿐이야!"
    hide hajun_angry

    show hajun_smile at left_bottom_offset
    hajun "드디어 잡았네, 최민재"
    hide hajun_smile

    show hajun_hard at left_bottom_offset
    hajun "젊어서 그런가 진짜 빠르네"
    hajun "어우 힘들어"
    hide hajun_hard

    show hajun at left_bottom_offset
    hajun "그래도 할 건 해야지?"
    hajun "최민재 너를 살인 혐의로 체포한다."
    play sound "sfx_handcuff.mp3"
    hajun "너는 묵비권을 행사 할 수 있고, 변호사를 선임 할 수 있으며,\n   모든 발언은 법정에서 불리하게 작용할 수 있다."
    hajun "자 서로 가서 알고 있는 것 다 말해야 할거야."
    hide hajun

    show minjae_angry at right_bottom_offset
    play sound "sfx_shake.mp3" volume 0.7
    minjae "이거 놔! 놓으라고!" with hpunch
    hide minjae_angry

    show minjae_hard at right_bottom_offset
    minjae "너희들이 뭘 알아! 우리가 어떤 취급을 받았는지.."
    minjae "지금까지 아무것도 안한 어른들이 우리를... 이제와서..?"
    pause (1.0)
    hide minjae_hard

    scene chapter4_1_1bg with fade
    stop music fadeout 1.0   
    stop amb fadeout 1.0
    play amb "amb_room.mp3" fadein 1.0
    "그 후, 박하준은 최민재를 데리고 경찰서로 왔다."
    "선배가 건물에 있던 아이들을 보호하고\n간단한 조사 후에 보육 시설에 나눠서 보냈다고 했다."
    "최민재를 조사하던 중, 아이들의 배후에\n최도현이 있었다는 것을 알게 되었지만,"
    "이미 해외로 도망쳐 추적이 힘들었다"
    "최민재는 촉법 소년이였기 때문에 조사 후\n  지속적으로 감시를 받으며 보육 시설에 보내질 예정이었다."

    pause(1.0)
    scene black with fade
    pause(1.0)
    "하지만,"
    play sound "sfx_hb.mp3" loop
    scene chapter3_1bg with fade
    
    play music "bgm_ch5_1_tragic.mp3" fadeout 1.0
    stop amb fadeout 1.0
    play amb "amb_outside.mp3" fadein 1.0 volume 0.3
    show minjae_hard at right_bottom_offset
    minjae "흐.. 흐하.... 하아.."
    minjae "아무도.. 믿을 수 없어.. 도현 아저씨도 우리를 버렸고.."
    hide minjae_hard
    show minjae at right_bottom_offset
    minjae "내가.. {i}{size=40}{color=#803232}새로운 교주{/i}{/size}{/color}가 되는거야.."
    hide minjae
    scene black with fade

    "민재는 보육 시설의 사람들 몇 명을 죽이고\n보육 시설을 조용히 빠져나갔다."
    "그 후, 각각 다른 시설에 보낸 아이들이\n  하나 둘 씩 실종되었다는 소식이 들려왔다.."
    "과연 아이들은 어디로 사라진 것인가.."
    pro "\n Bad End 1 : 새로운 시작"

    scene black with fade
    
    stop music fadeout 2.0   
    stop amb fadeout 2.0
    pause(1.0)
    return