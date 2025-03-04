# Mind Hackers: Whispers in the wires - Project 2024 SECont
# File contains dialogues for the contacts-screen on the phone

default hide_textbox = False
default show_image_buttons = True

# ###################################### Alex: ########################################
label call_alex:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    if current_location == "end_game":
        A "Hey, I'm still right here. Glad we got Felix out of there."
    else:
        A "Are you blind? I'm standing right next to you, Haha."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
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

# ####################################### Joe: ########################################
label call_joe_arnold:
    if joe_called == 0:
        $ show_image_buttons = False
        if show_textbox == False:
            $ show_textbox = True
            $ hide_textbox = True
        hide screen phone_hand_contact
        with dissolve
        $ trust = 25
        $ called_from_smartphone = True
        "You call the number from the notes."
        with dissolve
        #$ show_image_buttons = True
        if hide_textbox == True:
            $ show_textbox = False
            $ hide_textbox = False
        jump voice_phishing
        show screen phone_hand_contact
        with dissolve
    elif joe_called == 1:
        $ show_image_buttons = False
        if show_textbox == False:
            $ show_textbox = True
            $ hide_textbox = True
        hide screen phone_hand_contact
        with dissolve
        $ joe_called = 2
        JA "I can't talk right now."
        with dissolve
        $ show_image_buttons = True
        if hide_textbox == True:
            $ show_textbox = False
            $ hide_textbox = False
        show screen phone_hand_contact
        with dissolve
    else:
        $ show_image_buttons = False
        if show_textbox == False:
            $ show_textbox = True
            $ hide_textbox = True
        hide screen phone_hand_contact
        with dissolve
        $ trust == 25
        $ called_from_smartphone = True
        "Biep ... Biep ..."
        "No one answers."
        with dissolve
        $ show_image_buttons = True
        if hide_textbox == True:
            $ show_textbox = False
            $ hide_textbox = False
        show screen phone_hand_contact
        with dissolve
    return

# ##################################### Leonie: #######################################
label call_leonie:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    if have_USB == False and before_office == False:
        L "You lost the USB? Should have know you two would mess it up. Just come back and i'll give you another one."
    elif have_USB == False:
        L "You lost the USB? Should have know you two would mess it up. Wait a sec I'll send you a copy of the mallware to install on a spare USB."
    elif current_location == "end_game":
        L "Nice job, but why are you calling me?"
    elif leonie_away == True:
        L "Why are you calling for no reason?"
    else:    
        L "Hey, I'm right here [PN]."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
    
    if have_USB == False and before_office == False:
        hide screen phone_hand_contact
        jump get_another_USB
    elif have_USB == False:
        hide screen phone_hand_contact
        jump install_malware
    elif infront_facility == True:
        jump menu_outside
    elif current_location == "before_office":
        jump before_the_office
    show screen phone_hand_contact
    with dissolve
    return

# ##################################### Felix: ########################################
label call_felix:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve

    if current_location == "end_game":
        F "Thanks for getting me out of there"
    else:
        "Beep beep beep."
        "..."
        "It seems like noone answers the phone."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
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


screen call_screen:
    add Solid("#00000000")
    zorder 1
    modal False
