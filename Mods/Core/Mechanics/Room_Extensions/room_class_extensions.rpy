init -1 python:
    ###########################################
    # Custom Compare Functions For Room Class #
    ###########################################
    def room_compare(self, other):
        if isinstance(self, other.__class__):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Room.__cmp__ = room_compare

    # add room hash function
    def room_hash(self):
        return hash(self.name)

    Room.__hash__ = room_hash
    Room.hash = room_hash

    def room_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Room.__eq__ = room_eq

    def room_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Room.__ne__ = room_ne

    #################################
    # Extend Default Room Functions #
    #################################

    # extend the default move_person function
    def move_person_extended(org_func):
        def move_person_wrapper(room, person, destination):
            # run original function
            org_func(room, person, destination)
            # run extension code
            if not person.follow_mc and not room is destination:
                if person.location == gym:
                    person.apply_gym_outfit()
                elif person.location == university and not person is nora:
                    person.apply_university_outfit()
                else:
                    person.apply_planned_outfit()
            return

        return move_person_wrapper

    Room.move_person = move_person_extended(Room.move_person)

    ########################
    # Added Room Functions #
    ########################
    def purchase_room_on_buy_function(room):
        room.visible = True

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
        # special character aunt and cousin locations
        if person in [aunt, cousin]:
            add_location(aunt_apartment)
            for c in aunt_apartment.connections:
                add_location(c)

        return possible_locations

    # Adds an action to the room if not already present. Used with PolicyMod.
    def add_action(self, act):
        if act not in self.actions:
            self.actions.append(act)

    Room.add_action = add_action

    # Remove an action from if present
    def remove_action(self, act):
        if isinstance(act, basestring):
            found = find_in_list(lambda x: x.effect == act, self.actions)
            if found:
                self.actions.remove(found)

        if act in self.actions:
            self.actions.remove(act)

    Room.remove_action = remove_action
