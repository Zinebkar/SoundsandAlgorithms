# Smoke and Algorithms - Project 2024 SECont
# Main file; Organizing file for calling the starting level

# Initialize Variables
default notes = Notes([])
default show_textbox = True
default gallery = Pictures([])
define medievilColor = "#e46b6bff" # Text color used everytime "Medievil" is mentioned in dialogue
default current_location = 0 # -1 = Error, 0 = Dorms, 1 = University
default mouse_index = 0
default hide_map = False

# Define level and experience variables
default level = 0
default experience = 0
default experience_needed = 100  # XP needed to level up
label gain_experience(amount):
    $ experience += amount  # Add XP

    if experience >= experience_needed:
        $ experience -= experience_needed  # Carry over extra XP
        $ level += 1  # Level up!
        "You leveled up to Level [level]!"

    return


init python:
    offset = renpy.random.randint(0,10)

# Splashscreen thats been shown after opening the game before the main menu
label splashscreen:
    scene black
    with Pause(1)
    show text "Social Engineering Group presents"
    with dissolve
    with Pause(2)
    hide text
    with dissolve
    with Pause(1)
    return

# Label called when player tries to use map, but it's disabled
label map_disabled:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map
    with dissolve
    "You cannot leave right now!"
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    with dissolve
    if USB_placed_0 == True and before_office == False:
        jump menu_outside
    elif have_USB == False:
        jump before_the_office
    elif infront_facility == True:
        jump menu_outside
    elif current_location == "before_office":
        jump before_the_office
    return

# Label "start" is being called by renpy automatically after starting the game
label start:
    $ randomize_indices()
    
    $ gallery.add_data(["gallery_meme"], False)
    jump level_2_start

# Zoom-in effect for the background
# Zoom-in effect for the background
transform zoom_in :
    zoom 1.0
    linear 30.0 zoom 1.2  # Gradually zoom in over 2 seconds to 120% of original size

 
transform lv0zoom_in :
    
    zoom 2.0  # Start at normal scale
    
    linear 30.0 zoom 2.2  # Gradually zoom in over 2 seconds to 120% of original size   

transform zoom_inn :
    zoom 1.3 # Start at normal scale
    ypos 0.1
    linear 30.0 zoom 1.5


transform room_zoom_inn :
    zoom 2.5 # Start at normal scale
    
    linear 30.0 zoom 2.8

transform video_zoom_inn :
    zoom 0.8 # Start at normal scale
    ypos 0.1
    xpos 0.08


transform shake_effect:
    xpos 0.2
    ypos 0.0
    alpha 1.0
    linear 0.05 xpos 0.15 ypos 0.05  # Shake left-up
    linear 0.05 xpos 0.25 ypos -0.05 # Shake right-down
    linear 0.05 xpos 0.15 ypos -0.05 # Shake left-down
    linear 0.05 xpos 0.25 ypos 0.05  # Shake right-up
    linear 0.05 xpos 0.2 ypos 0.0    # Return to original position
    repeat 2                         # Repeat the shake twice


