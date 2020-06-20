# Alpha Girl personality definition: Mod by Corrado 
# Dominating personality applied to all girls with following traits:
# Older than 25, high charisma stat >=5, high intelligence >=4
# Likes or loves "taking control"

init 3 python:
    def alpha_personality_requirement():
        return True

    def change_alpha_personality_enabled(enabled):
        for person in all_people_in_the_game():
            update_alpha_personality(person)
        return

    alpha_personality_action = ActionMod("Alpha Personality", alpha_personality_requirement, "alpha_personality_dummy_label",
        menu_tooltip = "Enable or disable the Alpha personality.", category="Personality", on_enabled_changed = change_alpha_personality_enabled)

init 1400 python:
    def alpha_titles(person):
        valid_titles = []
        valid_titles.append("Mrs. " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.love > 40:
            valid_titles.append("Milady")
        if person.sluttiness > 70:
            valid_titles.append("Mistress")
        if person.sluttiness > 100 and the_person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_titles.append("Anal Queen")
        return valid_titles
    def alpha_possessive_titles(person):
        valid_possessive_titles = []
        valid_possessive_titles.append("Mrs. " + person.last_name)
        if person.love > 20:
            valid_possessive_titles.append(person.name)
        if person.sluttiness > 60:
            valid_possessive_titles.append("Your naughty Mistress")
        if person.sluttiness > 100 and (the_person.get_opinion_score("threesomes") > 0 or the_person.get_opinion_score("other girls") > 0):
            valid_possessive_titles.append("Your bisex queen")
        if person.sluttiness > 100 and the_person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_possessive_titles.append("Your anal queen")
        return valid_possessive_titles
    def alpha_player_titles(person):
        valid_player_titles = []
        valid_player_titles.append("Mr. " + mc.last_name)
        if person.happiness < 70:
            valid_player_titles.append("Small balls")
        if person.love > 40:
            valid_player_titles.append("Queen's King")
        if person.sluttiness > 60:
            valid_player_titles.append("Queen's Dick")
        return valid_player_titles

    alpha_personality = Personality("alpha", default_prefix = "reserved",
        common_likes = ["flirting", "HR work", "work uniforms", "working", "sports", "small talk", "other girls", "boots", "dresses", "high heels", "skirts", "the colour black", "the colour red"],
        common_sexy_likes = ["taking control", "threesomes", "getting head", "lingerie", "not wearing underwear", "showing her tits", "showing her ass", "skimpy outfits", "skimpy uniforms"],
        common_dislikes = ["conservative outfits", "pants", "punk", "the colour green", "the colour pink", "classical", "jazz"],
        common_sexy_dislikes = ["being submissive", "bareback sex", "being fingered", "missionary style sex"],
        titles_function = alpha_titles, possessive_titles_function = alpha_possessive_titles, player_titles_function = alpha_player_titles)

    # don't add it to the default list of personalities, let the generic personality hook change it based on Charisma

label alpha_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Yes, what do you want ?"
    elif the_person.happiness < 90:
        the_person.char "Hello..."
    else:
        if the_person.obedience > 100:
            if the_person.sluttiness > 60:
                the_person.char "Hello [the_person.mc_title]... Is there anything I can manage for you ?"
            else:
                the_person.char "Hello [the_person.mc_title]... Anything I can help you with ?"
        else:
            if the_person.sluttiness > 60:
                the_person.char "Hello [the_person.mc_title], how has your day been ? Maybe you can make mine better..."
            else:
                $ day_part = time_of_day_string()
                the_person.char "Good [day_part], [the_person.mc_title] !"
    return

label alpha_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person.char "I guess ? What can I do for you?"
    mc.name "I know this is strange, but I saw you and I just needed to know your name."
    "She laughs full of herself."
    the_person.char "Is that so ? You're not the first one... Maybe for today !"
    mc.name "Really, I just wanted to talk to you."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Well, if you insist, my name is [formatted_title]. It's nice to meet you..."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    "With a commanding gaze she waits for you to introduce yourself."
    return

label alpha_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person.char "Well, I will use it if my mood will decide so."
        the_person.char "Thank you for the outfit, [the_person.mc_title]."
    else:
        the_person.char "Oh that's a nice combination! I'll try it at home later and I'll check how it fit."
    return

label alpha_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person.char "I know it would make your day if I wore this for you [the_person.mc_title] !"
        the_person.char "I'm sorry, I know you are disappointed, but I will make it up to you."
    else:
        if the_person.sluttiness > 60:
            the_person.char "I... [the_person.mc_title], do you think that's the best for a woman with my... 'assets' ?"
            "[the_person.possessive_title] wink, smile but shakes her head."
            the_person.char "No, you should find something better to wear for me..."
        else:
            the_person.char "[the_person.mc_title], I'm a lady... I can't show my face in public with something like that!"
            "[the_person.possessive_title] shakes her head and gives you a scowl."
    return

label alpha_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Turn around [the_person.mc_title], I'm really not looking ladylike right now. Just give me a moment to get dressed..."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], you shouldn't see me like this... Just give me a moment and I'll get dressed."
        elif not the_person.relationship == "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person.char "Oh my, what would my [so_title] say if he saw me here, like this... with you ? Turn around, I need to get dressed."
        else:
            the_person.char "Oh [the_person.mc_title], I'm at my best ! Turn around now, I need to get dressed."
    return

label alpha_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I know it would make your day [the_person.mc_title], but I don't think I should take anything else off. I'm a lady, after all."
    elif the_person.obedience < 70:
        the_person.char "Not yet sweety. You just need to relax and let [the_person.title] take care of you."
    else:
        the_person.char "Don't touch that [the_person.mc_title]. Could you imagine if it came off ?"
    return

label alpha_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person.char "Such a nice body you have [the_person.mc_title] and I love sex... Let's try it with you !"
        else:
            the_person.char "I love sex [the_person.mc_title], and I love it more when it's with you !"
    else:
        the_person.char "Okay, lets try this... I hope you know how to treat a real woman during sex !"
    return

label alpha_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I know I shouldn't do this, I'm not a slut..."
        the_person.char "But you look so strong and nice... Let me feel your body !"
    else:
        if the_person.obedience > 130:
            the_person.char "I... We really shouldn't... But I know this will makes both of us happy: lets do it [the_person.mc_title]..."
        else:
            the_person.char "How does this keep happening [the_person.mc_title] ? I like you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks straight in your eyes, conflicted."
            if not the_person.relationship == "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Ok... You just have to make sure my [so_title] never finds out about this..."
            else:
                the_person.char "Ok... But that doesn't means we're more than just friends, ok ?"
    return

label alpha_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet [the_person.mc_title], I need to get warmed up first. Let's start a little slower and enjoy ourselves."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. I see someone else..."
    return

label alpha_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "Wait, what ? I have a [so_title], what did you think we were going to be doing ?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person.char "Oh god, what did you just say [the_person.mc_title] ?"
        the_person.char "I'm the best, how could you even think about that!"
    else:
        the_person.char "What ? Oh god, I'm steps over you [the_person.mc_title] ! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person.char "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return


label alpha_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh, god ! I'm almost... I'm going to..."
        the_person.char "{b}Cum!{/b} Ahhh !"
    else:
        the_person.char "Oh keep doing that [the_person.mc_title], I'm cumming !"
    return

label alpha_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck ! Oh fuck, you're making me cum so hard [the_person.mc_title] !"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Oh my god, I'm going to cum. I'm going to cuuuum !"
        "She closes her eyes and squeals with pleasure."
    return

label alpha_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Ah! Yes [the_person.mc_title] ! Right there, yes... pump me... I'm cumming !"
        "She closes her eyes and goes into a frenzy of multiple orgasms."
    else:
        the_person.char "Oh god, that's it...keep going...yes [the_person.mc_title]..yes ! Yes ! YES !"
    return

label alpha_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person.char "I'm going to cum ! Pump my ass hard and make me cum !"
    else:
        the_person.char "Oh fuck, I think... I think I'm going to cum !"
    return

label alpha_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Do you need the touch of a skilled woman, [the_person.mc_title] ? I know how stressed you can get you."
        else:
            the_person.char "Oh sweety... What do you need my help with [the_person.mc_title] ?."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Well, how about you let me take care of you for a change ? I'm the best..."
        elif the_person.sluttiness > 20:
            the_person.char "What do you mean [the_person.mc_title] ? Do you want to spend some good time with me ?"
        else:
            the_person.char "I'm not sure I understand: what do you need from me, [the_person.mc_title] ?"
    return

label alpha_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            "[the_person.possessive_title] pinches your ass cheek, whispering..."
            the_person.char "You can't say things like that in public [the_person.mc_title] ! Think of my reputation."
            "She looks around quickly to see if anyone heard you, then takes your hand in hers."
            the_person.char "Come on, I'm sure we can find a quiet place were you can take care of me."
        elif the_person.sluttiness < 70:
            "[the_person.possessive_title] smiles and devours your body with her eyes, making sure nobody around you notices."
            the_person.char "Okay, but we need to be discreet: I have a repute. Let's find someplace quiet."
        else:
            the_person.char "Oh my [the_person.mc_title]... why don't you take care of me right here !"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person.char "No point wasting any time, right ? I hope my [so_title] won't be too jealous."
        else:
            the_person.char "Okay, but we need to be careful. I don't want my [so_title] to find out what we're doing."
    return

label alpha_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            the_person.char "I can't believe I'm saying this... I'll play along for now, but you better not disappoint me."
            mc.name "Of course [the_person.title], I promise."
        elif the_person.sluttiness < 70:
            the_person.char "Oh [the_person.mc_title], what kind of goddess would I be if I said no ? Come on, let's enjoy ourselves."
        else:
            the_person.char "Oh [the_person.mc_title], I'm so glad I make you feel this way. Come on, let's get started !"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person.char "Come on [the_person.mc_title], lets get going, screw my [so_title]!"
        else:
            the_person.char "I have a [so_title], I shouldn't be doing this..."
            "Her eyes tell quite a different story."
    return

label alpha_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just what I like, don't you ?"
        else:
            the_person.char "Oh my... that feels very good, [the_person.mc_title]!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Keep doing that [the_person.mc_title]... Wow, you're good !"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Oh gods, that feels amazing !"
        else:
            the_person.char "Oh lord... I could get use to you touching me like this !"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Touch me [the_person.mc_title], I want you to touch me !"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad... but my selfish [so_title] never touches me this way !"
                the_person.char "I need this, so badly!"
        else:
            the_person.char "I want you to keep touching me, I'd never guessed you could make me feel this way, but I want more !"
    return

label alpha_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person.char "Oh my... that feels..."
            "She sighs happily."
            the_person.char "Yes, right there !"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Yes, just like that ! Mmmmmh!"
        else:
            the_person.char "Keep doing that [the_person.mc_title], it excite me so badly !"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you really know how to put that tongue of yours to good use. That feels amazing !"
        else:
            the_person.char "Oh lord... your tongue is addictive, I just want more and more of it !"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh I need this so badly [the_person.mc_title]! If you keep going you'll make me climax !"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad, but you make me feel so good, my worthless [so_title] never does this for me !"
        else:
            the_person.char "Oh sweet lord in heaven... This feeling is intoxicating!"
    return

label alpha_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I love feeling you inside of me !"
        else:
            the_person.char "Oh lord, you're so big... Whew !"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Oh that feels very good, keep doing that !"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes ! Oh god yes, fill me !"
        else:
            the_person.char "Oh lord your... cock feels so big !"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Keep... keep going [the_person.mc_title] ! I'm going to climax soon !"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Keep going! My [so_title]'s tiny cock never makes me climax and I want it so badly !"
                the_person.char "I should feel bad, but all I want is your cock in me right now !"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label alpha_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you feel so big when you're inside me like this."
        else:
            the_person.char "Be gentle, it feels like you're going to tear me in half !"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Give it to me, [the_person.mc_title], give me every last inch !"
        else:
            the_person.char "Oh god ! Owwww ! Move a little slower..."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I hope my ass isn't too tight for you, I don't want you to cum too early."
        else:
            the_person.char "I think I'll have some problem walking in public after this !"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Your cock feels like it was made to perfectly fill me ! Keep going, I might actually climax !"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] give me some anal, but I never felt like this... My second hole belongs to you, [the_person.mc_title] !"
        else:
            the_person.char "Oh lord, this is actually starting to feel good... If you keep this up, I'm going to cum !"
    return

label alpha_seduction_refuse(the_person):
    if the_person.sluttiness < 30:
        the_person.char "Oh my god, what are you saying [the_person.mc_title] ! Don't you think I'm a little too much for you ? I'm sure you can't handle me..."
    elif the_person.sluttiness < 60:
        the_person.char "I'm sorry [the_person.mc_title], but we really shouldn't do this anymore. It's just... not going to happen."
    else:
        the_person.char "I'm sorry [the_person.mc_title], I know how much you like to spend time with me, but now isn't a good time for me. I'll make it up to you though, I promise."
    return

label alpha_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            # She's in uniform and likes how it looks.
            the_person.char "Thank you [the_person.mc_title]. I think these are nice uniforms as well."
            mc.name "It helps having such an attractive employees to wear it."
            "[the_person.possessive_title] smiles."
            the_person.char "Well, thank you... I know, right ?"
        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.outfit.vagina_visible():
                # Her pussy is on display.
                the_person.char "I would not call it much of an uniform, if you know what it mean."
                the_person.char "I understand it's the company uniform, but not all women could wear it like me..."
                mc.name "It will take some getting used to, but I think it would be a shame to cover up your wonderful figure."
                "[the_person.possessive_title] smiles and nods, she's so full of herself..."

            elif the_person.outfit.tits_visible():
                # Her tits are out
                if the_person.has_large_tits():
                    the_person.char "Thank you, but I can tell this uniform was designed by a horny man."
                    the_person.char "Large chested women, like myself, appreciate a little more support in their outfits to shows their best."
                else:
                    the_person.char "Thank you, but I do hope you'll consider a more respectable uniform in the future."
                    the_person.char "It's not the workplace my first choice to show my goods off like a bimbo."
                mc.name "I understand it's a little uncomfortable, but I'm sure you'll get used to it."
                the_person.char "Perhaps, in time, but for now I really don't enjoy it at all."

            elif the_person.outfit.underwear_visible():
                # Her underwear is visible.
                the_person.char "Thank you. But this is not appropriate for a woman like me, it should be more decent and respectable, like me."
                mc.name "I know it can take some getting used to, but you look fantastic in it. You definitely have the body to pull this off."
                "[the_person.possessive_title] smiles and nods, she's so full of herself..."

            else:
                # It's just generally slutty.
                "[the_person.possessive_title] smiles warmly."
                the_person.char "Thank you, although I don't think I would ever wear this if it wasn't company policy."
                mc.name "Well you look fantastic in it either way. Maybe you should rethink your normal wardrobe."
                the_person.char "My wardrobe is damn perfect ! Anyway I'll think about it."

    else:
        #She's in her own outfit.
        "[the_person.possessive_title] seems caught off guard by the compliment."
        the_person.char "Oh, thank you! I'm not wearing anything special, it's just one of my normal outfits."
        mc.name "Well, you make it look good."
        "She smiles and laughs proud of herself."
        the_person.char "Men will be always men."
    return

label alpha_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.outfit.tits_visible():
                the_person.char "What it shows off most are my breasts. I'm not complaining though, between you and me, I kind of like it."
                "She winks and shakes her shoulders, jiggling her tits for you."
            else:
                the_person.char "With my body and your fashion taste, how could I look bad ? These uniforms are very flattering."
                mc.name "It's easy to make a beautiful model look wonderful."
                if the_person.effective_sluttiness() > 20:
                    $ the_person.draw_person(position = "back_peek")
                    the_person.char "It makes my butt look pretty good too. I don't think that was an accident."
                    "She gives her ass a little shake."
                    mc.name "It would be a crime not to try and show your nice buttocks off."
                    $ the_person.draw_person()
                "She smiles softly."
                the_person.char "You know just what to say to make a woman feel special."

        else:
            # the_person.char "I think it shows off a little too much!"
            if the_person.outfit.vagina_visible():
                the_person.char "What doesn't this outfit show off!"

            elif the_person.outfit.tits_visible():
                the_person.char "It certainly shows off my breasts!"

            else:
                the_person.char "And it shows off a {i}lot{/i} of my body!"

            the_person.char "The workplace isn't my best choice to show so much skin, anyway someone else would have much more problem than me."
            mc.name "It may take some time to adjust, but with enough time you'll feel perfectly comfortable in it."
            "She smiles and nods."
            the_person.char "I already fill perfectly comfortable in it, I just don't know if everybody else here could feel the same way !"
    else:
        if the_person.effective_sluttiness() < 20 and mc.location.get_person_count() > 1:
            "[the_person.possessive_title] smiles, then glances around."
            the_person.char "Keep your voice down [the_person.mc_title], there are other people around."
            mc.name "I'm sure they're all thinking the same thing."
            "She rolls her eyes and laughs softly."
            the_person.char "Maybe they are, but it's still embarrassing."
            the_person.char "You'll have better luck if you save your flattery for when we're alone."
            mc.name "I'll keep that in mind."

        else:
            "[the_person.possessive_title] gives a subtle smile and nods her head."
            the_person.char "Thank you [the_person.mc_title]. I'm glad you like it... And me."
            the_person.char "What do you think of it from the back? It's hard for me to get a good look."
            $ the_person.draw_person(position = "back_peek")
            "She turns and bends over a little bit, accentuating her butt."
            if not the_person.outfit.wearing_panties() and not the_person.outfit.vagina_visible(): #Not wearing underwear, but you can't see so she coments on it.
                the_person.char "My panties were always leaving unpleasant lines, so I had to stop wearing them. I hope you don't mind."
            else:
                the_person.char "Well ?"
            mc.name "You look just as fantastic from the back as you do from the front."
            $ the_person.draw_person()
            "She turns back and smiles, proud of herself."
    return

label alpha_flirt_response_high(the_person):
    if mc.location.get_person_count() > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person.char "[the_person.mc_title], there are people around."
        "She bites her lip and leans close to you, whispering in your ear."
        the_person.char "But if we were alone, maybe we could figure something out..."
        menu:
            "Find someplace quiet":
                mc.name "Follow me."
                "[the_person.possessive_title] nods and follows a step behind you."
                "After searching for a couple of minutes you find a quiet, private space."
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person.char "And what are you planning now that you win the big prize ?"

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She closes her eyes and leans her body against yours."
                else:
                    "You answer with a kiss. She closes her eyes and leans her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_high_1

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person.char "You're smart enough, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.get_person_count() == 1: #She's shy but you're alone
            "[the_person.title] blushes and stammers out a response."
            the_person.char "I... I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide your feelings... I feel the same way."
            "She nods and takes a deep breath..."
            the_person.char "Okay, you're right. What are your intentions now ?"

        else:  #You're not alone, but she doesn't care.
            the_person.char "Well I wouldn't want you to go into a frenzy. You'll just have to find a way to get me out of this outfit..."
            if the_person.has_large_tits(): #Bounces her tits for you
                $ the_person.draw_person(the_animation = blowjob_bob)
                "[the_person.possessive_title] bites her lip sensually and rubs her boobs, while pinching her nipples."

            else: #No big tits, so she can't bounce them
                "[the_person.possessive_title] bites her lip sensually and looks you up and down, as if she's mentally undressing you."

            the_person.char "Well, have you made up your mind, [the_person.mc_title] ?"

        menu:
            "Kiss her":
                $ the_person.draw_person()
                "You step close to [the_person.title] and put an arm around her waist."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She presses her body up against yours."
                else:
                    "When you lean in and kiss her she responds by pressing her body tight against you."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_high_2

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Nothing right now, but I've got a few ideas for later."
                "If [the_person.title] is disappointed she does a good job hiding it. She nods and smiles."
                the_person.char "Well maybe if you take me out for dinner we can talk about those ideas, I'm interested to hear about them."
    return

label alpha_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title] stop, you're making me horny again..."
        else:
            the_person.char "Oh stop [the_person.mc_title], it's not nice to make fun of me like that."
            "[the_person.possessive_title] blushes and looks away."
    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 60:
            the_person.char "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that though, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person.char "I have a [so_title], you really shouldn't be talking to me like that..."
            "She seems more worried about what people could say than actually flirt with you."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh my...hmmm... Thank you, [the_person.mc_title]."
            "[the_person.possessive_title] smiles at you and turns around slowly, giving you a full look at her body."
            the_person.char "I know you cannot avoid to notice me."
        else:
            the_person.char "Oh [the_person.mc_title], do you think too I look good ?"
    return

label alpha_cum_face(the_person):
    if SB_check_fetish(the_person, cum_external_role) or the_person.obedience > 130:
        if SB_check_fetish(the_person, cum_external_role) or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("cum facials") > 0:
            $ pronoun = person_body_shame_string(the_person, "little cum slut")
            the_person.char "Ah... do you like to see my face covered [the_person.mc_title] ? Am I your good [pronoun] ?"
        else:
            the_person.char "Oh, it's everywhere! Next time be more careful, I'm only doing this for you."
    else:
        if the_person.effective_sluttiness() > 70  or the_person.get_opinion_score("cum facials") > 0:
            the_person.char "Oh, yes [the_person.mc_title], I'm covered with your load: it's good for my skin !"
        else:
            if the_person.sex_record.get("Cum Facials", 0) < 3:
                the_person.char "[the_person.mc_title], next time don't mess up my makeup like this."
            elif the_person.sex_record.get("Cum Facials", 0) < 6:
                the_person.char "Again ? Are you not listening ? Cum messes up make up."
            else:
                "[the_person.title] just sighs."
            "She pulls out a tissue and wipes her face quickly."
    return

label alpha_cum_mouth(the_person):
    if SB_check_fetish(the_person, cum_internal_role) or the_person.obedience > 130:
        if SB_check_fetish(the_person, cum_internal_role) or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 0:
            the_person.char "It seems I did a good job, you have a wonderful taste [the_person.mc_title]."
        else:
            if the_person.sex_record.get("Cum in Mouth", 0) < 3:
                the_person.char "I'm not sure I'm really into this, I'll try to like it for you [the_person.mc_title]."
            else:
                "[the_person.title] smiles at you in an obviously fake manner. She clearly doesn't like you cumming in her mouth."
    else:
        if the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 0:
            the_person.char "Mmm, you taste great [the_person.mc_title], you can fill my mouth with your load anytime..."
        else:
            "She spits your cum on the floor..."
            if the_person.sex_record.get("Cum in Mouth", 0) < 4:
                the_person.char "Give me a little heads up next time, [the_person.mc_title]."
    return

label alpha_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Oh... your seed is so close to me. Just a thin, thin condom in the way..."
        else:
            the_person.char "I can feel your seed through the condom. Well done, there's a lot of it."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Yes, give me your seed !"
                the_person.char "If I become pregnant I can say it's my [so_title]'s. I'm sure he would believe it."
            else:
                the_person.char "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know ?"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh no... You need to cum outside, [the_person.mc_title]."
                the_person.char "What would I tell my [so_title] if I got pregnant? He might not believe it's his !"
            else:
                the_person.char "Oh no... You need to cum outside, [the_person.mc_title]."
                the_person.char "I'm in no position to be getting pregnant."
                the_person.char "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."
    return

label alpha_cum_anal(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 200:
            $ pronoun = person_body_shame_string(the_person, "little anal slave")
            the_person.char "Ah...yes pump your seed into your [pronoun]?"
        else:
            the_person.char "Oh my, you filled up my bottom... Remember [the_person.mc_title], you're the only one I let do this."
    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
            the_person.char "Cum inside me [the_person.mc_title], fill my beautiful ass with your cum !"
        else:
            the_person.char "Oh lord, I hope I'm ready for this !"
    return

label alpha_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "I hope you don't mind if I slip this off..."
        else:
            the_person.char "I'm just going to take this off for you [the_person.mc_title]..."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "How about I take this off for you."
        else:
            the_person.char "Oh [the_person.mc_title], you make me feel even more beautiful than I am !"
            the_person.char "I really need to take some more off and show my perfect body."
    else:
        if the_person.arousal < 50:
            the_person.char "I'm really horny: I bet you want to see some more of me."
        else:
            the_person.char "I need to get this off, I want to feel your body against mine !"
    return

label alpha_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my !","Oh, that's not good !", "Darn !", "Oh !", "My word !", "How about that !", "Shock and horror !", "I'll be jiggered !"])
    the_person.char "[rando]"
    return

label alpha_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I'm sorry [the_person.mc_title], but I'm busy. Could we talk later?"
        the_person.char "Maybe you could take me somewhere nice."
    else:
        the_person.char "I'm sorry [the_person.mc_title], we will have to chit-chat later."
    return

label alpha_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "[the_person.mc_title] ! Why do you want me to watch that !"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.possessive_title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(emotion = "sad")
        $ the_person.change_happiness(-1)
        the_person.char "[the_person.mc_title] ! Could you at least try a more private place?"
        "[the_person.possessive_title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(emotion = "default")
        the_person.char "[the_person.mc_title], Why are you doing this here..."
        $ the_person.change_slut_temp(1)
        "[the_person.possessive_title] looks in another direction, but she keeps glancing at you and [the_sex_person.name]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Oh my, [the_person.mc_title] ! You might want I show you my personal skills on that someday..."
        $ the_person.change_slut_temp(2)
        "[the_person.possessive_title] judges [the_sex_person.name]'s performance while you [the_position.verb] her."

    else:
        $ the_person.draw_person(emotion = "happy")
        $ pronoun = person_body_shame_string(the_sex_person, "slut")
        the_person.char "You can do better [the_person.mc_title], give that little [pronoun] what she needs."
        "[the_person.possessive_title] watches you eagerly while [the_position.verb]ing [the_sex_person.name]."

    return

label alpha_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "Come on [the_person.mc_title], do me a little harder."
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.name]. I'm just taking care of you, [the_person.mc_title] !"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person.char "[the_person.mc_title], I need you so much. I think [the_watcher.name] sees that."
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh [the_person.mc_title], I know it's be wrong but being with you right here, just feels so right!"
        $ the_person.change_arousal(1)
        "The longer [the_watcher.name] keeps watching, the more turned on [the_person.possessive_title] gets."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], we shouldn't do this. Not here. What would people think of me ?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.possessive_title] seems uneasy with [the_watcher.name] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "[the_watcher.name], I'm glad you don't criticize me."
        the_person.char "I know I shouldn't do this, but this man makes me feel so live."
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.possessive_title] seems more comfortable [the_position.verb]ing you with [the_watcher.name] around."

    return

label alpha_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        if the_person.obedience > 120:
            "[the_person.possessive_title] gives you a nod and then turns back to her work."
        else:
            "[the_person.possessive_title] does not acknowledge you when you enter."
    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title] looks up from her work when you enter the room."
            the_person.char "Hello [the_person.mc_title]. Let me know if you need my help..."
            "Smiling at you while looking at your crotch, slowly turning back to her work."
        else:
            "[the_person.possessive_title] gives you a warm smile."
            the_person.char "Hello [the_person.mc_title], good to see you here !"
    else:
        if the_person.obedience < 90:
            "[the_person.possessive_title] glances up from her work."
            the_person.char "Hey, how's it going, sexy ?"
        else:
            "[the_person.possessive_title] looks at you when you enter the room."
            the_person.char "Hello [the_person.mc_title], let me know if you need any help."
    return

label alpha_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "You've been good enough tonight ! Come with me: I think you can make me feel even more good..."
            else:
                the_person.char "You were a perfect gentleman tonight [the_person.mc_title], would you like to join me at my place ?"
        else:
            if the_person.love > 40:
                the_person.char "I had such a wonderful time tonight. You make me feel so good, do you want to take a nightcap at my place ?"
            else:
                the_person.char "You've been the wonderful date I deserve. Would you like to share a bottle of wine at my place ?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "You've been such a gentleman tonight. My [so_title] went night fishing with some buddies, so..."
                the_person.char "Join me at my place: I think you can make me feel good..."
            else:
                the_person.char "You were a perfect gentleman tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person.char "He has his poker night with some friends. Would you like to join me at my place and have glass of wine ?"
        else:
            if the_person.love > 40:
                the_person.char "I don't want this night to end. My [so_title] is on a business trip this weekend..."
                the_person.char "Do you want to come over to my place so we can spend more time together ?"
            else:
                the_person.char "Tonight was fantastic. I think my [so_title] is out for the night."
                the_person.char "So... do you want to come over to my place for a cup of coffee ?"
    return

label alpha_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Is that it ? You're going to drive me crazy [the_person.mc_title], I'm so horny..."
            else:
                the_person.char "All done ? I hope you were having a good time."
        else:
            if the_person.arousal > 60:
                the_person.char "Already done ? I don't know how you can stop, I'm so excited at the moment !"
            else:
                the_person.char "Leaving already ? Well, that's disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "That's it ? Well, you could at least make me cum too."
            else:
                the_person.char "All done ? Maybe we can pick this up the next time when we're alone."
        else:
            if the_person.arousal > 60:
                the_person.char "I... I don't know what to say, did I exhaust you ?"
            else:
                the_person.char "That's all you wanted ? I guess we're finished then."
    return

label alpha_sex_take_control(the_person):
    if the_person.arousal > 60:
        the_person.char "I just can't let you go [the_person.mc_title], you're going to finish what you started !"
    else:
        the_person.char "Do you think you're going somewhere ? You are not yet done with me [the_person.mc_title]."
    return

label alpha_sex_beg_finish(the_person):
    "Wait, you can't stop now ! C'mon [the_person.mc_title], I'm almost there, do your job !"
    return


## Taboo break dialogue ##
label alpha_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person.char "Oh, well hello there ! Do you... Want to do anything with me ?"
    elif the_person.love >= 20:
        the_person.char "So you feel it too ?"
        "She sighs happily."
        the_person.char "I... I want to kiss you. I know you want the same..."
    else:
        the_person.char "I don't know if this is a good idea [the_person.mc_title]..."
        mc.name "Let's just see how it feels. Trust me."
        "[the_person.title] eyes you warily, but you watch her resolve break down."
        the_person.char "Okay... Just one kiss, to start."
    return

label alpha_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person.char "Do you want to know something ?"
        mc.name "What ?"
        the_person.char "I've had dreams just like this before. They always stop just before you touch me."
        mc.name "Well, let's fix that right now."

    elif the_person.love >= 20:
        the_person.char "I want you to know I take this very seriously, [the_person.mc_title]."
        mc.name "Of course. So do I [the_person.title]."
        the_person.char "I normally wouldn't even think about letting you touch me."
        mc.name "What do you mean ?"
        the_person.char "I've always been the leader, the number one... But I get this feeling when you're around..."
        the_person.char "Somehow I just can't say no to you."
    else:
        the_person.char "You shouldn't be doing this [the_person.mc_title]. We... we barely know each other."
        mc.name "You don't want me to stop though, do you ?"
        the_person.char "I don't... I don't know what I want."
        mc.name "Then let me show you."
    return

label alpha_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person.char "Look at how big your penis is. Darn, did I just found the right one for me ?"
        the_person.char "Relax [the_person.mc_title], and let me enjoy it, okay ?"
    elif the_person.love >= 20:
        the_person.char "Oh my... If I'm honest I wasn't expecting it to be quite so... Big."
        mc.name "Don't worry, it doesn't bite. Go ahead and touch it, I want to feel your hand on me."
        "She bites her lip playfully."
    else:
        the_person.char "We should stop here... I don't want you to get the wrong idea about me."
        mc.name "Look at me [the_person.mc_title], I'm rock hard. Nobody would ever know if you gave it a little feel."
        "You see her resolve waver."
        the_person.char "It is very... Big. Just feel it for a moment ?"
        mc.name "Just a moment. No longer than you want to."
        "She bites her lip as her resolve breaks completely."
    return

label alpha_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person.char "Do it [the_person.mc_title]. Touch my pussy."
    elif the_person.love >= 20:
        the_person.char "I'm as nervous as a little girl. Does a woman like me make you feel that way too [the_person.mc_title] ?"
        mc.name "Just take a deep breath and relax. You trust me, right ?"
        the_person.char "Of course. I trust you."
    else:
        the_person.char "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person.char "Be very careful!"
        mc.name "Just a little. Trust me, it's going to feel amazing."
    return

label alpha_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person.char "What would you like ?"
    mc.name "I'd like you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person.char "I... I really should say no."
        mc.name "But you aren't going to."
        "She shakes her head."
        the_person.char "I've told people all my life that I didn't do things like this, but now it's all I can think about."
    elif the_person.love >= 30:
        the_person.char "Oh [the_person.mc_title] ! Really ? I know most men are into that sort of thing, but I..."
        the_person.char "Well, I'm a little more sophisticated than that."
        mc.name "What's not classy about giving pleasure to your partner ? Come on [the_person.title], aren't you a little curious ?"
        the_person.char "I'm curious, but I... Well... How about I just give it a taste and see how that feels ?"
        mc.name "Alright, we can start slow and go from there."
    else:
        the_person.char "I'm sorry, I think I misheard you."
        mc.name "No you didn't. I want you to put my cock in your mouth and suck on it."
        the_person.char "I could never do something like that [the_person.mc_title], what would people think ?"
        the_person.char "I'm not some kind of cheap hooker that you pickup on the street, I don't \"suck cocks\"."
        mc.name "Yeah you do, and you're going to do it for me."
        the_person.char "And why would I do that?"
        mc.name "Because deep down, you want to. You can be honest with me and with yourself: aren't you curious what it's going to be like?"
        "She looks away, but you both know the answer."
        mc.name "Just get on your knees, put it in your mouth, and if you don't like how it feels you can stop."
        the_person.char "What are you doing to me [the_person.mc_title] ? I used to think I was better than this..."
    return

label alpha_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready ?"
    if the_person.effective_sluttiness() >= 45:
        the_person.char "Oh what a gentleman I have ! Why don't you get down to business, [the_person.mc_title]!"
    elif the_person.love >= 30:
        the_person.char "You're such a gentleman [the_person.mc_title], but you don't have to do that."
        mc.name "I don't think you understand. I {i}want{/i} to eat you out, I'm just waiting for you to say it."
        "[the_person.title] won't admit it..."
        the_person.char "Oh... Well then, I suppose you can get right to it."
    else:
        the_person.char "You're a gentleman [the_person.mc_title], but you don't need to do that."
        if not the_person.has_taboo("sucking_cock"):
            the_person.char "It's flattering that you'd want to return the favour though, so thank you."

        mc.name "No, I don't think you understand what I'm saying. I {i}want{/i} to eat you out, I'm just waiting for you to say it."
        "[the_person.title] won't admit it..."
        the_person.char "Really ? I mean... I just haven't met many men who {i}want{/i} to do that."
        mc.name "Well you have now. Just relax and enjoy yourself."
    return

label alpha_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person.char "[the_person.mc_title], I'm not ashamed to say I'm very excited right now !"
        "She giggles gleefully."
        the_person.char "Come on and show me what you can do to a goddess with that monster !"
    elif the_person.love >= 45:
        the_person.char "Go ahead [the_person.mc_title]. I think we're both ready for this."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person.char "Oh my god, what am I doing here with you [the_person.mc_title] ?"
            the_person.char "I'm not the type of person to do this... Am I ? Is this who I've always been, and I've just been lying to myself ?"
            mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
            "She closes her eyes and takes a deep breath."
            the_person.char "I... I want to have sex with you. I'm ready."
        else:
            the_person.char "I'm glad you're doing this properly this time."
            "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return

label alpha_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person.char "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."

    elif the_person.love >= 60:
        the_person.char "This is really something you want to do then [the_person.mc_title] ?"
        mc.name "Yeah, it is."
        the_person.char "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person.char "I don't know if you'll even fit though. Your penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person.char "Oh lord, what happened to me ?"
            the_person.char "I am a respectable lady, now I'm about to get fucked in the ass..."
            the_person.char "We've never even had sex before and now I'm letting you penetrate my ass !"

        else:
            the_person.char "I'm not sure about this [the_person.mc_title]... I'm not even sure if you can fit inside me there !"
            mc.name "You're the sexiest: I just can't resist to try your ass !"
            the_person.char "Oh lord, what happened to me..."
            the_person.char "I am a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person.char "I doubt it. Come on then, there's no point stalling any longer."
    return

label alpha_condomless_sex_taboo_break(the_person):
    if the_person.get_opinion_score("bareback sex") > 0:
        the_person.char "You want to have sex without any protection? I'll admit, that would really turn me on."
        if the_person.get_opinion_score("creampies") > 0:
            the_person.char "It would be very naughty if you came inside me though..."
            mc.name "Don't you think we're being naughty already?"
            "She bites her lip and nods."
            the_person.char "I think we are."
        elif the_person.get_opinion_score("creampies") < 0:
            the_person.char "You will need to pull out though, I hate having it dripping out of me all day."
        else:
            the_person.char "You will need to pull out though, understood ? Good."

    elif the_person.love > 60:
        the_person.char "If you think you're ready for this commitment, I am to. I want to feel close to you."
        if the_person.get_opinion_score("creampies") > 0:
            the_person.char "When you're going to finish you don't have to pull out unless you want to. Okay ?"
            mc.name "Are you on the pill ?"
            "She shakes her head."
            the_person.char "No, but I trust you to make the decision that is right for both of us."
        elif the_person.get_opinion_score("creampies") < 0:
            if the_person.kids == 0:
                the_person.char "You will have to pull out though, do you understand ? I really didn't plan to become a mother."
            else:
                the_person.char "You will have to pull out though, do you understand ? I've been pregnant before and it isn't nice."
        else:
            if the_person.kids == 0:
                the_person.char "You will have to pull out though. I really didn't plan to become a mother."
            else:
                the_person.char "You will have to pull out though, understood ? You are definitely not ready for that."

    else:
        the_person.char "You want to have sex without protection ? That's very risky [the_person.mc_title]."
        if the_person.has_taboo("vaginal_sex"):
            mc.name "I want our first time to be special though, don't you ?"
            "She takes a second to think, then nods."
            the_person.char "I do. You need to be very careful where you finish, do you understand ?"
        else:
            mc.name "It will feel so much better raw, for both of us."
            the_person.char "I have wondered what it would be like..."
            "She takes a moment to think, then nods."
            the_person.char "Fine, you don't need a condom. Be very careful where you finish, understood ?"
    return

label alpha_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.get_opinion_score("skimpy outfits") * 5):
        the_person.char "This is the first time you've gotten to see my underwear. I hope you like what you see."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I will. You have good taste."
            the_person.char "Well then, what are you waiting for ?"
        else:
            mc.name "I've already seen you out of your underwear, but I'm sure it complements your form."
            the_person.char "Time to find out. What are you waiting for ?"

    elif the_person.love > 15:
        the_person.char "This is going to be the first time you've seen me in my underwear. You'll be amazed !"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I'll be: you look stunning in it."
            the_person.char "Well then, take off my [the_clothing.display_name] for me."

        else:
            mc.name "I already know you have a beautiful body, some nice underwear can only enhance the experience."
            the_person.char "You really know how to please me ! Help me take off my [the_clothing.display_name]."

    else:
        the_person.char "If I take off my [the_clothing.display_name] you'll see me in my underwear."
        mc.name "That's the plan, yes."
        the_person.char "I shouldn't be going around half naked for men I barely know. What would people think ?"
        mc.name "Why do you care what other people think ? Forget about them and just focus on us."

        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Why do you care what other people think ? Forget about them and just focus on the moment."
            the_person.char "I have to keep some kind of decorum, but I am intrigued..."

        else:
            mc.name "You might have wanted to worry about that before I saw you naked. You have nothing left to hide."
            the_person.char "I suppose you're right..."
    return

label alpha_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.get_opinion_score("showing her tits") * 5):
        the_person.char "Oh, so you want to take a look at my breasts ?"
        if the_person.has_large_tits():
            "She bounces her chest for you, jiggling the big tits hidden underneath her [the_clothing.display_name]."
        else:
            "She bounces her chest and gives her small tits a little jiggle."
        the_person.char "Well it would be a shame not to let you get a glimpse, right ? I've been waiting for you to ask."
        mc.name "Let's get that [the_clothing.display_name] off so I can see them then."

    elif the_person.love > 25:
        the_person.char "Oh, you want to get my breasts out ?"
        if the_person.has_large_tits():
            "She looks down at her own large rack, tits hidden restrained by her [the_clothing.display_name]."
            the_person.char "I don't have to ask why, but I'm glad you're interested in them."
        else:
            the_person.char "I'm glad you're still interested in smaller breasts. It seems like every man is mad boob-crazy these days."
        mc.name "Of course I'm interested, let's get that [the_clothing.display_name] out of the way so I can get a good look at you."

    else:
        the_person.char "[the_person.mc_title] ! If you take off my [the_clothing.display_name] I won't be decent any more !"
        mc.name "I want to see your breasts and it's blocking my view."
        the_person.char "I'm aware it's \"blocking your view\", that's why I put it on this morning."
        if the_person.has_large_tits() and the_clothing.underwear:
            the_person.char "Besides, a woman like me needs a little support. These aren't exactly light."
        mc.name "Come on [the_person.title]. You're gorgeous, I'm just dying to see more of you."
        the_person.char "Well I'm glad I have that effect on you. And you always know the right keys to use on me..."
    return

label alpha_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.get_opinion_score("showing her ass") * 5):
        the_person.char "You want to get me out of my [the_clothing.display_name] ? Well, I'm glad you've finally asked."

    elif the_person.love > 35:
        the_person.char "Oh, slowly there [the_person.mc_title]. If you take off my [the_clothing.display_name] I'll be nude in front of you..."
        if the_person.has_taboo("touching_vagina"):
            mc.name "That's exactly what I want: to get a look at your magnificent body."
            the_person.char "Oh, continue... That's the best way to talk to a lady like me."

        else:
            mc.name "That's exactly what I want: to get a look at your magnificent body."
            the_person.char "Oh stop, you, I suppose you can take it off and have a look."

    else:
        the_person.char "Oh! Be careful, or you're going to have me showing you everything !"
        mc.name "That is what I was hoping for, yeah."
        the_person.char "Well ! I mean... I'm not that kind of woman [the_person.mc_title] !"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Don't you want to be though ? Don't you want me to enjoy your body?"
            the_person.char "I... I mean, I might, but I shouldn't... You shouldn't..."
        else:
            mc.name "Of course you are! I've had my hand on your pussy already, I just want to see what I was feeling before."
            the_person.char "I... I mean, that wasn't... I..."

        "You can tell her protests are just to maintain her image, and she already knows what she wants."
        mc.name "Just relax and let it happen, you'll have a good time."
    return

label alpha_facial_cum_taboo_break(the_person):

    return

label alpha_mouth_cum_taboo_break(the_person):

    return

label alpha_body_cum_taboo_break(the_person):

    return

label alpha_creampie_taboo_break(the_person):

    return

label alpha_anal_creampie_taboo_break(the_person):

    return