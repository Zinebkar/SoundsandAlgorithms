# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file contains various interactive screens used in mini games

# ############################ Felix room point and click: ############################
label hide_felix_room_interactables():
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    return

label show_felix_room_interactables():
    show screen felixes_bin
    show screen felixes_bed
    show screen felixes_pc
    show screen felixes_notebook
    show screen felixes_map
    show screen felixes_wall1
    show screen felixes_wall2
    show screen felixes_wall3
    return

screen felixes_notebook():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f notebooks.png" 
            idle "images/backgrounds/felix room/fb notebooks.png" 
            focus_mask True
            action Hide("felixes_notebook"),Jump("notebooks")

screen felixes_bin():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f bin.png" 
            idle "images/backgrounds/felix room/fb bin.png" 
            focus_mask True
            action Hide("felixes_bin"),Jump("bin")


screen felixes_bed():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f bed.png" 
            idle "images/backgrounds/felix room/fb bed.png" 
            focus_mask True
            action Hide("felixes_bed"),Jump("bed")


screen felixes_map():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f map.png" 
            idle "images/backgrounds/felix room/fb map.png" 
            focus_mask True
            action Hide("felixes_map"),Jump("map")


screen felixes_pc():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f pc.png" 
            idle "images/backgrounds/felix room/fb pc.png" 
            focus_mask True
            action Hide("felixes_pc"),Jump("pc")

screen felixes_wall1():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall1.png" 
            idle "images/backgrounds/felix room/fb wall1.png" 
            focus_mask True
            action Hide("felixes_wall1"),Jump("wall1")

screen felixes_wall2():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall2.png" 
            idle "images/backgrounds/felix room/fb wall2.png" 
            focus_mask True
            action Hide("felixes_wall2"),Jump("wall2")

screen felixes_wall3():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall3.png" 
            idle "images/backgrounds/felix room/fb wall3.png" 
            focus_mask True
            action Hide("felixes_wall3"),Jump("wall3")


# ################################ Janitor mini game: #################################
screen round_rect(trust):
    image "gui/bar/bottom back.png":
        xalign 0.976 ypos 297
        ysize 506
        
    vbar:
        xalign 0.974 ypos 300
        ysize 500
        value AnimatedValue(trust,100,0.5)

        if (trust >= 75 ):
            bottom_bar "gui/bar/bottomgreen.png"
        elif (trust > 40):
            bottom_bar "gui/bar/bottomyellow.png"
        else:
            bottom_bar "gui/bar/bottomred.png"

    
    text "{size=50}{b}TRUST{/b}{/size}":
        xalign 0.99 ypos 210
        size 50
        outlines [(3, "#000000ff", 0, 0)]
        color "#AA4473FF"


# ############################ Lab room point and click: ##############################
label hide_lab_screens:
    hide screen left_cage
    hide screen left_pc
    #hide screen medical_tools
    hide screen left_wall
    hide screen symbol_screen
    hide screen right_cage
    hide screen right_pc
    hide screen trash
    return

screen left_cage:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left cage hover.png" 
            idle "images/backgrounds/lab/left cage idle.png" 
            focus_mask True
            action Hide("left_cage"),Jump("rat_in_cage_left")

screen left_pc:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left pc hover.png" 
            idle "images/backgrounds/lab/left pc idle.png" 
            focus_mask True
            action Hide("left_pc"),Jump("left_pc_stats")

screen left_wall:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left wall hover.png" 
            idle "images/backgrounds/lab/left wall idle.png" 
            focus_mask True
            action Hide("left_wall"),Jump("left_wall_obj")

screen symbol_screen:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/monitor hover.png" 
            idle "images/backgrounds/lab/monitor idle.png" 
            focus_mask True
            action Hide("symbol_screen"),Jump("symbols_on_screen")

screen right_cage:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/right cage hover.png" 
            idle "images/backgrounds/lab/right cage idle.png" 
            focus_mask True
            action Hide("right_cage"),Jump("rat_in_cage_right")

screen right_pc:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/right pc hover.png" 
            idle "images/backgrounds/lab/right pc idle.png" 
            focus_mask True
            action Hide("right_pc"),Jump("right_pc_stats")
screen trash:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/trash hover.png" 
            idle "images/backgrounds/lab/trash idle.png" 
            focus_mask True
            action Hide("trash"),Jump("empty_trash")


# ############################## Lab pin pad mini game: ###############################
define pin_correct = "471965"
default pin_current = ""

screen pin_pad_input:
    image "images/backgrounds/pinpad/bg pinpad.png"

    if len(pin_current) > 0:
        image "images/backgrounds/pinpad/pin enter %s.png" %len(pin_current)

    # Number buttons
    for i in range(0, 10):
        imagebutton:
            idle "images/backgrounds/pinpad/%s idle.png" %i
            hover "images/backgrounds/pinpad/%s hover.png" %i
            focus_mask True
            action Function(pin_add_number, i)
    
    # Clear button
    imagebutton:
        idle "images/backgrounds/pinpad/c idle.png"
        hover "images/backgrounds/pinpad/c hover.png"
        focus_mask True
        action Function(pin_clear_input)
    
    # Enter button
    imagebutton:
        idle "images/backgrounds/pinpad/e idle.png"
        hover "images/backgrounds/pinpad/e hover.png"
        focus_mask True
        action Function(pin_enter)

init python:
    def pin_add_number(num):
        global pin_current
        if len(pin_current) < 6:
            pin_current = pin_current + str(num)
            renpy.sound.play("audio/sfx/pin_pad_enter.wav")
        # renpy.notify(pin_current) # DEBUG
        return

    def pin_clear_input():
        global pin_current
        pin_current = ""
        renpy.sound.play("audio/sfx/pin_pad_clear.wav")
        return

    def pin_enter():
        if pin_correct == pin_current:
            renpy.sound.play("audio/sfx/pin_pad_correct.wav")
            renpy.jump("pin_pad_mini_game_complete")
        else:
            renpy.sound.play("audio/sfx/pin_pad_false.wav")


# ########################### Bob room point and click: ###############################
label hide_bob_screens:
    hide screen bob_laptop
    hide screen bob_book_shelf
    hide screen bob_sofa
    hide screen bob_painting
    hide screen phone_icon
    hide screen bob_phone
    return

screen bob_laptop:
    zorder 0
    modal False
    if show_image_buttons == True and computer_seen == False:
        imagebutton :
            hover "images/backgrounds/Bob Office/bob computer hover.png" 
            idle "images/backgrounds/Bob Office/bob computer idle.png"
            focus_mask True
            action Hide("bob_laptop"),Jump("laptop")

screen bob_phone:
    zorder 0
    modal False
    if show_image_buttons == True and phone_seen == False:
        if number_found == False:
            imagebutton :
                hover "images/backgrounds/Bob Office/bob phone hover.png" 
                idle "images/backgrounds/Bob Office/bob phone idle.png"
                focus_mask True
                action Hide("bob_phone"),Jump("phone")
        else:
            imagebutton :
                hover "images/backgrounds/Bob Office/bob phone hover.png" 
                idle "images/backgrounds/Bob Office/bob phone idle.png"
                focus_mask True
                action Hide("bob_phone"),Jump("phone_2")

screen bob_book_shelf:
    zorder 0
    modal False
    if show_image_buttons == True and books_seen == False:
        imagebutton :
            hover "images/backgrounds/Bob Office/bob bookshelf hover.png" 
            idle "images/backgrounds/Bob Office/bob bookshelf idle.png" 
            focus_mask True
            action Hide("bob_book_shelf"),Jump("book_shelf")

screen bob_sofa:
    zorder 0
    modal False
    if show_image_buttons == True and sofa_seen == False:
        imagebutton :
            hover "images/backgrounds/Bob Office/bob sofa hover.png" 
            idle "images/backgrounds/Bob Office/bob sofa idle.png"
            focus_mask True
            action Hide("bob_sofa"),Jump("sofa")

screen bob_painting:
    zorder 0
    modal False
    if show_image_buttons == True and painting_seen == False:
        imagebutton :
            hover "images/backgrounds/Bob Office/bob painting hover.png" 
            idle "images/backgrounds/Bob Office/bob painting idle.png" 
            focus_mask True
            action Hide("bob_painting"),Jump("painting")


# ########################## optional room point and click: ###########################
label hide_optional_room_screen:
    hide screen optional_room
    hide screen phone_icon

screen optional_room:
    zorder 0
    modal False
    if show_image_buttons == True and hospital_bed_seen == False:
        imagebutton:
            hover "images/backgrounds/Bob Office/bed hover.png" 
            idle "images/backgrounds/Bob Office/bed idle.png"  
            focus_mask True
            action Hide("optional_room"),Jump("hospital_bed")
    if show_image_buttons == True and operation_table_seen == False:
        imagebutton:
            hover "images/backgrounds/Bob Office/tools hover.png"
            idle "images/backgrounds/Bob Office/tools idle.png"
            focus_mask True
            action Hide("optional_room"),Jump("operation_table")
    if show_image_buttons == True and skull_anatomy_seen == False:
        imagebutton:
            hover "images/backgrounds/Bob Office/skull hover.png" 
            idle "images/backgrounds/Bob Office/skull idle.png"
            focus_mask True
            action Hide("optional_room"),Jump("skull_anatomy")
