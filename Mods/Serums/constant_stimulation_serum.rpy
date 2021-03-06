# Pheremone Therapy Serum by Starbuck

init -1 python:
    def constant_stimulation_on_turn(the_person, add_to_log, fire_event = True):
        if get_suggest_tier(the_person) > get_slut_tier(the_person):  #If the tier of sluttiness is less than the suggest tier
            the_person.change_slut_core(1, add_to_log)
            the_person.change_slut_temp(1, add_to_log)
        elif get_suggest_tier(the_person) == get_slut_tier(the_person): #If they are equal
            if renpy.random.randint(0,100) <50:
                the_person.change_slut_core(1, add_to_log)
                the_person.change_slut_temp(1, add_to_log)
        elif get_slut_tier(the_person) < 5:
            if renpy.random.randint(0,100) < (30 - (5 * get_slut_tier(the_person))):
                the_person.change_slut_core(1, add_to_log)
                the_person.change_slut_temp(1, add_to_log)

    def add_constant_stimulation_serum():
        constant_stimulation_ther = SerumTraitMod(name = "Constant Stimulation",
                desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestibility.",
                positive_slug = "Slowly increases sluttiness based on suggestibility, +$15 Value",
                negative_slug = "+100 Serum Research",
                value_added = 15,
                research_added = 100,
                base_side_effect_chance = 50,
                on_turn = constant_stimulation_on_turn,
                tier = 1,
                start_researched =  False,
                research_needed = 500,
            )


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_constant_stimulation_serum_trait(stack):
    python:
        add_constant_stimulation_serum()
        execute_hijack_call(stack)
    return
