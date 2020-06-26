init -1 python:
    def get_hr_director(self):
        if not hasattr(self, "_hr_director"):
            self._hr_director = False
        return self._hr_director

    def set_hr_director(self, value):
        self._hr_director = value

    def del_hr_director(self):
        del self._hr_director

    # add follow_mc attribute to person class (without sub-classing)
    Business.hr_director = property(get_hr_director, set_hr_director, del_hr_director, "The company HR director position.")

    def get_funds_yesterday(self):
        if not hasattr(self, "_funds_yesterday"):
            self._funds_yesterday = 1000 # default start money
        return self._funds_yesterday

    def set_funds_yesterday(self, value):
        self._funds_yesterday = value

    def del_funds_yesterday(self):
        del self._funds_yesterday

    Business.funds_yesterday = property(get_funds_yesterday, set_funds_yesterday, del_funds_yesterday, "Holds business funds from day before")

    def get_unisex_restroom_unlocks(self):
        if not hasattr(self, "_unisex_restroom_unlocks"):
            self._unisex_restroom_unlocks = {}
        return self._unisex_restroom_unlocks

    def set_unisex_restroom_unlocks(self, value):
        self._unisex_restroom_unlocks = value

    def del_unisex_restroom_unlocks(self):
        del self._unisex_restroom_unlocks

    Business.unisex_restroom_unlocks = property(get_unisex_restroom_unlocks, set_unisex_restroom_unlocks, del_unisex_restroom_unlocks, "Tracking dictionary for the unisex restroom event.")

    def update_employee_status(self, new_person):
        if new_person.event_triggers_dict.get("employed_since", -1) == -1:
            new_person.event_triggers_dict["employed_since"] = day
            self.listener_system.fire_event("new_hire", the_person = new_person)

        for other_employee in self.get_employee_list():
            town_relationships.begin_relationship(new_person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

    Business.update_employee_status = update_employee_status

    def hire_person(self, new_person, target_division, add_to_location = False):
        div_func = {
            "Research" : [ self.research_team, self.r_div],
            "Production" : [ self.production_team, self.p_div],
            "Supply" : [ self.supply_team, self.s_div ],
            "Marketing" : [ self.market_team, self.m_div ],
            "HR" : [ self.hr_team, self.h_div ]
        }
        div_func[target_division][0].append(new_person)
        new_person.add_role(employee_role)
        new_person.job = self.get_employee_title(new_person)
        new_person.set_work([1,2,3], div_func[target_division][1])
        self.update_employee_status(new_person)
        if add_to_location:
            div_func[target_division][1].add_person(new_person)

    Business.hire_person = hire_person

    def add_unique_mandatory_crisis(self, the_crisis):
        if the_crisis not in self.mandatory_crises_list:
            self.mandatory_crises_list.append(the_crisis)

    Business.add_unique_mandatory_crisis = add_unique_mandatory_crisis

    def calculate_strip_club_income(self):
        income = 0
        if get_strip_club_foreclosed_stage() >= 5: # The player owns the club
            for stripper in people_in_role(stripper_role): # More strippers more money, and linked to the difficulty choice made...
                income += calculate_stripper_profit(stripper)
                # extra modifiers for later stages (not yet implemented)
                #    if foreclosed_stage >= 6: # The club have a manager = +10% income
                #        income += int (income * 0.1)
                #    if foreclosed_stage >= 7: # The club have waitresses = +5% income
                #        income += int (income * 0.05)

            # deduce stripper costs
            for stripper in people_in_role(stripper_role):
                income -= stripper.stripper_salary

        return income

    Business.calculate_strip_club_income = calculate_strip_club_income

    # extend the default run day function
    def business_run_day_extended(org_func):
        def run_day_wrapper(business):
            # run original function
            org_func(business)
            # run extension code
            strip_club_income = business.calculate_strip_club_income()
            if strip_club_income != 0:
                mc.business.funds += strip_club_income
                mc.business.add_normal_message("The [strip_club.formalName] has made a net profit of $" + str(__builtin__.round(strip_club_income, 1)) + " today!")

        return run_day_wrapper

    # wrap up the run_day function
    Business.run_day = business_run_day_extended(Business.run_day)
