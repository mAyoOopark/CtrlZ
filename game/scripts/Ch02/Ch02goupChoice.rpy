label chapter2_6_group_choice:

    "선택지 그룹 게임을 시작합니다!"
    $ found_groups = []
    $ selections = []
    $ update_choices()
    call screen choose_items

    return


init python:
    import random

    choice_groups = {
        "group1": ["칼", "시신"],
        "group2": ["피 글자", "교리서적"],
        "group3": ["주사기", "핸드폰", "일기장"]
    }

    decoy_items = ["머리카락"]  # 방해용 오답

    all_items = []  # 표시될 선택지
    selections = []  # 플레이어가 선택한 것

    def toggle_selection(item):
        if item in selections:
            selections.remove(item)
        else:
            selections.append(item)

    def validate_selection():
        for group_name, items in choice_groups.items():
            if all(item in items for item in selections) and len(selections) in [2, 3] and group_name not in found_groups:
                found_groups.append(group_name)
                selections.clear()
                renpy.call_in_new_context("story_" + group_name)
                return
        selections.clear()
        renpy.call_in_new_context("retry_choice")

    def update_choices():
        global all_items
        active_items = []

        # 이미 찾은 그룹 제외
        for group, items in choice_groups.items():
            if group not in found_groups:
                active_items.extend(items)

        # 오답 아이템 포함
        active_items += decoy_items
        random.shuffle(active_items)
        all_items = active_items


screen choose_items():
    tag menu

    frame:
        align (0.5, 0.5)
        padding (30, 30)
        background "#202020AA"
        has vbox:
            spacing 20
            align (0.5, 0.5)

        text "2-3개의 관련된 항목을 선택하세요:" size 32

        vbox:
            spacing 10
            for i in range(0, len(all_items), 3):
                hbox:
                    spacing 10
                    for item in all_items[i:i+3]:
                        textbutton item:
                            action Function(toggle_selection, item)
                            selected item in selections
                            xsize 200
                            ysize 60

        text "선택됨: [selections]" size 24 color "#FFFFFF" xalign 0.5

        hbox:
            spacing 30
            xalign 0.5

            if 2 <= len(selections) <= 3:
                textbutton "확인":
                    action Function(validate_selection)
                    xsize 150
                    ysize 50

            textbutton "취소":
                action Function(selections.clear)
                xsize 150
                ysize 50


label retry_choice:
    
    show hajun_sigh at left_bottom_offset
    hajun "아니야. 전혀 정리가 되지 않아."
    hajun "뭐지? 어디서부터 잘못된거야? 전혀 이야기가 되지 않아."
    hide hajun_sigh
    $ update_choices()
    call screen choose_items
    return


label choice_menu:
    if len(found_groups) == 3:
        jump chapter2_7
    $ update_choices()
    call screen choose_items
    return


label story_group1:
    show hajun_serious at left_bottom_offset
    hajun "아마 이 칼로 피해자를 죽였겠지. 아주 잔인하게. 사인은 과다출혈로 인한 쇼크사인 것 같아."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "그리고 이 범행 수법은 얼마 전에 주택에서 일어났던 살인사건과 똑같아,"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "찌르고, 베고 수십 번을 반복한 것과 의자에 포박하여 고문하듯이 죽인 것이 말이야."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "아마도, 두 사건 다 동일인물인 것이 확실해. 일어난 지 얼마 뒤에 또 일어난 걸 보면 말이야."
    hide hajun_serious
    call choice_menu from _call_choice_menu
    return

label story_group2:
    
    show hajun at left_bottom_offset
    hajun "집에 있는 교리서적 그리고 종교적 의미를 담고 있는 피로 쓰인 글씨. 아마도 종교살인이 아닐까?"
    hide hajun

    show hajun at left_bottom_offset
    hajun "지금이 21세기인데 한국에서 종교 살인이라니…"
    hide hajun

    show hajun at left_bottom_offset
    hajun "아마도 종교인이 살해한 것으로 보여. 하지만 대체 어떤 사이비 종교길래 이런 방식으로 살인을 저지른 거지?"
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "결코 평범한 사이비 종교는 아니야. 매우 수상해."
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "그리고 이 범행 수법은 얼마 전에 주택에서 일어났던 살인사건과 똑같아,"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "'주께선 너를 아셨으나, 네가 주를 부인하였도다.'라니… 그럼 피해자는 이 종교에 몸담았다가, 이단 짓을 벌였다는 것인가?"
    hide hajun_serious

    show hajun_serious at left_bottom_offset
    hajun "그리고 이 교리서적, 저번에 수사했던 집에서도 있었지. 이것 또한 연관되어 있는 증거라고 볼 수 있어."
    hide hajun_serious
    call choice_menu from _call_choice_menu_1
    return

label story_group3:
    show hajun at left_bottom_offset
    hajun "일기장의 내용으로 봐서는 어떤 곳에서 훔쳐온 이 주사기, 즉 마약으로 사람들에게 판 것 같아."
    hide hajun

    show hajun at left_bottom_offset
    hajun "그리고, 훔쳐온 곳의 사람들에게서 죽은 것 같아."
    hide hajun

    show hajun at left_bottom_offset
    hajun "그렇지만 그냥 죽인 것도 아니고 이렇게 고통스럽게… 이럴 만한 이유가 있을까..?"
    hide hajun

    show hajun_serious at left_bottom_offset
    hajun "이 마약 때문에 죽일 정도라면, 절대 작은 단체일 수는 없을 거야. 아마도 매우 큰 단체일 것이 분명하지."
    hide hajun_serious
    call choice_menu from _call_choice_menu_2
    return

