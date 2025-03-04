# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file contains the security mini game encountered in level 3

# ############################## Mini game explanation: ###############################
label security_minigame_start:
    $ show_textbox = False
    if detected == True:
        $ show_image_buttons = False
        show screen minigame_screen()
        jump game_lost
    else:
        if first_time_in:
            $ show_textbox = True
            $ show_image_buttons = False
            show screen minigame_screen()
            "[[1/5] You are the golden circle."
            "[[2/5] Use the Buttons with arrows to move in the according direction."
            "[[3/5] Avoid the vision cones of the security."
            "[[4/5] Follow the personal to get through the glas doors."
            if fire_alarm == True:
                show screen office_exit
                "[[5/5] The green room is the exit of the office area and the yellow rooms are for you to explore."
                hide screen office_exit
            else:
                show screen bobs_office
                "[[5/5] The green room is bobs office and the yellow rooms are for you to explore."
                hide screen bobs_office
            $ first_time_in = False
            $ show_image_buttons = True
            $ show_textbox = False
        show screen minigame_screen()
    #$ renpy.notify("to early")
        jump empty_label
    #outside of tuple:
    #0s are no field 
    #1s are field 
    #2s are rooms 
    #3 bobs room
    #in tuple:
    #0 is notailgate person in 
    #1s are orange tailgate people
    #2s are green tailgate people
    #3s are purple tailgate people
    #4s are blue tailgate people
    #[field,security on field,is player on field,tailgate people] (t for true f for false) extra: door open : O door closed : C
    # 120, 60

# #################################### Variables: #####################################
default x = 0
default y = 0

define char_icon_offset = -47

screen bobs_office:
    image "security minigame goal"

screen office_exit:
    image "security minigame backwards goal"

# ################################ Mini game screen: ##################################
screen minigame_screen():
    zorder 0
    modal False
    if fire_alarm == False:
        image "bg security minigame"
    else :
        image "bg security minigame backwards"
    
    if visability_list2[1] == True or cameras_off == False:
        if door_state == False:
            image "door closed"
        else:
            image "door open"
    if visability_list2[0] == True or cameras_off == False:
        if door_state1 == False:
            image "door closed":
                xpos -841
        else:
            image "door open":
                xpos -841

    for i in range(0,4):
        # ######################## Guard positioning: #################################
        $ x = sec_list[i][0][sec_list[i][1]][1]
        $ y = sec_list[i][0][sec_list[i][1]][0]
        if (i == 0 and cameras_off == False) or (i == 0 and visability_list[i] == True):
            if security_aware == True:
                image "guard cone long":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60 
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            else:
                image "guard cone":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60 
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard icon" :
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif (i == 1 and cameras_off == False) or (i == 1 and visability_list[i] == True):
            if security_aware == True:
                image "guard cone long":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            else:
                image "guard cone":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard icon" :
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif (i == 2 and cameras_off == False) or (i == 2 and visability_list[i] == True):
            if security_aware == True:
                image "guard cone long":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            else:
                image "guard cone":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard icon" :
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif (cameras_off == False and i == 3) or (i == 3 and visability_list[i] == True):
            if security_aware == True:
                image "guard cone long":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            else:
                image "guard cone":
                    alpha 0.5
                    anchor (0.5,0.5)
                    ypos  120 * x + 60
                    xpos 1800 - (60 + 120 * y) + 60
                    rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard icon" :
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset

        # ###################### Employee positioning: ################################
        $ x = tailgate_list[i][0][tailgate_list[i][1]][1]
        $ y = tailgate_list[i][0][tailgate_list[i][1]][0]

        if ((i == 0 and cameras_off == False) or (i == 0 and visability_list1[i] == True)) and tailgate_list[i][0][tailgate_list[i][1]][1] != -1:
            image "orange icon" :
                rotate 90 * (tailgate_list[i][0][tailgate_list[i][1]][2]-2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif ((i == 1 and cameras_off == False) or (i == 1 and visability_list1[i] == True)) and tailgate_list[i][0][tailgate_list[i][1]][1] != -1:
            image "green icon":
                rotate 90 * (tailgate_list[i][0][tailgate_list[i][1]][2]-2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif ((i == 2 and cameras_off == False) or (i == 2 and visability_list1[i] == True)) and tailgate_list[i][0][tailgate_list[i][1]][1] != -1:
            image "purple icon" :
                rotate 90 * (tailgate_list[i][0][tailgate_list[i][1]][2]-2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset
        elif ((i == 3 and cameras_off == False) or (i == 3 and visability_list1[i] == True)) and tailgate_list[i][0][tailgate_list[i][1]][1] != -1:
            image "blue icon" :
                rotate 90 * (tailgate_list[i][0][tailgate_list[i][1]][2]-2)
                ypos  120 * x + char_icon_offset
                xpos 1800 - (60 + 120 * y) + char_icon_offset

    # ###################### Player and movement buttons: #############################
    $ x = player_pos[1]
    $ y = player_pos[0]
    image "player" :
        ypos  120 * x + 16
        xpos  1800 - (60 + 120 * y) + 16
    if cameras_off == True:
        image "security view circle":
            zoom 2
            ypos  120 * x + 32 - 1050
            xpos  1800 - (60 + 120 * y) + 41 - 1900
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "mid idle" 
            hover "mid hover"
            action Function(turn,0),Hide("minigame_screen"),Jump("security_minigame_start")
    if show_image_buttons == True and valid_inputs[4] == 1:    
        imagebutton:
            focus_mask True
            idle "up idle" 
            hover "up hover"
            if valid_inputs[4] == 1:
                action Function(turn,4),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True and valid_inputs[1] == 1:    
        imagebutton:
            focus_mask True
            idle "right idle" 
            hover "right hover"
            if valid_inputs[1] == 1:
                action Function(turn,1),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True and valid_inputs[2] == 1:    
        imagebutton:
            focus_mask True
            idle "down idle" 
            hover "down hover"
            if valid_inputs[2] == 1:
                action Function(turn,2),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True and valid_inputs[3] == 1:    
        imagebutton:
            focus_mask True
            idle "left idle" 
            hover "left hover"
            if valid_inputs[3] == 1:
                action Function(turn,3),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")

# ############################### Logic for mini game: ################################
init python:
    def real_notify(string):
        pass
        # DEBUG renpy.notify(string)
    def turn(input):
        global game_matrix
        global sec_list
        global tailgate_list
        global valid_inputs
        global player_pos
        global door_timer
        global door_state
        global door_timer1
        global door_state1
        global optional_flag
        global courtyard_flag
        global bobs_flag
        global detected
        if door_timer < 0:
            door_state = False
        door_timer -= 1
        if door_timer1 < 0:
            door_state1 = False
        door_timer1 -= 1
        turn_personal(game_matrix,tailgate_list)
        turn_player(input,game_matrix)
        turn_security(game_matrix,sec_list)
        in_vision()
        in_vision_personal()
        in_vision_door()
        for i in range(0,4):
            if see(sec_list[i][0][sec_list[i][1]][1],sec_list[i][0][sec_list[i][1]][0],sec_list[i][0][sec_list[i][1]][2],game_matrix) == 1:
                renpy.sound.play("audio/sfx/security_caught.wav")
                renpy.jump("game_lost")
                #renpy.notify("u lost")
                #detected = True
        if player_pos == [6,5] and courtyard_flag:
            courtyard_flag = False
            renpy.jump("courtyard")
        elif player_pos == [1,1] and bobs_flag and fire_alarm == False:
            bobs_flag = False
            renpy.jump("bobs_office")
        elif player_pos == [9,0] and optional_flag:
            optional_flag = False
            renpy.jump("optional")
        elif player_pos == [14,1] and fire_alarm == True:
            renpy.jump("find_felix")
        #renpy.notify(door_timer)
        renpy.restart_interaction()
        #renpy.show("minigame_screen")
    def turn_player(input,matrix):
        
        global player_pos
        global valid_inputs
        if input == 1:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[0] -= 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 2:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[1] += 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 3:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[0] += 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 4:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[1] -= 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"

        if player_pos[0] == 0:
            valid_inputs[1] = 0
        elif matrix[player_pos[0]-1][player_pos[1]] == 0:
            valid_inputs[1] = 0
        else:
            valid_inputs[1] = 1
        if player_pos[1] == 8:
            valid_inputs[2] = 0
        elif matrix[player_pos[0]][player_pos[1]+1] == 0:
            valid_inputs[2] = 0
        else:
            valid_inputs[2] = 1
        if player_pos[0] == 14:
            valid_inputs[3] = 0
        elif matrix[player_pos[0]+1][player_pos[1]] == 0:
            valid_inputs[3] = 0
        else:
            valid_inputs[3] = 1
        if player_pos[1] == 0:
            valid_inputs[4] = 0
        elif matrix[player_pos[0]][player_pos[1]-1] == 0:
            valid_inputs[4] = 0
        else:
            valid_inputs[4] = 1
    
        if player_pos == [4,5]:
            if door_state == False:
                valid_inputs[1] = 0
                # DEBUG renpy.notify(valid_inputs[1])
        if player_pos == [3,5]:
            if door_state == False:
                valid_inputs[3] = 0
        if player_pos == [10,5]:
            if door_state1 == False:
                valid_inputs[3] = 0
                # DEBUG renpy.notify(valid_inputs[1])
        if player_pos == [11,5]:
            if door_state1 == False:
                valid_inputs[1] = 0
    
    def turn_personal(matrix,path_list):
        global door_state
        global door_timer
        global door_state1
        global door_timer1
        for i in range(0,4):
            #matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = 0
            path_list[i][1] +=1
            path_list[i][1] = path_list[i][1] % (len(path_list[i][0]))
            #matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = 1
            if i == 3:
                if path_list[3][0][path_list[3][1]][0] == 3 and path_list[3][0][path_list[3][1]][1] == 5:
                    door_state = True
                    door_timer = 2
                    #renpy.notify(door_state)
            if i == 2:
                if path_list[2][0][path_list[2][1]][0] == 4 and path_list[2][0][path_list[2][1]][1] == 5:
                    door_state = True
                    door_timer = 2
                    #renpy.notify(door_state)
            if i == 0:
                if path_list[0][0][path_list[0][1]][0] == 11 and path_list[0][0][path_list[0][1]][1] == 5:
                    door_state1 = True
                    door_timer1 = 2
                    #renpy.notify(door_state)
            if i == 1:
                if path_list[1][0][path_list[1][1]][0] == 11 and path_list[1][0][path_list[1][1]][1] == 5:
                    door_state1 = True
                    door_timer1 = 2
                    #renpy.notify(door_state)
    def turn_security(matrix,path_list):
        for i in range(0,4):
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][0] = 0
            path_list[i][1] +=1
            path_list[i][1] = path_list[i][1] % (len(path_list[i][0]) - 1)
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = path_list[i][0][path_list[i][1]][2]
    
    def see(x,y,d,matrix):
        if matrix[y][x][1] == "t":
            return 1
        if d == 4:
            if (x - 1) < 0:
                pass
            else:
                #print(str(x) + "," + str(y))
                if matrix[y][x - 1] == 0:
                    return 0
                elif matrix[y][x - 1][1] == "t":
                    return 1
            if x - (1 * 2) < 0:
                pass
            else:
                if matrix[y][x - (1 * 2)] == 0:
                    pass
                elif matrix[y][x-2][1] == "t":
                    return 1
            if security_aware == True:
                if x - (1 * 3) < 0:
                    pass
                else:
                    if matrix[y][x - (1 * 3)] == 0:
                        pass
                    elif matrix[y][x-3][1] == "t":
                        return 1
            if (y-1) < 0:
                pass
            else:
                if matrix[y-1][x] == 0:
                    pass
                elif matrix[y-1][x][1] == "t":
                    return 1
            
            if (y+1) > 14:
                pass
            else:
                if matrix[y+1][x] == 0:
                    pass
                elif matrix[y+1][x][1] == "t":
                    return 1

        if d == 2:
            if x + 1 > 8:
                pass
            else:
                if matrix[y][x + 1] == 0:
                    pass
                elif matrix[y][x + 1][1] == "t":
                    return 1
            if x + (1 * 2) > 8 :
                pass
            else:
                if matrix[y][x + (1 * 2)] == 0:
                    pass
                elif matrix[y][x+2][1] == "t":
                    return 1
            if security_aware == True:
                if x + (1 * 3) > 8 :
                    pass
                else:
                    if matrix[y][x + (1 * 3)] == 0:
                        pass
                    elif matrix[y][x+3][1] == "t":
                        return 1
            if (y-1) < 0:
                pass
            else:
                if matrix[y-1][x] == 0:
                    pass
                elif matrix[y-1][x][1] == "t":
                    return 1
            
            if (y+1) > 14:
                pass
            else:
                if matrix[y+1][x] == 0:
                    pass
                elif matrix[y+1][x][1] == "t":
                    return 1
            
        if d == 1:
            if y - 1 < 0:
                pass
            else:
                if matrix[y - 1][x] == 0:
                    pass
                elif matrix[y - 1][x][1] == "t":
                    return 1
            if y - (1 * 2) < 0:
                pass
            else:
                if matrix[y - (1 * 2)][x] == 0:
                    pass
                elif matrix[y-2][x][1] == "t":
                    return 1
            if security_aware == True:
                if y - (1 * 3) < 0:
                    pass
                else:
                    if matrix[y - (1 * 3)][x] == 0:
                        pass
                    elif matrix[y-3][x][1] == "t":
                        return 1
            if (x-1) < 0:
                pass
            else:
                if matrix[y][x-1] == 0:
                    pass
                elif matrix[y][x-1][1] == "t":
                    return 1
            
            if (x+1) > 8:
                pass
            else:
                if matrix[y][1+x] == 0:
                    pass
                elif matrix[y][1+x][1] == "t":
                    return 1

        if d == 3:
            if y + 1 > 14:
                pass
            else:
                if matrix[y + 1][x] == 0:
                    pass
                elif matrix[y + 1][x][1] == "t":
                    return 1
            if y + (1 * 2) > 14:
                pass
            else:
                if matrix[y + (1 * 2)][x] == 0:
                    pass
                elif matrix[y+2][x][1] == "t":
                    return 1
            if security_aware == True:
                if y + (1 * 3) > 14:
                    pass
                else:
                    if matrix[y + (1 * 3)][x] == 0:
                        pass
                    elif matrix[y+3][x][1] == "t":
                        return 1
            if (x-1) < 0:
                pass
            else:
                if matrix[y][x-1] == 0:
                    pass
                elif matrix[y][x-1][1] == "t":
                    return 1
            
            if (x+1) > 8:
                pass
            else:
                if matrix[y][1+x] == 0:
                    pass
                elif matrix[y][1+x][1] == "t":
                    return 1
        return 0

    def in_vision():
        global visability_list
        global game_matrix
        global player_pos
        global sec_list
        #sight_range = 3
        for i in range(0,4):
            ydif = sec_list[i][0][sec_list[i][1]][0] - player_pos[0]
            xdif = sec_list[i][0][sec_list[i][1]][1] - player_pos[1]
            #distance = ((sec_list[i][0][sec_list[i][1]][0] - player_pos[0])**2 + (sec_list[i][0][sec_list[i][1]][1] - player_pos[1]) **2)**0.5
            if ydif == 0 and xdif == 0:
                visability_list[i] = True
            elif abs(ydif) <= 3 and ydif < 0 and xdif == 0:
                if ydif == -1:
                    visability_list[i] = True
                elif ydif == -2:
                    if game_matrix[player_pos[0]-1][player_pos[1]] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        #renpy.notify("in vision")
                        visability_list[i] = True
                elif ydif == -3:
                    if game_matrix[player_pos[0]-1][player_pos[1]] == 0 or game_matrix[player_pos[0]-2][player_pos[1]] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True

            elif abs(ydif) <= 3 and ydif > 0 and xdif == 0:
                if ydif == 1:
                    visability_list[i] = True
                elif ydif == 2:
                    if game_matrix[player_pos[0]+1][player_pos[1]] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True
                elif ydif == 3:
                    if game_matrix[player_pos[0]+1][player_pos[1]] == 0 or game_matrix[player_pos[0]+2][player_pos[1]] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True    
            
            elif abs(xdif) <= 3 and xdif > 0 and ydif == 0:
                if xdif == 1:
                    visability_list[i] = True
                elif xdif == 2:
                    if game_matrix[player_pos[0]][player_pos[1]+1] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True
                elif xdif == 3:
                    if game_matrix[player_pos[0]][player_pos[1]+1] == 0 or game_matrix[player_pos[0]][player_pos[1]+2] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True 

            elif abs(xdif) <= 3 and xdif < 0 and ydif == 0:
                if xdif == -1:
                    visability_list[i] = True
                elif xdif == -2:
                    if game_matrix[player_pos[0]][player_pos[1]-1] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True
                elif xdif == -3:
                    if game_matrix[player_pos[0]][player_pos[1]-1] == 0 or game_matrix[player_pos[0]][player_pos[1]-2] == 0:
                        visability_list[i] = False
                        continue
                    else:
                        visability_list[i] = True
            else:
                visability_list[i] = False
    
    def in_vision_personal():
        global visability_list1
        global game_matrix
        global player_pos
        global tailgate_list
        #sight_range = 3
        for i in range(0,4):
            ydif = tailgate_list[i][0][tailgate_list[i][1]][0] - player_pos[0]
            xdif = tailgate_list[i][0][tailgate_list[i][1]][1] - player_pos[1]
            #distance = ((sec_list[i][0][sec_list[i][1]][0] - player_pos[0])**2 + (sec_list[i][0][sec_list[i][1]][1] - player_pos[1]) **2)**0.5
            if ydif == 0 and xdif == 0:
                visability_list1[i] = True
            elif abs(ydif) <= 3 and ydif < 0 and xdif == 0:
                if ydif == -1:
                    visability_list1[i] = True
                elif ydif == -2:
                    if game_matrix[player_pos[0]-1][player_pos[1]] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True
                elif ydif == -3:
                    if game_matrix[player_pos[0]-1][player_pos[1]] == 0 or game_matrix[player_pos[0]-2][player_pos[1]] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True

            elif abs(ydif) <= 3 and ydif > 0 and xdif == 0:
                if ydif == 1:
                    visability_list1[i] = True
                elif ydif == 2:
                    if game_matrix[player_pos[0]+1][player_pos[1]] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True
                elif ydif == 3:
                    if game_matrix[player_pos[0]+1][player_pos[1]] == 0 or game_matrix[player_pos[0]+2][player_pos[1]] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True    
            
            elif abs(xdif) <= 3 and xdif > 0 and ydif == 0:
                if xdif == 1:
                    visability_list1[i] = True
                elif xdif == 2:
                    if game_matrix[player_pos[0]][player_pos[1]+1] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True
                elif xdif == 3:
                    if game_matrix[player_pos[0]][player_pos[1]+1] == 0 or game_matrix[player_pos[0]][player_pos[1]+2] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True 

            elif abs(xdif) <= 3 and xdif < 0 and ydif == 0:
                if xdif == -1:
                    visability_list1[i] = True
                elif xdif == -2:
                    if game_matrix[player_pos[0]][player_pos[1]-1] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True
                elif xdif == -3:
                    if game_matrix[player_pos[0]][player_pos[1]-1] == 0 or game_matrix[player_pos[0]][player_pos[1]-2] == 0:
                        visability_list1[i] = False
                        continue
                    else:
                        visability_list1[i] = True
            else:
                visability_list1[i] = False

    def in_vision_door():
        global visability_list2
        global game_matrix
        global player_pos
        global sec_list
        if player_pos == [13,5] or player_pos == [12,5] or player_pos == [11,5] or player_pos == [10,5] or player_pos == [9,5]:
            visability_list2[0] = True
        else:
            visability_list2[0] = False
        
        if player_pos == [2,5] or player_pos == [3,5] or player_pos == [4,5] or player_pos == [5,5]:
            visability_list2[1] = True
        else:
            visability_list2[1] = False
        

    def reset():
        global detected
        global sec_list
        global tailgate_list
        global game_matrix
        global sec_index_1 
        global sec_index_2 
        global sec_index_3 
        global sec_index_4 
        global orange_index
        global green_index 
        global purple_index 
        global blue_index 
        global player_pos
        global valid_inputs
        global optional_flag 
        global bobs_flag 
        global courtyard_flag
        global door_timer 
        global door_state
        global door_timer1 
        global door_state1
        global a 
        global b 
        global visability_list
        global visability_list1
        global visability_list2
        detected = False
        visability_list = [False,False,False,False]
        visability_list1 = [False,False,False,False]
        visability_list2 = [False,False]
        door_timer = 0
        door_state = 0
        door_timer1 = 0
        door_state1 = 0
        operation_table_seen = False
        hospital_bed_seen = False
        skull_anatomy_seen = False
        optional_flag = True
        bobs_flag = True
        courtyard_flag = True
        if fire_alarm:
            a = "f"
            b = "t"
            player_pos = [1,1]
            valid_inputs = [1,0,0,1,0]
        else:
            a = "t"
            b = "f"
            player_pos = [14,1]
            valid_inputs = [1,1,0,0,0]
        game_matrix = [
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

        for i in range(0,4):
            if i == 0:
                sec_list[i][1] = 11
            else:
                sec_list[i][1] = 0
        for i in range(0,4):
            tailgate_list[i][1] = 0
            if i == 3:
                tailgate_list[i][1] = 8
            if i == 2:
                tailgate_list[i][1] = 10
            if i == 1:
                tailgate_list[i][1] = 5
            if i == 0:
                tailgate_list[i][1] = 2
        sec_index_1 = 11
        sec_index_2 = 0
        sec_index_3 = 0
        sec_index_4 = 0
        green_index = 0
        purple_index = 0
        blue_index = 8
