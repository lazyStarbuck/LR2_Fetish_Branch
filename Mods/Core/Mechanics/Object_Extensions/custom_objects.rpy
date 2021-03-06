# NOTE: Masterfile for objects that can be used in rooms. Since these are only relevant if in use I'd like to just throw them all into one place so they are always available to creators.
# NOTE: If this list ever grows huge and you are just looking for something be smart with search functions Ctrl + F. e.g "bed" or "kneel", "sit"

# Objects aimed at the dungeon. Want to give some bonuses for having purchased it.
# Since the Dungeon itself is fairly cheap the items will cost money to unlock as well.
init -1 python:

    def make_bdsmbed():
        the_bdsmbed = Object("Bed Cuffs", ["Lay", "Low", "Kneel"], sluttiness_modifier = 10, obedience_modifier = 20) # Normal bed is +10.
        return the_bdsmbed

    def make_pillory():
        the_pillory = Object("Pillory", ["Stand", "Lean", "Kneel", "Low"], sluttiness_modifier = 15, obedience_modifier = 25)
        return the_pillory

    def make_woodhorse():
        the_woodhorse = Object("Wood Horse", ["Sit", "Lean", "Lay"], sluttiness_modifier = 20, obedience_modifier = 30)
        return the_woodhorse

    def make_cage():
        the_cage = Object("Cage", ["Lay", "Low", "Kneel"], sluttiness_modifier = 10, obedience_modifier = 20)
        return the_cage

    def make_toilet():
        the_toilet = Object("Toilet", ["Sit", "Low"], sluttiness_modifier = 10, obedience_modifier = 5)
        return the_toilet
