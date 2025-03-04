# Mind Hackers: Whispers in the wires - Project 2024 SECont
# File for the story of level 1

$ renpy.include("inventory.rpy")

# Level related variables:
define window_not_done = True
define lock_not_done = True
define book_seen = False
define poster_seen = False
define calendar_seen = False
define map_seen = False
define newspaper_seen = False
define password_icon = True
define trust = 40
define trust_delta = 20


label level_1_start:
    
    with dissolve
    A "We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."

    play music mystery_music1
menu:
    "Take the drive to the police.":
        PC "Yes, we should go to the police and hand them the drive, they will know what to do."
        jump choice_1_1_police
    
    "Take a look at his room to find more information.":
        PC "He must have left us some info on how to get access to this data. Let's take a look into his room."
        jump choice_1_1_room

label choice_1_1_police:
    scene bg police station
    with dissolve

    "The police take the flash drive as evidence and you don't ever hear anything about the case again."
    "...or of Felix."
    jump game_over

label choice_1_1_room:
    scene bg felix door at zoom_in
    with dissolve

    "You step outside the kitchen and head towards Felix's room but find out that it's locked."
    show leonie serious at left:
        xalign -0.5
        yalign 0.5
    
    L "As I expected, too bad he is too paranoid to let his door open like the rest of us."
    jump choice_1_1_done


label choice_1_1_done:
    scene black_background 
    show Alex hallway 

    A "So... Anyone's got a clue as to how we're going to get into his room."

image leonie_video = Movie(play="images/backgrounds/level1/leonie_door.webm") 
image leonie_video2 = Movie(play="images/backgrounds/level1/leonie_video2.webm")
image leonie_video3 = Movie(play="images/backgrounds/level1/felix_kidnapped.webm")
image leonie door = "images/backgrounds/level1/leo_door.png"
image leoalex  = "images/backgrounds/level1/leo_alex.png"
image closeupalex  = "images/backgrounds/level1/alex_scared.png"
image leonie_closeup = "images/backgrounds/level1/leonie_serious.png"
image closeupalex2  = "images/backgrounds/level1/closeup_alex4.png"
image closeupalex3  = "images/backgrounds/level1/closeup_alex3.png"
image leonie_closeup2 = "images/backgrounds/level1/closeup_leonie2.png"
image Alex hallway="images/backgrounds/level1/door_alex2.png"
image Alex hallway2="images/backgrounds/level1/door_alex.png"

label menu_1_2:
    scene black_background 
    show bg felix door
menu:
    "Take a look at his windows." if window_not_done:
        PC "His windows. If they're still open, Leonie can climb up there and open the door from inside."
    
        show leonie door at zoom_in
        with dissolve
        L "What..."
        with dissolve
        show Alex hallway2 at zoom_in
        A "Good idea, you're probably the smallest one of us so you're most likely to fit through."

        scene black_background
    # Scene with a scaled video
        show leonie_video 
        L "Well if you insist it's worth a try I guess."
        with dissolve

        jump choice_1_2_windows


    "Get help from the Janitor":
        PC "The janitor probably has a master key. Maybe we can ask him for help?"
        show leonie door at zoom_in
        L "If he opens up random rooms by request, he'd be a pretty poor janitor."
        with dissolve

        show door_alex 
        A "Right, but maybe we can trick or pay him."
        with dissolve

        
        L "Or steal his key."
        show leonie door at zoom_in
        with dissolve

        PC "Really???"
        with dissolve 
        show leonie_video2
        L "It's an emergency. And it's not like we're going to keep it."
        with dissolve 
        show leoalex
        jump choice_1_2_janitor

    "Pick the lock." if lock_not_done:
        
        show leoalex at zoom_in
        PC "Can one of you pick locks. Shouldn't be too hard right?"
        with dissolve
        L "I have a few paper clips in my room we could use, but no idea how to pick a lock with them."
        with dissolve

        A "Me neither, but we can look up a tutorial on the internet. Should be fine."
        PC "If Leonie has enough paper clips to spare"
        jump choice_1_2_lock_pick

label choice_1_2_windows:
    scene bg window view 
    with dissolve

    "Looks like luck is not on your side today. The window to his room is closed and there is no way to open it except brute force."
    "Since you neither want to break your friends window nor get in trouble with the janitor you decide to look for another way in."
    $ window_not_done = False
    jump menu_1_2

label choice_1_2_lock_pick:
    scene bg felix door at zoom_in
    "After dismantling 13 paper clips and watching the tutorial for the 6th time you decide that there may yet be a better way to get inside."
    $ lock_not_done = False
    jump menu_1_2

label choice_1_2_janitor:
    $ gloss_bribery_seen = True
    $ gloss_impersonation_seen = True
    $ phone_not_glossary = True
menu:
    "Try to impersonate as Felix." :
        scene leoalex at zoom_in 
        PC "Maybe one of us should try to pose as Felix to get him to open the door."
        jump help_from_janitor
    
    "Bribe the janitor.":
        scene bg felix door at zoom_in
        PC "Do you think he's bribable?"
        show alex surprisedleft at alex_left:
            xalign 1.0
            yalign 0.5
        show leonie sidelooking2 at alex_right:
            zoom 1
        with dissolve
        
        A "Sure. Everyone is vulnerable to money."
        with dissolve
        show closeupalex
        A "If I offer him a few bucks he surely won't say no to lending us his keys for a minute."
        PC "All right Alex, you have my trust."
        with dissolve 
        scene bg hallwaay at zoom_in
        with dissolve

        "All of you head into the hallway and Alex leaves behind the corner to find the janitor."
        show leonie thinking at left:
            xalign 0.5
            yalign 4
        with dissolve
        
        "You hear a loud exchange of words and soon after, Alex returns defeated."

        hide leonie thinking
        show alex disgusted at alex_right:
            xalign 1.5
            yalign 3.0
            linear 1.0 yalign 1.0

        A "He said wasn't taking any money from me."

        show leonie_video2
        with dissolve

        L "Damn, I suspect he won't fall for any of our tricks now."
        jump game_over

    "Steal the keys from the janitor.":
        PC "How about I go grab his keys."
        show alex serious at alex_right
        with dissolve

        A "I'm not so sure this is a good idea."
        PC "Leave it to me. I've seen it in plenty of movies."
        scene bg hallwaay at zoom_in
        with dissolve

        show janitor neutral1 at janitor_right

        "As you approach the janitor, you stumble in front of him on purpose, fall right into him and get a hold of his key chain."

        show janitor angry at janitor_right
        show bg hallwaay at zoom_in
        with vpunch

        "The victorious spirits start rushing to your brain, but as you pull on his keys they won't come loose."
        scene bg stars at zoom_in
        with vpunch

        "The janitor, visibly furious of what stunt you're trying to pull off here, grabs you by the shirt and shoves you against the wall."
        jump game_over_police


label help_from_janitor:
    PC "I think you have the best chances Alex."
    show closeupalex at zoom_in
    with dissolve

    A "Yeaaah... I'm not so sure about that."
    show leonie_closeup at zoom_in 
    
    L "Don't be so humble. You're the most charismatic out of us and your Felix impression is unmatched. Besides you look the most like him."
    with dissolve

    show door_alex at zoom_in 
    A "That's great and all but I think we're counting on him not knowing who Felix is, because otherwise we're screwed."
    with dissolve

    PC "Either way you're our best shot and we need to get into this room."
    
    show leonie_video2
    L "And since we are Felix's room mates we can back up your story."
    with dissolve 
    hide leonie_video2
    show closeupalex 
    with dissolve

    A "Alright, alright I'll do it but you better have my back."
    with dissolve
    show bg felix door 
    show leonie happy2 at left:
        yalign 0.3
        xalign 0.4
    with dissolve

    L "Sure thing Felix."
    
    show closeupalex at zoom_in
    with dissolve
    A "Ha Ha."
    scene bg hallwaay
       
    with dissolve

    "All three of you head out to find the janitor. Traversing the building you see him in a hallway heading your direction."
    PC "Showtime Alex."

    show leonie sidelooking2 at alex_right:
        zoom 1
  
    L "Pay attention to what he's saying and react accordingly."

    show alex surprisedleft at alex_left:
        xalign 1.0
        yalign 0.5
    with dissolve

    A "Pshhh I know."
    hide leonie
    hide alex
    with dissolve
    "Alex approaches the janitor trying to hide his true intentions."
    show janitor neutral2 at janitor_middle
        

    A "Excuse me, my name is Felix and I wanted to ask if you can open my room for me. It looks like I've lost my key."
    
    show janitor neutral1 at janitor_right
    with dissolve
    show screen round_rect(trust)
    with dissolve
    play music funky_music1 volume loudness fadeout 1.0

    $ experience += 20  # Gain XP for checking the drive
    call gain_experience(20)
    # Start of Janitor mini game
    play music mystery_music2
    menu:
        J "Is this urgent? I'm already on my way to help with the printers and I've got my hands full of work."
        "Understanding that his hands are full.":
        
            A "I'm sorry that your hands are full of work however, I really have to get into my room and I can't find my keys. Our assignment is due in an hour and we need a book in my room to complete it."
            $ trust += trust_delta
        
        "Should be easy.":
            
            A "Unfortunately I've somehow lost or misplaced my keys and I have to get in. Unlocking a door shouldn't take all too long."
            $ trust -= trust_delta

        "I need access now.":
          
            A "Please help us, this is very urgent. I've misplaced my key and there are things inside my room I really need NOW."
            $ trust -= trust_delta
 

    call janitor_look(trust) from _call_janitor_look
    show screen round_rect(trust)

    menu:
        J "Have you tried looking for your key? How about tracing back your last steps?"
        "No.":
            
            A "We havent had time for that, and really need to move on."
            $ trust -= trust_delta

        "Traced back every step.":
            
            A "The first thing we did was trace back every one of our steps."
            $ trust += trust_delta

        "Isn't this your job to help.":
            
            A "Isn't this your job, now go and help us."
            $ trust -= trust_delta

    call janitor_look(trust) from _call_janitor_look_1
    show screen round_rect(trust)

    menu:
        J "Let me see your ID. I can't just give out access without verifying this kinda stuff."
        "That's personal information.":
      
            A "No, you have no right to see personal information like that."
            $ trust -= trust_delta
        
        "Left the ID at my parents place.":
            
            A "I'm soo sorry, I left my ID at my parent's over the weekend. Maybe you could make an exception."
            $ trust += trust_delta

        "It got stolen or i lost it, not sure":
        
            A "Its been gone for a couple of im sorry."
            $ trust -= trust_delta

    call janitor_look(trust) from _call_janitor_look_2
    show screen round_rect(trust)

    menu:
        J "Well, I'm not so sure if I'll be able to let you in, then. I don't want to get in trouble with Mrs Mill again."
        "I won't tell anyone.":
         
            A "I won't rat you out. Come on just help me this one time."
            $ trust -= trust_delta

        "I'll explain to Mrs Mill.":
        
            A "That won't be a problem, I'll call Mrs Mill first thing tomorrow to explain the situation."
            $ trust += trust_delta

        "The office would understand.":
           
            A "I'm sure the office will understand, you are helping out a student in need."
            $ trust -= trust_delta

    call janitor_look(trust) from _call_janitor_look_3
    show screen round_rect(trust)
    
    if trust > 75:
        J "Well, you seem to be honest."
        J "Let's go to your room then, shall we."
        hide screen round_rect
        jump janitor_trust
        $ experience += 20  # Gain XP for checking the drive
        call gain_experience(20)
    else:
        hide screen round_rect
        J "You're not going to fool me. Who are you really?"
        scene bg hallwaay
        "After being pressured by the janitor, Alex admits, he is not Felix and gets kicked out of the building and his rental contract."
        jump game_over

label janitor_trust:
    show bg felix door at zoom_in
   

    "The four of you go to Felix's room where the janitor opens the door for you."
    show janitor neutral1 at janitor_right
    with dissolve

    J "So about a replacement key..."
    
    with dissolve

    A "That won't be necessary. I've just got a message from a friend who found my key. Seems like I forgot them at his place."
    show janitor angry #at janitor_angry_right
    with dissolve
    J "And you didn't think of that before?"
   

    A "Well... "

    A "Apparently not."

    "The janitor looks at Alex with disapproval."
  

    A "Still. Thanks a lot for helping me out."
    show janitor thinking at janitor_right
    with dissolve

    J "Just don't lose them again you hear me."
    

    A "I promise."
    show janitor neutral2 at janitor_right
    with dissolve

    "He takes his leave and you gained access to Felix's room."
    hide janitor
    with dissolve


play music suspense_music1 volume loudness fadeout 1.0
label felix_room:
    scene bg felix room at zoom_in
    with dissolve

    "As you go through the door a gust of bad air comes your way."
    show leonie disgusted at left:
        xalign -3
        yalign 1.0
        linear 1.0 xalign 0.1
    with dissolve


    L "Wow, this room is quite messy. And it smells like something died in here."

    show alex disgusted at alex_right:
        xalign 0.9
        yalign 3.0
        linear 1.0 yalign 1.0

    A "Well, we know Felix and he did leave in quite a rush."
    PC "Let's focus on why we're here. We don't have time to waste. Who knows if and when the janitor will return to lock the door."
    
    show closeupalex3 at zoom_in

    A "What exactly are we looking for, anyway?"

    show leonie_closeup2 at zoom_in

    L "Typically, people choose passwords they can easily remember. Given Felix's conspiratorial nature, I doubt he has something simple like \"qwerty\" , \"123456\" or \"password.\" Let's look around for any hints."

    scene bg felix room at zoom_in
    with dissolve
    "Investigate the room with your mouse."
    show screen phone_icon
    with dissolve

# Start of interactable mini game in Felix's room
label felix_room_menu:
    scene bg felix room
    call show_felix_room_interactables from _call_show_felix_room_interactables
    with dissolve
    play sound not2
    "Explore the room or use your phone to crack the password."
    jump felix_room_menu

label notebooks:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables
    hide screen phone_icon

    scene bg f notebooks zoom
    with dissolve

    "Looking through his books, you find a few books about cyber security, one book about the fall of the roman empire and a few books about conspiracy theories."
    "One worn down book especially catches your sight. It's about the [[9/11] attacks and seems to have quite a few sticky notes and annotations in it."
    $ book_seen = True
    $ notes.add_data(NoteData("info: 9/11"))
    show screen phone_icon
    jump felix_room_menu

label bin:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_1
    hide screen phone_icon

    scene bg f bin zoom
    with dissolve

    "You close your nose with your fingers as you lean down upon the trash bin. This is not the day to be petty. You force yourself to take aside some old pizza crusts and used tissues."
    "After the bin is empty you accept that you'll probably only find trash and put the garbage back into the bin."
    show screen phone_icon
    jump felix_room_menu
    $ experience += 20  # Gain XP for checking the drive
    call gain_experience(20)
label bed:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_2
    hide screen phone_icon

    scene bg f bed zoom
    with dissolve
    
    "Under Felix's bed located, are some dirty clothes, empty bottles, and spider webs."
    
    show screen phone_icon
    jump felix_room_menu

label wall2:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_3
    hide screen phone_icon

    scene bg f wall2 zoom
    with dissolve

    "You catch sight of a \"portal\" poster. The following quote sticks out: \"the cake is a lie\"."
    show closeup_leonie2
    with dissolve
    L "Try around with some combinations."
    $ poster_seen = True
    $ notes.add_data(NoteData("info: \"the cake is a lie\""))
    show screen phone_icon
    jump felix_room_menu

label wall3:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_4
    hide screen phone_icon

    scene bg f wall3 zoom
    with dissolve

    "Your eyes meet a Calendar with marked dates. A red circled date [[04/17] labeled with \"Half Life 3\" stands out."
    $ calendar_seen = True
    $ notes.add_data(NoteData("info: 04/17 (Half Life 3 release)"))
    show closeup_leonie2
    with dissolve
    L "The password might be a combination of these informations. Try around with some combinations."
    with dissolve
    show closeupalex3
    with dissolve
    A "First we have to make sure we found all the relevant information in the room."
    with dissolve
    show screen phone_icon
    jump felix_room_menu

label map:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_5
    hide screen phone_icon

    scene bg f map zoom
    with dissolve

    "You catch sight of a Nevada map, with multiple pins on a specific Area. Written beneath it reads [[Area51]."
    show closeup_leonie2
    with dissolve
    L "You can keep track of the information pieces in your notes on your phone."
    with dissolve
    $ map_seen = True
    $ notes.add_data(NoteData("info: Area 51"))
    show screen phone_icon
    jump felix_room_menu

label wall1:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_6
    hide screen phone_icon

    scene bg f wall1 zoom
    with dissolve

    "You see some hung up newspaper articles about some apparent proof that the earth is actually flat."
    $ newspaper_seen = True
    show screen phone_icon
    jump felix_room_menu

label pc:
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_7
    hide screen phone_icon

    scene bg f pc zoom
    with dissolve

    "You try to get access to his PC but it's password protected."
    show closeup_leonie2
    with dissolve
    L "Who would have thought."
    show screen phone_icon
    jump felix_room_menu


label password_help:
    hide screen reset_password_text_timer
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_password
    with dissolve

    show closeup_leonie2
    with dissolve
    L "Hmm, this password is not as simple as we might have thought."
    with dissolve

    show closeupalex3
    with dissolve
    A "First we have to make sure we found all the relevant information in the room."
    with dissolve

    show closeup_leonie2
    with dissolve
    L "You can keep track of the information pieces in your notes on your phone."
    with dissolve

    show closeup_leonie2
    with dissolve
    L "The password might be a combination of these informations. Try around with some combinations."
    with dissolve
    
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_password
    with dissolve
    jump felix_room_menu


label password_cracked:
    hide screen reset_password_text_timer
    $ password_icon = False
    call hide_felix_room_interactables from _call_hide_felix_room_interactables_8
    hide screen phone_hand_password
    hide screen phone_hand
    hide screen phone_icon
    $ show_image_buttons = True
    $ experience += 20
    call gain_experience(20)


    play music kid volume loudness fadeout 1.0
    

    show leonie happy2 at left:
        zoom 2
        xalign 0.5
        yalign 0.2
    with dissolve

    L "Nice that did it. Time to see why he was so stressed out."
    hide leonie happy2
    
    "You see Felix's notes about his work at {color=[medievilColor]}Medievil{/color}. At first there is nothing unusual, but the deeper you go, the more distressed the writing becomes."
    "He seems to have discovered some kind of conspiracy about the implants from {color=[medievilColor]}Medievil{/color}. One name pops up several times throughout the files. \"Bob Anderson\"."
    PC "Is he talking about the implants from {color=[medievilColor]}Medievil{/color}? I thought they're used to treat diseases."

    show closeupalex2 at zoom_in
    with dissolve

    A "Neurological disorders, yes."

    show leonie_closeup2 at zoom_in
    with dissolve

    L "Well, according to him {color=[medievilColor]}Medievil{/color} is looking to use them for something else, but he doesn't specify what. Only that it's about profit and he thinks it's dangerous."

    show closeupalex3
    with dissolve

    A "And what's up with Bob Anderson. Any clue who that guy is."
    with dissolve
    hide closeupalex3
    show leonie_closeup2
    with dissolve

    L "Looks like he's Felix's supervisor or something."

    PC "Is this shit real or is Felix just getting too far into his conspiracy obsession."

    show closeupalex3 at zoom_in
    with dissolve

    A "I don't know, but he seemed really scared today. Maybe there is really more to it."

    show leonie_video3 at zoom_in
    with dissolve

    L "Yeah. I've never seen him like that before. Do you think they were onto him. I mean why would he give us the flash drive in such a hurry. Maybe he's been kidnapped."
    hide leonie_video3

    show closeupalex3
    with dissolve

    A "That's a pretty big jump you're taking don't you think. From what we know there is no hard evidence against {color=[medievilColor]}Medievil{/color} and Felix is not known to be the most rational person."
    hide closeupalex3
    show leonie_closeup2
    with dissolve

    L "Yes yes but he's not here and he hasn't answered any of our calls. Do you not think that's odd even for him."

    PC "Maybe he wants us to investigate {color=[medievilColor]}Medievil{/color}. I mean what else is the drive good for, other than raising our suspicion."
    hide leonie_closeup2
    show closeupalex2 at zoom_in
    with dissolve

    A "If you think there is actually something messed up going on, then maybe going to the police should be our next move."
menu:
    "Go to the police with the information you got.":
        scene bg police station at zoom_in
        "You go to the police and show them the information you got from the drive. They ask you questions about Felix and the answers make it sound like Felix is making this whole story up."
        "The fact that you have no hard evidence to show also doesn't help. In the end the police claims the drive as property of {color=[medievilColor]}Medievil{/color} and puts out a missing person report."
        show leonie serious at left:
            xalign -0.5
            yalign 0.5
        with dissolve
        L "Good thing I made a copy of everything so we didn't lose anything."

        show alex disgusted at alex_right:
            xalign 0.9
            yalign 3.0
            linear 1.0 yalign 1.0

        A "At least now we know that the police won't be much help against {color=[medievilColor]}Medievil{/color}. Looks like we're on our own."
        show leonie disgusted at left:
            xalign -3
            yalign 1.0
            linear 1.0 xalign 0.1
        with dissolve
        L "Let's get back to our dorm and take matters in our own hands."
        PC "I left my laptop in the kitchen, so let's just get going there."

        jump level_2_start

    "Investigate on your own what is happening at {color=[medievilColor]}Medievil{/color}.":
        scene bg felix room
        show leonie serious at left:
            xalign -0.5
            yalign 0.5
        with dissolve
        show alex disgusted at alex_right:
            xalign 0.9
            yalign 3.0
            linear 1.0 yalign 1.0
       
        PC "Well then, I think it's best if we do our research on {color=[medievilColor]}Medievil{/color}. There should be more room in the kitchen for all of us."
        
        show closeupalex2
        A "Mhm. We need to act fast. Who knows what actually happened to Felix…"
        show leonie_closeup2 
        with dissolve 
        L "From what I know, {color=[medievilColor]}Medievil{/color} is quite a large company. We should be able to find out a lot online."
        PC "I left my laptop there anyway, so I guess I'll take over the research."
        PC "From there, I guess we can fulfill Felix's wish and investigate properly."
        with dissolve
        $ experience += 20
        call gain_experience(20)

        jump level_2_start
    

# Game over screens

label game_over:
    scene bg game over 1
    with dissolve
    pause 1.5
return

define red_game_over_color = "#d40e0eff"
label game_over_police:
    scene bg jail
    with dissolve
    $ show_textbox = False
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}"
    scene bg game over 1
    with dissolve
    pause 1.5
return