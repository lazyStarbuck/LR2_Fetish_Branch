init 2 python:
    def draw_mannequin(mannequin, outfit, position = None, emotion = None, special_modifier = None, background_fill = "#0026a5"): # Small tweak of draw_person to allow for an outfit that is not theirs to be shown (NOTE: outfit.generate_draw_list)
        renpy.scene("Active")

        if position is None:
            position = mannequin.idle_pose

        if emotion is None:
            emotion = mannequin.get_emotion()

        if not persistent.vren_animation:
            background_fill = None

        lighting = [0.98,0.98,0.98]

        draw_outfit = outfit.get_copy()
        if mannequin.base_outfit:
            draw_outfit = outfit.merge_outfit(mannequin.base_outfit)

        mannequin.apply_outfit(draw_outfit)

        final_image = mannequin.build_person_displayable(position, emotion,special_modifier, lighting, background_fill)

        renpy.show(mannequin.name,at_list=[character_right, scale_person(mannequin.height)],layer="Active",what=final_image,tag=mannequin.name)
        renpy.restart_interaction()       

init 2: # Moved to screen so that it can be refreshed upon changes made in outfit_creator
    screen mannequin(outfit, model = "mannequin"):
        $ renpy.scene("Active")
        zorder 102
        fixed: #TODO: Move this to it's own screen so it can be shown anywhere
            pos (1450,0)
            add mannequin_average
            if outfit is not None:
                for cloth in outfit.generate_draw_list(None,"stand3"):
                    add cloth
