# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file contains all characters and their corresponding images as well as their custom transforms if needed

# ################################### Characters: #####################################
define narrator = Character(            what_italic=True, what_outlines=[(0, "#080808", 5, 5)])
define PC = Character("[PN]",           what_prefix='"', what_suffix='"', who_color="#ffffff", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define A = Character("Alex",            what_prefix='"', what_suffix='"', who_color="#27e700", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define F = Character("Felix",           what_prefix='"', what_suffix='"', who_color="#2469ff", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define L = Character("Leonie",          what_prefix='"', what_suffix='"', who_color="#FF7F50", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define J = Character("Janitor",         what_prefix='"', what_suffix='"', who_color="#AA4473", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define R = Character("Receptionist",    what_prefix='"', what_suffix='"', who_color="#44aa99", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define S1 = Character("Secretary",      what_prefix='"', what_suffix='"', who_color="#b60000", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define S2 = Character("Security",       what_prefix='"', what_suffix='"', who_color="#686868", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define JA = Character("Joe Arnold",     what_prefix='"', what_suffix='"', who_color="#dacb00", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])

# ################################# Leonie sprites: ###################################
image leonie neutral:
    "images/NewImages/Leonie/11.png"
    zoom 1
image leonie happy:
    "images/NewImages/Leonie/5.png" 
    zoom 1
image leonie happy2:
    "images/NewImages/Leonie/4.png" 
    zoom 1
image leonie smile:
    "images/NewImages/Leonie/3.png" 
    zoom 1
image leonie sidelooking:
    "images/NewImages/Leonie/9.png" 
    zoom 1
image leonie sidelooking2:
    "images/NewImages/Leonie/leo_hd.png" 
    zoom 1
image leonie standing:
    "images/NewImages/Leonie/12.png" 
    zoom 1
image leonie surprised:
    "images/NewImages/Leonie/8.png"
    zoom 1
image leonie sad:
    "images/NewImages/Leonie/7.png"
    zoom 1
image leonie serious:
    "images/NewImages/Leonie/1.png"
    zoom 1
image leonie thinking:
    "images/NewImages/Leonie/6.png"
    zoom 1
image leonie disgusted:
    "images/NewImages/Leonie/leo_disgusted.png"
    zoom 1
    
# ################################## Alex sprites: ####################################
image alex neutral:
    "images/NewImages/Alex/4.png"
    zoom 1.5
image alex disgusted:
    "images/NewImages/Alex/alex_disgusted.png"
    zoom 1
image alex happy:
    "images/NewImages/Alex/18.png"
    zoom 1.3
image alex surprised:
    "images/NewImages/Alex/7.png"
    zoom 0.1
image alex smile:
    "images/NewImages/Alex/20.png"
    zoom 1.5
image alex serious1:
    "images/NewImages/Alex/25.png"
    zoom 1.5
image alex serious2:
    "images/NewImages/Alex/26.png"
    zoom 1.5
image alex serious3:
    "images/NewImages/Alex/29.png"
    zoom 1.5
image alex serious2left:
    "images/NewImages/Alex/6.png"
    zoom 1.5
image alex angry:
    "images/NewImages/Alex/5.png"
    zoom 1.5
image alex angryleft:
    "images/NewImages/Alex/17.png"
    zoom 1.5
image alex neutralleft:
    "images/NewImages/Alex/8.png"
    zoom 1.5
image alex happyleft:
    "images/NewImages/Alex/17.png"
    zoom 1.5
image alex surprisedleft:
    "images/NewImages/Alex/alex_hd.png"
    zoom 1.5
image alex smileleft:
    "images/NewImages/Alex/20.png"
    zoom 1.5
transform alex_right:
    xalign 1.65
    yalign 0.1
transform alex_midleft:
    xalign  0.15
    yalign 0.1
transform alex_left:
    xalign -1
    yalign 0.1
transform alex_mid:
    xalign  0.35
    yalign -0.8

# ################################## Felix sprites: ###################################
image felix running:
    "images/characters/felix/felix running scared.png"
    zoom 0.8

image felix shouting:
    "images/characters/felix/felix shouting.png"
    zoom 0.8
transform felix_right:
    zoom 0.6
    xalign 0.9
    ypos 60

# ################################# Janitor sprites: ##################################
image janitor neutral1:
    "images/characters/janitor/janitor neutral1.png"
    zoom 0.85
image janitor neutral2:
    "images/characters/janitor/janitor neutral2.png"
    zoom 0.85
image janitor smile:
    "images/characters/janitor/janitor smile.png"
    zoom 0.85
image janitor thinking:
    "images/characters/janitor/janitor smile.png"
    zoom 0.85
image janitor angry:
    "images/characters/janitor/janitor angry.png"
    zoom 0.85
transform janitor_right:
    xalign 0.6
    yalign 0.5
transform janitor_middle:
    xalign 0.3
    yalign -0.1


# ############################## Receptionist sprites: ################################
image receptionist friendly:
    zoom 0.55
    "images/characters/Receptionist (Male)/friendly.png"
image receptionist neutral:
    zoom 0.55
    "images/characters/Receptionist (Male)/neutral.png"
image receptionist suspicious:
    "images/characters/Receptionist (Male)/suspicious.png"
    zoom 0.55
image receptionist annoyed:
    "images/characters/Receptionist (Male)/annoyed.png"
    zoom 0.55

transform receptionist_right:
    xalign 0.9
    yalign 1.0

# ################################ Secretary sprites: #################################
image secretary angry:
    "images/characters/Secretary (Female)/angry.png"
image secretary neutral:
    "images/characters/Secretary (Female)/neutral.png"
image secretary friendly:
    "images/characters/Secretary (Female)/friendly.png"
image secretary suspicious:
    "images/characters/Secretary (Female)/suspicious.png"
image secretary thinking:
    "images/characters/Secretary (Female)/thinking.png"

transform secretary_right:
    ypos 1300
    xalign 1.2
transform secretary_right_smile:
    ypos 1250
    xalign 1.2
    zoom 0.95
transform security:
    yalign 0.4
    xalign 0.5

# ########################### Janitor trust bar sprites: ##############################
label janitor_look(trust):
    if (trust > 75 ):
        show janitor thinking at janitor_right
        with dissolve
    elif (trust > 40):
        show janitor neutral1 at janitor_right
        with dissolve
    else:
        show janitor angry at janitor_right
        with dissolve
