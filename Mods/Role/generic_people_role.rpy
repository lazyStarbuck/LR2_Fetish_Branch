init 2 python:
    # Schedule Person | Allows you to modify the schedule of the_person. Change requirement to be dependent on obedience?
    schedule_actions_list = [] # NOTE: Use this list to display all the schedule actions.
    # Follow Me | Allows you to put a person in a list_of_followers that comes along with you upon every location change (follow normal schedule on time advance, might want to remove them from the list during that, although they will come back if not)
    list_of_followers = []

    # Build a location list where the person can be scheduled.
    def build_schedule_location_list(person):
        possible_locations = []

        def add_location(location, add_when_not_visible = False):
            if location.visible or add_when_not_visible:
                if not location in possible_locations:
                    possible_locations.append(location)

        # person home
        add_location(person.home, add_when_not_visible = True)
        # add the mall and all its connections
        add_location(mall)
        for c in mall.connections:
            add_location(c)
        # add employee locations
        if person.is_employee():
            add_location(lobby)
            for c in lobby.connections:
                add_location(c)
        # special character mom and lily locations
        if person in [mom, lily]:
            add_location(hall)
            for c in hall.connections:
                add_location(c)
        # special character aunt and cousing locations
        if person in [aunt, cousin]:
            add_location(aunt_apartment)
            for c in aunt_apartment.connections:
                add_location(c)

        return possible_locations

    # Schedule Person Requirements
    def schedule_person_requirement(person):
        if person.obedience >= 130:
            return True
        return False

    def schedule_early_morning_requirement():
        return True
    def schedule_morning_requirement():
        return True
    def schedule_afternoon_requirement():
        return True
    def schedule_evening_requirement():
        return True
    def schedule_night_requirement():
        if person.obedience >=150:
            return True
        else:
            return "Requires: 150 Obedience"

    # Follow Me Requirements
    def start_follow_requirement(person):
        if person not in list_of_followers:
            if person.obedience >= 110:
                return True
        return False

    def stop_follow_requirement(person):
        if person in list_of_followers:
            return True
        return False

    # Hire Person Requirements
    def hire_person_requirement(person):
        if person not in mc.business.get_employee_list():
            return True
        return False

    # Rename Person Requirements
    def rename_person_requirement(person):
        if person.obedience >= 150:
            return True
        return False

    def spend_the_night_requirement(person):
        if time_of_day is 4 and person.love > 50 and mc.location is person.home: #Has to be night, need to have some love and be in the_person's home location
            return True
        return False
    # Schedule Actions
    schedule_person_action = Action("Schedule [the_person.title]", schedule_person_requirement, "schedule_menu", menu_tooltip = "Schedule where the person should be throughout the day.")
    schedule_early_morning_action = Action("Early Morning", schedule_early_morning_requirement, "schedule_early_morning", menu_tooltip = "Schedule where the person should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning_action)
    schedule_morning_action = Action("Morning", schedule_morning_requirement, "schedule_morning", menu_tooltip = "Schedule where the person should be during the Morning.")
    schedule_actions_list.append(schedule_morning_action)
    schedule_afternoon_action = Action("Afternoon", schedule_afternoon_requirement, "schedule_afternoon", menu_tooltip = "Schedule where the person should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon_action)
    schedule_evening_action = Action("Evening", schedule_evening_requirement, "schedule_evening", menu_tooltip = "Schedule where the person should be during the Evening.")
    schedule_actions_list.append(schedule_evening_action)
    schedule_night_action = Action("Night", schedule_night_requirement, "schedule_night", menu_tooltip = "Schedule where the person should be during the Night.")
    schedule_actions_list.append(schedule_night_action)

    start_follow_action= Action("Follow me.", start_follow_requirement, "start_follow", menu_tooltip = "Have the person follow you around.")
    stop_follow_action = Action("Stop following me.", stop_follow_requirement, "stop_follow", menu_tooltip = "Have the person stop following you.")

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    hire_person_action = Action("Employ [the_person.title]\n Costs: $300", hire_person_requirement, "hire_person", menu_tooltip = "Hire the the person to work for you in your business. Costs $300")
    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    rename_person_action = Action("Rename [the_person.title]", rename_person_requirement, "rename_person", menu_tooltip = "Change the name of the person.")
    # Spend the Night | Allows you to sleep in the home of a person you have increased the love stat.
    spend_the_night_action = Action("Spend the night with [the_person.possessive_title]", spend_the_night_requirement, "spend_the_night", menu_tooltip = "Allows you to sleep in this location")

    # A role added to all people in the game to enable actions through the "Special Actions Menu..."
    generic_people_role = Role("Generic", [schedule_person_action, start_follow_action, stop_follow_action, hire_person_action, rename_person_action, spend_the_night_action]) # This role is meant to not display in the person_ui_hud

    # NOTE: This extension of "any person" can be toggled from the Action Mod Core menu under "Misc", listed as Generic People Actions


# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
label spend_the_night(person): # Consider adding the sleep_action to the_person's room, but stats jump all over the place so doesn't nescessarily make sense.
    "You go to sleep in [person.home.name]"
    $ person.change_love(5)
    $ person.change_happiness(5)
    call advance_time
    return

label rename_person(person):
    "You tell [person.possessive_title] that you are giving her a new name."
    while True:
        menu rename_person_menu:
            "Name: [person.name]":
                $ newname = str(renpy.input("Name: ", person.name))
                $ person.name = newname

            "Last name: [person.last_name]":
                $ new_last_name = str(renpy.input("Last name: ", person.last_name))
                $ person.last_name = new_last_name

            "Title: [person.title]":
                $ new_title = str(renpy.input("Title: ", person.title))
                $ person.title = new_title

            "Possessive Title: [person.possessive_title]":
                $ new_title = str(renpy.input("Possessive Title: ", person.possessive_title))
                $ person.possessive_title = new_title

            "Your Title: [person.mc_title]":
                $ new_title = str(renpy.input("Your Title: ", person.mc_title))
                $ person.mc_title = new_title

            "Back":
                return

# Hire Person Labels
label hire_person(person):
    if mc.business.funds < 300:
        "Hiring [person.title] will cost you $300 and put you in debt due to low funds."
    else:
        "Hiring [person.title] will cost you $300, do you wish to proceed?"
    menu:
        "Yes":
            pass
        "No":
            return
    "You complete the nessesary paperwork and hire [person.title]. What division do you assign them to?"
    menu:
        "Research and Development.":
            $ mc.business.add_employee_research(person)
            $ mc.location.move_person(person, mc.business.r_div)
            $ person.set_work([1,2,3], mc.business.r_div)

        "Production.":
            $ mc.business.add_employee_production(person)
            $ mc.location.move_person(person, mc.business.p_div)
            $ person.set_work([1,2,3], mc.business.p_div)

        "Supply Procurement.":
            $ mc.business.add_employee_supply(person)
            $ mc.location.move_person(person, mc.business.s_div)
            $ person.set_work([1,2,3], mc.business.s_div)

        "Marketing.":
            $ mc.business.add_employee_marketing(person)
            $ mc.location.move_person(person, mc.business.m_div)
            $ person.set_work([1,2,3], mc.business.m_div)

        "Human Resources.":
            $ mc.business.add_employee_hr(person)
            $ mc.location.move_person(person, mc.business.h_div)
            $ person.set_work([1,2,3], mc.business.h_div)

        "Back":
            return
    $ mc.business.pay(-300)

    $ person.event_triggers_dict["employed_since"] = day
    $ mc.business.listener_system.fire_event("new_hire", the_person = person)
    $ person.special_role.append(employee_role)

    $ work_station_destination = mc.business.get_employee_workstation(person).formalName
    "[person.title] heads over to the [work_station_destination]..."
    return


    # Schedule Person Labels

label schedule_menu(person): # TODO: Find a way to handle "None" instances of schedule to display formalName on Action.
    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        schedule_options = []
        for act in schedule_actions_list:
            schedule_options.append(act)
        schedule_options.append("Back")

    "You decide where [person.title] should be at throughout the day."
    while True:
        $ act_choice = call_formated_action_choice(schedule_options)
        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action(person)

label schedule_early_morning(person):
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return
    else:
        $ person.schedule[0] = room_choice
        "Early Morning Schedule Set: [room_choice.formalName]"
        return

label schedule_morning(person):
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return
    else:
        $ person.schedule[1] = room_choice
        "Morning Schedule Set: [room_choice.formalName]"
        return

label schedule_afternoon(person):
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[2] = room_choice
        "Afternoon Schedule Set: [room_choice.formalName]"
        return

label schedule_evening(person):
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[3] = room_choice
        "Evening Schedule Set: [room_choice.formalName]"
        return

label schedule_night(person):
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[4] = room_choice
        "Night Schedule Set: [room_choice.formalName]"
        return

# Follower Labels
label start_follow(person):
    "You tell [person.title] to follow you around."
    $ list_of_followers.append(the_person)
    return

label stop_follow(person):
    "You tell [person.title] to stop following you around."
    $ list_of_followers.remove(the_person)
    return
