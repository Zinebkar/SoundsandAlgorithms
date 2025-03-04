# Mind Hackers: Whispers in the wires - Project 2024 SECont
# This file covers the mini game encountered in level 3 where the player has to catch a butterfly

init python:
    # ################################# Butterfly class: ##################################
    # Class handles the butterfly (and bee) logic and visuals
    class Butterfly():
        def __init__(self, is_bee):
            from random import randint

            if is_bee:
                self.visual = Movie(size=(150, 150), play="videos/wasp.webm", loop=True, mask="videos/wasp_mask.webm", framedrop=False)
            else:
                sizee = randint(80, 140)
                self.visual = Movie(size=(sizee, sizee), play="videos/butterfly.webm", loop=True, mask="videos/butterfly_mask.webm", framedrop=False)
            self.OFFSET = (83, 83)
            self.SPEED = (160, 500, 200) # Idle speed, max speed, bee speed
            self.TARGET_TIME = (1.0, 5.0) # Time before butterfly selects new target (range)
            self.FLEE_DISTANCE = 500.0

            self.pos = (randint(200.0, 1720), randint(200.0, 880))
            self.target_pos = (0, 0)
            self.target_time_c = 0.0
            self.rot_degree_aim = 0.0 # aim for the rotation (for lerping)
            self.rot_degree = 0.0
            self.is_bee = is_bee
            self.is_dead = False
        
        # Logic for butterfly
        def movement(self, dtime, cursor_pos, field_width, field_height):
            from random import randint
            from random import uniform
            import math
            global mouse_index

            # Get new target for random movement
            self.target_time_c -= dtime
            if self.target_time_c < 0:
                self.target_time_c = uniform(self.TARGET_TIME[0], self.TARGET_TIME[1])
                self.target_pos = (randint(0, field_width), randint(0, field_height))

            if self.is_bee:
                speed_c = self.SPEED[2]
                # Calculate direction
                if mouse_index != 1:
                    direction = (cursor_pos[0] - self.pos[0], cursor_pos[1] - self.pos[1])
                    dir_lenght = vec2_distance(cursor_pos, self.pos)
                else:
                    direction = (-100 - self.pos[0], -100 - self.pos[1])
                    dir_lenght = vec2_distance((-100, -100), self.pos)
                    
                # Bee catches the player
                if dir_lenght < 1 and mouse_index != 1:
                    mouse_index = 1
                    renpy.config.mouse_displayable = MouseDisplayable("gui/mouse/cursor_default_red.png", 0, 0)
                    renpy.sound.play("audio/sfx/bee_stung.wav")
                    renpy.restart_interaction()
            
            # Let butterfly flee from cursor
            elif vec2_distance(self.pos, cursor_pos) < self.FLEE_DISTANCE:
                speed_c = self.SPEED[1]
                # Calculate direction
                direction = (self.pos[0] - cursor_pos[0], self.pos[1] - cursor_pos[1])
                dir_lenght = vec2_distance(cursor_pos, self.pos)
            else:
                speed_c = self.SPEED[0]
                # Calculate direction
                direction = (self.target_pos[0] - self.pos[0], self.target_pos[1] - self.pos[1])
                dir_lenght = vec2_distance(self.target_pos, self.pos)

            if dir_lenght > 0:
                direction_n = (direction[0] / dir_lenght, direction[1] / dir_lenght) # normalized direction
            else:
                direction_n = (0, 0)
            
            # Update position
            delta_pos = (direction_n[0] * dtime * speed_c, direction_n[1] * dtime * speed_c)
            self.pos = (self.pos[0] + delta_pos[0], self.pos[1] + delta_pos[1])

            # Calculate rotation
            if delta_pos[1] >= 0:
                self.rot_degree_aim = math.degrees(math.acos(direction_n[0])) + 90
            else:
                self.rot_degree_aim = 360 - math.degrees(math.acos(direction_n[0])) + 90
            
            self.rot_degree = lerp_degrees(self.rot_degree, self.rot_degree_aim, dtime * 4)
        
        def die(self):
            if not self.is_dead:
                self.is_dead = True
                self.visual = Solid("#0000")
                self.SPEED = (0, 0, 0)
                renpy.sound.play("audio/sfx/butterfly_caught.wav")
                return True
            else:
                return False

    # ################################ Displayable class: #################################
    # Class handles user input and the renpy render pipeline
    class ButterflyDisplayable(renpy.Displayable):

        def __init__(self):
            renpy.Displayable.__init__(self)
            self.FIELD_WIDTH = 1920
            self.FIELD_HEIGHT = 1080

            self.butterf_count = 5
            self.butterf_caught = 0
            
            self.butterflies = [Butterfly(False) for i in range(self.butterf_count - 1)]
            self.butterflies.append(Butterfly(True))

            self.cursor_pos = (0.0, 0.0)

            # The time of the past render-frame.
            self.oldst = None
    

        # Must return all child displayables
        def visit(self):
            return [self.butterflies[i].visual for i in range(self.butterf_count)]


        # Function render is being called by the call screen in renpy automatically
        # Function renders the displayables
        def render(self, width, height, st, at):
            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Move and display each butterfly
            for butterfly in self.butterflies:
                butterfly.movement(dtime, self.cursor_pos, self.FIELD_WIDTH, self.FIELD_HEIGHT)
                t = Transform(child=butterfly.visual, rotate=butterfly.rot_degree)
                bf = renpy.render(t, width, height, st, at)
                r.blit(bf, (int(butterfly.pos[0] - butterfly.OFFSET[0]), int(butterfly.pos[1] - butterfly.OFFSET[1])))

            # re-render ASAP, so we can show the next frame (has to be here)
            renpy.redraw(self, 0)

            # Return the Render object
            return r
        

        # Handles events; called by renpy automatically
        def event(self, ev, x, y, st):
            import pygame

            self.cursor_pos = (x, y)

            # Let players click on the butterflies to catch em
            if not (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1):
                raise renpy.IgnoreEvent()
            else:
                for i in range(self.butterf_count):
                    d = vec2_distance(self.cursor_pos, self.butterflies[i].pos)
                    if d < 100 and self.butterflies[i].is_bee == False:
                        if self.butterflies[i].die() == True:
                            self.butterf_caught += 1
                            if self.butterf_caught == self.butterf_count - 1:
                                renpy.jump("butterfly_minigame_completed")
                                renpy.restart_interaction()

# ################################ Mini game screen: ##################################
transform arrow2_pos:
    zoom 0.35
    xalign 0.02
    yalign 0.02

screen butterfly_mini_game():
    zorder 2
    modal True

    image "images/backgrounds/Bob Office/bg courtyard.png"
    add Solid("#0004")

    default minigame = ButterflyDisplayable()


    add minigame

    # Return arrow
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow2_pos
        xpos 50
        ypos 0
        xsize 500
        ysize 300
        action Jump("butterfly_minigame_canceled")

# ############################### Mini game dialogue: #################################
label butterfly_minigame_canceled:
    scene bg courtyard
    hide screen butterfly_mini_game
    with dissolve
    "There are certainly more important matters right now."
    "You decide to go back into the building."
    play music security_music volume loudness
    jump security_minigame_start

label butterfly_minigame_completed:
    scene bg courtyard
    hide screen butterfly_mini_game
    with dissolve
    "A sense of connection with nature overwhelms you as you release the butterflies again and their shimmering wings sparkle in the sunlight."
    "..."
    "After a moment of inner peace, you remember, that there are more important things at hand."
    "You decide to go back into the building."
    play music security_music volume loudness
    jump security_minigame_start


# ################################ Helper functions: ##################################
init python:
    # lets value1 approach value2 by factor[0, 1]
    def lerp(value1, value2, factor):
        new_value1 = value1 + ((value2 - value1) * factor)
        return new_value1
    
    # Lerps in modulus 360
    def lerp_degrees(value1, value2, factor):
        value1 = value1 % 360
        value2 = value2 % 360
        new_value1 = 0
        delta = (value2 - value1) % 360

        if delta <= 180:
            new_value1 = value1 + (delta * factor)
        else:
            new_value1 = value1 + ((-360 + delta) * factor)

        return new_value1 % 360

    def vec2_lenght(vector):
        import math
        return math.sqrt(vector[0]**2 + vector[1]**2)

    def vec2_distance(vector1, vector2):
        import math
        return math.sqrt((vector1[0] - vector2[0])**2 + (vector1[1] - vector2[1])**2)
