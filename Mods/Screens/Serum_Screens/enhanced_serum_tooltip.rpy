init -1:
    python:
        def serum_rename_func(new_name):
            cs = renpy.current_screen()
            cs.scope["the_serum"].name = new_name


init 2:
    screen serum_tooltip(the_serum, set_x_align = 0.9, set_y_align = 0.1):
        frame:
            background "#888888"
            xalign set_x_align
            yalign set_y_align
            yanchor 0.0
            xsize 500
            ysize 900
            vbox:
                xalign 0.5
                spacing 10
                button:
                    id "serum_rename_id"
                    selected

                    style "serum_textbutton_style_header"
                    xalign 0.5
                    xsize 480

                    action NullAction()

                    add Input(
                    size =  24,
                    color = "#dddddd",
                    default = the_serum.name,
                    changed = serum_rename_func,
                    length = 25,
                    button = renpy.get_widget("serum_tooltip", "serum_rename_id")
                    ) xalign 0.5

                    unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors

                frame:
                    background "#777777"
                    xalign 0.5
                    xsize 480
                    ysize 150
                    vbox:
                        hbox:
                            spacing 5
                            vbox:
                                spacing 5
                                frame:
                                    background "#000080"
                                    xsize 225
                                    text "Research Required: {color=98fb98}[the_serum.research_needed]{/color}" style "serum_text_style_traits"

                                frame:
                                    background "#000080"
                                    xsize 225
                                    text "Production Cost: {color=#cd5c5c}[the_serum.production_cost]{/color}" style "serum_text_style_traits"

                                frame:
                                    background "#000080"
                                    xsize 225
                                    text "Value: $[the_serum.value]" style "serum_text_style_traits"

                            vbox:
                                spacing 5
                                $ calculated_profit = (the_serum.value*mc.business.batch_size)-the_serum.production_cost
                                if calculated_profit > 0:
                                    frame:
                                        background "#000080"
                                        xsize 225
                                        text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style_traits"
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    frame:
                                        background "#000080"
                                        xsize 225
                                        text "Expected Profit:{color=#cd5c5c} -$[calculated_profit]{/color}" style "serum_text_style_traits"

                                frame:
                                    background "#000080"
                                    xsize 225
                                    text "Duration: [the_serum.duration] Turns" style "serum_text_style_traits"

                                if renpy.get_screen("review_designs_screen"): #Make it so you have to be in the review screen to edit things (still need to protect already created serum somehow)
                                    textbutton "Edit Serum":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        xsize 225
                                        action Show("serum_design_ui", None, the_serum, the_serum.traits)

                frame:
                    background "#777777"
                    xalign 0.5
                    xsize 480
                    if the_serum.side_effects:
                        ysize 450
                    else:
                        ysize 650

                    viewport:
                        scrollbars "vertical"
                        xsize 480
                        mousewheel True
                        vbox:
                            spacing 5
                            for trait in the_serum.traits:
                                frame:
                                    background "#000080"
                                    xsize 480
                                    text trait.name style "serum_text_style"

                                hbox:
                                    spacing 5
                                    frame:
                                        background "#007000"
                                        xsize 225
                                        text "[trait.positive_slug]" style "serum_text_style_traits"

                                    frame:
                                        background "#930000"
                                        xsize 225
                                        text "[trait.negative_slug]" style "serum_text_style_traits"

                if the_serum.side_effects:
                    frame:
                        background "#000080"
                        xsize 480
                        text "Side Effects:" style "serum_text_style"

                    frame:
                        background "#777777"
                        xalign 0.5
                        xsize 480
                        viewport:
                            scrollbars "vertical"
                            xsize 480
                            mousewheel True
                            vbox:
                                spacing 5
                                for side_effect in the_serum.side_effects:
                                    frame:
                                        background "#000080"
                                        xsize 480
                                        text side_effect.name style "serum_text_style_traits"

                                    frame:
                                        background "#930000"
                                        xsize 480
                                        text "[side_effect.negative_slug]" style "serum_text_style_traits"
