# Mind Hackers: Whispers in the wires - Project 2024 SECont
# File for the story of level 3

label level_3_start:
    # Level related variables:
    $ in_dorms = False
    define level_3_s = False
    $ level_3_s = True
    define fire_alarm = False
    define door_state = False
    define leonie_away = True
    define a = "t"
    define b = "f"
    define have_USB = True
    define security_aware = False
    define detected = False
    define cameras_off = True
    define visability_list = [False,False,False,False]
    define visability_list1 = [False,False,False,False]
    define visability_list2 = [False,False]
    define number_found = False
    define phone_seen = False
    define first_time_in = True

    # Matrices for handling logics of the security mini game
    define game_matrix= [
                        [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                        [0,["c",b,0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                        [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                        [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                        [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                        [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                        [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                        [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                        [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                        [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                        [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                        [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                        [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                        [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                        [0,[0,a,0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                        ]
    define orange_path = [[14,3,1],[13,3,1],[12,3,1],[11,3,2],[11,4,2],[11,5,1],[10,5,1],[9,5,2],[9,6,2],[9,7,2],[9,8,1],[8,8,1],[7,8,1],[6,8,4],[5,8,4],[5,7,4],[5,6,4],[5,5,3],[6,5,3],[-1,-1]]
    define green_path = [[14,5,1],[13,5,1],[12,5,1],[11,5,1],[10,5,1],[9,5,4],[9,4,4],[9,3,4],[9,2,1],[8,2,1],[7,2,4],[7,1,4],[7,0,4],[-1,-1]]
    define purple_path = [[7,0,2],[7,1,2],[7,2,1],[6,2,1],[5,2,2],[5,3,2],[5,4,2],[5,5,1],[4,5,1],[3,5,1],[2,5,2],[2,6,2],[2,7,2],[2,8,2],[-1,-1]]
    define blue_path = [[2,0,2],[2,1,2],[2,2,2],[2,3,2],[2,4,2],[2,5,3],[3,5,3],[4,5,3],[5,5,4],[5,4,4],[5,3,4],[5,2,3],[6,2,3],[7,2,4],[7,1,4],[7,0,4],[-1,-1]]
    define sec_path_1 = [[2,8,4],[2,7,4],[2,6,4],[2,5,4],[2,4,4],[2,3,4],[2,2,4],[2,1,4],[2,0,4],[2,0,2],[2,1,2],[2,2,2],[2,3,2],[2,4,2],[2,5,2],[2,6,2],[2,7,2],[2,8,2],[-1,-1]]
    define sec_path_2 = [[11,8,4],[11,7,4],[11,6,4],[11,5,4],[11,4,4],[11,3,4],[11,2,4],[11,1,4],[11,0,4],[11,0,2],[11,1,2],[11,2,2],[11,3,2],[11,4,2],[11,5,2],[11,6,2],[11,7,2],[11,8,2],[-1,-1]]
    define sec_path_3 = [[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[-1,-1]]
    define sec_path_4 = [[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[-1,-1]]
    define sec_index_1 = 11
    define sec_index_2 = 0
    define sec_index_3 = 0
    define sec_index_4 = 0
    define sec_list = [[sec_path_1,sec_index_1],[sec_path_2,sec_index_2],[sec_path_3,sec_index_3],[sec_path_4,sec_index_4]]
    define orange_index = 2
    define green_index = 5
    define purple_index = 10
    define blue_index = 8
    define tailgate_list = [[orange_path,orange_index],[green_path,green_index],[purple_path,purple_index],[blue_path,blue_index]]
    define valid_inputs = [1,1,0,0,0]
    define player_pos = [14,1]
    define door_timer = 0
    define door_timer1 = 0
    define door_state1 = False
    
    define optional_flag = True
    define bobs_flag = True
    define courtyard_flag = True
    define painting_seen = False
    define sofa_seen = False
    define computer_seen = False
    define books_seen = False
    define hospital_bed_seen = False
    define operation_table_seen = False 
    define skull_anatomy_seen = False


    scene bg back office far at zoom_in
    with dissolve

    play music mystery_music1 volume loudness
    $ hide_map = True

    "As the sun starts to set, your team arrives at the facility where {color=[medievilColor]}Medievil{/color} probably conducts tons of unethical experiments and also where Bob Anderson works."

    show leonie serious at left:
        xoffset -200
        yalign 0.4
        linear 1.0 xoffset 0
    with dissolve

    L "With the access code Bob unknowingly gave us, we should be able to enter via the back entrance."

    show alex serious1 at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve

    A "Although it's probably emptier than at day, there are still a few people going in and out of the building. We have to be careful."

    show bg back office far at shake_effect:
        zoom 1.4
        ypos 0.0
        xpos 0.0
    with dissolve

    "While staying at a safe distance from the facility, Leonie examines the building."

    show leonie sad at left:
        zoom 1.0
        yalign 0.4
        linear 2.0 zoom 1.2
    with dissolve

    L "It's no use. From here, I can't really make out their methods of security."

    "Somewhere in the facility, a door slams shut with a resounding crash, sending a faint tremor through the air."

    PC "Ok, let's go in then and take a closer look. That's what we have the codes for."


    scene bg back office at zoom_in
    with dissolve

    "As the sun starts to set, your team arrives at the facility..."

    # Leonie tippt den Code ein: Keypad-Beep-Sound
    show leonie thinking at left:
        yalign -1.0
        zoom 0.9
        linear 0.5 zoom 1.0
    with dissolve

    L "..."

    play sound "audio/sfx/keypad_beep.mp3" volume 0.7
    pause 0.3

    show leonie happy2 at truecenter :
        zoom 1.2
        ypos 0.8
    with dissolve

    L "Yes, the code worked."

    show alex happy at alex_right:
        xalign 2.0
        yalign 0.3
        linear 0.5 xalign 3.0
    with dissolve

    A "Nice. We do it well"

    scene bg hallway night 3 at zoom_in
    with dissolve

    "With the door open, you sneakily follow the hallways towards the office areas..."

    show leonie serious at left:
        yalign -1
        linear 0.5 yalign 0.4
    with dissolve

    "Leonie whispers:"
    L "Wait, here it says that Bob's office and all the other important spaces are all in this area."

    show alex happy at alex_right:
        yalign 0.3
        xalign 1.0
        linear 0.5 xalign 0.9
    with dissolve

    A "Sweet, let's go..."
    $ experience += 20
    call gain_experience(20)

    show leonie surprised at left:
        yalign 0.4
    with dissolve

    L "Wait!"

    "Leonie grabs Alex by his shirt and pulls him back behind the corner."
    show alex surprised at alex_right:
        xoffset 0.8
        yalign 0.4
        linear 0.2 xoffset 1.0
    with dissolve

    show leonie serious at left:
        yalign 0.4
    with dissolve
    L "The following area seems to be secured by cameras and guards..."

    show alex surprisedleft at alex_right:
        xalign 2.0
        yalign 0.4
        linear 0.5 xalign 1.0
    with dissolve
    A "Oh crap, thanks Leonie."

    show leonie neutral at truecenter :
        zoom 0.9
        ypos 0.7
        xalign -1.0
        linear 0.5 xalign 0.1
    with dissolve
    L "Additionally, it seems as if we can't really get any further anyway..."

    PC "I'm not sure how we are supposed to get our hands on one of these."

    show alex smile at alex_right:
        xalign 2.0
        yalign 0.0
        linear 0.5 xalign 1.0
        zoom 1.0
        linear 0.5 zoom 1.1
        linear 0.3 zoom 1.0
    with dissolve

    A "I don't think we have to."

    show leonie thinking at left:
        yalign 0.4
        xalign 1.0
        zoom 0.9
    with dissolve
    L "What do you mean?"

    show alex neutral at alex_right:
        xalign 1.0
        yalign 0.4
    with dissolve
    A "'Tailgating.' We follow one of the employees..."

    $ gloss_tailgating_seen = True
    $ phone_not_glossary = True

    show leonie serious at left:
        yalign 0.4
    with dissolve
    L "Great idea. So we have to come back during the day for this to work."

    PC "Yup, let's do this."


    scene black
    with dissolve

    play music main_music1 volume loudness

    pause 0.5

    "Your group returns the way you came in and goes home without any incidents."

    pause 0.5

    "The next day during breakfast, you talk about your approach."

    scene bg new kitchen at truecenter:
        zoom 1.7
        linear 10 zoom 2
    with dissolve

    show alex neutral at alex_right:
        alpha 0.0
        yalign 0.4
        linear 0.5 alpha 1.0
    with dissolve

    show leonie thinking at left:
        xalign -3.0
        alpha 0.0
        yalign 0.4
        linear 0.5 alpha 1.0
        linear 0.5 xalign 1.0
    with dissolve

    L "I think I'm going to stay here. There were cameras all over the office spaces and if I stay here, I could give you support from afar."

    show leonie serious at left:
        yoffset 0
        xalign 1.0
        yalign 0.4
        linear 0.2 yoffset -15
        linear 0.2 yoffset 0
    with dissolve

    L "Take this USB-Drive. If you manage to plug it into their security network, I get access to the cameras and can give you directions."

    PC "Hmm, this seems useful. Alright, everything set for today's infiltration?"

    show alex smile at alex_right:
        zoom 1.0
        linear 0.3 zoom 1.05
        linear 0.3 zoom 1.0
    with dissolve

    A "Yes."

    show leonie happy at truecenter :
        ypos 0.7
        xpos 0.8
        linear 0.2 xpos 1400
    with dissolve

    L "Yup."

    scene black
    with dissolve

    "With Leonie staying home, only Alex and you go towards the facility."

    play music mystery_music1 volume loudness

    scene bg front office 2 at zoom_in
    with dissolve

    "You find yourself at the spot you were yesterday."

    $ phone_open = False

    #hide alex with dissolve

define main_entrace_flag = False
define observe_entrance_flag = False
define infront_facility = False

label menu_outside:
    $ infront_facility = True
    scene bg front office 2 at zoom_in
    with dissolve
    
    hide alex

    if not phone_open:
        show screen phone_icon

    menu:
        "Take the main entrance." if main_entrace_flag == False:
            hide screen phone_icon
            pause 0.3
            "You and Alex decide to go through the main entrance."
            "Upon entering, you are greeted by ... no one. Every employee seems to be heavily invested in their work, and there is a lot of security roaming around."
            jump main_entrance
        
        "Observe the people entering the facility." if observe_entrance_flag == False:
            hide screen phone_icon
            scene bg front office 2 at zoom_in
            with dissolve
            "All the people you see look like they have business at this place. You can't spot anyone who looks like a visitor in your eyes."
            "Through the opening main entrance door, you can make out that there is heavy security guarding this place, but they don't seem to check the people entering."
            $ observe_entrance_flag = True
            jump menu_outside
        
        "Go through the back door with the pin you got from Bob.":
            hide screen phone_icon
            scene bg back office day at zoom_in
            with dissolve
            "The two of you sneakily enter the building with the same method from yesterday."
            jump back_entrance


define stairs_went = False
define receptionist_talked = False
define USB_placed_0 = False
define main_entrance_entered = False

label main_entrance:
    hide phone_icon
    scene bg front lobby at zoom_in
    with dissolve
    
    show alex serious2 at alex_right:
        alpha 0.0
        linear 0.5 alpha 1.0
    with dissolve
    
    if main_entrance_entered == False:
        A "(whispering){size=23}Is it just me, or are they not expecting visitors?{/size}"
        PC "(whispering){size=23}That's you, they are probably just really busy.{/size}"
        A "(whispering){size=23}Yeah sure. Anyway, what's the plan now.{/size}"
        $ main_entrance_entered = True
    
    jump main_entrance_menu

label main_entrance_menu:
    menu:
        "Go back outside":
            "Alex and you leave through the entrance you came in, attracting a few weird looks but nothing more."
            $ main_entrace_flag = True
            jump menu_outside
            $ experience += 20
            call gain_experience(20)

        "Talk to the receptionist" if receptionist_talked == False:
            scene bg receptionist at zoom_in
            with dissolve

            "Alex goes up to what looks like the guest reception. The lady at the desk doesn't notice you at first."

            show alex neutralleft at alex_left:
                alpha 0.0
                linear 0.5 alpha 1.0
            show receptionist neutral at receptionist_right:
                alpha 0.0
                linear 0.5 alpha 1.0
            with dissolve

            A "Excuse me!"

            show receptionist annoyed at receptionist_right:
                zoom 1.0
                linear 0.3 zoom 1.1
                linear 0.2 zoom 1.0
            with dissolve

            "He looks up slightly annoyed."
            R "Can I help you?"

            show alex smileleft at alex_left:
                yoffset 0
                linear 0.1 yoffset -10
                linear 0.1 yoffset 0
            with dissolve

            A "My name is Gill Cameron and I need to deliver some packages to Bob Anderson."

            show receptionist suspicious at receptionist_right
            with dissolve
            R "Let me see your ID, please."
            "Knowing that this will probably not work out, you signal Alex with a look that it's time to bail."

            show alex happyleft at alex_left:
                zoom 1.0
                linear 0.2 zoom 1.05
                linear 0.2 zoom 1.0
            with dissolve

            A "Yeah sure, it’s in my van outside. I'll be back in a minute."

            "Alex and you leave the building through the main entrance, not daring to go back this way."
            $ receptionist_talked = True
            $ main_entrace_flag = True
            jump menu_outside

        "Try to go into the restricted office area" if stairs_went == False:
            show bg front lobby at shake_effect
            with dissolve

            "As you approach the stairs to the office area, the security stops and questions you. By letting Alex talk, you get out rather easily, but the security now keeps an eye out for you."
            $ stairs_went = True
            $ security_aware = True
            jump main_entrance_menu

        "Place the USB-Drive with a deceiving note on a nearby desk" if USB_placed_0 == False:
            "You try to sneakily place Leonie's drive on the desk. As you leave, you notice a security guard inspecting your trap. Shortly after, he looks up with a determined, suspicious face."

            show alex serious1 at alex_right:
                yoffset 0
                linear 0.2 yoffset -15
                linear 0.2 yoffset 0
            with dissolve

            A "(Whispering) {size=23}I don't think he fell for it.{/size}"
            PC "(Whispering) {size=23}We should probably leave before he finds what he is looking for.{/size}"

            "With your ninja-like agility, you avoid the guard's gaze while leaving through the entrance."
            $ USB_placed_0 = True
            $ have_USB = False
            $ main_entrace_flag = True
            jump menu_outside


label back_entrance:
    scene bg secretary office at zoom_in
    with dissolve

    "As you try to go the same way as before, you get noticed by what looks like a secretary."

    # Sekretärin slidet ins Bild
    show secretary suspicious at center:
        alpha 0.0
        linear 0.5 alpha 1.0
    with dissolve

    S1 "Excuse me, who are you? I have not seen you here before."

    menu:
        "Tell her that you are the new interns of Bob Anderson, and you need to go to his office.":
            show secretary suspicious at secretary_right:
                xoffset 0
                linear 0.3 xoffset 0.02
            show alex smileleft at alex_left:
                yalign 0.1
                xalign 2.0
                alpha 0.0
                linear 0.3 alpha 1.0
            with dissolve

            A "We are Bob Anderson's new interns, and it's our first day..."

            S1 "Bob didn't mention any new interns."

            show alex neutralleft at alex_left:
                yalign 0.4
                xalign 2.0
            with dissolve
            A "How else would we have gotten access."

            show secretary thinking at secretary_right:
                zoom 1.0
                linear 0.3 zoom 1.05
                linear 0.2 zoom 1.0
            with dissolve

            S1 "Well that's a good point. Sorry for being so mistrustful..."

            show alex happyleft at alex_left:
                yalign 0.3
                xalign 2.0
                yoffset 0
                linear 0.2 yoffset -10
                linear 0.2 yoffset 0
            with dissolve

            A "Yeah, we know. Bob also said to us we shouldn't speak of what we do here..."

            show secretary neutral at secretary_right
            with dissolve
            S1 "Sounds like him. Anyway, his office is in the area with the others just down this corridor."

            show alex smileleft at alex_left:
                yalign 0.1
                xalign 2.0
                zoom 1.0
                linear 0.3 zoom 1.05
                linear 0.2 zoom 1.0
            with dissolve

            A "Okay, great. Thank you."

            show secretary friendly at secretary_right_smile:
                zoom 1.0
                linear 0.4 zoom 1.1
                linear 0.2 zoom 1.0
            with dissolve

            S1 "No problem."

        "Tell her you need to go to the bathroom and make a run for it":
            show secretary thinking at secretary_right:
                pause 0.3
            scene bg hallway 2 at zoom_inn
            with dissolve

            "After you tell her your reason, she looks like she wants to say something, but you just start running..."

            "The secretary will remember that."
            $ security_aware = True

        "Pretend to be technicians":
            show secretary suspicious at secretary_right
            show alex neutralleft at alex_left:
                yalign 0.4
                xalign 2.0
                alpha 0.0
                linear 0.5 alpha 1.0
            with dissolve

            A "We are technicians and here for problems with the internet connection..."

            show secretary thinking at secretary_right
            with dissolve
            S1 "Well, I don't know where he is, but just wait here a minute; I will call him right now."

            show alex happyleft at alex_left:
                yalign 1.0
            with dissolve
            A "That's not going to be necessary; we will just look for him ourselves, thank you."

            show secretary friendly at secretary_right_smile
            with dissolve
            S1 "No, no, it's nothing really. Just one second."

            show secretary neutral at secretary_right
            show alex serious2left at alex_left:
                yalign 1.0
            with dissolve

            "The secretary starts to type something on her phone and then proceeds to wait for a call."

            "You decide it's best if you bail out while she is distracted before your lie falls apart right in front of you."

            scene bg hallway 2 at zoom_in
            with dissolve

            "With that in mind, you make a run for the office area before she can stop you."

            scene bg hallway 1 at zoom_in
            show guard_angry at security:
                alpha 0.0
                linear 0.3 alpha 1.0
            with dissolve

            "After only a few minutes, you find security waiting for you around the corner."
            jump game_over

define USB_placed_office = False   # statt USB_placed_1 oder USB_placed_0
define before_office = False

##############################################################################
# Weg zum Büro (neues Label, an das wir nach 'back_entrance' anspringen)
##############################################################################

label way_to_the_office:
    scene bg hallway 1
    hide alex
    hide secretary
    with dissolve

    "Going further into the facility, you find the beginning of the office area you were looking for."

    show alex serious1 at right:
        zoom 0.9
        xalign 2.0
        linear 0.5 xalign 1.0
    with dissolve
    A "Well, what do we do now? We still don't have control of the cameras."

    # Optional: Kurze Überlegung/Spielerdialog
    PC "Leonie did say she'd try to hack in if we plug a USB drive in somewhere, right?"
    $ experience += 20
    call gain_experience(20)

    jump before_the_office


##############################################################################
# Vor dem Büro: Entscheidungen (USB platzieren, Bob's Office infiltrieren usw.)
##############################################################################

label before_the_office:
    scene bg hallway 1
    with dissolve

    # Du hattest in deinem Code:
    $ infront_facility = False
    $ current_location = "before_office"
    $ before_office = True

    # Falls du das Telefon-Icon nur zeigen willst, wenn es noch nicht offen ist:
    if not phone_open:
        show screen phone_icon

    menu:
        "Infiltrate Bob's office":
            $ current_location = -1
            hide screen phone_icon

            "You decide that now is the time to infiltrate Bob's office."
            play music security_music volume loudness

            # Hier dein eigenes Reset oder Cleanup, falls du z. B. Variablen zurücksetzen möchtest
            $ reset()

            # Wenn kein USB mehr im Besitz => Kameras scheinbar schon manipuliert/aus.
            if have_USB == False:
                $ cameras_off = True
            else:
                $ cameras_off = False  # Falls du willst, dass die Kameras standardmäßig an sind

            # Start deines Security-Minispiels
            show screen minigame_screen()
            hide screen minigame_screen

            jump security_minigame_start

        "Place the USB-Drive as a bait for employees" if (USB_placed_office == False and have_USB == True):
            hide screen phone_icon
            "You put the USB-Drive on a nearby desk with a note saying, \"Observation team, please have a look at this\"."

            "To avoid further confrontation, you hide in the bathroom until you get a call from Leonie telling you that she is now in control of the cameras."

            $ cameras_off = True     # Kameras werden von Leonie übernommen
            $ USB_placed_office = True
            $ have_USB = False       # USB-Stick ist nun nicht mehr im Besitz

            jump before_the_office

        "Activate the fire alarm":
            $ current_location = -1
            hide screen phone_icon

            "After activating the fire alarm, you heard sirens going off and speakers talking. While everyone is leaving the building, you hide in the bathroom and wait a bit."

            "With no one in the building, you can just stroll into the office of Bob Anderson."

            $ fire_alarm = True
            jump bobs_office


##############################################################################
# Innenhof (courtyard) - Mini-Abschnitt
##############################################################################

label courtyard:
    scene bg courtyard
    play music main_music1 volume loudness
    hide screen minigame_screen
    with dissolve

    $ show_textbox = True
    "You see beautiful flowers and a nice garden."
    "Upon staring at the delightful scenery, a group of butterflies comes across your sight."
    "You feel like you could maybe try to catch them."

    show screen butterfly_mini_game
    with dissolve

    # Danach geht es wahrscheinlich irgendwo weiter,
    # z. B. zurück zur letzten Station oder zu einem anderen Label.
    return


##############################################################################
# Optionaler Bereich: "secret lab"
##############################################################################

label optional:
    scene bg secret lab
    hide screen minigame_screen
    with dissolve

    $ show_textbox = True
    "You sneakily open the door, somewhat afraid an employee might be here, and walk in slowly."

    show alex serious2left at left
    with dissolve

    A "Since we are already in this weird room, we might as well take a look around."

    jump optional_clicking


label optional_clicking:
    if hospital_bed_seen and operation_table_seen and skull_anatomy_seen:
        jump optional_clicking_done

    $ show_textbox = False
    scene bg secret lab
    show screen optional_room
    with dissolve

    show screen phone_icon
    with moveinright
    jump empty_label


label hospital_bed:
    call hide_optional_room_screen
    scene bg secret lab beds
    with dissolve

    $ show_textbox = True
    "You see a blood-stained operational seat that gives you the creeps."

    A "Wow, this looks quite frightening. I wonder what they did here."

    $ show_textbox = False
    $ hospital_bed_seen = True

    show screen phone_icon
    jump optional_clicking


label operation_table:
    call hide_optional_room_screen
    scene bg secret lab equipment
    with dissolve

    $ show_textbox = True
    "You see messy operational equipment. Looks like they have been used lately."

    A "Ok, this is getting out of hand. They haven't used this on other people, have they?"

    $ show_textbox = False
    $ operation_table_seen = True

    show screen phone_icon
    jump optional_clicking


label skull_anatomy:
    call hide_optional_room_screen
    scene bg secret lab skull
    with dissolve

    $ show_textbox = True
    "You see an anatomy picture of a skull with marks on it."

    A "God, I hope Felix is alright."

    $ show_textbox = False
    $ skull_anatomy_seen = True

    show screen phone_icon
    jump optional_clicking


label optional_clicking_done:
    $ show_textbox = True
    hide screen phone_icon

    "Upon inspecting the room, you decide to go back into the hallway."
    jump security_minigame_start


##############################################################################
# Bobs Büro
##############################################################################

label bobs_office:
    scene bg bob office
    hide screen minigame_screen
    with dissolve

    $ show_textbox = True

    show alex serious2 at left:
        zoom 0.9
        xalign 0.9
        yalign 0.4
        linear 0.5 xalign 0.1
    with dissolve

    A "Now this is what we were talking about. We finally made it."

    PC "I can't believe this place has that many security guards and employees roaming around."

    show alex angryleft at left:
        yalign 0.3
    with dissolve

    A "You know there's probably a good reason why there are so many security guards here around the clock, right?"

    PC "Well, let's try to find clues about Felix now though."

    jump bob_clicking


##############################################################################
# Minigame: Bob's Office Interaktionen
##############################################################################

label bob_clicking:
    $ show_textbox = False

    scene bg bob office
    with dissolve

    show screen bob_laptop
    show screen bob_book_shelf
    show screen bob_sofa
    show screen bob_painting
    show screen bob_phone
    with dissolve

    show screen phone_icon
    with moveinleft

    # Leeres Label oder Wartepunkt, damit die Bildschirme interagieren können:
    jump empty_label


label laptop:
    call hide_bob_screens
    scene bg bob office computer
    with dissolve

    $ show_textbox = True
    "When observing the laptop, you see that the laptop is locked."

    $ show_textbox = False
    $ computer_seen = True

    show screen phone_icon
    jump bob_clicking


label book_shelf:
    call hide_bob_screens
    scene bg bob office books
    with dissolve

    $ show_textbox = True
    "You see interesting books and look for a secret doorway behind them, unsuccessfully."

    $ show_textbox = False
    $ books_seen = True

    show screen phone_icon
    jump bob_clicking


label phone:
    call hide_bob_screens
    scene bg bob office phone
    with dissolve

    $ show_textbox = True
    "This must be Bob's phone. It looks pretty fancy and expensive."

    $ show_textbox = False
    $ phone_seen = True

    show screen phone_icon
    jump bob_clicking


label phone_2:
    call hide_bob_screens
    scene bg bob office phone
    with dissolve

    $ show_textbox = True
    $ trust = 50   # Beispielhafte Variable für „Vertrauen“, wenn du sie brauchst
    "You call the number from the notes you found."

    $ show_textbox = False
    show screen phone_icon
    jump voice_phishing


label sofa:
    call hide_bob_screens
    scene bg bob office sofa
    with dissolve

    $ show_textbox = True
    "The sofa seems quite comfy; however, there's nothing of interest here."

    $ show_textbox = False
    $ sofa_seen = True

    show screen phone_icon
    jump bob_clicking


label painting:
    call hide_bob_screens
    scene bg bob office painting
    with dissolve

    $ gloss_voice_seen = True
    $ show_textbox = True

    "You look at the painting and wonder why it's placed so low and in the middle."
    "You realize that you can take off the painting, and there's a hidden little space with letters and a note with what seems to be a phone number."

    scene bg bob office
    "The letters are from someone called \"Joe Arnold\". They talk about how he was supposed to look after Felix because Bob Anderson found his latest behavior suspicious."
    "They even mention the day you last saw Felix and that the problem was taken care of."

    show alex neutralleft at left:
        yalign 0.4
    with dissolve

    A "Is this about Felix? What does 'taken care of' mean? Do you think he's ... dead?"

    PC "I don't know, but we shouldn't jump to conclusions. We need to find out if he's still alive."

    show alex serious1 at left:
        zoom 0.9
        yalign 0.4
        linear 0.5 yalign 1.0
    with dissolve

    A "The number from the notes! I think there's a good chance it belongs to this Joe Arnold. If we call him and pretend to be Bob Anderson, he might tell us what happened to Felix."

    $ show_textbox = False
    $ painting_seen = True
    $ number_found = True
    $ phone_seen = False
    $ phone_not_glossary = True

    show screen phone_icon
    jump bob_clicking


define trust_delta_2 = 25 
define called_from_smartphone = False
define joe_called = 0

##############################################################################
# Voice-Phishing-Minigame
##############################################################################

label voice_phishing:
    # Falls es Screens/Layer gibt, die hier geschlossen sein sollen, 
    # kannst du das hier beibehalten oder anpassen:
    call hide_bob_screens

    scene bg bob office
    hide screen phone_icon
    $ show_textbox = True

    # Markiere, dass wir jetzt mit Joe telefoniert haben:
    $ joe_called = 1

    # Zeige den Screen, der z.B. einen "Trust"-Balken anzeigt:
    show screen round_rect(trust)
    with dissolve

    "Biep ... Biep ...."
    if not called_from_smartphone:
        JA "Hey Bob, what is it? I'm kinda busy."
        menu:
            "Hi Joe. I'm not Mr. Anderson. Only his assistant, but I have a question from him.":
                jump voice_phishing_1

            "I'm Bob's assistant, and I have a question.":
                $ trust -= trust_delta_2
                jump voice_phishing_1

            "Hello, Mr. Arnold. I'm Mr. Anderson's assistant, and he wanted me to ask you something.":
                $ trust += trust_delta_2
                jump voice_phishing_1

    else:
        JA "Hello, who is there? I'm kinda busy."
        menu:
            "Hi Joe. I'm Mr. Anderson's assistant, and I have a question from him.":
                jump voice_phishing_1

            "I'm Bob's assistant, and I have a question":
                $ trust -= trust_delta_2
                jump voice_phishing_1

            "Hello, Mr. Arnold. I'm Mr. Anderson's assistant, and he wanted me to ask you something.":
                $ trust += trust_delta_2
                jump voice_phishing_1


label voice_phishing_1:
    show screen round_rect(trust)
    JA "Ok, just make it quick."

    menu:
        "Do you remember his former intern Felix, whom he needed help with? \
        The small and anxious one who looks kinda like Shaggy from Scooby Doo. \
        Where you told Mr. Anderson he was 'taken care of'.":
            $ trust -= trust_delta_2
            jump voice_phishing_2

        "Do you recall when Mr. Anderson asked you to have an eye on someone?":
            jump voice_phishing_2

        "It's about this intern Felix you took care of.":
            $ trust += trust_delta_2
            jump voice_phishing_2


label voice_phishing_2:
    show screen round_rect(trust)
    JA "Yeah, I can remember Felix. Now what about him."

    menu:
        "I need you to tell me where he is. I have a question for him.":
            $ trust -= trust_delta_2
            jump voice_phishing_3

        "Can you give me his location? Mr. Anderson has something to ask him.":
            $ trust += trust_delta_2
            jump voice_phishing_3

        "I need his whereabouts to ask him something.":
            jump voice_phishing_3


label voice_phishing_3:
    show screen round_rect(trust)
    JA "If you want an answer from him, why not let me ask the question."

    menu:
        "No need for you to get involved again. We will take over from here.":
            $ trust -= trust_delta_2
            jump voice_phishing_done

        "Mr. Anderson wants to handle this more privately.":
            jump voice_phishing_done

        "Well, Mr. Anderson trusted me with this task, and since you're busy, \
        I think it's best if I talk to him.":
            $ trust += trust_delta_2
            jump voice_phishing_done

label voice_phishing_done:
    show screen round_rect(trust)

    # Überprüfung, ob "trust" hoch genug ist:
    if trust < 75:
        JA "No way Bob sent you. Who are you really?"
        "You try to explain that you are actually Bob's assistant, but he doesn't fall for it and hangs up."
        "This was your best chance to find your friend, and you ruined it."
        jump game_over
    else:
        JA "Alright, we took him to the experimental department in the facility at Cityville Street 12345. We locked him in Laboratory 2 in the cellar."
        hide screen round_rect
        $ show_image_buttons = True

        PC "Ok, great, and how can I get in?"
        JA "Oh right, the pin to the door is 385529."
        PC "Perfect, thank you for your time."
        JA "Sure."
        $ experience += 20
        call gain_experience(20)

        show alex serious1 at left:
            zoom 0.7
            xalign 0.1
            linear 0.5 xalign 0.3
        with dissolve
        A "He is here in this facility. C'mon, we have to help him."

        menu:
            "Activate the fire alarm" if not fire_alarm:
                "After activating the fire alarm, you hear sirens going off and speakers talking. While everyone is leaving the building, you wait in Bob's office."
                "With no one in the building, you can just stroll out of the office area again."
                $ fire_alarm = True
                jump find_felix

            "Sneak out of the security area":
                if fire_alarm:
                    "You head out to find Felix, but by now the entire building is full of people again, and the doors you got past for free last time are now keycard locked again."
                else:
                    $ fire_alarm = True
                play music security_music volume loudness

                # Dein Reset-Befehl (falls du mit einer bestimmten Funktion Variablen zurücksetzt)
                $ reset()

                $ player_pos = [1,1]
                $ valid_inputs = [1,0,0,1,0]
                $ game_matrix= [
                    [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                    [0,["c","t",0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                    [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                    [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                    [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                    [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                    [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                    [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                    [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                    [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                    [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                    [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                    [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                    [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                    [0,[0,"f",0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                    ]
                show screen minigame_screen()
                hide screen minigame_screen
                jump security_minigame_start


##############################################################################
# (Optional) label leave_facility (falls wirklich unbenutzt -> kann weg)
##############################################################################

label leave_facility:
    $ show_textbox = True
    hide screen minigame_screen
    "You see grass for the first time."
    "You get scared and accidentally run into traffic and die."
    jump security_minigame_start


##############################################################################
# Spielende bei Verlust: game_lost (Security fängt dich)
##############################################################################

label game_lost:
    # scene bg game_over
    hide screen minigame_screen
    show screen minigame_screen()
    $ show_image_buttons = False

    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"

    $ show_image_buttons = True
    $ detected = False
    $ reset()

    hide screen minigame_screen
    show screen minigame_screen()
    hide screen minigame_screen
    jump security_minigame_start


##############################################################################
# label get_another_USB / install_malware (nur wenn du sie brauchst)
##############################################################################

label get_another_USB:
    scene black
    with dissolve
    $ have_USB = True
    $ phone_open = False
    "You return to Leonie, and she gives you another USB-drive after lecturing you to not lose it again."
    show screen phone_icon
    jump menu_outside

label install_malware:
    scene black
    with dissolve
    $ have_USB = True
    $ phone_open = False
    "After receiving a file from Leonie, you install the content on a spare drive you have in your pockets."
    show screen phone_icon
    jump before_the_office


##############################################################################
# label find_felix: Spieler findet Felix im Keller
##############################################################################

label find_felix:
    scene bg hallway 1 at zoom_inn
    $ renpy.hide_screen("minigame_screen")
    $ show_textbox = True
    with dissolve

    "As you are both stepping out of the office area, you both let out a sigh of relief."

    show alex serious1 at right:
        zoom 0.7
        xalign 2.0
        linear 0.5 xalign 0.9
    with dissolve
    A "Ok, now that we are finally away from this high security, we can start looking for Felix."

    PC "This Joe said they hold him captive in the basement, so let's just follow the staircase downwards."

    scene black
    with dissolve
    "You and Alex go after the signs indicating the way to the basements. Along the way, there are no people aside from you."

    "After reaching the bottom of the stairs, you follow the hallways."

    scene bg basement 2 at zoom_inn
    with dissolve
    "There are no windows down here, and the light emanating from the halogen lamps fills the hallways with a constant dazzling brightness. Combined with walls that smell like freshly poured concrete, it creates an unnerving ambience."

    "You hear two women from afar, their voices echoing in the barren hallways. They appear to be office workers, and you avoid them by staying out of sight until they've passed you."

    "Keeping communication to simple hand signs so as not to raise attention, the two of you push forward, passing a series of heavy metal doors labeled with cryptic numbers and letter combinations."

    "Finally, you find the door behind which Felix is supposedly kept."

    "The PIN Joe gave you works just fine, and Alex opens the door with a loud creak that reflects along the drawn-out hallways."

    scene bg felix cell at zoom_in
    with dissolve
    show felix neutral1 at right:
        zoom 0.6
        yalign 7.0
        linear 0.5 yalign 0.7
    with dissolve

    F "[PN]? Alex?"

    "Before you sits Felix on a simple metal chair. The room you enter seems to be a small file storage space with metal racks filled with file boxes. Felix seems exhausted, his hair still a tangled mess, and his clothes visibly unchanged in a while."

    scene bg basement 2 at zoom_inn
    show alex happy at left:
        xalign -1.0
        linear 0.5 xalign 0.1
    with dissolve

    A "Oh man, I was so worried about you."

    "The three of you share a big hug before Felix's energetic spirit comes back."

    # Textgeschwindigkeit manipulieren:
    $ temp_cps = preferences.text_cps
    $ preferences.text_cps = 60

    show felix thinking at right:
        zoom 0.6
    with dissolve
    F "I knew it. I fricking knew it. From the start, when I got the internship here, it was clear ... {nw}"

    show felix serious at right:
        zoom 0.6
    with dissolve
    F "... so I planned to get access to their system via infiltrating it with a USB drive ... {nw}"

    # Textgeschwindigkeit zurücksetzen:
    $ preferences.text_cps = temp_cps

    show alex surprised at left
    with dissolve
    A "Felix, wai—"

    # Nochmal Zeitlupe:
    $ temp_cps = preferences.text_cps
    $ preferences.text_cps = 60

    show felix thinking at right:
        zoom 0.6
    with dissolve
    F "... but of course they caught on to me. Just as I had feared, I contacted Bob Anderson, my supervisor, \
    to try to talk my way out of this situation ... {nw}"

    # Zurücksetzen
    $ preferences.text_cps = temp_cps

    PC "Felix, stop!"
    PC "The flash drive you gave us helped us get to you, but right now we have to get out of here first. Leonie helped too, but she stayed at home to give technical support."

    show alex serious1 at left
    with dissolve
    A "Right. They will probably notice your absence, so we should get away as fast as possible."

    show felix serious at right:
        zoom 0.6
    with dissolve
    F "Of course, of course. Wait a minute, I found something interesting in these documents."

    "Felix scoops up a pile of opened documents and loose paper lying next to a couple of opened file boxes and tries to fit most of it under his shirt and in his pockets."

    show felix neutral1 at right:
        zoom 0.6
    with dissolve
    F "Alright, I'm ready. Do you know how to get out of here?"

    show alex serious2 at left
    with dissolve
    A "Yes, follow us. We'll take the back entrance. There shouldn't really be anyone there."

    scene black
    with dissolve
    $ in_dorms = True
    "The three of you leave the facility without further occurrences and head home, where Leonie waits."

    play music main_music1 volume loudness

    scene bg new kitchen at zoom_inn
    show alex neutral at alex_mid:
        xalign 0.55 
        yalign 3.0
        linear 0.5 yalign 1.0
    show leonie happy at left:
        yalign -1.0
        xalign -1.0
        linear 0.5 xalign 0.1
    show felix smile at felix_right:
        yalign 1.0
        xalign 2.0
        linear 0.5 xalign 1.0
    with dissolve

    L "Felix! We were worried sick. You have to tell us what happened."

    show alex happy at alex_mid:
        xalign 0.55
        yalign 1.0
    with dissolve
    A "Not so fast. I believe Felix should get some rest first after what happened to him."

    show felix neutral2 at felix_right:
        yalign 1.0
    with dissolve
    "Alex pours Felix a glass of water and rummages through the fridge in an attempt to find something edible."

    play music end_music volume loudness

    scene bg kitchen party at zoom_in
    show felix smile at right:
        zoom 0.5
        xalign 2.0
        linear 0.5 xalign 0.9
    with dissolve

    F "Thank you guys for believing me. I knew I could put my trust in you."

    show alex smile at left:
        xalign 0.6
        yalign 2.0
        linear 0.5 yalign 1.1
    with dissolve
    A "Always, Felix."

    show leonie thinking at left:
        zoom 0.7
        xalign -1.0
        linear 0.5 xalign 0.1
    with dissolve
    L "Phew, this was quite the adventure. I can't believe {color=[medievilColor]}Medievil{/color} really held you captive."

    show alex happy at alex_mid:
        zoom 1
        yalign 1.0
        xalign 0.55
    with dissolve
    A "Yes, I'm glad we got you out of there. However, we can't let them continue. Felix is quite possibly still in great danger, and so might we be."

    PC "Correct. We shouldn't let our guard down now. We have to investigate further into this company and bring them down once and for all."

    F "Haha, it was their mistake locking me in that storage room. I may have found something that could be useful for us, but we have to investigate this further."

    A "So what is it? What did you find?"

    show leonie happy at left:
        zoom 1.1
        yalign -1.0
        xalign -1.0
        linear 0.5 xalign 0.1
    with dissolve
    L "I agree that Medievil deserves to be brought down, but why don't we enjoy at least this evening together without worrying about evil corporations hunting us?"

    show alex smile at alex_mid:
        zoom 1
        yalign 1.0
        xalign 0.55
    with dissolve
    A "Alright. Good idea."
    $ experience += 20
    call gain_experience(20)

    "You have reached the end of this game. Thank you for playing."

    $ show_textbox = False
    $ current_location = "end_game"

    show screen end_screen
    show screen phone_icon
    with dissolve

    jump empty_label


##############################################################################
# Screen für das Endbild
##############################################################################

screen end_screen:
    image "images/backgrounds/bg kitchen party.png"

    image "images/characters/player/male/pcm smile.png":
        zoom 1.6
        xpos 150
        ypos 200

    image "images/characters/felix/felix smile.png":
        zoom 0.8
        xpos 1150
        ypos -100

    image "images/characters/leonie/leonie happy.png":
        zoom 0.3
        xpos -100
        ypos 200
        xzoom -1

    imagebutton:
        idle "images/objects/main menu button idle.png"
        hover "images/objects/main menu button hover.png"
        focus_mask True
        action Jump("game_finished")


label game_finished:
    $ MainMenu()
    return