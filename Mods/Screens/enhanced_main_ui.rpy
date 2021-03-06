init 2:
    screen main_ui(): #The UI that shows most of the important information to the screen.
        python:
            known = len(known_people_in_the_game([mc]))
            total = len(all_people_in_the_game([mc]))

        frame:
            background "Info_Frame_1.png"
            xsize 600
            ysize 400
            yalign 0.0
            vbox:
                text day_names[day%7] + " - " + time_names[time_of_day] + " (day [day])" style "menu_text_style" size 18
                textbutton "Outfit Manager" action Call("outfit_master_manager",from_current=True) style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Design outfits to set as uniforms or give to suggest to women."
                textbutton "Check Inventory" action ui.callsinnewcontext("check_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check what serums you are currently carrying."
                if mc.stat_goal.completed or mc.work_goal.completed or mc.sex_goal.completed:
                    textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 background "#44BB44" insensitive_background "#222222" hover_background "#aaaaaa" tooltip "Check your stats, skills, and goals."
                else:
                    textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check your stats, skills, and goals."
                textbutton "Perk Sheet" action Show("mc_perk_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check your stat, item, and ability perks."

                textbutton "Arousal: [mc.arousal]/[mc.max_arousal] {image=gui/extra_images/arousal_token.png}":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Your personal arousal. When you reach your limit you will be forced to climax and your energy will drop."
                    action NullAction()
                    sensitive True

                textbutton "Energy: [mc.energy]/[mc.max_energy] {image=gui/extra_images/energy_token.png}":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Many actions require energy to perform, sex especially. Energy comes back slowly throughout the day, and most of it is recovered after a good nights sleep."
                    action NullAction()
                    sensitive True

                textbutton "World: [known]/[total]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Shows the number of known and total people in your world."
                    action NullAction()
                    sensitive True
