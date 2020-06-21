#init -1 python: #TODO: Go through everything again so that it uses copies where it should and remove instances where it shouldn't.
                      # I want outfits to be editable without forcing commitet changes upon `selected_clothing`
                      # Right now, this seems to only be a problem when editing a `Person`'s wardrobe since the MC Wardrobe always use copies anyway.
                      # Fix issue with hitting "Abandon" when using Outfit Manager through "Add Outfit" for a Person, seems to be coming from the fact it does not give the expected return of "No Return".
                      # Best solution would be for Vren to change that in the main script so all the outfit screen expect the same return.
                      # Figure out why and fix actions only running certain functions on every second press.
                      # Add logic for the instances where multiple cloth items from a category can be applied so it displays properly at all times. (no known issues with the end result, just display)

init 10 python:

    # NOTE: Override the color changing functions

    def get_heart_image_list_cloth(slut_value, multiplier = 5): ## Returns a string of hearts. Since we are dealing with lower values this version has 20 as it's 100% filled value. Used to indicate sluttiness requirement for the cloth item.

        heart_string = "{image=" + get_individual_heart(0, slut_value*multiplier, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-20, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-40, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-60, 0) + "}"
        heart_string += "{image=" + get_individual_heart(0, slut_value*multiplier-80, 0) + "}"


        return heart_string

    def replace_cloth(cloth):

        cs = renpy.current_screen()

        if not cs.scope["valid_check"](cs.scope["item_outfit"], cs.scope["selected_clothing"]) and cs.scope["selected_from_outfit"] is not None:
            cs.scope["item_outfit"].remove_clothing(cs.scope["selected_from_outfit"])
            cs.scope["apply_method"](cs.scope["item_outfit"], cs.scope["selected_clothing"])
        else:
            cs.scope["apply_method"](cs.scope["item_outfit"], cs.scope["selected_clothing"])

        cs.scope["selected_from_outfit"] = cloth

        renpy.restart_interaction()

    def update_outfit_color(cloth_to_color):

        cs = renpy.current_screen()


        if cs.scope["selected_colour"] == "colour_pattern":
            cloth_to_color.colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]
        else:
            cloth_to_color.colour = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]

        renpy.restart_interaction()

    def preview_outfit(outfit = "demo_outfit"):

        renpy.scene("Active")
        cs = renpy.current_screen()
        if cs.scope["mannequin"] == "mannequin":
            renpy.show_screen("mannequin", cs.scope[outfit])
        else:
            if renpy.get_screen("mannequin"):
                renpy.hide_screen("mannequin")
            draw_mannequin(cs.scope["mannequin"], cs.scope[outfit], cs.scope["mannequin_pose"])

        renpy.restart_interaction()

    def preview_apply(cloth): # Temporarily remove the selected clothing with the one being hovered over.

        cs = renpy.current_screen()


        if cs.scope["selected_clothing"] is not None:
            if cs.scope["selected_clothing"] in cs.scope["categories_mapping"][cs.scope["category_selected"]][0]:
                cs.scope["demo_outfit"].remove_clothing(cs.scope["selected_clothing"])
                cs.scope["apply_method"](cs.scope["demo_outfit"], cloth)

        else:
            if cs.scope["selected_clothing"] is not None and cs.scope["demo_outfit"].in_outfit(cs.scope["selected_clothing"].name):
                cs.scope["demo_outfit"].remove_clothing(cs.scope["selected_clothing"])
            cs.scope["apply_method"](cs.scope["demo_outfit"], cloth)

        renpy.restart_interaction()

    def preview_restore(cloth):

        cs = renpy.current_screen()

        if cloth is cs.scope["selected_clothing"] and cs.scope["categories_mapping"][cs.scope["category_selected"]][0]:
            pass
        else:
            cs.scope["demo_outfit"].remove_clothing(cloth)

        if cs.scope["selected_clothing"] is not None:
            cs.scope["apply_method"](cs.scope["demo_outfit"], cs.scope["selected_clothing"])
        else:
            preview_outfit()

        renpy.restart_interaction()


    def outfit_valid_check():

        cs = renpy.current_screen()

        if cs.scope["selected_clothing"] is not None:
            if cs.scope["valid_check"](cs.scope["item_outfit"], cs.scope["selected_clothing"]) or cs.scope["cloth"].layer in cs.scope["valid_layers"]:
                return True
            else:
                return False

    def set_generated_outfit(category, slut_value):
        cs = renpy.current_screen()

        outfit = cs.scope["outfit_builder"].build_outfit(cs.scope["outfit_class_selected"], slut_value)
        cs.scope["item_outfit"] = outfit.get_copy()
        cs.scope["demo_outfit"] = outfit
        switch_outfit_category(category)

    def get_outfit_copy_with_name(outfit):
        new_outfit = outfit.get_copy()
        new_outfit.build_outfit_name()
        return new_outfit

    def update_outfit_name(outfit):
        default_names = ["New Outfit", "New Overwear Set", "New Underwear Set"]
        if outfit.name in default_names:
            outfit.build_outfit_name()
        return

    def switch_outfit_category(category):

        cs = renpy.current_screen()

        cs.scope["selected_clothing"] = None
        cs.scope["selected_from_outfit"] = None
        cs.scope["category_selected"] = category
        cs.scope["selected_colour"] = "colour" # Default to altering non- pattern colors

        cs.scope["demo_outfit"] = cs.scope["item_outfit"].get_copy()

        # select cloth item from category we have selected
        for cloth in cs.scope["item_outfit"].upper_body + cs.scope["item_outfit"].lower_body + cs.scope["item_outfit"].feet + cs.scope["item_outfit"].accessories:
            if not cloth.is_extension:
                if cloth in cs.scope["categories_mapping"][category][0]:
                    cs.scope["selected_clothing"] = cloth
                    cs.scope["selected_from_outfit"] = cloth
                    break

        preview_outfit()

        # if cs.scope["selected_clothing"] is not None and not cs.scope["starting_outfit"].has_clothing(cs.scope["selected_clothing"]):
        #     cs.scope["demo_outfit"].remove_clothing(cs.scope["selected_clothing"])

    def colour_changed_bar(new_value): # Handles the changes to clothing colors, both normal and with patterns. Covers all channels.
        if not new_value:
            new_value = 0
        try:
            new_value = float(new_value)
        except ValueError:
            new_value = 0
        if float(new_value) < 0:
            new_value = 0
        elif float(new_value) > 1:
            new_value = 1.0

        cs = renpy.current_screen()
        bar_value = cs.scope["bar_value"]

        if bar_value == "current_a":
            cs.scope["current_a"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], __builtin__.round(float(new_value),2)]

        if bar_value == "current_r":
            cs.scope["current_r"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [__builtin__.round(float(new_value),2), cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [__builtin__.round(float(new_value),2), cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]

        if bar_value == "current_g":
            cs.scope["current_g"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], __builtin__.round(float(new_value),2), cs.scope["current_b"], cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], __builtin__.round(float(new_value),2), cs.scope["current_b"], cs.scope["current_a"]]

        if bar_value == "current_b":
            cs.scope["current_b"] = __builtin__.round(float(new_value),2)
            if cs.scope["selected_colour"] == "colour_pattern":
                cs.scope["selected_clothing"].colour_pattern = [cs.scope["current_r"], cs.scope["current_g"], __builtin__.round(float(new_value),2), cs.scope["current_a"]]
            else:
                cs.scope["selected_clothing"].colour = [cs.scope["current_r"], cs.scope["current_g"], __builtin__.round(float(new_value),2), cs.scope["current_a"]]

        preview_outfit()

    def update_slut_generation(new_value):
        cs = renpy.current_screen()

        if new_value < 0:
            new_value = 1
        if new_value > 12:
            new_value = 12

        cs.scope["slut_generation"] = new_value
        renpy.restart_interaction()

init -1 python:

    def in_outfit(self, cloth_name): # Checks if the clothing item exists in the outfit by name to account for instances where copies are used.
        for cloth in self.upper_body + self.lower_body + self.feet + self.accessories:
            if cloth.name == cloth_name:
                return True
        else:
            return False
    Outfit.in_outfit = in_outfit



    def get_category(item): # Should re-write this function if possible.
        cs = renpy.current_screen()
        fluids_list = cs.scope["fluids_list"]
        cloth_master_list = [
        panties_list + neckwear_list + bracelet_list + rings_list +
        earings_list + shoes_list + bra_list + pants_list + skirts_list +
        shirts_list + dress_list +  socks_list + fluids_list
        ]
        for cloth in cloth_master_list:
            if item in panties_list:
                return "Panties"
            if item in bra_list:
                return "Bras"
            if item in pants_list:
                return "Pants"
            if item in skirts_list:
                return "Skirts"
            if item in dress_list:
                return "Dresses"
            if item in shirts_list:
                return "Shirts"
            if item in socks_list:
                return "Socks"
            if item in shoes_list:
                return "Shoes"
            if item in earings_list:
                return "Facial"
            if item in rings_list:
                return "Rings"
            if item in bracelet_list:
                return "Bracelets"
            if item in neckwear_list:
                return "Neckwear"
            if item in fluids_list:
                return "Not Paint"
            else:
                return "Item not in Category"
init 2:
    python:
        def custom_log_outfit(the_outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"): #NOTE: This is just a version of the default log_outfit that does not append .xml to the file name
            file_path = os.path.abspath(os.path.join(config.basedir, "game"))
            file_path = os.path.join(file_path,"wardrobes")
            file_name = os.path.join(file_path, wardrobe_name)

            if not os.path.isfile(file_name): #We assume if the file exists that it is well formed. Otherwise we will create it and guarantee it is well formed.
                #Note: if the file is changed (by inserting extra outfits, for example) exporting outfits may crash due to malformed xml, but we do not overwrite the file.
                missing_file = open(file_name,"w+")
                starting_element = ET.Element("Wardrobe",{"name":wardrobe_name})
                starting_tree = ET.ElementTree(starting_element)
                ET.SubElement(starting_element,"FullSets")
                ET.SubElement(starting_element,"UnderwearSets")
                ET.SubElement(starting_element,"OverwearSets")

                indent(starting_element)
                starting_tree.write(file_name,encoding="UTF-8")


            wardrobe_tree = ET.parse(file_name)
            tree_root = wardrobe_tree.getroot()
            outfit_root = tree_root.find(outfit_class)

            outfit_element = ET.SubElement(outfit_root,"Outfit",{"name":the_outfit.name})
            upper_element = ET.SubElement(outfit_element, "UpperBody")
            lower_element = ET.SubElement(outfit_element, "LowerBody")
            feet_element = ET.SubElement(outfit_element, "Feet")
            accessory_element = ET.SubElement(outfit_element, "Accessories")


            for cloth in the_outfit.upper_body:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(upper_element,"Item", item_dict)
            for cloth in the_outfit.lower_body:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(lower_element,"Item", item_dict)
            for cloth in the_outfit.feet:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(feet_element,"Item", item_dict)
            for cloth in the_outfit.accessories:
                item_dict = build_item_dict(cloth)
                if not cloth.is_extension:
                    ET.SubElement(accessory_element,"Item", item_dict)

            indent(tree_root)
            wardrobe_tree.write(file_name,encoding="UTF-8")

init 2:
    screen outfit_creator(starting_outfit, target_wardrobe = mc.designed_wardrobe, outfit_type = "full"): ##Pass a completely blank outfit instance for a new outfit, or an already existing instance to load an old one.| This overrides the default outfit creation screen

        #add "Paper_Background.png"
        modal True
        zorder 100

        $ renpy.block_rollback()

        $ fluids_list = [face_cum, mouth_cum, stomach_cum, tits_cum, ass_cum, creampie_cum]

        default category_selected = "Panties"
        default mannequin = "mannequin"
        default mannequin_pose = "stand3"
        default mannequin_selection = False
        default mannequin_poser = False

        default selected_xml = "Exported_Wardrobe.xml"
        default cloth_pattern_selection = True
        default transparency_selection = True
        default outfit_stats = True
        default outfit_class_selected = "FullSets"
        default color_selection = True
        default import_selection = False

        default quick_category = None # Used to get category of the item
        default selected_from_outfit = None # Used to temporarily remember what clothing you have selected from starting_outfit if any
        default colour_cloth = None # A variable to fetch the copy of selected_clothing.get_copy()
        default demo_outfit = starting_outfit.get_copy()
        default item_outfit = starting_outfit.get_copy()
        default outfit_builder = WardrobeBuilder(None)
        default max_slut = outfit_type == "over" and 8 or 12

        if outfit_type == "under":
            $ valid_layers = [0,1]
            $ outfit_class_selected = "UnderwearSets"
        elif outfit_type == "over":
            $ valid_layers = [2,3]
            $ outfit_class_selected = "OverwearSets"
        else:
            $ valid_layers = [0,1,2,3]
            $ outfit_class_selected = "FullSets"

        $ valid_categories = ["Panties", "Bras", "Pants", "Skirts", "Dresses", "Shirts", "Socks", "Shoes", "Facial", "Rings", "Bracelets", "Neckwear", "Not Paint"] #Holds the valid list of categories strings to be shown at the top.

        $ categories_mapping = {
            "Panties": [panties_list, Outfit.can_add_lower, Outfit.add_lower],  #Maps each category to the function it should use to determine if it is valid and how it should be added to the outfit.
            "Bras": [bra_list, Outfit.can_add_upper, Outfit.add_upper],
            "Pants": [pants_list, Outfit.can_add_lower, Outfit.add_lower],
            "Skirts": [skirts_list, Outfit.can_add_lower, Outfit.add_lower],
            "Dresses": [dress_list, Outfit.can_add_dress, Outfit.add_dress],
            "Shirts": [shirts_list, Outfit.can_add_upper, Outfit.add_upper],
            "Socks": [socks_list, Outfit.can_add_feet, Outfit.add_feet],
            "Shoes": [shoes_list, Outfit.can_add_feet, Outfit.add_feet],
            "Facial": [earings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Rings": [rings_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Bracelets": [bracelet_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Neckwear": [neckwear_list, Outfit.can_add_accessory, Outfit.add_accessory],
            "Not Paint": [fluids_list, Outfit.can_add_accessory, Outfit.add_accessory]}


        default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha
        default bar_value = None # Stores information about which bar is being changed and is then passed to colour_changed_bar() as default value

        default selected_clothing = None
        default selected_clothing_colour = None
        default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"

        default current_r = 1.0
        default current_g = 1.0
        default current_b = 1.0
        default current_a = 1.0

        default slut_generation = 0


        # $ current_colour = [1.0,1.0,1.0,1.0] #This is the colour we will apply to all of the clothing

        #Each category below has a click to enable button. If it's false, we don't show anything for it.
        #TODO: refactor this outfit creator to remove as much duplication as possible.


        hbox: #The main divider between the new item adder and the current outfit view.
            xpos 15
            yalign 0.5
            yanchor 0.5
            spacing 15
            frame:
                background "#aaaaaa"
                padding (20,20)
                xysize (880, 1015)
                hbox:
                    spacing 15
                    frame:
                        xsize 200

                        viewport:
                            mousewheel True
                            draggable True
                            grid 1 __builtin__.len(valid_categories): #categories select on far left
                                for category in valid_categories:
                                    textbutton category:
                                        style "textbutton_style"
                                        text_style "serum_text_style"

                                        xfill True
                                        sensitive category is not category_selected

                                        action [
                                            Function(switch_outfit_category, category) # If a clothing item is selected and currently being previewed then remove it from preview.
                                        ]
                    vbox:
                        spacing 15
                        viewport:
                            ysize 480
                            xminimum 605
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 620
                                yminimum 480
                                background "#888888"
                                vbox:
                                    #THIS IS WHERE ITEM CHOICES ARE SHOWN
                                    if category_selected in categories_mapping:
                                        $ valid_check = categories_mapping[category_selected][1]
                                        $ apply_method = categories_mapping[category_selected][2]
                                        $ cloth_list_length = __builtin__.len(categories_mapping[category_selected][0])

                                        for cloth in sorted(categories_mapping[category_selected][0], key = lambda x: (x.layer, x.slut_value, x.name)):
                                            textbutton cloth.name + (" | " + get_heart_image_list_cloth(cloth.slut_value) if cloth.slut_value > 0 else ""):
                                                style "textbutton_style"
                                                text_style "custom_outfit_style"

                                                if selected_clothing is not None:
                                                    sensitive outfit_valid_check()
                                                else: # If we are not editing an item already in the outfit then abide by the valid_layers rules.
                                                    sensitive cloth.layer in valid_layers

                                                xfill True
                                                xalign 0.5

                                                action [
                                                    SetScreenVariable("selected_clothing", cloth.get_copy()),
                                                    SetScreenVariable("selected_colour", "colour")
                                                ]

                                                hovered [
                                                    Function(preview_apply, cloth.get_copy()), # Add the hovered outfit to the demo outfit
                                                    Function(update_outfit_color, cloth.get_copy()),
                                                    Function(preview_outfit)
                                                ]

                                                unhovered [
                                                    Function(preview_restore, cloth), # Remove the hovered outfit from the demo outfit and focus on the selected item if any.
                                                    If(selected_clothing is not None, Function(update_outfit_color, selected_clothing)),
                                                    Function(preview_outfit)
                                                ]
                        frame:
                            #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                            xysize (605, 480)
                            background "#888888"
                            if selected_clothing is not None:
                                vbox:
                                    spacing 5
                                    frame:
                                        background "#aaaaaa"
                                        xfill True
                                        textbutton "Add " + selected_clothing.name + " to outfit" + "\n+" + __builtin__.str(selected_clothing.slut_value) + " Slut Requirement":

                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                            xalign 0.5
                                            xfill True

                                            sensitive outfit_valid_check()

                                            action [
                                                Function(update_outfit_color, selected_clothing), #Make sure color is updated
                                                Function(replace_cloth, selected_clothing),
                                                Function(preview_outfit) # NOTE: We are no longer interested in the demo outfit so view the final outfit, starting_outfit
                                            ]

                                            hovered [
                                                Function(preview_apply, selected_clothing),
                                                Function(update_outfit_color, selected_clothing),
                                                Function(preview_outfit)
                                            ]

                                    frame:
                                        background "#888888"
                                        yfill True
                                        xfill True
                                        viewport:
                                            xsize 605
                                            draggable True
                                            mousewheel True
                                            yfill True
                                            vbox:
                                                spacing 5
                                                if __builtin__.type(selected_clothing) is Clothing: #Only clothing items have patterns, facial accessories do not (currently).
                                                    vbox:
                                                        spacing 5
                                                        hbox:
                                                            frame:
                                                                background "#aaaaaa"
                                                                xfill True
                                                                textbutton "Cloth Pattern Selection":
                                                                    style "textbutton_no_padding_highlight"
                                                                    text_style "serum_text_style"
                                                                    xfill True

                                                                    action ToggleScreenVariable("cloth_pattern_selection")
                                                        hbox:
                                                            spacing 5
                                                            if cloth_pattern_selection:
                                                                frame:
                                                                    background "#aaaaaa"
                                                                    ysize 50
                                                                    viewport:
                                                                        mousewheel "horizontal"
                                                                        draggable True

                                                                        grid __builtin__.len(selected_clothing.supported_patterns) 1:
                                                                            xfill True
                                                                            for pattern in selected_clothing.supported_patterns:

                                                                                textbutton pattern:
                                                                                    style "textbutton_no_padding_highlight"
                                                                                    text_style "serum_text_style"
                                                                                    xalign 0.5
                                                                                    xfill True

                                                                                    if selected_clothing.pattern == selected_clothing.supported_patterns[pattern]:
                                                                                        background "#4f7ad6"
                                                                                        hover_background "#4f7ad6"
                                                                                    else:
                                                                                        background "#1a45a1"
                                                                                        hover_background "#3a65c1"

                                                                                    sensitive True
                                                                                    action SetField(selected_clothing,"pattern",selected_clothing.supported_patterns[pattern])

                                                        hbox:
                                                            xfill True
                                                            spacing 5 #We will manually handle spacing so we can have our colour predictor frames
                                                            frame:
                                                                ysize 50
                                                                background "#aaaaaa"
                                                                hbox:
                                                                    spacing 5
                                                                    textbutton "Primary Colour":
                                                                        style "textbutton_no_padding_highlight"
                                                                        text_style "serum_text_style"

                                                                        if selected_colour == "colour":
                                                                            background "#4f7ad6"
                                                                            hover_background "#4f7ad6"
                                                                        else:
                                                                            background "#1a45a1"
                                                                            hover_background "#3a65c1"
                                                                        sensitive True
                                                                        if selected_colour == "colour_pattern":
                                                                            action [
                                                                                SetField(selected_clothing,"colour_pattern",[current_r,current_g,current_b,current_a]),
                                                                                SetScreenVariable("selected_colour","colour"),
                                                                                SetScreenVariable("current_r",selected_clothing.colour[0]),
                                                                                SetScreenVariable("current_g",selected_clothing.colour[1]),
                                                                                SetScreenVariable("current_b",selected_clothing.colour[2]),
                                                                                SetScreenVariable("current_a",selected_clothing.colour[3])
                                                                            ]
                                                                        else:
                                                                            action ToggleScreenVariable("color_selection")

                                                                    frame:
                                                                        if selected_colour == "colour":
                                                                            background Color(rgb=(current_r,current_g,current_b,current_a))
                                                                        else:
                                                                            background Color(rgb=(selected_clothing.colour[0], selected_clothing.colour[1], selected_clothing.colour[2]))
                                                                        yfill True
                                                                        xsize 50


                                                                    if __builtin__.type(selected_clothing) is Clothing and selected_clothing.pattern is not None:
                                                                        textbutton "Pattern Colour":
                                                                            style "textbutton_no_padding_highlight"
                                                                            text_style "serum_text_style"

                                                                            if selected_colour == "colour_pattern":
                                                                                background "#4f7ad6"
                                                                                hover_background "#4f7ad6"
                                                                            else:
                                                                                background "#1a45a1"
                                                                                hover_background "#3a65c1"
                                                                            sensitive True
                                                                            if selected_colour == "colour":
                                                                                action [
                                                                                    SetField(selected_clothing,"colour",[current_r,current_g,current_b,current_a]),
                                                                                    SetScreenVariable("selected_colour","colour_pattern"),
                                                                                    SetScreenVariable("current_r",selected_clothing.colour_pattern[0]),
                                                                                    SetScreenVariable("current_g",selected_clothing.colour_pattern[1]),
                                                                                    SetScreenVariable("current_b",selected_clothing.colour_pattern[2]),
                                                                                    SetScreenVariable("current_a",selected_clothing.colour_pattern[3])
                                                                                ]
                                                                            else:
                                                                                action ToggleScreenVariable("color_selection")
                                                                        frame:
                                                                            if selected_colour == "colour_pattern":
                                                                                background Color(rgb=(current_r,current_g,current_b,current_a))
                                                                            else:
                                                                                background Color(rgb=(selected_clothing.colour_pattern[0], selected_clothing.colour_pattern[1], selected_clothing.colour_pattern[2]))
                                                                            yfill True
                                                                            xsize 50

                                                vbox:
                                                    spacing 5
                                                    hbox:
                                                        spacing 5
                                                        frame:
                                                            background "#aaaaaa"
                                                            textbutton "Color Selection":
                                                                style "textbutton_no_padding_highlight"
                                                                text_style "serum_text_style"
                                                                xfill True

                                                                action ToggleScreenVariable("color_selection")
                                                    hbox:
                                                        spacing 5
                                                        if color_selection:
                                                            hbox:
                                                                spacing 5
                                                                grid 2 2:
                                                                    xfill True
                                                                    frame:

                                                                        background "#aaaaaa"
                                                                        hbox:
                                                                            button:
                                                                                background "#dd1f1f"
                                                                                action ToggleScreenVariable("bar_select", 1, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_r")

                                                                                if bar_select == 1:
                                                                                    input default current_r length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "R "+ "%.2f" % current_r style "serum_text_style" yalign 0.5 size 16
                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_r, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_r")
                                                                                unhovered [SetScreenVariable("current_r",__builtin__.round(current_r,2))]

                                                                    frame:

                                                                        background "#aaaaaa"
                                                                        hbox:
                                                                            button:
                                                                                background "#3ffc45"
                                                                                action ToggleScreenVariable("bar_select", 2, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_g")

                                                                                if bar_select == 2:
                                                                                    input default current_g length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "G "+ "%.2f" % current_g style "serum_text_style" yalign 0.5 size 16
                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_g, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_g")
                                                                                unhovered [SetScreenVariable("current_g",__builtin__.round(current_g,2))]
                                                                    frame:

                                                                        background "#aaaaaa"
                                                                        hbox:
                                                                            button:
                                                                                background "#3f87fc"
                                                                                action ToggleScreenVariable("bar_select", 3, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_b")

                                                                                if bar_select == 3:
                                                                                    input default current_b length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "B "+ "%.2f" % current_b style "serum_text_style" yalign 0.5 size 16

                                                                                xsize 75
                                                                                ysize 45
                                                                            bar:
                                                                                adjustment ui.adjustment(range = 1.00, value = current_b, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_b")
                                                                                unhovered [SetScreenVariable("current_b",__builtin__.round(current_b,2))]

                                                                    frame:

                                                                        background "#aaaaaa"
                                                                        hbox:
                                                                            button:
                                                                                background "#111111"
                                                                                action ToggleScreenVariable("bar_select", 4, 0)
                                                                                hovered SetScreenVariable("bar_value", "current_a")

                                                                                if bar_select == 4:
                                                                                    input default current_a length 4 changed colour_changed_bar allow ".0123456789" style "serum_text_style" size 16
                                                                                else:
                                                                                    text "A "+ "%.2f" % current_a style "serum_text_style" yalign 0.5 size 16
                                                                                xsize 75
                                                                                ysize 45

                                                                            bar:

                                                                                adjustment ui.adjustment(range = 1.00, value = current_a, step = 0.1, changed = colour_changed_bar)
                                                                                xfill True
                                                                                ysize 45
                                                                                style style.slider

                                                                                hovered SetScreenVariable("bar_value", "current_a")
                                                                                unhovered [SetScreenVariable("current_a",__builtin__.round(current_a,2))]
                                                    if color_selection:
                                                        for block_count, colour_list in __builtin__.enumerate(split_list_in_blocks(persistent.colour_palette, 13)):
                                                            hbox:
                                                                spacing 0
                                                                yanchor (block_count * .1)

                                                                for count, a_colour in __builtin__.enumerate(colour_list):
                                                                    frame:
                                                                        background "#aaaaaa"
                                                                        padding [3, 3]
                                                                        button:
                                                                            background Color(rgb=(a_colour[0], a_colour[1], a_colour[2]))
                                                                            xysize (38, 38)
                                                                            sensitive True
                                                                            xalign True
                                                                            yalign True
                                                                            action [
                                                                                SetScreenVariable("current_r", a_colour[0]),
                                                                                SetScreenVariable("current_g", a_colour[1]),
                                                                                SetScreenVariable("current_b", a_colour[2]),
                                                                                SetScreenVariable("current_a", a_colour[3]),
                                                                                Function(update_outfit_color, selected_clothing),
                                                                                Function(preview_outfit)
                                                                            ]
                                                                            alternate [
                                                                                Function(update_colour_palette, count + (block_count * 13), current_r, current_g, current_b, current_a)
                                                                            ]
                                                # vbox:
                                                #     spacing 5
                                                #     hbox:
                                                #         frame:
                                                #             background "#aaaaaa"
                                                #             xfill True
                                                #             textbutton "Transparency":
                                                #                 style "textbutton_no_padding_highlight"
                                                #                 text_style "serum_text_style"
                                                #
                                                #                 xfill True
                                                #
                                                #                 action ToggleScreenVariable("transparency_selection")
                                                #     hbox:
                                                #         if transparency_selection:
                                                #             frame:
                                                #                 background "#aaaaaa"
                                                #                 ysize 50
                                                #                 viewport:
                                                #                     xfill True
                                                #                     draggable True
                                                #                     mousewheel "horizontal"
                                                #                     ysize 50
                                                #                     hbox:
                                                #                         spacing 5
                                                #                         textbutton "Normal":
                                                #                             style "textbutton_no_padding_highlight"
                                                #                             text_style "serum_text_style"
                                                #                             xalign 0.5
                                                #                             xsize 200
                                                #
                                                #                             if current_a == 1.0:
                                                #                                 background "#4f7ad6"
                                                #                             else:
                                                #                                 background "#1a45a1"
                                                #                             action [
                                                #                             SetScreenVariable("current_a", 1.0),
                                                #                             SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                #                             Function(preview_outfit)
                                                #                             ]
                                                #
                                                #                         textbutton "Sheer":
                                                #                             style "textbutton_no_padding_highlight"
                                                #                             text_style "serum_text_style"
                                                #                             xalign 0.5
                                                #                             xsize 200
                                                #                             if current_a == 0.95:
                                                #                                 background "#4f7ad6"
                                                #                             else:
                                                #                                 background "#1a45a1"
                                                #
                                                #                             action [
                                                #                             SetScreenVariable("current_a", 0.95),
                                                #                             SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                #                             Function(preview_outfit)
                                                #                             ]
                                                #
                                                #                         textbutton "Translucent":
                                                #                             style "textbutton_no_padding_highlight"
                                                #                             text_style "serum_text_style"
                                                #                             xalign 0.5
                                                #                             xsize 200
                                                #                             if current_a == 0.8:
                                                #                                 background "#4f7ad6"
                                                #                             else:
                                                #                                 background "#1a45a1"
                                                #
                                                #
                                                #                             action [
                                                #                             SetScreenVariable("current_a", 0.8),
                                                #                             SetField(selected_clothing, selected_colour,[current_r,current_g,current_b,current_a]),
                                                #                             Function(preview_outfit)
                                                #                             ]












                # vbox: #Items selector
                #     #W/ item customixing window at bottom
                #
            vbox:
                spacing 15
                frame:
                    xysize (540, 500)
                    background "#aaaaaa"
                    vbox:
                        spacing 5
                        grid 2 1:
                            xfill True
                            spacing 5
                            frame:
                                background "#888888"
                                xfill True
                                textbutton "View Outfit Stats":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("outfit_stats")
                            frame:
                                background "#888888"
                                xfill True
                                textbutton "Current Items":
                                    style "textbutton_no_padding"
                                    text_style "serum_text_style"
                                    xfill True

                                    action NullAction()

                        hbox:
                            spacing 5
                            vbox:
                                xalign 0.5
                                if outfit_stats:
                                    frame:
                                        background "#888888"
                                        yfill True
                                        viewport:
                                            draggable True
                                            mousewheel True
                                            yfill True
                                            xsize 250
                                            vbox:
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Sluttiness (Full Outfit): " + str(demo_outfit.slut_requirement) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    if demo_outfit.is_suitable_underwear_set():
                                                        text "Sluttiness (Underwear): " + str(demo_outfit.get_underwear_slut_score()) style "serum_text_style_traits"
                                                    else:
                                                        text "Sluttiness (Underwear): Invalid" style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    if demo_outfit.is_suitable_overwear_set():
                                                        text "Sluttiness (Overwear): " + str(demo_outfit.get_overwear_slut_score()) style "serum_text_style_traits"
                                                    else:
                                                        text "Sluttiness (Overwear): Invalid" style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Tits Visible: " + str(demo_outfit.tits_visible()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Tits Usable: " + str(demo_outfit.tits_available()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Wearing a Bra: " + str(demo_outfit.wearing_bra()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Bra Covered: " + str(demo_outfit.bra_covered()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Pussy Visible: " + str(demo_outfit.vagina_visible()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Pussy Usable: " + str(demo_outfit.vagina_available()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Wearing Panties: " + str(demo_outfit.wearing_panties()) style "serum_text_style_traits"
                                                frame:
                                                    background "#000080"
                                                    xsize 250
                                                    padding [1,1]
                                                    text "Panties Covered: " + str(demo_outfit.panties_covered()) style "serum_text_style_traits"

                                                # DEBUG CODE TO SEE WHAT IS SELECTED WHEN WE CLICK AROUND
                                                # frame:
                                                #     background "#007000"
                                                #     xsize 250
                                                #     padding [1,1]
                                                #     if (selected_from_outfit):
                                                #         text "From outfit: " + selected_from_outfit.name style "serum_text_style_traits"
                                                # frame:
                                                #     background "#007000"
                                                #     xsize 250
                                                #     padding [1,1]
                                                #     if (selected_clothing):
                                                #         text "Seletect Item: " + selected_clothing.name style "serum_text_style_traits"



                            vbox:
                                frame:
                                    background "#888888"

                                    xfill True
                                    viewport:
                                            scrollbars "vertical"
                                            mousewheel True
                                            yfill True
                                            xfill True
                                            vbox:

                                                spacing 5 #TODO: Add a viewport here too.
                                                for cloth in item_outfit.upper_body + item_outfit.lower_body + item_outfit.feet + item_outfit.accessories:
                                                    if not cloth.is_extension: #Don't list extensions for removal.
                                                        button:
                                                            background Color(rgb = (cloth.colour[0], cloth.colour[1], cloth.colour[2]))

                                                            action [ # NOTE: Left click makes more sense for selection than right clicking

                                                                SetScreenVariable("selected_from_outfit", cloth),
                                                                SetScreenVariable("category_selected", get_category(cloth)),
                                                                SetScreenVariable("selected_clothing", cloth),
                                                                Function(preview_apply, cloth),

                                                                #Function(preview_restore, cloth),
                                                                SetScreenVariable("current_r",cloth.colour[0]),
                                                                SetScreenVariable("current_g",cloth.colour[1]),
                                                                SetScreenVariable("current_b",cloth.colour[2]),
                                                                SetScreenVariable("current_a",cloth.colour[3]),

                                                                Function(preview_outfit) # Make sure it is showing the correct outfit during changes, demo_outfit is a copy of starting_outfit
                                                            ]
                                                            alternate [
                                                                Function(item_outfit.remove_clothing, cloth),
                                                                Function(demo_outfit.remove_clothing, cloth),
                                                                Function(preview_outfit)
                                                            ]
                                                            xalign 0.5
                                                            xfill True
                                                            yfill True
                                                            text cloth.name xalign 0.5 yalign 0.5 xfill True yfill True style "custom_outfit_style"


                frame:
                    background "#aaaaaa"

                    xysize (540, 500)
                    #padding (20,20)
                    hbox:
                        spacing 5
                        vbox:
                            hbox:
                                spacing 5
                                vbox:
                                    spacing 5
                                    frame:
                                        background "#888888"
                                        xsize 250
                                        vbox:
                                            xalign 0.5
                                            textbutton "Save Outfit":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                    Function(update_outfit_name, item_outfit),
                                                    Return(item_outfit),
                                                    Hide("mannequin"),
                                                    Hide("outfit_creator")
                                                ]

                                            textbutton "Abandon / Exit":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                action [
                                                    Return("Not_New"),
                                                    Hide("mannequin"),
                                                    Hide("outfit_creator")
                                                ]
                                    frame:
                                        background "#888888"
                                        xsize 250
                                        vbox:
                                            xalign 0.5
                                            textbutton ("Export to [selected_xml]" if mannequin == "mannequin" else "Add to [mannequin.name] wardrobe"):
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True

                                                if mannequin == "mannequin":
                                                    action [
                                                        Function(custom_log_outfit, item_outfit, outfit_class = outfit_class_selected,
                                                        wardrobe_name = selected_xml),
                                                        Function(renpy.notify, "Outfit exported to " + selected_xml + "]")
                                                    ]

                                                else:
                                                    if outfit_type == "full":
                                                        action [
                                                            Function(mannequin.wardrobe.add_outfit, get_outfit_copy_with_name(item_outfit)),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]
                                                    elif outfit_type == "over":
                                                        action [
                                                            Function(mannequin.wardrobe.add_overwear_set, get_outfit_copy_with_name(item_outfit)),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]

                                                    elif outfit_type == "under":
                                                        action [
                                                            Function(mannequin.wardrobe.add_underwear_set, get_outfit_copy_with_name(item_outfit)),
                                                            Function(renpy.notify, "Outfit added to " + mannequin.name + " wardrobe")
                                                        ]

                                            textbutton "Type: [outfit_class_selected]":
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                action NullAction()
                                                # action [
                                                # If(outfit_class_selected == "FullSets", SetScreenVariable("outfit_class_selected", "OverwearSets")),
                                                # If(outfit_class_selected == "OverwearSets", SetScreenVariable("outfit_class_selected", "UnderwearSets")),
                                                # If(outfit_class_selected == "UnderwearSets", SetScreenVariable("outfit_class_selected", "FullSets"))
                                                # ]
                                                # alternate [
                                                # If(outfit_class_selected == "FullSets", SetScreenVariable("outfit_class_selected", "UnderwearSets")),
                                                # If(outfit_class_selected == "OverwearSets", SetScreenVariable("outfit_class_selected", "FullSets")),
                                                # If(outfit_class_selected == "UnderwearSets", SetScreenVariable("outfit_class_selected", "OverwearSets"))
                                                # ]
                                    frame:
                                        background "#888888"
                                        xsize 250
                                        vbox:
                                            textbutton "Generate [outfit_class_selected]":
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                action [
                                                    Function(set_generated_outfit, category_selected, slut_generation)
                                                ]

                                            hbox:
                                                button:
                                                    background "#505050"
                                                    text "Slut "+ str(slut_generation) style "serum_text_style" yalign 0.5
                                                    xsize 90
                                                    ysize 45
                                                bar:
                                                    adjustment ui.adjustment(range = max_slut, value = slut_generation, step = 1, changed = update_slut_generation)
                                                    xfill True
                                                    ysize 45
                                                    style style.slider

                                    $ love_list = outfit_builder.get_love_list()
                                    $ hate_list = outfit_builder.get_hate_list()
                                    if outfit_builder and len(love_list + hate_list) > 0:
                                        frame:
                                            background "#888888"
                                            xsize 250
                                            vbox:
                                                spacing 0
                                                frame:
                                                    background "#000080"
                                                    xsize 240
                                                    padding [1,1]
                                                    text "Preferences:" style "serum_text_style_traits"
                                                viewport:
                                                    scrollbars "vertical"
                                                    draggable True
                                                    mousewheel True
                                                    yfill True
                                                    xsize 240
                                                    vbox:
                                                        if __builtin__.len(love_list) > 0:
                                                            for pref in love_list:
                                                                frame:
                                                                    background "#007000"
                                                                    xsize 220
                                                                    padding [1,1]
                                                                    text pref style "serum_text_style_traits"
                                                        if __builtin__.len(hate_list) > 0:
                                                            for pref in hate_list:
                                                                frame:
                                                                    background "#930000"
                                                                    xsize 220
                                                                    padding [1,1]
                                                                    text pref style "serum_text_style_traits"

                                vbox:

                                    frame:
                                        background "#888888"
                                        xfill True
                                        vbox:
                                            textbutton "Import Design":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5

                                                if import_selection:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [
                                                ToggleScreenVariable("import_selection"),
                                                If(mannequin_selection or mannequin_poser, [SetScreenVariable("mannequin_selection", False), SetScreenVariable("mannequin_poser", False)])
                                                ]

                                            textbutton "Mannequin Selection":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5

                                                if mannequin_selection:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [
                                                ToggleScreenVariable("mannequin_selection"),
                                                If(import_selection or mannequin_poser, [SetScreenVariable("import_selection", False), SetScreenVariable("mannequin_poser", False)])
                                                ]

                                            textbutton "Mannequin Poser":
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"
                                                xfill True
                                                xalign 0.5
                                                if mannequin_poser:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"


                                                action [
                                                    SensitiveIf(mannequin != "mannequin"),
                                                    ToggleScreenVariable("mannequin_poser"),
                                                    If(import_selection or mannequin_selection, [SetScreenVariable("import_selection", False), SetScreenVariable("mannequin_selection", False)])
                                                ]

                                    if import_selection:
                                        frame:
                                            background "#888888"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    for n in get_xml_files_from_path():
                                                        textbutton n:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if selected_xml == n:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                                Show("import_outfit_manager", None, target_wardrobe, n)
                                                            ]
                                                            alternate [ #Right clicking selects the path that outfits should be exported to
                                                            SetVariable("selected_xml", n)
                                                            ]

                                    if mannequin_selection:
                                        frame:
                                            background "#888888"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    textbutton "Default Mannequin":
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        xfill True
                                                        xalign 0.5

                                                        action [
                                                            SetScreenVariable("mannequin", "mannequin"),
                                                            SetScreenVariable("outfit_builder", WardrobeBuilder(None)),
                                                            Function(preview_outfit)
                                                        ]
                                                    for person in sorted(known_people_in_the_game(), key = lambda x: x.name):
                                                        textbutton person.name:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if mannequin == person:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                                SetScreenVariable("mannequin", person),
                                                                SetScreenVariable("outfit_builder", WardrobeBuilder(person)),
                                                                Function(preview_outfit)
                                                            ]

                                    if mannequin_poser:
                                        frame:
                                            background "#888888"
                                            xfill True
                                            viewport:
                                                scrollbars "vertical"
                                                mousewheel True
                                                draggable True
                                                vbox:
                                                    for x in sorted(["stand2","stand3","stand4","stand5","walking_away","kissing","kneeling1","doggy","missionary","blowjob","against_wall","back_peek","sitting","standing_doggy","cowgirl"]):
                                                        textbutton x:
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True
                                                            xalign 0.5

                                                            if mannequin_pose == x:
                                                                background "#4f7ad6"
                                                                hover_background "#4f7ad6"

                                                            action [
                                                            SetScreenVariable("mannequin_pose", x),
                                                            Function(preview_outfit)
                                                            ]

                                                            alternate NullAction()
        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xanchor 1.0
            xalign 1.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"outfit_tutorial")


        $ outfit_tutorial_length = 8 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["outfit_tutorial"] > 0 and mc.business.event_triggers_dict["outfit_tutorial"] <= outfit_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/outfit_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["outfit_tutorial"])+".png"
                hover "/tutorial_images/outfit_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["outfit_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"outfit_tutorial")
