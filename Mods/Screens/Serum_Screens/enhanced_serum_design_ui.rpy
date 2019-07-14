init 2:
    screen serum_design_ui(starting_serum,current_traits):
        add "Science_Menu_Background.png"
        default trait_tooltip = primitive_serum_prod
        python:
            effective_traits = 0
            for trait_count in starting_serum.traits:
                if not "Production" in trait_count.exclude_tags:
                    effective_traits += 1
        hbox:
            yalign 0.15
            xanchor 0.5
            xalign 0.5
            xsize 1080
            spacing 20
            frame:
                background "#888888"
                ysize 800


                vbox:
                    xsize 530
                    frame:
                        background "#000080"
                        xsize 530
                        text "Pick Production Type" style "serum_text_style_header"

                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 300

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                    if trait not in starting_serum.traits and trait.researched and "Production" in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = " - "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "{color=#d38c19}[[" + a_tag + "]{/color}"
                                        $ trait_allowed = True
                                        python: # Check to see if the trait is excluded by any of the traits currently in the serum. A long looped segment only to deal with lists of tags, which are unlikely.
                                            for checking_trait in starting_serum.traits:
                                                for tag in trait.exclude_tags:
                                                    for checking_tag in checking_trait.exclude_tags:
                                                        if tag == checking_tag:
                                                            trait_allowed = False

                                        $ trait_side_effects = str(trait.get_effective_side_effect_chance()) # Put this section into a function?

                                        if trait.get_effective_side_effect_chance() >= 60: # Red (Color code the side effect risk for quicker identification)
                                            $ trait_side_effects_text = "{color=#cd5c5c}[trait_side_effects]{/color}"

                                        elif trait.get_effective_side_effect_chance() >= 20: # Yellow
                                            $ trait_side_effects_text = "{color=#eee000}[trait_side_effects]{/color}"

                                        else: # Green
                                            $ trait_side_effects_text = "{color=#98fb98}[trait_side_effects]{/color}"


                                        $ trait_mastery_level = str(trait.mastery_level)

                                        if trait.mastery_level <= 10: # Red
                                            $ trait_mastery_text = "{color=#cd5c5c}[trait_mastery_level]{/color}"
                                        elif trait.mastery_level <= 50: # Yellow
                                            $ trait_mastery_text = "{color=#eee000}[trait_mastery_level]{/color}"
                                        else: # Green
                                            $ trait_mastery_text = "{color=#98fb98}[trait_mastery_level]{/color}"

                                        textbutton trait.name + trait_tags + "\nMastery Level: " + trait_mastery_text + " | " + "Side Effect Chance: " + trait_side_effects_text + " %":
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 530

                                            sensitive trait_allowed

                                            action [
                                            Function(starting_serum.add_trait,trait)
                                            ]



                                            hovered [
                                            SetScreenVariable("trait_tooltip", trait)
                                            ]

                                            #unhovered [
                                            #Hide("trait_tooltip")
                                            #]
                    frame:
                        background "#000080"
                        xsize 530
                        text "Add Serum Traits" style "serum_text_style_header"
                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 375

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True

                            vbox:


                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                    if trait not in starting_serum.traits and trait.researched and "Production" not in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = " - "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[[" + a_tag + "]"
                                        $ trait_allowed = True
                                        python: # Check to see if the trait is excluded by any of the traits currently in the serum. A long looped segment only to deal with lists of tags, which are unlikely.
                                            for checking_trait in starting_serum.traits:
                                                for tag in trait.exclude_tags:
                                                    for checking_tag in checking_trait.exclude_tags:
                                                        if tag == checking_tag:
                                                            trait_allowed = False

                                        $ trait_side_effects = str(trait.get_effective_side_effect_chance()) # Put this into a function?

                                        if trait.get_effective_side_effect_chance() >= 60: # Red (Color code the side effect risk for quicker identification)
                                            $ trait_side_effects_text = "{color=#cd5c5c}[trait_side_effects]{/color}"

                                        elif trait.get_effective_side_effect_chance() >= 20: # Yellow
                                            $ trait_side_effects_text = "{color=#eee000}[trait_side_effects]{/color}"

                                        else: # Green
                                            $ trait_side_effects_text = "{color=#98fb98}[trait_side_effects]{/color}"


                                        $ trait_mastery_level = str(trait.mastery_level)

                                        if trait.mastery_level <= 10: # Red
                                            $ trait_mastery_text = "{color=#cd5c5c}[trait_mastery_level]{/color}"
                                        elif trait.mastery_level <= 50: # Yellow
                                            $ trait_mastery_text = "{color=#eee000}[trait_mastery_level]{/color}"
                                        else: # Green
                                            $ trait_mastery_text = "{color=#98fb98}[trait_mastery_level]{/color}"

                                        textbutton trait.name + trait_tags + "\nMastery Level: " + trait_mastery_text + " | " + "Side Effect Chance: " + trait_side_effects_text + " %":
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 530

                                            sensitive trait_allowed

                                            action [

                                            Function(starting_serum.add_trait,trait)
                                            ]



                                            hovered [
                                            SetScreenVariable("trait_tooltip", trait)
                                            ]

                                            #unhovered [
                                            #Hide("trait_tooltip")
                                            #]
            frame:
                background "#888888"
                ysize 800
                vbox:
                    frame:
                        background "#000080"
                        xsize 530
                        text "Remove a trait" style "serum_text_style_header"

                    frame:
                        background "#666666"
                        xalign 0.5
                        xsize 530
                        ysize 450
                        viewport:

                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in starting_serum.traits:
                                    $ trait_tags = ""
                                    if trait.exclude_tags:
                                        $ trait_tags = " - "
                                        for a_tag in trait.exclude_tags:
                                            $ trait_tags += "[[" + a_tag + "]"
                                    $ trait_side_effects = str(trait.get_effective_side_effect_chance()) # Put this into a function?

                                    if trait.get_effective_side_effect_chance() >= 60: # Red (Color code the side effect risk for quicker identification)
                                        $ trait_side_effects_text = "{color=#cd5c5c}[trait_side_effects]{/color}"

                                    elif trait.get_effective_side_effect_chance() >= 20: # Yellow
                                        $ trait_side_effects_text = "{color=#eee000}[trait_side_effects]{/color}"

                                    else: # Green
                                        $ trait_side_effects_text = "{color=#98fb98}[trait_side_effects]{/color}"


                                    $ trait_mastery_level = str(trait.mastery_level)

                                    if trait.mastery_level <= 10: # Red
                                        $ trait_mastery_text = "{color=#cd5c5c}[trait_mastery_level]{/color}"
                                    elif trait.mastery_level <= 50: # Yellow
                                        $ trait_mastery_text = "{color=#eee000}[trait_mastery_level]{/color}"
                                    else: # Green
                                        $ trait_mastery_text = "{color=#98fb98}[trait_mastery_level]{/color}"

                                    textbutton trait.name + trait_tags + "\nMastery Level: " + trait_mastery_text + " | " + "Side Effect Chance: " + trait_side_effects_text + " %":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 520

                                        action[
                                        Function(starting_serum.remove_trait,trait)
                                        ]

                                        hovered [
                                        SetScreenVariable("trait_tooltip", trait)
                                        ]

                                        #unhovered Hide("trait_tooltip")


                    vbox:
                        frame:
                            background "#000080"
                            xsize 530
                            text "Trait Information: [trait_tooltip.name]" style "serum_text_style_header"

                        frame:
                            background "#666666"
                            xsize 530
                            xalign 0.5
                            viewport:
                                draggable True
                                xsize 530
                                mousewheel "vertical"
                                vbox:
                                    spacing 5
                                    hbox:
                                        spacing 5
                                        vbox:
                                            frame:
                                                background "#007000"
                                                xsize 255
                                                text "[trait_tooltip.positive_slug]" style "serum_text_style"
                                        vbox:
                                            frame:
                                                background "#930000"
                                                xsize 255
                                                text "[trait_tooltip.negative_slug]" style "serum_text_style"
                                    hbox:
                                        frame:
                                            background "#000080"
                                            xsize 515
                                            text "[trait_tooltip.desc]" style "serum_text_style"

            frame:
                background "#888888"
                ysize 800
                vbox:
                    xsize 550
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 550
                        text "Current Serum Statistics:" style "serum_text_style_header"

                    frame:
                        if effective_traits > starting_serum.slots:
                            background "#930000"
                        else:
                            background "#000080"
                        xsize 550
                        text "Trait Slots: " + str(effective_traits) +"/[starting_serum.slots]" style "serum_text_style"

                    viewport:
                        draggable True
                        xsize 550
                        ysize 50
                        mousewheel "horizontal"
                        hbox:
                            xanchor 0.5
                            xalign 0.5
                            spacing 10
                            xsize 550
                            for num in __builtin__.range(__builtin__.max(starting_serum.slots,effective_traits)):
                                if num < effective_traits and num < starting_serum.slots:
                                    add "Serum_Slot_Full.png" xanchor 0.5 xalign 0.5
                                elif num < effective_traits and num >= starting_serum.slots:
                                    add "Serum_Slot_Incorrect.png" xanchor 0.5 xalign 0.5
                                else:
                                    add "Serum_Slot_Empty.png" xanchor 0.5 xalign 0.5
                    hbox:
                        spacing 5
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 270
                                text "Research Required: {color=#ff0000}[starting_serum.research_needed]{/color}" style "serum_text_style"
                            frame:
                                background "#000080"
                                xsize 270
                                text "Production Cost: {color=#ff0000}[starting_serum.production_cost]{/color}" style "serum_text_style"
                            frame:
                                background "#000080"
                                xsize 270
                                text "Value: ${color=#98fb98}[starting_serum.value]{/color}" style "serum_text_style"
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 270
                                
                                $ calculated_profit = (starting_serum.value*mc.business.batch_size)-starting_serum.production_cost
                                if calculated_profit > 0:
                                    text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style"
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    text "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}" style "serum_text_style"

                            frame:
                                background "#000080"
                                xsize 270
                                text "Duration: [starting_serum.duration] Turns" style "serum_text_style"

                            null #Placeholder to keep the grid aligned

                    frame:
                        background "#000080"
                        xsize 550
                        text "Serum Effects:" style "serum_text_style_header"

                    viewport:
                        xsize 550
                        scrollbars "vertical"
                        mousewheel True
                        frame:
                            xsize 550
                            background None
                            vbox:
                                for trait in starting_serum.traits:
                                    textbutton trait.name:
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 550

                                        action  NullAction()
                                        hovered SetScreenVariable("trait_tooltip", trait)

                                    hbox:
                                        spacing 5
                                        vbox:
                                            frame:
                                                background "#007000"
                                                xsize 270
                                                text "[trait.positive_slug]" style "serum_text_style"
                                        vbox:
                                            frame:
                                                background "#930000"
                                                xsize 270
                                                text "[trait.negative_slug]" style "serum_text_style"

        frame:
            background "#888888"
            xsize 250
            xanchor 0.5
            xalign 0.5
            yalign 0.9
            vbox:
                xanchor 0.5
                xalign 0.5
                textbutton "Create Design":
                    action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return(starting_serum)]
                    sensitive (starting_serum.slots >= effective_traits and len(starting_serum.traits) and starting_serum.has_tag("Production")) > 0

                    style "textbutton_style"
                    text_style "serum_text_style"
                    xanchor 0.5
                    xalign 0.5
                    xsize 230

                textbutton "Reject Design":
                    action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return("None")]

                    style "textbutton_style"
                    text_style "serum_text_style"
                    xanchor 0.5
                    xalign 0.5
                    xsize 230

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"design_tutorial")

        $ design_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["design_tutorial"] > 0 and mc.business.event_triggers_dict["design_tutorial"] <= design_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/design_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["design_tutorial"])+".png"
                hover "/tutorial_images/design_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["design_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"design_tutorial")
