init -2 python:
    class Scene():
        def __init__(self):
            self.actors = []

        def add_actor(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            self.actors.append(Actor(person, position, emotion, special_modifier, character_placement))
            self.draw_scene()

        def update_actor(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if actor is None:
                return
            if not position is None:
                actor.position = position
            if not emotion is None:
                actor.emotion = emotion
            if not special_modifier is None:
                actor.special_modifier = special_modifier
            if not character_placement is None:
                actor.character_placement = character_placement
            self.draw_scene()

        def strip_actor_outfit_to_max_sluttiness(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, temp_sluttiness_boost = 0):
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Strip " + actor.person.title, "gray_float_text")
                actor.person.strip_outfit_to_max_sluttiness(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, narrator_messages = narrator_messages, character_placement = actor.character_placement, position = actor.position, emotion = actor.emotion, scene_manager = self)

        def draw_animated_removal(self, person, the_clothing): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            actor = find_in_list(lambda x: x.person is person, self.actors)
            if not actor is None:
                #mc.log_event("Remove clothing " + actor.person.title, "gray_float_text")
                actor.person.draw_animated_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, character_placement = actor.character_placement, scene_manager = self)

        def remove_actor(self, person):
            actor_to_remove = find_in_list(lambda x: x.person is person, self.actors)
            if not actor_to_remove is None:
                self.actors.remove(actor_to_remove)
                self.draw_scene()

        def draw_scene(self):
            renpy.scene("Active")
            for actor in self.actors:
                actor.draw_actor()

        # helper function for strip and animated removal functions
        def draw_scene_without(self, person):
            renpy.scene("Active")
            actor_missing = find_in_list(lambda x: x.person is person, self.actors)
            for actor in self.actors:
                if not actor is actor_missing:
                    actor.draw_actor()   
            
    class Actor():
        def __init__(self, person, position = None, emotion = None, special_modifier = None, character_placement = None):
            self.person = person
            self.position = position
            self.emotion = emotion
            self.special_modifier = special_modifier
            self.character_placement = character_placement

            if position is None:
                self.position = person.idle_pose

            if emotion is None:
                self.emotion = person.get_emotion()

            if character_placement is None:
                self.character_placement = character_right

        def draw_actor(self):
            self.person.draw_person(position = self.position, emotion = self.emotion, special_modifier = self.special_modifier, character_placement = self.character_placement, from_scene = True)
