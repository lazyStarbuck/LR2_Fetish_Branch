init python:
  def set_pos_align(trans, xchange, ychange):
    trans.xalign = xchange
    trans.yalign = ychange
    return None


transform threesome_test_1():
    function set_pos_align
    zoom 1.0

transform threesome_test_2():
    function set_pos_align
    zoom 1.0

init -1 python:
    list_of_threesomes = []
    girl_swap_pos = False  #Nasty hack to tell threesome code to swap girl 1 and girl 2. #TODO find a better way to do this
    class Threesome_Position(renpy.store.object):
        def __init__(self,name,slut_requirement,position_one_tag, position_two_tag,girl_one_final_description,girl_two_final_description,requires_location,requirements,
        p1_transform, p2_transform, can_swap = False, verb = "fuck" ):
            self.name = name
            self.slut_requirement = slut_requirement #The required slut score of the girl. Obedience will help fill the gap if possible, at a happiness penalty. Value from 0 (almost always possible) to ~100
            self.position_one_tag = position_one_tag # The tag used to get the correct position image set
            self.position_two_tag = position_two_tag # The tag used to get the correct position image set
            self.girl_one_final_description = girl_one_final_description   #Textual position description if girl one is the final one in position
            self.girl_two_final_description = girl_two_final_description      #textual position description if girl two is the final one in position
            self.requires_location = requires_location #
            self.requirements = requirements        #The requirements to run this position. Should be a function
            self.mc_position = []                   #Holds the positions that MC can take during this position
            self.verb = verb #A verb used to describe the position. "Fuck" is default, and mostly used for sex positions or blowjobs etc. Kiss, Fool around, etc. are also possibilities.
            self.current_modifier = None #We will update this if the posisiion has a special modifier that shoudl be applied, like blowjob.
            self.p1_transform = p1_transform
            self.p2_transform = p2_transform
            self.can_swap = can_swap

        def create_scene(self, the_person_one, the_person_two):
            scene_manager.add_actor(the_person_one, position = self.position_one_tag, character_placement = self.p1_transform)
            scene_manager.add_actor(the_person_two, position = self.position_two_tag, character_placement = self.p2_transform)
            scene_manager.draw_scene()
            return

        def align_position(self, the_person_one, the_person_two):
            scene_manager.draw_scene()
            return

        def redraw_scene(self, the_person_one, the_person_two):
            scene_manager.draw_scene()
            return




    class Threesome_MC_position(renpy.store.object):
        def __init__(self,name,description,skill_tag_p1,skill_tag_p2,girl_one_arousal,girl_two_arousal,girl_one_source,girl_two_source,girl_one_energy,girl_two_energy,
        guy_arousal,skill_tag_guy,guy_source,guy_energy,intro,scenes,outro,strip_description,strip_ask_description,orgasm_description,swap_description,requirement):
            self.name = name
            self.description = description #Describes the position the MC is in
            self.skill_tag_p1 = skill_tag_p1 #The skill that will provide a bonus to this for girl 1
            self.skill_tag_p2 = skill_tag_p2 #The skill that will provide a bonus to this for girl 2
            self.girl_one_arousal = girl_one_arousal # The base arousal the girl recieves from this position.
            self.girl_two_arousal = girl_two_arousal # The base arousal the girl recieves from this position.
            self.girl_one_source = girl_one_source  #Who is giving girl 1 pleasure. 0 = MC, 1 = herself, 2 = girl 2
            self.girl_two_source = girl_two_source  #Who is giving girl 2 pleasure. 0 = MC, 1 = girl 1, 2 = herself
            self.girl_one_energy = girl_one_energy  #energy cost for girl 1
            self.girl_two_energy = girl_two_energy  #energy cost for girl 2
            self.guy_arousal = guy_arousal # The base arousal the guy recieves from this position.
            self.skill_tag_guy = skill_tag_guy #The skill that will decide how much arousal MC receives.
            self.guy_source = guy_source # Who is giving MC pleasure. 0 = MC, 1 = girl 1, 2 = girl 2
            self.guy_energy = guy_energy #Energy burn for guy
            self.intro = intro
            self.scenes = scenes
            self.outro = outro
            self.strip_description = strip_description
            self.strip_ask_description = strip_ask_description
            self.orgasm_description = orgasm_description
            self.swap_description = swap_description
            self.requirement = requirement

        def call_intro(self, the_person_one, the_person_two, the_location, the_object, round):
            renpy.call(self.intro,the_person_one, the_person_two, the_location, the_object, round)

        def call_scene(self, the_person_one, the_person_two, the_location, the_object, round):
            random_scene = renpy.random.randint(0,len(self.scenes)-1)
            renpy.call(self.scenes[random_scene],the_person_one, the_person_two, the_location, the_object, round)

        def call_orgasm(self, the_person_one, the_person_two, the_location, the_object, round):
            renpy.call(self.orgasm_description,the_person_one, the_person_two, the_location, the_object, round)

        def call_outro(self, the_person_one, the_person_two, the_location, the_object, round):
            renpy.call(self.outro,the_person_one, the_person_two, the_location, the_object, round)

        def call_transition(self, the_person_one, the_person_two, the_location, the_object, round):
            renpy.call(self.swap_description,the_person_one, the_person_two, the_location, the_object, round)

label threesome_test():
    call join_threesome(mom, lily, "missionary") from threesome_test_call_1
    return "Test Complete"

label threesome_alignment():
    $ position_choice = threesome_double_blowjob
    $ position_choice.create_scene(mom, lily)
    $ finished = False
    while not finished:
        menu:
            "mom + x":
                $ position_choice.p1_transform.xpos += .01
                pass
            "mom - x":
                $ position_choice.p1_transform.xpos -= .01
                pass
            "mom + y":
                $ position_choice.p1_transform.yalign += .01
                pass
            "mom - y":
                $ position_choice.p1_transform.yalign -= .01
                pass
            "mom + zoom":
                $ position_choice.p1_transform.zoom += .01
                pass
            "mom - zoom":
                $ position_choice.p1_transform.zoom -= .01
                pass
            "lily + x":
                pass
            "lily - x":
                pass
            "lily + y":
                pass
            "lily - y":
                pass
            "lily + zoom":
                pass
            "lily - zoom":
                pass
        $ position_choice.align_position(the_person_one, the_person_two)  #This doesn't work lol. Delete? I hate transforms

label start_threesome(the_person_one, the_person_two, start_position = None, start_object = None, round = 0, private = True, girl_in_charge = False, position_locked = False, report_log = None, affair_ask_after = True, hide_leave = False):
    # When called
    if report_log is None:
        $ report_log = defaultdict(int) #Holds information about the encounter: what positiosn were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = ["Threesome"] #This is a list, not an int.

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = None
    $ object_choice = None

    #Family situational modifiers
    #Omitting these for now

    #Cheating modifiers
    #Also leaving these out

    #Privacy modifiers

    #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.

    #If no initial position set, get one now
    if start_position == None:
        call pick_threesome(the_person_one, the_person_two) from threesome_initial_position_set
        $ position_choice = _return
    else:
        $ position_choice = start_position
    #pick_threesome can give use the option to swap the girls opening spots
    if girl_swap_pos:
        $ the_person = the_person_one
        $ the_person_one = the_person_two
        $ the_person_two = the_person
        $ int_swap = report_log["girl one orgasms"]
        $ report_log["girl one orgasms"] = report_log["girl two orgasms"]
        $ report_log["girl two orgasms"] = int_swap

    #TODO fix this fucking stupid hack
    $ scene_manager.remove_actor(the_person_one, reset_actor = False)
    $ scene_manager.remove_actor(the_person_two, reset_actor = False)
    #end TODO

    $ position_choice.create_scene(the_person_one, the_person_two)
    "As the girls get into position, you consider how to begin your threesome."
    $ option_list = []
    python:
        for options in position_choice.mc_position:
            if options.requirement(the_person_one, the_person_two):
                option_list.append([options.description,options.name])
            pass
    $ option_list.append(["Change your mind and leave.", "Leave"])
    $ round_choice = None # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ active_mc_position = None
    $ round_choice = renpy.display_menu(option_list,True,"Choice")
    if round_choice == "Leave":
        "Really? You changed your mind? You leave the poor girls after you got them all ready for some action."
    else:
        python:
            for options in position_choice.mc_position:
                if round_choice == options.name:
                    active_mc_position = options
        if active_mc_position == None:
            "Something broke..."
            $ round_choice = "Leave"
        else:
            $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice, round)
    while not finished:
        # if girl_in_charge:
        #     # For now, default to guys only in charge
        if round_choice is None: #If there is no set round_choice
            #TODO: Add a varient of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            $ option_list = []
            python:
                if position_choice is not None:
                    if active_mc_position is not None:
                        option_list.append(["Keep going.","Continue"]) #Note: you're prevented from continuing if the energy cost would be too high by the pre-round checks.


                    option_list.append(["Pause and strip her down.","Strip"])

                    #Give option for MC to change position without changing the girls positions
                    for options in position_choice.mc_position:
                        if options != active_mc_position:
                            if options.requirement(the_person_one, the_person_two):
                                option_list.append([options.description,options.name])

                    if not position_locked and object_choice:
                        option_list.append(["Pause and change position.\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                        ##### For now, no implemantation of connections
                        # for position in position_choice.connections:
                        #     if object_choice.has_trait(position.requires_location):
                        #         appended_name = "Transition to " + position.build_position_willingness_string(the_person) #Note: clothing and energy checks are done inside of build_position_willingness, invalid positiosn marked (disabled)
                        #         option_list.append([appended_name,position])

                    if not hide_leave: #TODO: Double check that we can always get out
                        option_list.append(["Stop fucking and leave.", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

                else:
                    if not position_locked:
                        option_list.append(["Pick a new position.\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                    if not hide_leave:
                        option_list.append(["Stop and leave.", "Leave"])

            $ round_choice = renpy.display_menu(option_list,True,"Choice") #This gets the players choice for what to do this round.


        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignroe all of that
                "You decide to change it up."
                call pick_threesome(the_person_one, the_person_two) from threesome_mid_position_set
                $ position_choice = _return
                if girl_swap_pos:
                    $ the_person = the_person_one
                    $ the_person_one = the_person_two
                    $ the_person_two = the_person
                    $ int_swap = report_log["girl one orgasms"]
                    $ report_log["girl one orgasms"] = report_log["girl two orgasms"]
                    $ report_log["girl two orgasms"] = int_swap
                #TODO fix this fucking stupid hack
                $ scene_manager.remove_actor(the_person_one, reset_actor = False)
                $ scene_manager.remove_actor(the_person_two, reset_actor = False)
                #end TODO
                $ position_choice.create_scene(the_person_one, the_person_two)
                "As the girls get into position, you consider how to resume your threesome."
                $ option_list = []
                python:
                    for options in position_choice.mc_position:
                        if options.requirement(the_person_one, the_person_two):
                            option_list.append([options.description,options.name])
                $ option_list.append(["Change your mind and leave.", "Leave"])
                $ round_choice = None # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
                $ active_mc_position = None
                $ round_choice = renpy.display_menu(option_list,True,"Choice")
                if round_choice == "Leave":
                    $ finished = True
                    "You decide to finish the threesome instead."

                python:
                    for options in position_choice.mc_position:
                        if round_choice == options.name:
                            active_mc_position = options
                if active_mc_position == None:
                    "Something broke..."
                    $ finished = True
                else:
                    $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice, round)

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            if position_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call threesome_round(the_person_one, the_person_two, position_choice = active_mc_position, object_choice = None, private = private, report_log = report_log) from _call_threesome_round_1
                $ first_round = False
                if not active_mc_position.requirement(the_person_one, the_person_two):
                    "Your post orgasm cock softens, stopping you from continuing for now."
                    $ position_choice = None
                    $ active_mc_position = None
                elif active_mc_position.guy_energy > mc.energy:
                    "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                    $ active_mc_position = None
                elif active_mc_position.girl_one_energy > the_person_one.energy:

                    the_person_one.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_two.energy > 20:
                        #TODO give option to continue fucking the second girl
                        pass
                    else:
                        the_person_two.char "Yeah me too. I think I need a break!"
                        $ finished = True
                elif active_mc_position.girl_two_energy > the_person_two.energy:
                    the_person_two.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_one.energy > 20:
                        #TODO give option to continue fucking the second girl
                        pass
                    else:
                        the_person_one.char "Yeah me too. I think I need a break!"
                        $ finished = True
                #else: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                #for now disable stripping
                    #pass
                    #call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event




        elif round_choice == "Strip":
            #currently not implemented
            call threesome_strip_menu(the_person_one, the_person_two) from _call_strip_menu_threesome_1

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end


        elif round_choice == "Girl Leave":
            $ finished = True
        #Need to catch position changes here.
        else:
            python:
                for options in position_choice.mc_position:
                    if options.name == round_choice:
                        active_mc_position = options
                        active_mc_position.call_transition(the_person_one, the_person_two, mc.location, object_choice, round)

        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the begining of the loop we can set a mandatory choice for the first one.


    # Teardown the sex modifiers

    if report_log["girl one orgasms"] > 0:
        $ the_person_one.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_one.arousal = (the_person_one.arousal / 2)
    if report_log["girl two orgasms"] > 0:
        $ the_person_two.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_two.arousal = (the_person_two.arousal / 2)



    $ mc.condom = False
    $ mc.recently_orgasmed = False

    if affair_ask_after and private and ask_girlfriend_requirement(the_person_one) is True and not the_person_one.relationship == "Single":
        if the_person_one.love >= 60 and the_person_one.sluttiness >= 30 - (the_person_one.get_opinion_score("cheating on men") * 5): #If she loves you enoguh, is moderately slutty, and you made her cum
            call affaire_check(the_person_one, report_log) from _call_affaire_check_threesome_one


    python: #Log all of the different classes of sex, but only once per class.
        if the_person_one.sex_record.get("Threesomes", 0) == 0:
            the_person_one.sex_record["Threesomes"] = 1
        else:
            the_person_one.sex_record["Threesomes"] += 1
        if the_person_two.sex_record.get("Threesomes", 0) == 0:
            the_person_two.sex_record["Threesomes"] = 1
        else:
            the_person_two.sex_record["Threesomes"] += 1


    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label threesome_round(the_person_one, the_person_two, position_choice, round = 0, object_choice = None, private = True, report_log = None):
    #Draw event before calling this scene

    #Normal round events
    $ position_choice.call_scene(the_person_one, the_person_two, mc.location, object_choice, round)
    # TODO listener event, to log events for challenge
    if report_log is not None:
        $ report_log["total rounds"] += 1

    #Calculate arousal gains
    $ girl_one_arousal_change = position_choice.girl_one_arousal + ((the_person_one.get_opinion_score("threesomes") / 5) * position_choice.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
    if position_choice.girl_one_source == 0:  #MC is source#
        $ girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level
    elif position_choice.girl_one_source == 1: #Girl one is her own source? Maybe masturbating?
        $ girl_one_arousal_change += girl_one_arousal_change * the_person_one.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level
    else:  #Assume girl 2 is source
        $ girl_one_arousal_change += girl_one_arousal_change * the_person_two.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level

    $ the_person_one.change_arousal(girl_one_arousal_change)  #Make the change
    #Repeat for girl two
    $ girl_two_arousal_change = position_choice.girl_two_arousal + ((the_person_two.get_opinion_score("threesomes") / 5) * position_choice.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
    if position_choice.girl_two_source == 0:  #MC is source#
        $ girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level
    elif position_choice.girl_one_source == 1: #Girl 1 is source
        $ girl_two_arousal_change += girl_two_arousal_change * the_person_one.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level
    else:  #Assume girl 2 is source
        $ girl_two_arousal_change += girl_two_arousal_change * the_person_two.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level

    $ the_person_two.change_arousal(girl_two_arousal_change)  #Make the change

    #MC arousal change
    $ his_arousal_change = position_choice.guy_arousal
    if position_choice.guy_source == 0:
        $ his_arousal_change += 0.1 * mc.sex_skills[position_choice.skill_tag_guy]
    elif position_choice.guy_source == 1:
        $ his_arousal_change += 0.1 * the_person_one.sex_skills[position_choice.skill_tag_guy]
    else:
        $ his_arousal_change += 0.1 * the_person_two.sex_skills[position_choice.skill_tag_guy]


    $ mc.change_arousal(his_arousal_change)
    #Erection changes
    if mc.recently_orgasmed and mc.arousal >= 10:
        $ mc.recently_orgasmed = False
        "Your cock stiffens again, coaxed back to life by the girls."

    #Energy Changes
    $ mc.change_energy(-position_choice.guy_energy)
    $ the_person_one.change_energy(-position_choice.girl_one_energy)
    $ the_person_two.change_energy(-position_choice.girl_two_energy)

    #If girl(s) orgasms, call orgasm scene
    if the_person_one.arousal >= the_person_one.max_arousal or the_person_two.arousal >= the_person_two.max_arousal:
        $ position_choice.call_orgasm(the_person_one, the_person_two, mc.location, object_choice, round)

        if the_person_one.arousal >= the_person_one.max_arousal:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_one)
            $ the_person_one.change_arousal(-the_person_one.arousal/2)
            $ report_log["girl one orgasms"] += 1
            $ report_log["total orgasms"] += 1
        if the_person_two.arousal >= the_person_two.max_arousal:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_two)
            $ the_person_two.change_arousal(-the_person_two.arousal/2)
            $ report_log["girl two orgasms"] += 1
            $ report_log["total orgasms"] += 1

    #If MC orgasms, call outro
    if mc.arousal >= mc.max_arousal:
        $ position_choice.call_outro(the_person_one, the_person_two, mc.location, object_choice, round)
        $ the_person_one.change_obedience(3)
        $ the_person_two.change_obedience(3)
        $ mc.reset_arousal()
        $ mc.recently_orgasmed = True
        $ report_log["guy orgasms"] += 1
        $ report_log["total orgasms"] += 1

    #TODO set public sex responses

    return

label pick_threesome(the_person_one, the_person_two, girl_one_position = None, object_choice = None):  #We can pass in a position for girl one if the second girl "walks in" on the sex event
    $ girl_two_list = []
    $ position_choice = None
    if girl_one_position == None:
        python:
            girl_one_choice = None
            girl_one_list = []
            for threeway in list_of_threesomes:
                if threeway.requirements(the_person_one, the_person_two):
                    if (get_initial_threesome_pairing(threeway.position_one_tag)) not in girl_one_list: #This doesn't work for stand2-5 TODO
                        girl_one_list.append(get_initial_threesome_pairing(threeway.position_one_tag))
                    if (get_initial_threesome_pairing(threeway.position_two_tag)) not in girl_one_list:
                        girl_one_list.append(get_initial_threesome_pairing(threeway.position_two_tag))
        "What do you want [the_person_one.title] to do?"
        $ girl_one_choice = renpy.display_menu(girl_one_list,True,"Choice")
    else:
        $ girl_one_choice = girl_one_position
    python:
        for threeway in list_of_threesomes:
            if threeway.requirements(the_person_one, the_person_two):
                if threeway.position_one_tag == girl_one_choice:            #Look for positions that match with any position taken by girl 1
                    girl_two_list.append([threeway.girl_two_final_description, threeway.position_two_tag])
                elif threeway.position_two_tag == girl_one_choice:
                    girl_two_list.append([threeway.girl_one_final_description, threeway.position_one_tag])
    "What do you want [the_person_two.title] to do?"
    if len(girl_two_list) == 0:
        "Something has gone wrong, no available positions"  #Return something default?
    $ girl_two_choice = renpy.display_menu(girl_two_list,True,"Choice")

    python:
        for threeway in list_of_threesomes:
            if girl_one_choice == threeway.position_one_tag and girl_two_choice == threeway.position_two_tag:
                position_choice = threeway
                girl_swap_pos = False
            if girl_one_choice == threeway.position_two_tag and girl_two_choice == threeway.position_one_tag:
                position_choice = threeway
                girl_swap_pos = True
    #TODO figure out if position requires an object, if so select the object#
    return position_choice

label threesome_strip_menu(the_person_one, the_person_two):
    $ strip_menu = []
    $ strip_menu.append (["Finished Stripping", "leave"])
    if the_person_one.outfit.tits_available() and the_person_one.outfit.vagina_available():
        pass
    else:
        $ strip_menu.append (["Strip " + the_person_one.title, "strip_one"])
    if the_person_two.outfit.tits_available() and the_person_two.outfit.vagina_available():
        pass
    else:
        $ strip_menu.append (["Strip " + the_person_two.title, "strip_two"])
    $ strip_choice = renpy.display_menu(strip_menu,True,"Choice")
    if strip_choice == "strip_one":
        mc.name "[the_person_one.title], I want you to get naked now."
        the_person_one.char "Of course!"
        $ scene_manager.strip_actor_outfit(the_person_one, exclude_feet = False)
        "[the_person_one.title] is now naked."
        $ scene_manager.draw_scene()
    elif strip_choice == "strip_two":
        mc.name "[the_person_two.title], I want you to get naked now."
        the_person_two.char "Sounds good!"
        $ scene_manager.strip_actor_outfit(the_person_two, exclude_feet = False)
        "[the_person_two.title] is now naked."
        $ scene_manager.draw_scene()
    else:
        return
    call threesome_strip_menu(the_person_one, the_person_two) from _threesome_recurrent_strip_call_1
    return

label can_join_threesome(the_person_one, the_person_two, intial_position): #Can use this function to check if there is a threesome position available that a second girl can join.
    $ return_bool = False
    python:
        for threeway in list_of_threesomes:
            if threeway.requirements(the_person_one, the_person_two):
                if threeway.position_one_tag == girl_one_choice:            #Look for positions that match with any position taken by girl 1
                    return_bool =  True
                elif threeway.position_two_tag == girl_one_choice:
                    return_bool =  True
    return return_bool                                                          #No acceptable position found, cannot join threesome

label join_threesome(the_person_one, the_person_two, initial_position):  #We can use this function to add a second girl to an existing sex scene.
                                                                         #Works by selecting a position then calling threesome with the first position pre-set

    call pick_threesome(the_person_one, the_person_two, girl_one_position = initial_position) from _join_threesome_position_selection_1
    $ position_choice = _return
    call start_threesome(the_person_one, the_person_two, start_position = position_choice, private = False) from _join_threesome_in_progress_1

    return


init python:
    def get_initial_threesome_pairing(position_tag):
        if position_tag == "stand2" or position_tag == "stand3" or position_tag == "stand4" or position_tag == "stand5":
            return (["Stand Right There", "stand"])  #TODO this probably isn't going to work right. Figure out another way to do this. Or don't write positions using standX?
        elif position_tag == "walking_away":
            return (["Turn Away From Me", "walking_away"])
        elif position_tag == "kissing":
            return (["Put Your Arms Up", "kissing"])
        elif position_tag == "missionary":
            return (["Lay on Your Back", "missionary"])
        elif position_tag == "blowjob":
            return (["Get on Your Knees", "blowjob"])
        elif position_tag == "against_wall":
            return (["Put Your Back to the Wall", "against_wall"])
        elif position_tag == "back_peek":
            return (["Turn Away But Look At Me", "back_peek"])
        elif position_tag == "sitting":
            return (["Sit Down", "sitting"])
        elif position_tag == "kneeling1":
            return (["Lay Forward", "kneeling1"])
        elif position_tag == "standing_doggy":
            return (["Bend Over", "standing_doggy"])
        elif position_tag == "cowgirl":
            return (["Sit on Top", "cowgirl"])
        else:
            return (["Broken Position", "stand4"])
