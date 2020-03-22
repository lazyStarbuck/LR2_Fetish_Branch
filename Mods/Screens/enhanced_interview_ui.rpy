init 2:
    screen interview_ui(the_candidates, count):
        default current_selection = 0
        default the_candidate = the_candidates[current_selection]
        vbox:
            yalign 0.2
            xalign 0.4
            xanchor 0.5
            spacing 30
            frame:
                background "#1a45a1aa"
                ysize 80
                xsize 1320
                xalign 0.5
                xanchor 0.5
                text "[the_candidate.name] [the_candidate.last_name]" style "menu_text_style" size 50 xanchor 0.5 xalign 0.5 color the_candidate.char.who_args["color"] font the_candidate.char.what_args["font"]
            hbox:
                xsize 1320
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Personal Information" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the person: age, height, happiness, obedience, etc.
                        text "Required Salary: $[the_candidate.salary]/day" style "menu_text_style" size 16
                        if recruitment_knowledge_one_policy.is_owned():
                            text "Personality: " + the_candidate.personality.personality_type_prefix.capitalize() style "menu_text_style" size 16
                        if recruitment_knowledge_two_policy.is_owned():
                            text "Relationship: " + the_candidate.relationship style "menu_text_style" size 16
                            if the_candidate.relationship != "Single":
                                text "Significant Other: " + the_candidate.SO_name style "menu_text_style" size 16
                            if the_candidate.kids > 0:
                                text "Kids: " + str(the_candidate.kids) style "menu_text_style" size 16
                        if recruitment_stat_improvement_policy.is_owned():
                            text "" style "menu_text_style" size 16
                            text "Happiness: [the_candidate.happiness]" style "menu_text_style" size 16
                            text "Sluttiness: [the_candidate.sluttiness] - " + get_gold_heart(the_candidate.sluttiness) style "menu_text_style" size 16
                            text "Obedience: [the_candidate.obedience] - " + get_obedience_plaintext(the_candidate.obedience) style "menu_text_style" size 16
                        if recruitment_knowledge_three_policy.is_owned():
                            text "" style "menu_text_style" size 16
                            text "Age: [the_candidate.age]" style "menu_text_style" size 16
                            text "Height: " + height_to_string(the_candidate.height) style "menu_text_style" size 16
                            text "Cup size: [the_candidate.tits]" style "menu_text_style" size 16
                            text "Weight: " + get_person_weight_string(the_candidate) style "menu_text_style" size 16
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Stats and Skills" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the persons raw stats, work skills, and sex skills
                        text "Stats" style "menu_text_style" size 20
                        text "    Charisma: [the_candidate.charisma]" style "menu_text_style" size 16
                        text "    Intelligence: [the_candidate.int]" style "menu_text_style" size 16
                        text "    Focus: [the_candidate.focus]" style "menu_text_style" size 16
                        text "Work Skills" style "menu_text_style" size 20
                        text "    HR: [the_candidate.hr_skill]" style "menu_text_style" size 16
                        text "    Marketing: [the_candidate.market_skill]" style "menu_text_style" size 16
                        text "    Research: [the_candidate.research_skill]" style "menu_text_style" size 16
                        text "    Production: [the_candidate.production_skill]" style "menu_text_style" size 16
                        text "    Supply: [the_candidate.supply_skill]" style "menu_text_style" size 16
                        if recruitment_knowledge_four_policy.is_owned():
                            text "Sex Skills" style "menu_text_style" size 20
                            text "    Foreplay: " + str(the_candidate.sex_skills["Foreplay"]) style "menu_text_style" size 16
                            text "    Oral: " + str(the_candidate.sex_skills["Oral"]) style "menu_text_style" size 16
                            text "    Vaginal: " + str(the_candidate.sex_skills["Vaginal"]) style "menu_text_style" size 16
                            text "    Anal: " + str(the_candidate.sex_skills["Anal"]) style "menu_text_style" size 16

                frame:
                    $ master_opinion_dict = dict(the_candidate.opinions, **the_candidate.sexy_opinions)
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Opinions" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the persons loves, likes, dislikes, and hates
                        hbox:
                            spacing 5
                            vbox:
                                xsize 210
                                text "Loves" style "menu_text_style" size 22
                                for opinion in master_opinion_dict:
                                    if master_opinion_dict[opinion][0] == 2:
                                        if master_opinion_dict[opinion][1]:
                                            text opinion.title() style "menu_text_style" size 16
                                        else:
                                            text "????" style "menu_text_style" size 16
                            vbox:
                                text "Likes" style "menu_text_style" size 22
                                for opinion in master_opinion_dict:
                                    if master_opinion_dict[opinion][0] == 1:
                                        if master_opinion_dict[opinion][1]:
                                            text opinion.title() style "menu_text_style" size 16
                                        else:
                                            text "????" style "menu_text_style" size 16
                        hbox:
                            ysize 14
                        hbox:
                            spacing 5
                            vbox:
                                xsize 210
                                text "Dislikes" style "menu_text_style" size 20
                                for opinion in master_opinion_dict:
                                    if master_opinion_dict[opinion][0] == -1:
                                        if master_opinion_dict[opinion][1]:
                                            text opinion.title() style "menu_text_style" size 16
                                        else:
                                            text "????" style "menu_text_style" size 16

                            vbox:
                                text "Hates" style "menu_text_style" size 20
                                for opinion in master_opinion_dict:
                                    if master_opinion_dict[opinion][0] == -2:
                                        if master_opinion_dict[opinion][1]:
                                            text opinion.title() style "menu_text_style" size 16
                                        else:
                                            text "????" style "menu_text_style" size 16

            frame:
                background "#1a45a1aa"
                xsize 1320
                ysize 200
                vbox:
                    text "Expected Production" style "menu_text_style" size 30
                    text "    Human Resources: +" + str(the_candidate.hr_skill*2 + the_candidate.charisma*3 + the_candidate.int + 10) + "% Company Efficiency per time chunk." style "menu_text_style" size 16
                    text "    Marketing: " + str(the_candidate.market_skill*2 + the_candidate.charisma*3 + the_candidate.focus + 10) + " Units of serum sold per time chunk." style "menu_text_style" size 16
                    text "    Research and Development: " + str(the_candidate.research_skill*2 + the_candidate.int*3 + the_candidate.focus + 10) + " Research points per time chunk." style "menu_text_style" size 16
                    text "    Production: " + str(the_candidate.production_skill*2 + the_candidate.focus*3 + the_candidate.int + 10) + " Production points per time chunk." style "menu_text_style" size 16
                    text "    Supply Procurement: " + str(the_candidate.supply_skill*2 + the_candidate.focus*3 + the_candidate.charisma + 10) + " Units of supply per time chunk." style "menu_text_style" size 16

            frame:
                background "#1a45a1aa"
                xsize 1320
                ysize 100
                hbox:
                    yalign 0.5
                    yanchor 0.5
                    xalign 0.5
                    xanchor 0.5
                    textbutton "Previous Candidate" action [SetScreenVariable("current_selection",current_selection-1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection-1]),
                        Function(show_candidate,the_candidates[current_selection-1])] sensitive current_selection > 0 selected False style "textbutton_style" text_style "textbutton_text_style" xanchor 0.5 xalign 0.5 yalign 0.5 yanchor 0.5

                    null width 300
                    textbutton "Hire Nobody" action Return("None") style "textbutton_style" text_style "textbutton_text_style" xanchor 0.5 xalign 0.5 yalign 0.5 yanchor 0.5

                    textbutton "Hire " action Return(the_candidate) style "textbutton_style" text_style "textbutton_text_style" xanchor 0.5 xalign 0.5 yalign 0.5 yanchor 0.5
                    null width 300
                    textbutton "Next Candidate" action [SetScreenVariable("current_selection",current_selection+1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection+1]),
                        Function(show_candidate,the_candidates[current_selection+1])] sensitive current_selection < count-1 selected False style "textbutton_style" text_style "textbutton_text_style"  xanchor 0.5 xalign 0.5 yalign 0.5 yanchor 0.5


        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xanchor 1.0
            xalign 1.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"hiring_tutorial")


        $ hiring_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["hiring_tutorial"] > 0 and mc.business.event_triggers_dict["hiring_tutorial"] <= hiring_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/hiring_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["hiring_tutorial"])+".png"
                hover "/tutorial_images/hiring_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["hiring_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"hiring_tutorial")

