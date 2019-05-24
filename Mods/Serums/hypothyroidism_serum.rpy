# Hypothyroidism Serum by Tristimdorion

init -1 python:
    def hypothyroidism_serum_on_turn(person, add_to_log):
        return person.change_weight(amount = .2, chance = 20)
        
# any label that starts with serum_mod is added to the serum mod list
label serum_mod_hypothyroidism_serum_trait(stack):
    python:
        hypothyroidism_serum_trait = SerumTraitMod(name = "Hypothyroidism Serum",
            desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down methabolism, thus causing weight gain.",
            positive_slug = "-$15 Value, 20% Chance/Turn to increase body mass by 200 grams",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = hypothyroidism_serum_on_turn,
            requires = basic_med_app,
            tier = 1,
            research_needed = 500)

        # enable serum and append to mod_list
        hypothyroidism_serum_trait.initialize()

        execute_hijack_call(stack)
    return