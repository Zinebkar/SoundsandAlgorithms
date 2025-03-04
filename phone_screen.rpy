# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file contains the phone interactable that can be accessed during most of the game

$ renpy.include("screens.rpy")

# #################################### Variables: #####################################
default current_index = 0
image phone_icon_hover :
    "images/objects/phone/phone hover.png"
    zoom 0.15

image phone_icon_idle :
    "images/objects/phone/phone idle.png"
    zoom 0.15

image circ_anim = Movie(play="videos/circ_anim.webm", loop=True, mask="videos/circ_anim_mask.webm", framedrop=False)

transform icon_pos:
    zoom 1.3
    xalign 0.7

transform phone_pos:
    xalign 0
    yalign 1.28

transform arrow_pos:
    zoom 0.7
    xalign 0.07
    yalign 0.1

transform change_arrow:
    zoom 0.35

define phone_usable_area = (675, 140, 470, 720)
define phone_usable_area_quer = (150, 100, 1200, 720)
define phone_normal_text_color = "#000000"
define gil_social_media_seen = False

# Notification variables:
default phone_not_glossary = False
default phone_not_gallery = False
default phone_not_notes = False
default phone_not_map = False

# ############################## Notification function: ###############################
init python:
    def reset_notification(id):
        global phone_not_glossary
        global phone_not_gallery
        global phone_not_notes
        global phone_not_map
        
        if id == 0:
            phone_not_glossary = False
        elif id == 1:
            phone_not_gallery = False
        elif id == 2:
            phone_not_notes = False
        elif id == 3:
            phone_not_map = False

# ################################ Phone home screen: #################################
screen phone_hand():
    zorder 2
    modal True
    add Solid("#000c")
    if password_icon == True:
        image "images/objects/phone/phone hand empty.png":
            zoom 1.3
            xalign 0.7
    else:
        image "images/objects/phone/phone hand empty.png":
            zoom 1.3
            xalign 0.7
    
    # Return arrow (closes phone)
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow_pos
        xpos 200
        ypos 0
        xsize 500
        ysize 300
        action Hide("phone_hand"), Show("phone_icon"), Function(set_phone_open, False)
    
    # Phone icons
    imagebutton:
        hover "camera hover" at icon_pos
        idle "camera idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_camera")
    if phone_not_gallery:
        add "circ_anim":
                zoom 0.25
                xpos 1080
                ypos 845
    
    imagebutton:
        hover "contacts hover" at icon_pos
        idle "contacts idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_contact")
    
    imagebutton:
        hover "map hover" at icon_pos
        idle "map idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_map")
    if phone_not_map:
        add "circ_anim":
            zoom 0.25
            xpos 835
            ypos 375

    imagebutton:
        hover "notes hover" at icon_pos
        idle "notes idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_notes")
    if phone_not_notes:
        add "circ_anim":
                zoom 0.25
                xpos 1055
                ypos 155

    imagebutton:
        hover "glossary hover" at icon_pos
        idle "glossary idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_glossary")
    if phone_not_glossary:
        add "circ_anim":
                zoom 0.25
                xpos 1055
                ypos 375

    if password_icon == True:
        imagebutton:
            hover "password hover" at icon_pos
            idle "password idle"
            focus_mask True
            action Hide("phone_hand"), Show("phone_hand_password"),
    
    imagebutton:
        idle "pong idle" at icon_pos
        hover "pong hover"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_mini_game") # Call("play_pong") 

# ################################# Password screen: ##################################
default password =""
default password_check_text = ""
default first_guess = ""
default password_check_color = "00000000"
default password_guessed = False
default password_guessed_correct = False
default password_fail_counter = 0

screen phone_hand_password():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    image "images/objects/phone/phone hand password box.png":
        zoom 1.3
        xalign 0.7

    # Return arrow
    if show_image_buttons:
        imagebutton:
            hover "return hover" at icon_pos
            idle "return idle" 
            focus_mask True
            action Hide("phone_hand_password"), Show("phone_hand")
    else:
        image "return idle" at icon_pos
    frame:
        background "#00000000"
        area(675, 150, 460, 50)
        text "{color=[search_result]}{size=50}{b}Access USB{/b}{/size}{/color}" at center
    
    frame:
        background "#00000000"
        area(675, 200, 460, 50)
        text "{color=[search_result]}{size=50}{b}Drive{/b}{/size}{/color}" at center
    frame:
        background "#00000000"
        area(675, 300, 460, 50)
        text "{color=[search_result]}Enter password:{/color}" at center
    frame:
        area (675, 360, 460, 100)
        background "#00000000"
        input:
            copypaste True
            default""
            size 30
            pixel_width(440)
            color "#000000"
            value VariableInputValue('password')
    imagebutton:
        hover "phone hand password confirm hover" at icon_pos
        idle "phone hand password confirm idle"
        focus_mask True
        action Function(password_input,password), Show("reset_password_text_timer")
    frame:
        background "#58585800"
        area(675, 700, 460, 50)
        text "{size=30}{color=[password_check_color]}{b}[password_check_text]{/b}{/color}{/size}" at center:
            outlines [(3, "#000000ff", 0, 0)]


screen reset_password_text_timer():
    #image "images/characters/alex/alex laughing.png"
    timer 1.7 action Function(reset_password_text), Function(after_password_action), Hide("reset_password_text_timer")


define correct_password =[ 
                        ["9/11", "911", "9.11", "9-11"],
                        ["cake"],
                        ["lie"],
                        ["4/17", "417", "4.17", "4-17"],
                        ]

init python:
    def password_input(password_guess):
        global password_check_color
        global password_guessed
        global password_check_text
        global first_guess
        global password_guessed_correct
        global show_image_buttons
        global password_fail_counter

        if password_guessed == False or first_guess == password_guess:
            renpy.sound.play("audio/sfx/pin_pad_false.wav")
            first_guess = password_guess
            password_guessed = True
            password_check_color = "#970000ff"
            password_check_text = "Incorrect password"
            return

        for i in range(0,len(correct_password)):
            part_found = False
            for j in range(0,len(correct_password[i])):
                if correct_password[i][j] in password_guess.lower():
                    part_found = True
            if part_found == False:
                password_check_color = "#970000ff"
                password_check_text = "Incorrect password"
                password_fail_counter += 1
                return
        password_check_color = "#288f00ff"
        renpy.sound.play("audio/sfx/pin_pad_correct.wav")
        password_check_text = "Correct password"
            
        password_guessed_correct = True
        show_image_buttons = False


        # DEBUG renpy.notify(password_fail_counter)
        # Correct Password: thecakeisalie0417911
    
    def reset_password_text():
        global password_check_text
        password_check_text = ""
        return

    def after_password_action():
        global password_guessed_correct
        global password_fail_counter
        if password_guessed_correct:
            renpy.jump("password_cracked")
        
        # Gives the player help after some failed attempts
        elif password_fail_counter >= 5:
            password_fail_counter = 0
            renpy.jump("password_help")
        return

# ################################## Gallery screen: ##################################
transform change_arrow1:
        xpos 0.035
        ypos 0.40
        zoom 1.0
transform change_arrow2:
        xpos 0.75
        ypos 0.40
        zoom 1.0
transform index_gallery_pos:
        xpos 11.9
        ypos 22.9
default gallery_length = 1
$ gallery_length = len(gallery.items) 

screen phone_hand_camera():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 1)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_camera"), Show("phone_hand")
    imagebutton:
       
        idle "left arrow white idle" at change_arrow1
        hover "left arrow white hover"
        focus_mask True
        action Function(change_index,1), Hide("phone_hand_camera"), Show("phone_hand_camera")
        
    imagebutton:
        idle "right arrow white idle" at change_arrow2
        hover "right arrow white hover"
        focus_mask True
        action Function(change_index,-1), Hide("phone_hand_camera"), Show("phone_hand_camera")
    frame:
        area(670, 140, 467, 730)
        background "#00000000"
        image gallery.get_picture(current_index) at center
    frame: 
        text "[current_index +1 ] / [gallery_length]" at index_gallery_pos
        background "#00000000"

init python:
    def change_index(x):
        global gallery
        global current_index 
        global gallery_length
        gallery_length = len(gallery.items)
        if x < 0:
            current_index += 1 
            current_index = current_index % gallery_length 
        else:
            current_index-= 1  
            current_index = current_index % gallery_length 

# ################################# Contacts screen: ##################################
define contacts_font_size = 45
screen phone_hand_contact():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_contact"), Show("phone_hand")
    

    viewport:
        area (675, 140, 470, 720)
        #draggable False
        mousewheel True
        scrollbars "vertical"

        # Content of the contacts
        vbox:
            spacing 90
            frame:
                area(0, 0 , 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box alex idle"
                    hover "contact box alex hover"
                    focus_mask True
                    action Call("call_alex")

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box leonie idle"
                    hover "contact box leonie hover"
                    focus_mask True
                    action Call("call_leonie")

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box felix idle"
                    hover "contact box felix hover"
                    focus_mask True
                    action Call("call_felix")
            if number_found == True:
                frame:
                    area(0, 0 , 500, 200)
                    background "#00000000"
                    imagebutton:
                        xpos 0.08
                        idle "contact box joe idle"
                        hover "contact box joe hover"
                        focus_mask True
                        action Call("call_joe_arnold")


# ################################## Map screen: ######################################
init python:
    def already_here_notify():
        renpy.notify("You are already here.")
    def cant_go_there_notify():
        renpy.notify("You can't go there.")

screen phone_hand_map():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 3)

    image "images/objects/phone/map/bg map blank.png"
    
    # Dorms
    imagebutton:
        idle "map dorms idle"
        hover "map dorms hover"  
        focus_mask True
        if hide_map:
            action Call("map_disabled")
        elif in_dorms:
            action Function(already_here_notify)
        elif level_3_s:
            action Function(cant_go_there_notify)

    # University
    if website_2_not_seen == False:
        imagebutton:
            idle "map university idle"
            hover "map university hover"
            focus_mask True
            if current_location == 1:
                action Function(already_here_notify)
            elif hide_map:
                action Call("map_disabled")
            elif uni_access_denied:
                action Call("lab_access_denied")
            elif lab_seen:
                action Call("lab_visited")
            elif level_3_s:
                action Function(cant_go_there_notify)
            else:
                action Function(hide_all_screens), Jump("visitlab")

    # Medievil
    if website_3_not_seen == False:
        imagebutton:
            idle "map medievil idle"
            hover "map medievil hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif level_3_s:
                action Function(already_here_notify)
            elif dumpster_doven:
                action Call("dumpster_empty")
            else:
                action Function(hide_all_screens), Jump("dumpsterdive")

    # Gills Place
    if gil_visited == True and (gill_house_seen_bob or gill_house_seen_gill):
        imagebutton:
            idle "map gill house idle"
            hover "map gill house hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif level_3_s:
                action Function(cant_go_there_notify)
            elif dumpster2_doven:
                action Call("dumpster_empty")
            else:
                action Function(hide_all_screens), Jump("dumpsterdive2")
    
    # Return arrow (closes phone)
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow_pos
        xpos 200
        ypos 0
        xsize 500
        ysize 300
        action Hide("phone_hand_map"), Show("phone_hand")

init python:
    def hide_all_screens():
        renpy.hide_screen("phone_hand_map")
        renpy.hide_screen("web_screen")
        renpy.hide_screen("website1_screen")
        renpy.hide_screen("website2_screen")
        renpy.hide_screen("website3_screen")
        renpy.hide_screen("website4_screen")
        renpy.hide_screen("laptop_screen")
        renpy.hide_screen("social_screen_explore")
        renpy.hide_screen("social_screen_search")
        renpy.hide_screen("social_screen_bob")
        renpy.hide_screen("social_screen_gill")
        renpy.hide_screen("social_screen_bob_tag")
        renpy.hide_screen("mail_screen")
        return

# ################################## Notes screen: ####################################
define notes_font_size = 25
screen phone_hand_notes():
    zorder 2
    modal True
    add Solid("#000c")
    
    on "show" action Function(reset_notification, 2)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_notes"), Show("phone_hand")
    
    viewport:
        area phone_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0

        # Content of the notes
        vbox:
            spacing 20
            $ temp_items = notes.get_items_list()
            if len(temp_items) == 0:
                text "{size=[notes_font_size]}{color=[phone_normal_text_color]}There is no information in your notebook{/color}{/size}"
            else:
                for entry in notes.get_items_list():
                    text "{size=[notes_font_size]}{color=[phone_normal_text_color]}[entry.text]{/color}{/size}"

# ################################# Glossary screen: ##################################
define gloss_font_size_big = 70
define gloss_font_size_normal = 50

default gloss_bribery_seen = False
default gloss_impersonation_seen = False
default gloss_dumpster_seen = False
default gloss_tailgating_seen = False
default gloss_phishing_seen = False
default gloss_surfing_seen = False
default gloss_voice_seen = False

define gloss_text_list = ["""{b}{size=[gloss_font_size_big]}Bribery{/size}{/b}\n\nAlso known as “Quid pro quo”, Latin for “something for something”. Involves an exchange of information or services for a compensation. Subjects of bribery are usually aware of their wrongdoings although the true scale of the consequences may not be comprehensible to them at first.""",
                        """{b}{size=[gloss_font_size_big]}Impersonation{/size}{/b}\n\nExplains the act of posing as someone you are not in an attempt to deceive anyone. Impersonation can come in different styles: over the phone, where the voice is enough to pretend to be someone else, or even in person if the one being tricked doesn't know the impersonated one. Appearance, equipment and even other people can help strengthen the deception for example when wearing a warning vest and holding a clipboard.""",
                        """{b}{size=[gloss_font_size_big]}Dumpster Diving{/size}{/b}\n\nMost people don't dispose of their trash properly, leaving a lot of sensitive information in the form of letters, notes or invoices free to access for anyone willing to rummage through the garbage. If hardware is being disposed of, the data can also often still be accessed if the contents of the drives haven't been overwritten properly. Usually people forget their stuff once it's in the trash. “Out of sight out of mind”, but with enough patience, adversaries can get a lot of compromising data through dumpster diving.""",
                        """{b}{size=[gloss_font_size_big]}Tailgating{/size}{/b}\n\nAlso known as “piggybacking”. Describes the act of gaining access to a restricted area by following other people who have access. A perpetrator could, for example, disguise himself as a delivery person or a repair man and wait for someone holding up the door for him in a nice gesture.""",
                        """{b}{size=[gloss_font_size_big]}Shoulder Surfing{/size}{/b}\n\nShoulder surfing is an observational technique to gather information, by for example watching someone over the shoulder typing in confidential information. It doesn't specifically have to be over someones shoulder, but could be done further away by the usage of binoculars, as long as the adversary secretly views their data.""",
                        """{b}{size=[gloss_font_size_big]}Phishing Mail{/size}{/b}\n\nIs  an attack via a message which is used to bait the target into handing out sensitive information or installing malware. In these messages, the attacker pretends to be a legitimate source to gain the trust of the target so they will follow the instructions given. Another variant of this approach is Spear Phishing where the content of the message is directed towards a single individual. In this case, the attacker uses personal information to get to the targeted person.""",
                        """{b}{size=[gloss_font_size_big]}Voice Phishing{/size}{/b}\n\nSimilarly to phishing mail, baits the target into handing out sensitive information by the attacker pretending to be a trustworthy entity. However, unlike email-based phishing, this method involves verbal communication, typically over the phone. This has the advantage that in a call a person doesn't have as much time to think and answer as when responding to an email and thus it stresses out the targets, making them more likely to comply."""]
default gloss_entry_text = ""

define gloss_img_list = ["bribery", "impersonation", "dumpster", "tailgating", "surfing", "phishing", "voice phishing"]
default gloss_entry_img = ""

style gloss_buttons:
    color "#000000"
    hover_color "#9c0000"
    underline False
    hover_underline True
    size gloss_font_size_big

style gloss_text:
    color "#000000"
    size gloss_font_size_normal

style gloss_text_header:
    color "#000000"
    bold True
    size gloss_font_size_big

screen phone_hand_glossary():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 0)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_glossary"), Show("phone_hand")
    
    viewport:
        area phone_usable_area
        draggable True
        mousewheel True
        yinitial 1.0

        # List of buttons for the social engineering techniques
        vbox:
            spacing 20
            text "         Glossary" style "gloss_text_header"
            text "Read more about various social engineering techniques" style "gloss_text"
            if gloss_bribery_seen:
                textbutton "Bribery":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 0), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_impersonation_seen:
                textbutton "Impersonation":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 1), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_dumpster_seen:
                textbutton "Dumpster Diving":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 2), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_tailgating_seen:
                textbutton "Tailgating":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 3), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_surfing_seen:
                textbutton "Shoulder Surfing":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 4), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_phishing_seen:
                textbutton "Phishing":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 5), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_voice_seen:
                textbutton "Voice Phishing":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, 6), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")

# Seperate glossary entry screens
transform phone_landscape_glossary:
    anchor (0.5, 0.5)
    rotate -90
    yalign 0.5
    xalign 0.5
    zoom 1.5


# Seperate glossary entry screens
screen phone_hand_glossary_entry():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png" at phone_landscape_glossary:
        zoom 1.4
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_glossary_entry"), Show("phone_hand_glossary")
    
    viewport:
        area phone_usable_area_quer
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 0.0

        vbox:
            spacing 35
            # List of buttons for the social engineering techniques
            text [gloss_entry_text] style "gloss_text"
            if gloss_entry_img == "bribery" or gloss_entry_img == "voice phishing":
                pass
            else:
                image "images/objects/phone/glossary/gloss %s.png" %gloss_entry_img

init python:
    def set_gloss_text(technique_index):
        global gloss_entry_text
        global gloss_entry_img

        gloss_entry_text = gloss_text_list[technique_index]
        gloss_entry_img = gloss_img_list[technique_index]

init python:
    def set_gloss_text(technique_index):
        global gloss_entry_text
        global gloss_entry_img

        gloss_entry_text = gloss_text_list[technique_index]
        gloss_entry_img = gloss_img_list[technique_index]

# ################################## Pong logic: ######################################
init python:
    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 95
            self.PADDLE_HEIGHT = 12
            self.PADDLE_Y = 950
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_RIGHT = 1146
            self.COURT_LEFT = 660

            # Some displayables we use.
            self.paddle = Solid("#000000", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#000000", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playerx = (self.COURT_RIGHT - self.COURT_LEFT) / 2
            self.computerx = self.playerx

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, delta-position, and the speed of the ball.
            self.bx = self.playerx + (self.PADDLE_WIDTH / 2)
            self.by = self.PADDLE_Y - self.PADDLE_HEIGHT - 5
            self.bdx = 0.5
            self.bdy = -0.5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = -1

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and draws the screen.
        # Function render is being called by the call screen in renpy automatically
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            lastby = self.by

            if self.stuck:
                self.bx = self.playerx + (self.PADDLE_WIDTH / 2)
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.bx - (self.computerx + (self.PADDLE_WIDTH / 2))) <= cspeed:
                self.computerx = self.bx - (self.PADDLE_WIDTH / 2)
            else:
                self.computerx += cspeed * (self.bx - (self.computerx + (self.PADDLE_WIDTH / 2))) / abs(self.bx - (self.computerx + (self.PADDLE_WIDTH / 2)))

            # Clamp computer paddle
            self.computerx = min(self.computerx, self.COURT_RIGHT - self.PADDLE_WIDTH)
            self.computerx = max(self.computerx, self.COURT_LEFT)


            # Bounce off of right.
            ball_right = self.COURT_RIGHT - (self.BALL_WIDTH / 2)
            if self.bx > ball_right:
                self.bx = ball_right + (ball_right - self.bx)
                self.bdx = -self.bdx

                # if not self.stuck:
                #     renpy.sound.play("pong_beep.opus", channel=0)

            # Bounce off left.
            ball_left = self.COURT_LEFT + (self.BALL_WIDTH / 2)
            if self.bx < ball_left:
                self.bx = ball_left - (self.bx - ball_left)
                self.bdx = -self.bdx

                # if not self.stuck:
                #     renpy.sound.play("pong_beep.opus", channel=0)

            # Draw a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Rendering of the paddle
                pi = renpy.render(self.paddle, width, height, st, at)
                r.blit(pi, (int(px), int(py)))

                # Check for hit with ball...
                # ...on x axis:
                if px <= self.bx <= px + self.PADDLE_WIDTH:

                    hit = False

                    # ...on y axis:
                    if lastby >= hotside >= self.by:
                        self.by = hotside + (hotside - self.by)
                        self.bdy = -self.bdy
                        hit = True

                    elif lastby <= hotside <= self.by:
                        self.by = hotside - (self.by - hotside)
                        self.bdy = -self.bdy
                        hit = True

                    if hit:
                        renpy.sound.play("audio/sfx/pong_blip.wav")
                        self.bspeed *= 1.10

            # Draw the two paddles. (first player, then computer)
            paddle(self.playerx, self.PADDLE_Y, self.PADDLE_Y)
            paddle(self.computerx, 150, 150 + self.PADDLE_HEIGHT)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                            int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.by < 100:
                self.winner = 0
                # renpy.notify("winner player")

                # Needed to ensure that event is called, noticingthe winner.
                renpy.timeout(0)

            elif self.by > height - 50:
                self.winner = 1
                # renpy.notify("winner computer")
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and self.stuck == True:
                self.stuck = False
                renpy.sound.play("audio/sfx/pong_blip.wav")
                # renpy.notify("click")
                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            x = min(x, self.COURT_RIGHT - self.PADDLE_WIDTH)
            x = max(x, self.COURT_LEFT)
            self.playerx = x

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner != -1:
                self.reset_game(self.winner)
            else:
                raise renpy.IgnoreEvent()
        
        # Resets game so that it can be played again
        def reset_game(self, winner):
            global winner_text

            # Set winner text
            if winner == 0:
                winner_text = "player won"
            else:
                winner_text = "computer won"
            
            # Reset variables
            self.stuck = True
            self.bx = self.playerx + (self.PADDLE_WIDTH / 2)
            self.by = self.PADDLE_Y - self.PADDLE_HEIGHT - 5

            self.bdx = 0.5
            self.bdy = -0.5
            self.bspeed = 350.0
        
            # The time of the past render-frame.
            self.oldst = None

            self.winner = -1

            renpy.restart_interaction()


default winner_text = ""

# ################################## Pong screen: #####################################
screen phone_hand_mini_game():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    

    default pong = PongDisplayable()

    add pong   

    # text "Player":
    #     xpos 240
    #     xanchor 0.5
    #     ypos 25
    #     size 40

    # text "Computer":
    #     xpos (1280 - 240)
    #     xanchor 0.5
    #     ypos 25

    if pong.stuck:
        text "[winner_text]":
            xpos 765
            ypos 400
            size 40
            color "#000000"
        text "Click to Begin":
            xpos 765
            ypos 450
            size 40
            color "#000000"

        # Return arrow
        imagebutton:
            idle "return arrow idle"
            hover "return arrow hover" at arrow_pos
            xpos 200
            ypos 0
            xsize 500
            ysize 300
            action Hide("phone_hand_mini_game"), Show("phone_hand")

# ################################## Phone Icon: ######################################
default phone_open = False
screen phone_icon():
    zorder 2
    modal False
    if show_image_buttons:
        imagebutton:
            idle "phone_icon_idle" 
            hover "phone_icon_hover" at phone_pos
            
            focus_mask True
            action Show("phone_hand"), Hide("phone_icon"), Function(set_phone_open, True)
        
        # Displays notification circ if there's any new notification
        if phone_not_glossary or phone_not_gallery or phone_not_notes or phone_not_map:
            add "circ_anim":
                zoom 0.30
                xpos 210
                ypos 785

# Function to keep track if phone is open or not (necessary in level 3)
init python:
    def set_phone_open(boolean):
        global phone_open
        phone_open = boolean
        # DEBUG renpy.notify("phone:" + str(boolean))
        return