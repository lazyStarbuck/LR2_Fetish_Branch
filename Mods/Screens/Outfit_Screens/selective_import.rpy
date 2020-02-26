# Allows you to preview and select singular items from an XML file before importing.

init 2 python:
    def add_outfit(wardrobe, the_outfit, outfit_type = "full"):
            if outfit_type == "under":
                wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                wardrobe.add_outfit(the_outfit)

    def add_outfit_to_wardrobes(list_of_wardrobes, the_outfit, outfit_type = "full"): #Adds the outfit to every wardrobe in the list of wardrobes passed to it

        for wardrobe in list_of_wardrobes:
            if not wardrobe.has_outfit_with_name(the_outfit.name):
                if outfit_type == "under":
                    wardrobe.add_underwear_set(the_outfit)
                elif outfit_type == "over":
                    wardrobe.add_overwear_set(the_outfit)
                else: #outfit_type = full
                    wardrobe.add_outfit(the_outfit)

    def remove_outfit_from_wardrobes(list_of_wardrobes, the_outfit):

        for wardrobe in list_of_wardrobes:
            if wardrobe.has_outfit_with_name(the_outfit.name):
                wardrobe.remove_outfit(the_outfit)

    def wardrobes_has_outfit_with_name(list_of_wardrobes, the_name): # Check if every Wardrobe in the list has the outfit already

        max_count = len(list_of_wardrobes)
        count = 0
        for wardrobe in list_of_wardrobes:
            for checked_outfit in wardrobe.outfits + wardrobe.underwear_sets + wardrobe.overwear_sets:
                if checked_outfit.name == the_name:
                    count += 1
        if count == max_count:
            return True
        else:
            return False

    def selected_xml_wardrobe(target_wardrobe, xml_filename): # TODO: Use this instead -> Show("import_outfit_manager", None, target_wardrobe, n)
        renpy.show_screen("import_outfit_manager", target_wardrobe, xml_filename)
    def selected_xml_clothing(outfit):
        renpy.show_screen("outfit_creator", outfit.get_copy())

init 2:
    screen import_outfit_manager(target_wardrobe, xml_filename = None, show_export = True, slut_limit = None, underwear_limit = None, limited_to_top = False): ##Brings up a list of the players current saved outfits, returns the selected outfit or None.
        # NOTE: slut_limited and limited_to_top is passed from label set_uniform_description in script.rpy and is only used in that situation




        default outfit_categories = {"Full": ["FullSets", "full", "get_outfit_list", "reduced_coverage_uniform_policy"], "Overwear": ["OverwearSets", "over", "get_overwear_sets_list", "strict_uniform_policy"], "Underwear": ["UnderwearSets", "under", "get_underwear_sets_list", "reduced_coverage_uniform_policy"]} #NOTE: Key is display name, [0] is XML's category type, [1] is outfit type, [2] is function to retrive [0]
        add "Paper_Background.png"
        modal True
        zorder 100
        default preview_outfit = None
        default targeted_outfit = None
        #default business_wardrobes = [mc.business.m_uniform, mc.business.p_uniform, mc.business.r_uniform, mc.business.s_uniform, mc.business.h_uniform, mc.business.all_uniform]

        default import_wardrobes = {} # Holds the wardrobes you want to be able to import into or select #NOTE: Make sure it is a list inside of a list [[]]
        python:
            if slut_limit is None: # If slut_limit is None then add any and all options

                import_wardrobes["Your Wardrobe"] = [[mc.designed_wardrobe]]
                import_wardrobes["Slaves"] = [[x.wardrobe for x in people_in_role(slave_role)]]

            import_wardrobes["Marketing Division"] = [[mc.business.m_uniform]]
            import_wardrobes["Research Division"] = [[mc.business.r_uniform]]
            import_wardrobes["Production Division"] = [[mc.business.p_uniform]]
            import_wardrobes["Supply Division"] = [[mc.business.s_uniform]]
            import_wardrobes["HR Division"] = [[mc.business.h_uniform]]
            import_wardrobes["All Division"] = [[mc.business.all_uniform]]

        python:
            if xml_filename:
                wardrobe = wardrobe_from_xml(xml_filename)
            else:
                temp_wardrobe = Wardrobe("Temporary Wardrobe")
                for category in import_wardrobes:
                    for wardrobes in import_wardrobes[category][0]:
                        for outfit in wardrobes.outfits + mc.designed_wardrobe.outfits:
                            if outfit not in temp_wardrobe.outfits:
                                temp_wardrobe.outfits.append(outfit)

                        for outfit in wardrobes.overwear_sets + mc.designed_wardrobe.overwear_sets:
                            if outfit not in temp_wardrobe.overwear_sets:
                                temp_wardrobe.overwear_sets.append(outfit)

                        for outfit in wardrobes.underwear_sets + mc.designed_wardrobe.underwear_sets:
                            if outfit not in temp_wardrobe.underwear_sets:
                                temp_wardrobe.underwear_sets.append(outfit)

                wardrobe = temp_wardrobe

        # default import_wardrobes = {"Your Wardrobe": [[mc.designed_wardrobe]], "Marketing Division": [[mc.business.m_uniform]], "Research Division": [[mc.business.r_uniform]], "Production Division": [[mc.business.p_uniform]], "Supply Division": [[mc.business.s_uniform]], "HR Division": [[mc.business.h_uniform]], "All Divisions": [[mc.business.all_uniform]]}
        # $ import_wardrobes["Slaves"] = [[x.wardrobe for x in people_in_role(slave_role)]]

        grid len(outfit_categories) 1:
            for category in sorted(outfit_categories): # NOTE: Dictionary is not sorted. Don't know the best way to make it so.
                vbox:
                    xsize 480
                    frame:
                        text category style "serum_text_style" xalign 0.5
                        xfill True
                    viewport:
                        ysize 880
                        if len(getattr(wardrobe, outfit_categories[category][2])()) > 7:
                            scrollbars "vertical"
                        mousewheel True
                        vbox:
                            if len(getattr(wardrobe, outfit_categories[category][2])()) > 0: #Don't show a frame if it is empty
                                frame:
                                    vbox:
                                        for outfit in sorted(getattr(wardrobe, outfit_categories[category][2])(), key = lambda outfit: (outfit.slut_requirement, outfit.name)):  # Not sure if there's any good reason to sort XML lists since the default way it works is to place the newest outfit at the bottom which is predictable.
                                            frame:
                                                vbox:
                                                    id str(outfit)
                                                    xfill True
                                                    textbutton outfit.name + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                                        xfill True
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"


                                                        if slut_limit is None:
                                                            action [
                                                                Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = outfit_categories[category][1]), # Bring the outfit into the outfit_creator for editing when left clicked
                                                                Hide(renpy.current_screen().screen_name)
                                                                ]
                                                        else:
                                                            if slut_limit >= outfit.slut_requirement:
                                                                action NullAction()
                                                            else:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to slut limit " + str(slut_limit) + ". Purchase new uniform policies to increase")

                                                        hovered Show("mannequin", None, outfit)

                                                    if show_export: # If export mode is on show the export button that saves the outfits into Exported_Wardrobe.xml NOTE: Consider specifying specific XML file later (to quickly make wardrobe sets for sharing)
                                                        default exported = []

                                                        textbutton "Export to .xml File":
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True

                                                            action [
                                                                Function(exported.append, outfit), Function(log_outfit, outfit, outfit_class = outfit_categories[category][0], wardrobe_name = "Exported_Wardrobe"),
                                                                Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")
                                                                ]

                                                            sensitive outfit not in exported


                                                    textbutton ("Direct Import Selection:" if slut_limit is None else "Assign to Division:"): # Put the outfit directly into wardrobe(s), see the import_wardrobes dictionary to add more alternatives.

                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        xfill True
                                                        #sensitive slut_limit >= outfit.slut_requirement

                                                        if slut_limit is None:
                                                            action ToggleScreenVariable("targeted_outfit", renpy.get_widget(renpy.current_screen(), str(outfit)), None)
                                                        else:
                                                            if slut_limit >= outfit.slut_requirement:
                                                                action ToggleScreenVariable("targeted_outfit", renpy.get_widget(renpy.current_screen(), str(outfit)), None)
                                                            else:
                                                                background "#222222"
                                                                action Function(renpy.notify, "Can not assign due to slut limit " + str(slut_limit) + ". Purchase new uniform policies to increase")

                                                    if targeted_outfit == renpy.get_widget(renpy.current_screen(), str(outfit)):
                                                        frame:
                                                            vbox:
                                                                for wardrobes in import_wardrobes:
                                                                    textbutton str(wardrobes):
                                                                        style "textbutton_no_padding_highlight"
                                                                        text_style "serum_text_style"
                                                                        xfill True




                                                                        # if slut_limit is None:
                                                                        #     sensitive not wardrobes_has_outfit_with_name(import_wardrobes[wardrobes][0], outfit.name)# in getattr(wardrobes, outfit_categories[category][2])()

                                                                        if not wardrobes_has_outfit_with_name(import_wardrobes[wardrobes][0], outfit.name):
                                                                            action [
                                                                                If(slut_limit != None, Function(mc.business.listener_system.fire_event, "add_uniform", the_outfit = outfit, the_type = outfit_categories[category][1])), # Make sure it registers progress towards work_goals. #NOTE: Needs testing as I have been unable to setup proper test
                                                                                Function(add_outfit_to_wardrobes, import_wardrobes[wardrobes][0], outfit, outfit_type = outfit_categories[category][1]),
                                                                                Function(renpy.notify, ("Outfit imported to " + wardrobes if slut_limit is None else "Outfit assigned to " + wardrobes)),

                                                                                ]
                                                                        else:

                                                                            if slut_limit is not None:
                                                                                if wardrobes_has_outfit_with_name(import_wardrobes[wardrobes][0], outfit.name):
                                                                                    background "#3ffc45"
                                                                                #If the outfit is imported / assigned already then attempt to remove it.
                                                                                action [
                                                                                    Function(remove_outfit_from_wardrobes, import_wardrobes[wardrobes][0], outfit),
                                                                                    Function(renpy.notify, "Outfit removed from " + wardrobes)
                                                                                    ]

                                                        #
                                                        # action [
                                                        #     Function(add_outfit, target_wardrobe, outfit, outfit_type = outfit_categories[category][1]),
                                                        #     Function(renpy.notify, "Outfit imported to " + target_wardrobe.name)
                                                        #     ]
                                                        # sensitive not target_wardrobe.has_outfit_with_name(outfit.name)


        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.92]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                if slut_limit is None:
                    action Hide("import_outfit_manager")
                else:
                    action Return("No Return")
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
