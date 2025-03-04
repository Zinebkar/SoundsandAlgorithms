# Mind Hackers: Whispers in the wires - Project 2024 SECont
# File for the story of level 2

# Level related variables:
define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define new_objectives_not_heard = True
define search_visited = False
define bob_visited = False
define open_gil_post = False
define gil_visited = False
default lab_seen = False
default uni_access_denied = False
default dumpster_doven = False
default dumpster2_doven = False
default warning_counter = 0
default rat_seen = False
default medical_tools_seen = False
default symbols_seen = False 
default left_pc_seen = False 
default left_wall_seen = False 
default trash_seen = False
default dumpster_explained = False
default machine_struck_counter = 0
default snack_gotten = False
default open_gil_tag = False
default gill_house_seen_bob = False
default gill_house_seen_gill = False
default in_dorms = True

label level_2_start:
    
    $ in_dorms = True
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2
    
    "You walk over and gather around a table while opening up your laptop."
    scene bg laptop full at zoom_in
    play music suspense_music1 volume loudness fadeout 1.0
    L "What exactly is our plan now? What are we doing with the information we find?"
    PC "We could go to the facility Bob Anderson works at and look for Felix?"
    PC "I also don't think that we have access to his workplace and we probably won't find it just sitting on some website."
    L "If that is the problem we could try to write a phishing email to Bob Anderson so that he grants us access."
    A "Do you think it's realistic that we can convince him to do that?"
    L "Depends on what we find out about Bob Anderson's background. Maybe there is something we can use on his social media or some {color=[medievilColor]}Medievil{/color} web page?"
    PC "Either way we should do some research on him."

label research:
    $ current_location = 0
    $ in_dorms = True
    scene bg laptop full
    show screen phone_icon
    show screen laptop_screen
    with dissolve
    $ show_textbox = False
    ""
    jump empty_label

# Warnings to warn the player of writing the phishing mail without the sufficient information
label warning_1:
    $ show_image_buttons = False
    $ warning_counter = 1
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Im not sure if we have enough information for a phishing mail. We should do more research first!"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    return

label warning_2:
    $ show_image_buttons = False
    $ warning_counter = 2
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Didn't I already tell you? We need to do more research first!"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    return

label warning_3:
    $ show_image_buttons = False
    $ warning_counter = 3
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Are you hard of hearing? We need more information before we write a phishing mail!"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    return

label warning_4:
    $ show_image_buttons = False
    $ warning_counter = 4
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Ok fine if you are beyond reason, go and write your pathetic email!"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    hide screen laptop_screen
    show screen mail_screen
    return

# Dialogue for the social media section on the Laptop
label social_button_1:
    $ show_image_buttons = False
    $ show_textbox = True
    if search_visited == False:
        show screen social_screen_explore
        PC "Maybe we should look up Bob Anderson."
        $ show_image_buttons = True
        show screen social_screen_search
        $ show_textbox = False
        $ search_visited = True
        jump empty_label
    elif search_visited == True:
        $ show_image_buttons = True
        show screen social_screen_search
        $ show_textbox = False
        jump empty_label

label social_button_2:
    $ show_image_buttons = False
    $ show_textbox = True
    if bob_visited == False:
        show screen social_screen_bob
        PC "Interesting profile."
        L "Lucky that he isn't private."
        A "What a good looking man."
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        $ bob_visited = True
        jump empty_label
    elif bob_visited == True:
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        jump empty_label

label social_button_3:
    show screen social_screen_bob_tag
    $ show_image_buttons = False
    $ show_textbox = True
    if open_gil_tag == False:
        PC "Who is that person?"
        L "He seems like someone important."
        PC "The post is from his Bob's work."
        A "Then we should check him out as well. If he has something to do with {color=[medievilColor]}Medievil{/color} he might be of interest."
        $ show_image_buttons = True
        $ show_textbox = False
        $ open_gil_tag = True
        jump social_button_5
    elif open_gil_tag == True:
        $ show_image_buttons = True
        hide screen social_screen_bob_tag
        show screen social_screen_gill
        $ show_textbox = False
        jump empty_label

label social_button_4:
    show screen social_screen_bob
    $ show_image_buttons = False
    $ show_textbox = True
    if gill_house_seen_gill == False:
        A "Is this Bob's house?"
        if gil_visited == False:
            PC "No. It's from someone called Gill Cameron. Mr. Anderson is just visiting?"
            L "Gotta say it looks pretty nice."
        else:
            PC "No. It's Gills house."
            L "Gotta say it looks pretty nice."
            A "And even better, there is a street sign. Maybe we can get some information from his place."
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        $ gill_house_seen_bob = True
        if gil_visited == True:
            $ renpy.notify("new objectives on your map")
            $ phone_not_map = True
        jump empty_label
    else:
        "You see the same house from the picture on gills profile"
        $ gill_house_seen_bob = True
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        jump empty_label
    $ experience += 20
    call gain_experience(20)
    
label social_button_5:
    $ show_image_buttons = False
    $ show_textbox = False
    hide screen social_screen_bob_tag
    show screen social_screen_gill
    pause 1
    $ show_textbox = True
    if gil_visited == False:
        
        if gill_house_seen_bob == False:
            PC "Interesting profile."
            L "So this person is called Gill Cameron."
            A "Is there something interesting?"
            PC "Nothing new. Only that he knows Bob's from work."
        else:
            PC "This person, it's Gill Cameron."
            L "From the house post? Does he work for {color=[medievilColor]}Medievil{/color}?"
            PC "Not from what i found. But he seems to at least work with them"
            A "There was a street sign in that post from before. Maybe we could go to his place if we need more information."
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        $ gil_visited = True
        if gill_house_seen_bob == True:
            $ renpy.notify("new objectives on your map")
            $ phone_not_map = True
        jump empty_label
    elif gil_visited == True:
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        jump empty_label

    label social_button_6:
    show screen social_screen_gill
    $ show_image_buttons = False
    $ show_textbox = True
    if gill_house_seen_bob == False:
        L "Wow Gill has a nice looking house."
        A "And even better a visible street sign. If he works with Bob Anderson then maybe we can check out his place if we need more information."
        show screen social_screen_gill
        $ show_textbox = False
        $ gill_house_seen_gill = True
        if gil_visited == True:
            $ renpy.notify("new objectives on your map")
            $ pohone_not_map = True
            $ show_image_buttons = True
        jump empty_label
    else:
        "You see the same house from the post on Bobs profile."
        $ show_textbox = False
        $ gill_house_seen_gill = True
        $ show_image_buttons = True
        jump empty_label

# Dialogue for the web search section on the Laptop
label website1_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_1_not_seen = False
    show screen website1_screen
    PC "Apparently {color=[medievilColor]}Medievil{/color} is getting funds from our city."
    A "Is there a reason?"
    L "Not really. Just for stronger industry and more workplaces."
    $ show_image_buttons = True
    show screen website1_screen
    $ show_textbox = False
    jump empty_label
    ""
label website2_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_2_not_seen = False
    $ phone_not_map = True
    show screen website2_screen
    PC "Here is something about a lab at our university. According to these news it was offered to {color=[medievilColor]}Medievil{/color} for research."
    L "Maybe we should check it out."
    A "You think we have access?"
    L "I think we can get it if we really want."
    $ show_image_buttons = True
    call websearch_done from _call_websearch_done
    show screen website2_screen
    $ show_textbox = False
    jump empty_label
    ""
label website4_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_3_not_seen = False
    $ phone_not_map = True
    show screen website4_screen
    PC "Here's something interesting."
    A "What?"
    PC "The location of Mr. Andersons Office."
    L "Maybe we should pay him a visit."
    $ show_image_buttons = True
    play sound not2
    call websearch_done from _call_websearch_done_1
    show screen website4_screen
    $ show_textbox = False
    jump empty_label
    ""

label website1_call:
    show screen website1_screen
    ""
    jump empty_label
label website2_call:
    show screen website2_screen
    ""
    jump empty_label
label website3_call:
    show screen website3_screen
    ""
    jump empty_label
label website4_call:
    show screen website4_screen
    ""
    jump empty_label
label websearch_done:
    if not website_2_not_seen and not website_3_not_seen:
        $ renpy.notify("You have new objectives on your map.")
    return

label dumpsterdive:
    $ show_textbox = True
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 5 zoom 2
    show leonie serious at left:
        yalign 0.4
        xalign -1.0
        linear 0.5 xalign 0.1
    show alex serious1 at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve
    
    PC "Let's head to Bob Andersons office. I wonder what we can find there."
    

    if dumpster_explained == False:
        show leonie thinking at left:
            yalign 0.4
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show leonie thinking at alex_right:
            xalign 2.0
            yalign 0.4
            linear 0.5 xalign 1.0
        with dissolve
        A "We don't have to step in. We can stay outside and do dumpsterdiving, to find out more information."
        show leonie surprised at left:
            yalign 0.3
            zoom 1.2
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right:
            xalign -1
            yalign 0.4
        with dissolve
        A "People often times throw away sensitive information without disposing of it correctly. If we look at the trash we could find something compromising that could get us a lead."
        "You, Alex and Leonie go to the building."
        $ dumpster_explained = True
        
    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg back office at zoom_in
    with dissolve
    show leonie happy at left:
        xalign -1.0
        yalign 0.4
        linear 0.5 xalign 1.2
    with  moveinleft
    show alex neutral at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with  moveinright
    play music suspense_music1 volume loudness fadeout 1.0

    PC "Hmm, the building seems bigger than described on the internet."
    show leonie happy at left:
        yalign 0.4
        xalign 1.2
    with dissolve

    L "Yes but luckily the garbage bins are directly over there."
    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve

    A "I think someone has to look out for anyone incoming, not that they see us searching through the trash as thats pretty suspicious. Ill take on the role and whistle loudly to warn you."
    PC "Thank you bro. Let's get going then."
    $ experience += 20
    call gain_experience(20)

    scene bg wastepaper 

    jump dumpster_diving_minigame_start

label after_dumpsterdive:
    $ show_textbox = True
    scene bg back office at zoom_in
    with dissolve
    show leonie happy at left:
        xalign -1.0
        yalign 0.4
        linear 0.5 xalign 0.0
    with  moveinleft
    show alex smile at alex_right:
        xalign 6.0
        yalign 0.1
        linear 0.5 xalign -1.0
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a receipt from Restaurante Italiano."
    L "Isn't that the super fancy expensive restaurant where only celebrities and rich people go?"
    A "Yup, I've heard a lot of wild things about that restaurant. You're right, only the higher classes can afford it."
    PC "Seems like Bob Anderson went there with someone."
    L "I wonder whom he went there with. The food and drinks definitely look like for 2 people."
    A "Maybe we can use this for our phishing mail later."
    $ gloss_dumpster_seen = True
    $ phone_not_glossary = True
    $ dumpster_doven = True
    jump research 

label dumpsterdive2:
    $ show_textbox = True
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2
    show leonie serious at truecenter:
        yalign -1.0
        xalign 0.0
        linear 0.5 yalign 0.4
    show alex serious2 at alex_right:
        xalign 0
        yalign -1.0
        linear 0.5 yalign 0.4
    with dissolve

    PC "Well then I suggest we should head out to Gill's place and investigate there."

    if dumpster_explained == False:
        show leonie thinking at left:
            yalign 0.4
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show alex neutral at alex_right:
            xalign -4.0
            yalign 0.4
        with dissolve
        A "We don't have to step in. We can stay outside and do dumpster diving, to find out more information."
        show leonie surprised at left:
            zoom 1.6
            xalign 1.0
            yalign 0.4
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right:
            xalign 0
            yalign 0.4
        with dissolve
        A "People often times throw away sensitive information without disposing of it correctly. If we look at the trash we could find something compromising that could get us a lead."
        "You, Alex and Leonie go to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft

    #scene bg gilshouse #its dark outside
    scene bg gill house front
    with dissolve
    show leonie happy at left:
        yalign 1
        linear 0.4 yalign 0.4
    with  moveinleft
    show alex neutral at alex_right:
        xalign -3.0
        yalign -1
        linear 0.4 yalign 0.4
    with  moveinright
    play music suspense_music1 volume loudness fadeout 1.0

    PC "Wow, what a beautiful looking house."
    show leonie happy at left:
        yalign 0.4
    with dissolve

    L "Are we sure Gill is a bad guy? no way an evil person has such a wonderful house."
    show alex neutral at alex_right:
        yalign 0.4
        xalign -1.0
    with dissolve
    A "Well, in movies the bad guys tend to own a more expensive house, since they earn more money through illegal ways, than the average people do."

    PC "I suggest we should just go ahead and start, the more time we spend here the more suspicion we raise."

    show alex happy at alex_right:
        xalign 1.0
        yalign 0.2
    with dissolve 

    A "Alright, let's get digging then."

    show leonie neutral at left:
        yalign 0.3
    with dissolve
    L "Digging into trash... yippee."

    show alex angry at alex_right:
        zoom 0.5
        xalign 1.3
        yalign 0.1
    with dissolve
    A "Well, if you're not so enthusiastic about it, then I suggest you look out and warn us in case anyone comes here. [PN] and I will go on then don't worry."

    show leonie sad at left:
        yalign 0.4
    with dissolve

    L "Mhmm."

    scene bg gill dumpster at zoom_in
    jump dumpster_diving_minigame2_start

label after_dumpsterdive2:
    $ show_textbox = True
    scene bg gill house front at zoom_in
    with dissolve
    show leonie happy at left:
        yalign 0.4
    with  moveinleft
    show alex neutral at alex_right:
        xalign 0
        yalign 0.4
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a note from Gill."
    L "Says something about a handover."
    A "Interesting."
    PC "I wonder if this can be of any use for our phishing mail."
    $ gloss_dumpster_seen = True
    $ dumpster2_doven = True
    jump research

    $ experience += 20
    call gain_experience(20)


# Notifications for the map
label lab_access_denied:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "The security is alert of your attempted intrusion. They will surely not let you near the lab again."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label lab_visited:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You have already seen everything there is to see here."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label dumpster_empty:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You already have all the information from this garbage."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return


label visitlab:
    $ show_textbox = True
    $ current_location = 1

    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 10 zoom 2
    show leonie serious at left:
        yalign 4.0
        xalign 0.9
        linear 0.5 yalign 0.4
    show alex serious1 at alex_right:
        xalign 1.0
        yalign -5.0
        linear 0.5 yalign 0.5
    with dissolve

    PC "Fine, I'll suggest that we head to the university lab then. The lab is in a part of the campus that practically never gets used so that's quite shady."
    show leonie thinking at left:
        yalign 0.4
    with dissolve

    L "Good point, but maybe they just don't want to disturb others with their noises or get distracted?"
    show alex neutral at alex_right:
        xalign -2.0
        yalign 0.4
    with dissolve

    A "Or maybe they want to keep their activities hidden."
   
    PC "Damn dude, you almost sound like Felix."
    show alex serious2 at alex_right:
        xalign 0.4
        yalign 0.4
    with dissolve

    A "I really wonder where he is, I miss that little fella. We should get going for his sake."

    hide alex 
    hide leonie
    with dissolve
    scene black
    with dissolve

    "You head out to the university to find the lab the article mentioned."

    scene bg uni hallway at zoom_in
    with dissolve
    show leonie thinking at left:
        yalign -1.5
    with  moveinleft
    show alex neutral at alex_right:
        xalign 0.1
        yalign 0.4
    with  moveinright

    A "I've never been at this part of the university."

    show leonie neutral at left:
        yalign 0.3
        xalign 0
    with dissolve

    L "Well our campus is quite big and none of us were here. Barely anyone is ever here to be exact."

    PC "This part does seem more grim and gloomy."

    show alex angry at alex_right:
        zoom 0.55
        xalign 3.0
        yalign 0.2
        linear 0.5 xalign 1.5
    with dissolve

    A "Since you all seem so scared I guess I'll take the lead and get us going."

    hide alex 
    hide leonie 
    with dissolve

    "You head to the door of the lab, and see that there's a pin needed to unlock the door."

label lab_entry_choice:
    scene bg medievil front lab  at truecenter:
        zoom 1
        linear 20 zoom 2.5
    with dissolve

    show leonie thinking at left:
        xalign -1.0
        yalign 0.4
        linear 0.5 xalign 0.1
    with dissolve
    show alex neutral at alex_right:
        xalign 4.0
        yalign 4.0
        linear 0.5 yalign 0.4
    with dissolve

    L "What should we do now?"

    menu: 
        "Wait for someone to enter the lab in disguise.":
            show leonie neutral at left:
                yalign -4.0
                linear 0.5 yalign -1.0
            with dissolve
            L "Maybe we can wait until someone opens the door for us."
            show alex serious1 at alex_right:
                xalign 1.0
                yalign 0.4
            with dissolve
            A "And then sneak inside without them noticing. Really!?"
            show leonie serious at left:
                yalign 0.4
            with dissolve
            L "No, we simply watch what they input and then wait for them to leave."
            show alex neutral at alex_right:
                xalign -1.0
                yalign 0.4
            with dissolve
            A "We would have to wait quite far away to stay hidden."
            PC "That's fine. I have binoculars at home i can get."
            show leonie happy at left:
                yalign 0.4
            with dissolve
            L "And we will find a good spot for observation."
            scene black
            with dissolve
            "The three of you split up. Alex and Leonie search for a location that has a line of sight to the door while still being far enough away to not raise suspicions while you get your binoculars from home."
            jump lab_wait
        "Ask around to get access.":
            $ uni_access_denied = True
            hide leonie
            hide alex
            with dissolve
            "You ask the first person you see trying to enter to give you access."
            "They deny your request and notifiy the security about your presence."
            "Because you dont want to meddle with them any further you decide to return home and continue your research."
            jump research
        "Get a snack from the nearby vending machine" if snack_gotten == False:
            hide leonie
            hide alex
            show bg vending machine 1
            with dissolve
            $ snack_gotten = True
            "Researching all day made you kinda hungry and since there is nothing else nearby you decide to get a snack from the local wending machine."
            "After paying 1.20$ for an overpriced chocolate bar you watch as your snack gets stuck in the spiral of a lower row."
            jump wending_maschine

# Someone didn't know how to write vending machine
label wending_maschine:
    menu:
        "Shake the vending machine to get your snack" if machine_struck_counter == 0:
            $ machine_struck_counter += 1
            "You begin shaking the machine but the bar doesn't move."
            jump wending_maschine

        "Shake the wending machine even harder to get your snack" if machine_struck_counter == 1:
            #$ machine_struck_counter += 1
            "Again you shake the machine like a maniac and though the bar doesn't move you get noticed by a guy who was about to enter the lab."
            "You try to play it off but the person informs the security about your fight with the machine and even though you stay low for the next half hour they won't take their eyes off you."
            "Since the entire facility is now alert to your presence you decide to head home and continue your investigation from there."
            $ current_location = 0
            $ uni_access_denied = True
            jump research

        "Return to the lab door to figure out a way to get in":
            "You surrender your snack and your dignity to the machine and continue your mission."
            jump lab_entry_choice

label lab_wait:
    $ hide_map = True
    $ gloss_surfing_seen = True
    $ phone_not_glossary = True
    scene bg uni hallway at zoom_in # need better spot than hallway?
    with dissolve
    play music mystery_music1 volume loudness fadeout 1.0
    "As you return you got to the location Leonie sent you. A desk at the snack machine with four chairs."
    show leonie neutral at left:
        yalign -1.0
    show alex neutral at alex_right:
        xalign 1.0
        yalign -2
        linear 0.4 yalign 0.4
    with dissolve
    "You sit down and wait for what feels like an eternity until..."
    show alex serious3 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "Guys look. We caught one."
    show leonie serious at right:
        yalign 0.4
    with dissolve
    L "Quiet, we don't want him to notice us. Just observe what he presses."
    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    scene bg pinpad at zoom_in
    show binoculars
    with dissolve
    "You see an ominous person walking up to the door. He does not look like any university employee you know."
    "While you observe, you whisper to your friends what you see."
    show bg pinpad 4
    show binoculars
    with dissolve
    pause
    show bg pinpad 7
    show binoculars
    with dissolve
    pause
    show bg pinpad 1
    show binoculars
    with dissolve
    pause
    show bg pinpad 9
    show binoculars
    with dissolve
    pause
    show bg pinpad 6
    show binoculars
    with dissolve
    pause
    show bg pinpad 5
    show binoculars
    with dissolve
    pause
    show bg pinpad e
    show binoculars
    with dissolve
    pause

    $ notes.add_data(NoteData("Pinpad: 471965"))
    
    scene bg uni hallway at zoom_in
    with dissolve
    show alex serious2 at alex_right:
        xalign 1.0
        yalign 4.0
        linear 0.5 yalign 0.5
    with dissolve
    A "Is that all?"
    PC "Yup. The door is open."
    $ experience += 20
    call gain_experience(20)

    show leonie happy at left:
        yalign -1.0
        xalign -1.0
        linear 0.5 xalign 0.1
    with dissolve
    L "Great. Now we just have to wait until he leaves."
    show alex smile at alex_right:
        xalign 1.0
        yalign 0.1
    with dissolve
    A "Perfect. I needed a break after all the previous waiting."
    PC "You can follow him if you want, but don't expect us to follow."
    show alex happy at alex_right:
        xalign 1.0
        yalign 0.1
    with dissolve
    A "Nah I'm good. Just kidding."
    show leonie thinking at left:
        yalign 0.4
        zoom 0.8
    with dissolve
    L "We should change locations to avoid getting his attention. It could make him suspicious if we were still here when he leaves."
    show alex neutral at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "We could wait outside for him to exit."
    show leonie serious at left:
        yalign 0.3
    with dissolve
    L "Ok. Alex and I wait at the front and you wait at the back."
    PC "Roger that."
    scene black # could be changed to uni backside instead if we have the image
    with dissolve
    "You get into position and start waiting."
    "After a short while you get a message from Alex telling you to get to the lab."
    "When you approach the lab you see your friends in front of the open door."
    scene bg medievil front lab at truecenter:
            zoom 1
            linear 15 zoom 2.1
    with dissolve
    
    show leonie neutral at left:
        yalign -4.0
        linear 0.5 yalign -1.0
    show alex neutral at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve
    PC "I assume he left."
    show alex smile at alex_right:
        xalign 1.0
        yalign 0.1
    with dissolve
    A "No he invited us in."
    show leonie sad at right:
        yalign 0.4
    with dissolve
    "..."
    show leonie neutral at left:
        yalign -1.0
    with dissolve
    L "Anyways. Let's enter the PIN."

    show screen phone_icon
    show screen pin_pad_input
    with dissolve
    ""
    jump empty_label

label pin_pad_mini_game_complete:
    hide screen phone_icon
    hide screen pin_pad_input
    with dissolve
    # scene bg pinpad
    # show image "images/backgrounds/pinpad/pin enter 6.png"
    A "Nice. Seems like the door opened."
    scene bg medievil lab at truecenter:
            zoom 1.0
            linear 15 zoom 2
    with dissolve
    "Upon entering the lab, the three of you start to investigate." 
    L "Let's take a look around this lab."

label inside_lab:
    if rat_seen and left_pc_seen and left_wall_seen and symbols_seen:
        jump inside_lab_done
    $ show_textbox = False
    scene bg medievil lab
    show screen left_cage
    show screen left_pc
    show screen left_wall
    show screen symbol_screen
    show screen right_cage
    show screen right_pc
    show screen trash
    with dissolve
    #show screen medical_tools

    show screen phone_icon
    with moveinright
    jump empty_label

# Dialogues for interactables in lab mini game 
label rat_in_cage_left:
    call hide_lab_screens 
    scene bg left cage zoom
    with dissolve 
    $ show_textbox = True
    $ mail_1_text_unlocked[3] = 1
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water and some obstacles for the animal to walk around"
    $ show_textbox = False
    $ rat_seen = True
    jump inside_lab

label left_pc_stats:
    call hide_lab_screens 
    scene bg left pc zoom
    with dissolve 
    $ show_textbox = True
    "You look at the pic and see suspicious stats. You see percentages, probabilities and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab

label left_wall_obj:
    call hide_lab_screens 
    scene bg left wall zoom
    with dissolve
    $ show_textbox = True
    "Searching on the left cupboard you find some chemicals and medical tools alongside what looks like a few of {color=[medievilColor]}Medievil{/color}s implants but way smaller."
    $ show_textbox = False
    $ left_wall_seen = True 
    jump inside_lab

label symbols_on_screen:
    call hide_lab_screens 
    scene bg monitor zoom
    with dissolve
    $ show_textbox = True
    "You see a screen with three symbols. A arrow pointing left another pointing right and a circle between them. They seem to be lighting up on random. When observing them a bit more you notice that only one of the is active at a time."
    $ show_textbox = False
    $ symbols_seen = True
    jump inside_lab

label rat_in_cage_right:
    call hide_lab_screens
    scene bg right cage zoom
    with dissolve
    $ show_textbox = True
    $ mail_1_text_unlocked[3] = 1
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water and some obstacles for the animal to walk around."
    $ show_textbox = False
    $ rat_seen = True
    jump inside_lab

label right_pc_stats:
    call hide_lab_screens 
    scene bg right pc zoom
    with dissolve
    $ show_textbox = True
    "You look at the pic and see suspicious stats. You see percentages, probabilities and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab

label empty_trash:
    call hide_lab_screens 
    scene bg trash zoom
    with dissolve
    $ show_textbox = True
    "You look in and realise the bin is empty."
    $ show_textbox = False
    $ trash_seen = True
    jump inside_lab 


label inside_lab_done:
    hide screen phone_icon 
    call hide_lab_screens 
    scene bg medievil lab
    with dissolve
    $ show_textbox = True
    show leonie neutral at left:
        yalign -1.0
        xalign -1.0
        linear 0.5 xalign 0.1
    show alex neutral at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve
    PC "I believe I got what this place is about."
    A "The symbols on the screen. Do they show the movement of the rat?"

    show leonie serious at right:
        yalign -3
        linear 0.4 yalign 0.4
    with dissolve
    L "It looks like it. But its a bit offset. Like the screen knows what the rat will do before it does it."

    PC "Why would {color=[medievilColor]}Medievil{/color} develop something like that?"

    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "From what i know that is nothing that they're advertising so it's probably not for the world to know."

    show leonie sad at left:
        yalign 0.4
    with dissolve
    L "That can't be good. Looks like Felix was onto something for real."

    PC "In any case I think we shouldn't stick around in here any longer than we need to. I dont think we will find more information for our phishing mail here."

    show alex serious2 at alex_right:
        xalign 0
        yalign 0.3
    with dissolve
    A "Agreed."
    hide screen phone_icon
    scene black
    with dissolve
    "As you leave the lab you make sure that everything is left like you found it when you entered. After that you head out the back entrance and venture on home."
    $ lab_seen = True
    with dissolve

    $ hide_map = False
    $ current_location = 0
    jump research

label phishing_mail_done:
    $ show_textbox = True
    hide screen phone_icon
    hide screen mail_screen
    $ gloss_phishing_seen = True
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 10 zoom 2
    show leonie thinking at left:
        yalign 0.4
    show alex smile at alex_right:
        xalign 2
    with dissolve
    play music main_music1 volume loudness fadeout 1.0

    A "Alright, looking good. Now we just need to hope Bob falls for the mail."
    scene black
    "The three of you return to your dorms and go to sleep."
    "As the next day arises you gather around your laptop to read the reply from Bob Anderson."

    scene bg new kitchen at truecenter:
        zoom 1.7
    show leonie happy at left:
        yalign 0.4
    show alex happy at alex_left:
        xalign 1
    with dissolve
    L "Yes. He fell right into our trap and believed every word we said."

    show alex smile at alex_right:
        xalign 2
    with dissolve
    A "Look, he even sent us the access codes to the back entrance of the facility. Just like we expected."
    
    show leonie thinking at left:
        yalign 0.4
    with dissolve
    L "Nice. Let's check out the building this evening and see what we're dealing with."

    show alex happy at alex_right
    with dissolve
    A "Felix, we're coming."
    $ experience += 20
    call gain_experience(20)

    jump level_3_start

label phishing_mail_retry:
    $ show_textbox = True
    hide screen phone_icon
    hide screen mail_screen
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2.0
    show leonie serious at left:
        xalign -1.0
        yalign 0.4
        linear 0.5 xalign 0.1
    show alex serious1 at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve
    play music main_music1 volume loudness fadeout 1.0

    A "I dont think this one will work, but let's see."

    show leonie sad at left:
        yalign 0.4
    with dissolve

    L "I have a bad feeling about this."

    scene black
    "Hoping for a response the three of you go to bed and wait for tomorrow."
    "The next day you all go to your dorms room and look through your Emails."

    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2
    show leonie serious at left:
        yalign 0.4
    show alex serious2 at alex_right:
        xalign -1
    with dissolve

    PC "Hmm. No response yet."

    show alex serious1 at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve

    A "Maybe he still hasn't read it."

    show leonie sad at left:
        yalign 0.4
    with dissolve

    L "I think he just ignored us. It's probably best if we try again."

    show alex serious2 at alex_right:
        xalign -1
        yalign 0.3
    with dissolve
    A "Make sure you write a believable mail. Remember: we are trying to impersonate Gill Cameron and need to get access to the facility Bob works at."

    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "Maybe you could also take a second look at the pictures we took from the dumpster diving. They may contain valuable information."

    $ show_textbox = False

    scene bg laptop full
    show screen phone_icon
    show screen mail_screen
    jump empty_label

label phishing_mail_fail:
    $ show_textbox = True
    hide screen phone_icon
    hide screen mail_screen
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2
    show leonie serious at left:
        yalign 0.4
    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    play music main_music1 volume loudness fadeout 1.0

    L "No, that doesn't seem right. We can hope for it but I doubt Bob Anderson will fall for this Mail."

    show alex serious2 at alex_right:
        xalign -1
        yalign 0.4
    with dissolve
    A "Let's still hope for the best."
    scene black
    "The three of you return to your dorms and go to sleep."
    "As the next day arises you gather around your laptop to read the reply from Bob Anderson."
    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 15 zoom 2
    show leonie serious at left:
        yalign -2
        linear 0.5 yalign 0.4
    show alex serious1 at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "Damn it, he replied that we should stop bothering him and that he would block us"

    show leonie sad at left:
        yalign 0.4
    with dissolve
    L "Hmm. That mail was doomed from the start"
    jump game_over

init python:
    """
    # Not needed currently
    label in_progress:
        scene black
        with dissolve
        $ show_textbox = False
        "{size=90}Work in progress{/size}\nThank you for playing."
        with dissolve
        pause 2.5
        return
    """


# Empty label creates an empty loop that is needed when the player is currently in an interactable screen
# Without this label, when a screen with interactables would open, it would open on top of the dialogue...
# ...which would cause the dialogue to advance in the background without notice when the player...
# ...interacts with the screen in the foreground. Therefore it is adviced (by us; unless someone finds...
# ...a better alternative) to enter this label (jump to it) when entering an interactable screen like...
# ...the laptop so that relevant dialogue dosn't advance in the background. Of course afterwards the...
# ...game has to jump out of the empty label from the interactable screen after it's done.
label empty_label:
    ""
    # $ renpy.notify("in empty label")
    jump empty_label