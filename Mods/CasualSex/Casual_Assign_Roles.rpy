#Blank for now#


init 2 python:
    #def casual_sex_mod_initialization(action_mod):
    workout_wardrobe = wardrobe_from_xml("Workout_Wardrobe")
    casual_sex_list = [] #This will hold a list of girls looking for casual sex


    def casual_sex_test():

        people_to_process = [] #Create a list of everyone
        for place in list_of_places:
            for people in place.people:
                people_to_process.append([people,place])

        for (people,place) in people_to_process: #Figure out if person already has an important role
            disqualifying_role = 0
            for role in people.special_role:
                if role == generic_people_role:
                    pass
                else:
                    disqualifying_role = 1
            if disqualifying_role == 0:         #Assign new casual sex roles#
                if people.age < 30:
                    assign_casual_athlete_role(people)
                    people.wardrobe = copy.copy(workout_wardrobe)

                elif people.age < 40:
                    assign_casual_hotwife_role(people)

                else:
                    assign_casual_FA_role(people)


        return

    def casual_sex_add_person_to_list(the_person):
        if the_person in casual_sex_list:
            return False
        else:
            casual_sex_list.append (the_person)
            return True

        return False

init 1302 python:
    def assign_casual_athlete_role(the_person):
        the_person.special_role.append(casual_athlete_role)
        local_athlete_personality = Personality("athlete", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = [],
        common_sexy_likes = ["casual sex"],
        common_dislikes = ["relationships"],
        common_sexy_dislikes = [],
        titles_function = athlete_titles, possessive_titles_function = athlete_possessive_titles, player_titles_function = athlete_player_titles)
        local_athlete_personality.response_dict["hookup_rejection"] = "athlete_hookup_rejection"
        the_person.personality = local_athlete_personality
        the_person.event_triggers_dict["reject_position"] = "standing_doggy"
        the_person.schedule[1] = gym
        the_person.schedule[3] = gym

        return

    def remove_casual_athlete_role(the_person):
        the_person.special_role.remove(casual_athlete_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[1] = None    #Reset their schedule
        the_person.schedule[3] = None
        return

    def assign_casual_hotwife_role(the_person):
        the_person.special_role.append(casual_hotwife_role)
        local_hotwife_personality = Personality("hotwife", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = [],
        common_sexy_likes = ["casual sex", "cheating on men"],
        common_dislikes = [],
        common_sexy_dislikes = [],
        titles_function = hotwife_titles, possessive_titles_function = hotwife_possessive_titles, player_titles_function = hotwife_player_titles)
        local_hotwife_personality.response_dict["hookup_rejection"] = "hotwife_hookup_rejection"
        the_person.personality = local_hotwife_personality
        the_person.event_triggers_dict["reject_position"] = "blowjob"
        the_person.schedule[2] = downtown_bar
        the_person.schedule[3] = downtown_bar

        return

    def remove_casual_hotwife_role(the_person):
        the_person.special_role.remove(casual_hotwife_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[2] = None    #Reset their schedule
        the_person.schedule[3] = None

        return


    def assign_casual_FA_role(the_person):
        the_person.special_role.append(casual_FA_role)
        local_FA_personality = Personality("FA", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = ["traveling"],
        common_sexy_likes = ["casual sex"],
        common_dislikes = ["relationships"],
        common_sexy_dislikes = [],
        titles_function = FA_titles, possessive_titles_function = FA_possessive_titles, player_titles_function = FA_player_titles)
        local_FA_personality.response_dict["hookup_rejection"] = "FA_hookup_rejection"
        the_person.personality = local_FA_personality
        the_person.event_triggers_dict["reject_position"] = "blowjob"
        the_person.schedule[3] = downtown_bar

        return

    def remove_casual_FA_role(the_person):
        the_person.special_role.remove(casual_FA_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[2] = None    #Reset their schedule
        the_person.schedule[3] = None

        return














        return
