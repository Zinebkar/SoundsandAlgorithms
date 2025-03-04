# Mind Hackers: Whispers in the wires - Project 2024 SECont
# File for the story of level 0

default PN = "Max"
default gender = "neutral"
default heshe = "they"
default himher = "them"
default hishers = "their"


# Level related variables:
define follow = False
define check = False
define ignore = False



label level_0_start:
    play music suspense_music1 volume loudness
    show screen level_progress
    "[[Remember to save the game regularly; Ren'Py provides automatic saves in the tab 'A' in the saves]"
    "Buckle up for a journey where trust is a weapon, truth is a labyrinth, and the choices you make could unravel a conspiracy that reaches far beyond the walls of your imagination."

    # Read the player name
    $ PN = renpy.input("Enter your name.", "Max", length=15, exclude=" 0123456789+=,.?!<>@[]{}").strip() 
    
#    menu:
#        "Are you..."
#        "A Boy":
#            $ gender = "male"
#            $ heshe = "he"
#            $ himher = "him"
#            $ hishers = "his"
#        "A Girl":
#            $ gender = "female"
#            $ heshe = "she"
#            $ himher = "her"
#            $ hishers = "hers"
#        "Non-Binary":
#            $ gender = "neutral" 
    "Welcome [PN]. Let's get on with the story."



label dorm_1:
    play music funky_music1 volume loudness fadeout 1.0
    scene bg new kitchen at lv0zoom_in
    with dissolve

    "The late afternoon sun filters through the blinds, casting long shadows across a cluttered dorm room. Books, papers, and empty snack wrappers are scattered haphazardly across the floor, a testament to the chaotic energy of finals week."
    
    scene black_background
    show bedroom-1 at truecenter :
        zoom 1.6
        linear 50.0 zoom 1.8
    with dissolve
    "You sit hunched over your laptop, the glow of the screen illuminating the intricate tattoos on your left hand."
    scene black_background
    show bedroom cropped at room_zoom_inn
    show alex tired  at truecenter :
        zoom 1.5
        ypos 0.6
        linear 0.3 xpos 1200
    with dissolve

    PC "I can't focus. Complex systems theory is proving to be... well, complex."

    $ experience += 20  # Gain XP for checking the drive
    call gain_experience(20)
    scene black_background
    show room full of books at room_zoom_inn
    "Alex, sprawled across the floor amidst a sea of open books, lets out a dramatic sigh."


    scene bg new kitchen at lv0zoom_in
    show alex tired at truecenter :
        zoom 1.5
        ypos 0.6
    with dissolve

    A "Okay, I officially surrender to the forces of academia. My brain is officially mush."

    show alex laughing at truecenter :
        zoom 0.5
        ypos 0.45
    

    "You chuckle, a welcome distraction from your studies."

    PC "Don't worry, Alex. We're almost through this. Just a few more hours of this delightful torture."

    scene black_background
    show pizza at zoom_inn
    stop music fadeout 1.0
     
    
    "Alex groans dramatically, then reaches for a slice of pizza."
    show bedroom cropped at room_zoom_inn
    show alex laughing left lv0 at truecenter :
        zoom 1.5
        ypos 0.6
        linear 0.2 xpos 1000
    with dissolve 

    A "If caffeine and sugar were the keys to academic success, we'd all be Nobel laureates by now."
    

    

    image my_video = Movie(play="videos/keyboard.webm", size=(1080, 1980)) 
    image my_video2 = Movie(play="videos/thinking.webm", size=(1080, 1980))
    image my_video3 = Movie(play="videos/laughing.webm", size=(1080, 1980)) 

label video_with_scaled_size:
    scene black_background
    # Scene with a scaled video
    show my_video at truecenter
        
        

    play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/keyboard-typing.mp3" volume 0.5 
    
    with dissolve
    "A comfortable silence settles over the room, punctuated only by the rhythmic tapping of Leonie's keyboard from her beanbag chair in the corner."
    stop sound
   
    hide text with dissolve
    
    
    
    
    $ experience += 20
    call gain_experience(20)


    scene black_background
    show my_video2 at truecenter
    play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/answeranytext.mp3" volume 0.5 
    L "Hey, have either of you seen Felix today? He hasn't answered any of my texts."
    
    scene black_background
    show alex sitting at truecenter :
        zoom 1.27
        ypos 0.6
    "Alex sits up, a mischievous glint in his eyes."
    scene bedroom cropped at room_zoom_inn
    show alex laughing left lv0 at truecenter :
        zoom 1.5
        ypos 0.6
        linear 0.2 xpos 1000 
    
    
    

    A "Oh, you know Felix. He's probably off chasing UFOs or decoding secret messages in the cafeteria's meatloaf."

    show leonie laugh at truecenter :
        zoom 1.2
        ypos 0.65
        linear 0.1 xpos 200

    "You smile, but the worry doesn't quite fade. Felix, their conspiracy-obsessed friend, had been acting strangely lately. His usual playful banter had taken on a darker tone, his excitement about his internship at {color=[medievilColor]}Medievil{/color} replaced by a growing unease."

    show alex tired at truecenter :
        zoom 1.4
        ypos 0.7
        xpos 0.8

    show leonie laugh at truecenter :
        zoom 1
        ypos 0.7
        xpos 0.2

    A "Actually, now that you mention it... he seemed a little freaked out this morning. Almost like he was... scared."

    scene bedroom cropped at room_zoom_inn
    show leonie asking left at truecenter :
        zoom 1
        ypos 0.6 
        linear 0.2 xpos 1000
    L "Scared? Of what?"

   

    scene black_background
    show my_video3 at truecenter :
        zoom 0.9
        ypos 0.6
    play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/iknow.mp3" volume 0.5 
    A "I don't know. He was mumbling something about his internship at {color=[medievilColor]}Medievil{/color}, some experiment called \"NeuroMend\"... It was all very cryptic."

    hide alex
    hide leonie
    with dissolve

    stop music
    scene black_background 
    
    
    show door at shake_effect with dissolve :
        zoom 1.4
        ypos 0.0
        xpos 0.2
       
    "Suddenly, the dorm room door is thrown open, slamming against the wall with a resounding crash." 
    play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/open-door.mp3" volume 0.5
    
    show door at shake_effect with dissolve

    # Pause and shake the background mid-scene for added effect
    show bedroom-1 at truecenter :
        zoom 1.7
        
    with dissolve
    
    show felix worried at truecenter :
        ypos 0.7
        xpos 0.9
        linear 0.2 xpos 1600
    "Felix bursts into the room, his eyes wide with terror, his chest heaving as if he'd been running for miles. His usually meticulously styled hair was a tangled mess, and his clothes were rumpled and stained."
    
    
    hide felix worried
    show flex shouting at truecenter :
        ypos 0.9
        xpos 0.9 
    with dissolve

    "Felix gasps for air, his voice barely a whisper"

    F "{color=[medievilColor]}Medievil{/color}! They're not what they seem. This... this is everything. Trust no one."

    "With trembling hands, he thrusts a battered flash drive into your hand, then turns and flees, disappearing into the dimly lit hallway."

    hide flex shouting
    with dissolve

    

    play music mystery_music1 volume loudness 
    "The air crackles with tension, and a million thoughts race through your mind. What was that all about? Why is Felix so scared? What's on this flash drive? It feels heavy in your hand."

    show alex surprise at truecenter :
        zoom 1.3
        ypos 0.6
    
        linear 0.2 xpos 1800
    show leonie asking left at left:
        zoom 1
        xpos 0.2
        ypos 1.1
        linear 0.1 xpos 20
    with dissolve 



menu:
    "Try to go after him.":
        PC "We can't just let him run off like that. He's obviously terrified. Something's wrong."
        jump choice0_follow
    
    "Look what is on the drive he handed to you.":
        PC "He said this was important. Maybe it has answers. Leoni, can you take a look?"
        jump choice0_check

    "Try not to get involved.":
        PC "This looks like it could be dangerous. Maybe we should stay out of it."
        jump choice0_ignore

label choice0_ignore:

        scene bg new kitchen at truecenter:
            zoom 1.7
        with dissolve

        show alex tired at truecenter :
            zoom 1.2
            ypos 0.6
            xpos 0.9
        with dissolve

        A "Are you serious? [PN], Felix is our friend. We can't just abandon him!"

        show leonie asking left at truecenter :
            zoom 1
            ypos 0.6 
            linear 0.2 xpos 1000
        with dissolve

        L "Besides, curiosity is killing me. I want to know what's on that drive."

        "You're hesitatant, torn between caution and concern for your friend."

        show alex tired at truecenter :
            zoom 1.2
            ypos 0.6
            xpos 0.8
        with dissolve

        A "Exactly! And that's why we need to find out. Come on, [PN], let's go after him."

        show leonie asking left at truecenter :
            zoom 1
            ypos 0.6 
            linear 0.2 xpos 1000
        with dissolve
   
        L "I'll stay here and see if I can find anything on the drive. Maybe it'll give us some clues."

        "You hesitate, torn between caution and concern for your friend. But the weight of the unknown proves too heavy. You sink back onto your bed, a sense of unease settling in."

        show alex tired at truecenter :
            zoom 1.2
            ypos 0.6
            xpos 0.9 
        with dissolve

        A "Seriously? We're just going to let him disappear? What if he's in real trouble?"

        PC "I... I don't know what to do. I'm scared."

        "Leonie looks up from her laptop, her expression a mix of concern and determination."

        show leonie asking left at truecenter :
            zoom 1
            ypos 0.7
            linear 0.2 xpos 1000
        with dissolve

        L "I'm not finding anything on this drive yet. It's encrypted. But I'll keep trying. In the meantime, maybe we should just... wait and see?"

        hide alex

        hide leonie

        "Hours turn into days, and Felix remains missing. The unanswered questions gnaw at you, a constant reminder of your inaction. The flash drive remains a mystery, its secrets locked away."

        "Weeks later, a small article buried in a conspiracy theory tabloid catches your eyes. The headline reads: 'Shocking Discovery: Human DNA Found in Dog Food.'"

        "A chill runs down your spine. The article details a bizarre finding at a local pet food factory, a trace of human genetic material amidst the meat and grains. The source of the DNA remains unknown, the investigation ongoing."

        "You can't shake the feeling that this is somehow connected to Felix, to {color=[medievilColor]}Medievil{/color}, to the cryptic warning he delivered that fateful night. But without proof, it's just another unsolved mystery, a whisper in the wind."

        "The weight of regret settles heavily on your shoulders. The choice to ignore Felix's plea, to prioritize safety over friendship, has left a bitter taste in your mouth. The story ends not with a bang, but with a whimper, a silent echo of what could have been."

        jump game_over 
 
label choice0_check:
         
        scene bg new kitchen at lv0zoom_in
        
        show alex tired at truecenter :
            zoom 1.2
            ypos 0.6
            xpos 0.9
        with dissolve

        show leonie asking left at truecenter :
            zoom 1
            ypos 0.6
            linear 0.2 xpos 1000
        with dissolve
        
        "Leonie nods, taking the flash drive from you. She plugs it into her laptop and begins examining its contents."
        play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/keyboard-typing.mp3" volume 0.5 
        "Her fingers fly across the keyboard, a series of complex commands appearing on the screen."

        L "It's encrypted... heavily. This isn't something I can crack easily. We'll need more information, maybe something in Felix's room can help."

        PC "His room? You think he might have left something behind?"

        $ experience += 20  # Gain XP for checking the drive
        call gain_experience(20)
        jump level_1_start

label choice0_follow:
        scene black_background 
        show bg hallway at zoom_inn
        with dissolve

        "You rush out of the door, following the direction Felix took. Alex and Leonie exchange a worried glance before hurrying after you."

        "The hallway is dimly lit, the air heavy with the scent of stale pizza and disinfectant. Felix is nowhere to be seen. you quicken your pace, as your heart is pounding harder and harder."

        play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/felix_where_are_u.mp3" volume 0.5 
        PC "Felix! Where are you?"
       
        "Your voice echoes down the empty corridor, but there's no response. Your search every nook and cranny, every possible hiding spot, but Felix is gone."
        play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/Did you find him .mp3" volume 0.5 
        L "DID you find him"

        play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/losthim.mp3" volume 0.5 
        A "Damn it! We lost him."

        "Leonie picks up the flash drive Felix left behind, a sense of urgency washing over her."
        play sound "C:/games/renpy-8.3.3-sdk/Smoke and Algorithms/game/audio/sfx/sfx/findthedrive.mp3" volume 0.5 
        L "We have to figure out what's on this drive. Maybe it holds the answers to where Felix went and what he's so scared of."

        $ follow = False

        $ check = True

        jump choice0_check

return 