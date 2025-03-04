# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file contains the dumpster diving mini game encountered in level 2

# 1 is the receipt, 2 is the random trash, 3 is the handover note

# ################################ Dumpster diving 1: #################################
define diving1completed = False
default diving_minigame_active_index = 0

label dumpster_diving_minigame_start:
    $ diving_minigame_active_index = 0
    hide screen phone_icon
    call screen dumpster_diving_minigame_1 # Calling a screen hides the dialogue box

label dumpster_diving_minigame_completed_1:
    $ diving1completed = True
    $ mail_1_text_unlocked[2] = 1 # Sets variable to show the phishing mail text in the phishing mail mini game
    scene bg dumpster diving 3 finished
    pause 1.5
    # scene bg new kitchen
    $ gallery.add_data(["gallery_dd_receipt"], True)
    pause 1.5
    L "Interesting."
    jump after_dumpsterdive

    
# Variables
define placement_sens = 20 # How sensitive the pieces must be aligned with their assigned spot (lower is more sensitive)
define dd1_pieces_total = 16
default dd1_pieces_completed = 0
define dd1_piece_pos_goal = [(129, 36), (411, 35), (200, 37), (130, 334), (130, 238), (445, 255), (351, 289), (132, 459), (313, 448), (130, 552), (130, 712), (222, 725), (128, 775), (386, 617), (259, 899), (409, 753)]
define dd1_piece_pos_initial = [(1000, 512), (740, 700), (1400, 64), (880, 250), (1200, 730), (1550, 400), (1330, 350), (700, 120), (1500, 590), (750, 210), (1300, 472), (1100, 610), (1400, 61), (890, 400), (1100, 300), (850, 350)]

screen dumpster_diving_minigame_1:
    image "images/objects/dumpster diving/bg dumpster diving 3.jpg"
    add Solid("#0008")
    draggroup:
        # Draggable image pieces
        for i in range(dd1_pieces_total):
            drag:
                drag_name i
                pos dd1_piece_pos_initial[i]

                focus_mask True
                draggable True
                drag_raise True

                image "images/objects/dumpster diving/pieces 3/piece %s.png" %(i + 1)

        # Spots where the pieces should snap onto
        for i in range(dd1_pieces_total):
            drag:
                drag_name i
                pos dd1_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True          # Other drags can be dropped onto this drag
                dropped dropped_onto    # Function beeing called when dropped onto

                image "images/objects/dumpster diving/pieces 3/piece %s.png" %(i + 1) alpha 0.0
    text "Solve the Puzzle in the rectangle.":
        xalign 0.6
        yalign 0.03
        size 50


# ################################ Dumpster diving 2: #################################
label dumpster_diving_minigame2_start:
    $ diving_minigame_active_index = 1
    hide screen phone_icon
    call screen dumpster_diving_minigame_2 # Calling a screen hides the dialogue box

label dumpster_diving_minigame2_completed:
    $ diving1completed = True
    scene bg dumpster diving 1 finished
    pause 1.5
    scene bg gill dumpster
    L "Seems like that's just useless trash, go on."
    $ diving_minigame_active_index = 2
    call screen dumpster_diving_minigame_3

    
# Variables
define placement_sens = 20 # How sensitive the pieces must be aligned with their assigned spot (lower is more sensitive)
define dd2_pieces_total = 20
default dd2_pieces_completed = 0
define dd2_piece_pos_goal = [(96, 21), (185, 21), (538, 815), (158, 838), (606, 359), (537, 443), (310, 811), (96, 560), (312, 706), (96, 433), (96, 112), (570, 21), (405, 21), (537, 166), (529, 75), (392, 402), (275, 359), (176, 97), (315, 90), (288, 202)]
define dd2_piece_pos_initial = [(1400, 660), (1000, 300), (750, 350), (900, 50), (1240, 450), (840, 150), (1040, 550), (790, 500), (1250, 250), (1100, 420), (850, 80), (970, 290), (1145, 362), (1500, 130), (1080, 450), (1200, 320), (830, 150), (1320, 320), (790, 290), (1110, 410)]

screen dumpster_diving_minigame_2:
    image "images/objects/dumpster diving/bg dumpster diving 1.png"
    add Solid("#0008")
    draggroup:
        # Draggable image pieces
        for i in range(dd2_pieces_total):
            drag:
                drag_name i
                pos dd2_piece_pos_initial[i]

                focus_mask True
                draggable True
                drag_raise True

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1)

        # Spots where the pieces should snap onto
        for i in range(dd2_pieces_total):
            drag:
                drag_name i
                pos dd2_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True          # Other drags can be dropped onto this drag
                dropped dropped_onto    # Function beeing called when dropped onto

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1) alpha 0.0
    text "Solve the Puzzle in the rectangle.":
        xalign 0.6
        yalign 0.03
        size 50


# ################################ Dumpster diving 3: #################################
label dumpster_diving_minigame3_completed:
    $ diving1completed = True
    $ mail_1_text_unlocked[0] = 1 # Sets variable to show the phishing mail text in the phishing mail mini game
    $ mail_1_text_unlocked[1] = 1

    scene bg dumpster diving 2 finished
    pause 1.5
    scene bg gill dumpster

    $ gallery.add_data(["gallery_dd_notepage"], True)
    pause 1.5
    jump after_dumpsterdive2

# Variables
define dd3_pieces_total = 18
default dd3_pieces_completed = 0
define dd3_piece_pos_goal = [(49, 24), (260, 24), (134, 250), (49, 454), (49, 673), (124, 672), (193, 476), (486, 24), (560, 24), (648, 100), (617, 307), (410, 444), (283, 646), (283, 822), (437, 840), (664, 713), (548, 585), (630, 457)]
define dd3_piece_pos_initial = [(1500, 660), (1100, 300), (850, 350), (1000, 50), (1340, 450), (940, 150), (1140, 550), (890, 500), (1350, 250), (1200, 420), (950, 80), (1070, 290), (1245, 362), (1600, 130), (1180, 450), (1300, 320), (930, 150), (1420, 320)]

screen dumpster_diving_minigame_3:
    image "images/objects/dumpster diving/bg dumpster diving 2.png"
    add Solid("#0008")
    draggroup:
        # Draggable image pieces
        for i in range(dd3_pieces_total):
            drag:
                drag_name i
                pos dd3_piece_pos_initial[i]

                focus_mask True
                draggable True
                drag_raise True

                image "images/objects/dumpster diving/pieces 2/piece %s.png" %(i + 1)

        # Spots where the pieces should snap onto
        for i in range(dd3_pieces_total):
            drag:
                drag_name i
                pos dd3_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True          # Other drags can be dropped onto this drag
                dropped dropped_onto    # Function beeing called when dropped onto

                image "images/objects/dumpster diving/pieces 2/piece %s.png" %(i + 1) alpha 0.0
    text "Solve the Puzzle in the rectangle.":
        xalign 0.6
        yalign 0.03
        size 50


# ################################### Snap Function ###################################
init python:
    import math
    
    # Function called when one of the dragged_pieces is being dropped onto on of the snap_spots
    def dropped_onto(snap_spot, dragged_piece):
        global dd1_pieces_completed
        global dd2_pieces_completed
        global dd3_pieces_completed

        # Snap piece if piece is on correct spot and distance is close enough
        if snap_spot.drag_name == dragged_piece[0].drag_name:
            distance = math.sqrt((snap_spot.x - dragged_piece[0].x)**2 + (snap_spot.y - dragged_piece[0].y)**2)
            if distance < placement_sens:
                dragged_piece[0].snap(snap_spot.x, snap_spot.y, 0.1)
                dragged_piece[0].draggable = False
                dragged_piece[0].bottom()
                renpy.sound.play("audio/sfx/dumpster_clip.wav")

                if diving_minigame_active_index == 0:
                    dd1_pieces_completed +=1
                    if dd1_pieces_completed == dd1_pieces_total:
                        renpy.sound.play("audio/sfx/dumpster_done.wav")
                        renpy.jump("dumpster_diving_minigame_completed_1")
                elif diving_minigame_active_index == 1:
                    dd2_pieces_completed += 1
                    if dd2_pieces_completed == dd2_pieces_total:
                        renpy.sound.play("audio/sfx/dumpster_done.wav")
                        renpy.jump("dumpster_diving_minigame2_completed")
                elif diving_minigame_active_index == 2:
                    dd3_pieces_completed += 1
                    if dd3_pieces_completed == dd3_pieces_total:
                        renpy.sound.play("audio/sfx/dumpster_done.wav")
                        renpy.jump("dumpster_diving_minigame3_completed")