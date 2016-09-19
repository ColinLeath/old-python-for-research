#! /usr/bin/env python


""" imgv.py 
    Description: Image viewer written in Python using Pygame
    Version: 1.2
    Author: Ryan Kulla (gt3)
    Site: http://www.spankmonkies.com/imgv.html
    Email: ryan@spankmonkies.com """


import imghdr
import urllib
from StringIO import StringIO
from sys import argv, platform
from stat import S_IMODE, ST_MODE, ST_MTIME, ST_ATIME, ST_CTIME,\
                 ST_UID, ST_GID
from time import ctime, time
if platform != 'win32':
    from pwd import getpwuid
    from grp import getgrgid
from os import chdir, environ, getcwd
import os.path
from string import join, digits, replace, split, find
# use windib when the default is directx:
if platform == 'win32': 
    environ['SDL_VIDEODRIVER'] = 'windib'
import pygame, pygame.image, pygame.surface, pygame.transform,\
        pygame.font, pygame.version, pygame.cursors, pygame.draw
from pygame.locals import *
from glob import glob
from random import shuffle


def imgv_button(screen, msg, x, y, where):
    font = pygame.font.Font(FONT_NAME, 14)
    ren = font.render(msg, 1, SILVER)
    ren_rect = ren.get_rect().inflate(20, 10)
    if where == "topleft":
        ren_rect.topleft = screen.get_rect().topleft
        ren_rect[0] = x
        ren_rect[1] = y
    if where == "midtop":
        ren_rect.midtop = screen.get_rect().midtop
        ren_rect[1] = y
    if where == "topright":
        ren_rect.topright = screen.get_rect().topright
        ren_rect[0] = ren_rect[0] - x
        ren_rect[1] = y
    if where == None:
        ren_rect[0] = x
        ren_rect[1] = ren_rect[1] + y
    screen.fill(BLUE, ren_rect)
    screen.blit(ren, ren_rect.inflate(-20, -10))
    pygame.display.update(ren_rect)
    return ren_rect


def command_file_master(screen, file_names, msg, down, font_size,\
button_op, disable_right_click, again):
    screen_pause = place = marker = 0
    x = []
    esc_rect = edit_rect = back_rect = forward_rect = junk_rect()
    if len(file_names) < 1:
        my_string = input_box(screen, "You must create a play list. Enter play list name: ")
        if my_string != None:
            if (len(my_string) > 0) and my_string != "\n":
                return (file_names, None, None, my_string)
    while 1:
        event = pygame.event.poll()
        if screen_pause == 1:
            while 1:
                event = pygame.event.wait()
                cursor = pygame.mouse.get_pos()
                check_quit(event)
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return (None, None, None, None)
                if left_click(event):
                    if esc_rect.collidepoint(cursor):
                        return (None, None, None, None)
                if left_click(event):
                    for item in x:
                        if item[0].collidepoint(cursor):
                            if pygame.mouse.get_pressed()[0] and\
                            (pygame.key.get_pressed()[K_LCTRL] or\
                            pygame.key.get_pressed()[K_RCTRL]):
                                return (file_names, item[1], "deleteit", None)
                            if again == "do again":
                                return (file_names, item[1], "do again", None)
                            return (file_names, item[1], x, None)
                if right_click(event):
                    if not disable_right_click:
                        for item in x:
                            if item[0].collidepoint(cursor):
                                if not os.path.isfile(DATA_DIR + item[1]):
                                    if edit_rect != junk_rect():
                                        paint_screen(screen, edit_rect)
                                    edit_rect = show_message(screen,\
                                    "%s doesn't exist in %s" % (item[1],\
                                    DATA_DIR), "top", 9)
                                else:
                                    return (None, item[1], "rclicked", None)
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if not place >= len(file_names):
                        screen_pause = 0
                        marker = 0
                        x = []
                        break
                if left_click(event):
                    if forward_rect.collidepoint(cursor):
                        if not place >= len(file_names):
                            screen_pause = 0
                            marker = 0
                            x = []
                            break
                if event.type == KEYDOWN and event.key == K_BACKSPACE:
                    if ((place - marker) > 0):
                        screen.fill(0)
                        pygame.display.flip()
                        screen_pause = 0
                        place = place - (MAX_SCREEN_FILES + marker)
                        marker = 0
                        x = []
                        break
                if left_click(event):
                    if back_rect.collidepoint(cursor):
                        if ((place - marker) > 0):
                            screen.fill(0)
                            pygame.display.flip()
                            screen_pause = 0
                            place = place - (MAX_SCREEN_FILES + marker)
                            marker = 0
                            x = []
                            break
                if left_click(event):
                    if create_rect.collidepoint(cursor):
                        my_string = input_box(screen, "Enter name of list: ")
                        if my_string != None:
                            if (len(my_string) > 0) and my_string != "\n":
                                return (file_names, None, x, my_string)
        (file_names, x, screen_pause, place, marker, create_rect,\
        forward_rect, back_rect, esc_rect) = file_master(screen, file_names,\
        place, marker, x, msg, down, font_size, button_op)
        pygame.time.delay(5)


def file_master(screen, file_names, place, marker, x, msg, down, font_size,\
button_op):
    paint_screen(screen)
    show_message(screen, msg, down, font_size)
    font = pygame.font.Font(FONT_NAME, 9)
    font_height = font.size(file_names[0])[1]
    screen_height = screen.get_height()
    name_max = 16 
    max_file_width = 116
    line = 65 # leave room at top of screen for other stuff
    col = 30
    count = 0
    create_rect = back_rect = forward_rect = esc_rect = junk_rect()
    esc = font.render("Escape", 1, WHITE)
    esc_rect = esc.get_rect()
    esc_rect[0] = 5
    screen.blit(esc, esc_rect)
    pygame.display.update(esc_rect)
    if button_op:
        create_rect = imgv_button(screen, "Create New List", 0, 18, "midtop")
    for name in file_names[place:]:
        count = count + 1
        place = place + 1
        marker = marker + 1
        if count >= MAX_SCREEN_FILES or place >= len(file_names):
            ren_name = os.path.basename(name)
            if len(ren_name) > name_max:
                ren_name = ren_name[:name_max] + '~'
            ren = font.render(ren_name, 1, SILVER, BLACK)
            if (place + 1) < len(file_names):
                forward_rect = imgv_button(screen, "Forward", 10, 18,\
                "topright")
            if (((place + 1) - MAX_SCREEN_FILES) > 1):
                back_rect = imgv_button(screen, "Back", 10, 18, "topleft")
            ren_rect = ren.get_rect()
            ren_rect[0] = col
            ren_rect[1] = line
            x.append((ren_rect, name))
            screen.blit(ren, ren_rect)
            pygame.display.update(ren_rect)
            return (file_names, x, 1, place, marker, create_rect,\
            forward_rect, back_rect, esc_rect)
        ren_name = os.path.basename(name)
        if len(ren_name) > name_max:
            ren_name = ren_name[:name_max] + '~'
        ren = font.render(ren_name, 1, SILVER, BLACK)
        ren_rect = ren.get_rect()
        ren_rect[0] = col
        ren_rect[1] = line
        x.append((ren_rect, name))
        screen.blit(ren, ren_rect)
        line = line + 12
        if (line + font_height) >= (screen_height - 15):
            line = 65
            col = col + max_file_width
        pygame.display.update(ren_rect)
    return (file_names, x, 0, place, marker, create_rect, forward_rect,\
    back_rect, esc_rect)


def paint_screen(screen, *rect):
    if not rect:
        screen.fill(IMGV_COLOR)
        pygame.display.flip()
    else:
        screen.fill(IMGV_COLOR, rect)
        pygame.display.update(rect)


def check_quit(event):
    "quit the program if the close window icon or the 'q' key is hit"
    if event.type == KEYDOWN and event.key == K_q or event.type == QUIT:
        wait_cursor()
        clean_screen()
        raise SystemExit


def hit_key(event, key):
    if event.type == KEYDOWN and event.key == key:
        return 1
    return 0


def left_click(event):
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
        return 1
    return 0


def middle_click(event):
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
        return 1
    return 0 


def right_click(event):
    if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
        return 1
    return 0


def junk_rect():
    return (Rect(-1, -1, -1, -1))


def command_add_to_play_list(screen, filename):
    paint_screen(screen)
    normal_cursor()
    small_font = pygame.font.Font(FONT_NAME, 10)
    f = open(IMGV_PLAYLISTS)
    file_names = f.readlines()
    if len(file_names) == 0:
        return (file_names, None, None, None, None)
    f.close()
    file_names.sort()
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    (list_names, play_list_name, x, my_string) = command_file_master(screen,\
    file_names, "Click list name to add to list", 25, 13, 0, 1, 0)
    if (list_names == None):
        return
    play_list = DATA_DIR + play_list_name
    f = open(play_list, 'a')
    if os.sep not in filename:
        filename = os.getcwd() + os.sep + filename + "\n"
    f.write(filename)
    f.close()
    normal_cursor


def command_play_list_options(screen, file):
    paint_screen(screen)
    old_file = file
    pygame.display.set_caption("Esc to abort")
    (file, msg) = play_list_options(screen, file)
    if (msg != None and file != "rclicked" and file != "deleteit"):
        play_list_options_msg(screen, msg)
    if (file == "rclicked"):
        edit_play_list(screen, msg)
        file = old_file
    if (file == "deleteit"):
        delete_play_list(msg)
        file = old_file
    pygame.display.set_caption(TITLE)
    num_imgs = len(files)
    new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    my_update_screen(new_img, screen, rect, file, num_imgs)
    normal_cursor()
    return (new_img, new_img, new_img, file, rect, num_imgs)


def play_list_options(screen, file):
    global files
    global PLAY_LIST_NAME
    normal_cursor()
    f = open(IMGV_PLAYLISTS)
    file_names = f.readlines()
    f.close()
    file_names.sort()
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    (list_names, play_list_name, x, my_string) = command_file_master(screen,\
    file_names, "There are %d Play Lists. (Left-click list name to use. Right-click to edit. Ctrl+Left-click to delete)" % len(file_names), 47, 11, 1, 0, 0)
    wait_cursor()
    if x == "deleteit":
        return ("deleteit", play_list_name)
    if x == "rclicked":
        return ("rclicked", play_list_name)
    if my_string != None and my_string != "\n":
        my_string = str(join(my_string, ''))
        new_list = DATA_DIR + my_string
        f = open(IMGV_PLAYLISTS, 'a')
        new_list_name = os.path.basename(new_list + "\n")
        if new_list_name != "\n": # no blank lists (user just hit RETURN)
            f.write(new_list_name)
            f.close()
            open(new_list, 'w')
        return (file, None)
    if (play_list_name == None):
        return (file, None)
    play_list = DATA_DIR + play_list_name
    try:
        f = open(play_list)
        tmp_files = f.readlines()
        if len(tmp_files) > 0:
            files = tmp_files
            for count in range(len(files)):
                files[count] = replace(files[count], "\n", "")
            f.close()
            PLAY_LIST_NAME = os.path.basename(play_list)
            return (0, None)
        return (file, "\"%s\" is empty or not in %s" % (os.path.basename(\
        play_list), DATA_DIR))
    except IOError:
        return (file, "\"%s\" is empty or not in %s" % (os.path.basename(\
        play_list), DATA_DIR))


def edit_play_list(screen, play_list_name):
    paint_screen(screen)
    keep_going = 1
    play_list = DATA_DIR + play_list_name
    f = open(play_list)
    file_names = f.readlines()
    f.close()
    if len(file_names) < 1:
        play_list_options_msg(screen, "Can't edit %s, it is empty" %\
        play_list)
        keep_going = 0
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    normal_cursor()
    if keep_going:
        (list_names, play_list_item, x, my_string) = command_file_master(\
        screen, file_names, "Click item to delete it from play list",\
        47, 13, 0, 1, "do again")
        file_names = delete_item(screen, play_list_item, play_list)
        if x == "do again":
            while 1:
                if len(file_names) < 1:
                    break
                (list_names, play_list_item, x, my_string) =\
                command_file_master(screen, file_names,\
                "Click to delete another item from play list",\
                47, 13, 0, 1, "do again")
                file_names = delete_item(screen, play_list_item, play_list)
                if x != "do again":
                    break

def delete_item(screen, play_list_item, play_list):
    f = open(play_list)
    file_names = f.readlines()
    f.close()
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    # rewrite the list
    f = open(play_list, 'w+')
    for line in file_names:
        if line == play_list_item:
            continue # don't rewrite this item
        f.write(line + "\n")
    f.close()
    # get changed items
    f = open(play_list)
    file_names = f.readlines()
    f.close()
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    return file_names


def delete_play_list(play_list):
    if os.path.isfile(DATA_DIR + play_list):
        del_file = DATA_DIR + play_list
        os.remove(del_file)
    f = open(IMGV_PLAYLISTS)
    file_names = f.readlines()
    f.close()
    for count in range(len(file_names)):
        file_names[count] = replace(file_names[count], "\n", "")
    f = open(IMGV_PLAYLISTS, 'w+')
    for line in file_names:
        if line == play_list:
            continue # don't rewrite this item
        f.write(line + "\n")
    f.close()


def play_list_options_msg(screen, msg):
    paint_screen(screen)
    show_message(screen, msg, 100, 10)
    normal_cursor()
    while 1:
        event = pygame.event.wait()
        check_quit(event)
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            wait_cursor()
            break
            

def show_message(screen, msg, down_value, font_size):
    "write a message centered anywhere on the screen"
    font = pygame.font.Font(FONT_NAME, font_size) 
    ren = font.render(msg, 1, WHITE, BLACK)
    ren_rect = ren.get_rect()
    if down_value == "bottom":
        ren_rect.midbottom = screen.get_rect().midbottom
    elif down_value == "top":
        ren_rect.midtop = screen.get_rect().midtop
    else:
        ren_rect.centerx = screen.get_rect().centerx
        ren_rect[1] = down_value
    screen.blit(ren, ren_rect)
    pygame.display.update(ren_rect)
    return (ren_rect)


def input_box(screen, msg):
    font = pygame.font.Font(FONT_NAME, 12)
    input_msg = font.render(msg, 1, WHITE, BLACK)
    input_msg_rect = input_msg.get_rect()
    input_msg_width = input_msg.get_width()
    input_msg_rect.midtop = screen.get_rect().midtop
    screen.blit(input_msg, input_msg_rect)
    pygame.display.update(input_msg_rect)
    my_string = []
    dirty_rects = []
    char_space = 0
    while 1:
        event = pygame.event.wait()
        if event.type == QUIT:
            raise SystemExit
        if event.type == KEYDOWN:
            if event.unicode.isalnum():
                my_string.append(event.unicode)
                ren = font.render(event.unicode, 1, SILVER, BLACK)
                ren_rect = ren.get_rect()
                ren_rect.midtop = screen.get_rect().midtop
                ren_rect[0] = ren_rect[0] + (char_space + (input_msg_width/2))
                dirty_rects.append(ren_rect)
                screen.blit(ren, ren_rect)
                pygame.display.update(ren_rect)
                char_space = char_space + ren.get_width()
        if hit_key(event, K_ESCAPE):
            for rect in dirty_rects:
                paint_screen(screen, rect)
            paint_screen(screen, input_msg_rect)
            return None
        if hit_key(event, K_BACKSPACE):
            "erase whatever text was inputed"
            my_string = []
            for rect in dirty_rects:
                paint_screen(screen, rect)
            char_space = ren.get_width()
        if hit_key(event, K_RETURN) or hit_key(event, K_KP_ENTER):
            for rect in dirty_rects:
                paint_screen(screen, rect)
            paint_screen(screen, input_msg_rect)
            return my_string


def shorten_list(list_names):
    list_names_shortened = []
    for i in range(len(list_names)):
        if i >= MAX_PLAY_LISTS:
            break
        list_names_shortened.append(list_names[i])
    return list_names_shortened


def command_thumbs(screen, new_img, file):
    paint_screen(screen)
    (new_img, new_img, new_img, file) = thumbs_engine(screen, new_img, file)
    rect = get_center(screen, new_img)
    my_update_screen(new_img, screen, rect, file, len(files))
    normal_cursor()
    return (new_img, new_img, new_img, file, rect)


def thumbs_engine(screen, new_img, file):
    screen_pause = 0
    SPACER = 10
    x = []
    place = 0
    marker = 0
    (i, j) = (SPACER, SPACER)
    pygame.event.set_blocked(MOUSEMOTION)
    while 1:
        event = pygame.event.poll()
        check_quit(event)
        if hit_key(event, K_ESCAPE):
            pygame.display.set_caption(TITLE)
            break
        if screen_pause == 1:
            normal_cursor()
            pygame.display.set_caption(TITLE + " Click a thumb, Space for next page, Backspace for last page")
            while 1:
                event = pygame.event.wait()
                cursor = pygame.mouse.get_pos()
                if left_click(event):
                    for item in x:
                        if item[0].collidepoint(cursor):
                            wait_cursor()
                            pygame.display.set_caption(item[1])
                            new_img = load_img(item[1])
                            file = files.index(item[1])
                            return (new_img, new_img, new_img, file)
                check_quit(event)
                if hit_key(event, K_SPACE):
                    if not place >= len(files):
                        paint_screen(screen)
                        screen_pause = 0
                        marker = 0
                        x = [] # reset for page
                        break
                if hit_key(event, K_BACKSPACE):
                    if ((place - marker) > 0):
                        paint_screen(screen)
                        screen_pause = 0
                        place = place - (marker * 2)
                        marker = 0
                        x = []
                        break
        (x, i, j, place, screen_pause, marker) = show_thumbs(screen,\
        SPACER, x, i, j, place, marker)
        pygame.time.delay(5)
    return (new_img, new_img, new_img, file)


def show_thumbs(screen, SPACER, x, i, j, place, marker):
    wait_cursor()
    if place < len(files):
        img_name = files[place]
        load_msg = "(Esc to abort) Loading Thumbnails... %s: %d/%d" % \
        (img_name, place, len(files))
        pygame.display.set_caption(load_msg)
        img = pygame.image.load(img_name)
        (w, h) = split(THUMB_VAL, 'x')
        img = pygame.transform.scale(img, (int(w), int(h)))
        if (i + img.get_width()) >= screen.get_width():
            i = SPACER
            j = j + (img.get_height() + SPACER)
        if (j + img.get_height()) >= screen.get_height():
            i, j = SPACER, SPACER
            return (x, i, j, place, 1, marker)
        img_rect = img.get_rect()
        img_rect[0] = i
        img_rect[1] = j
        x.append((img_rect, img_name))
        screen.blit(img, (i, j))
        pygame.display.update(img_rect)
        i = i + (img.get_width() + SPACER)
        place = place + 1
        marker = marker + 1
    if place >= len(files):
        return (x, i, j, place, 1, marker)
    return (x, i, j, place, 0, marker)


def command_four(screen, file, new_img):
    paint_screen(screen)
    (file, new_img) = four(screen, file, new_img)
    pygame.display.set_caption(TITLE)
    rect = get_center(screen, new_img)
    num_imgs = len(files)
    my_update_screen(new_img, screen, rect, file, num_imgs)
    pygame.event.set_blocked(MOUSEMOTION)
    return (file, new_img, new_img, new_img, rect)


def four(screen, file, new_img):
    old_file = file
    def_rect = new_img.get_rect()
    (img_one_rect, img_two_rect, img_three_rect, img_four_rect) = (0, 0, 0, 0)
    (img_one_name, img_two_name, img_three_name, img_four_name) = (0, 0, 0, 0)
    (show_img_one, show_img_two, show_img_three, show_img_four) = (0, 0, 0, 0)

    rect = junk_rect()
    (file, img_one_rect, img_one_name, img_one_file) = square_one(screen,\
    file, def_rect)
    (file, img_two_rect, img_two_name, img_two_file) = square_two(screen,\
    file, def_rect)
    (file, img_three_rect, img_three_name, img_three_file) =\
    square_three(screen, file, def_rect)
    (file, img_four_rect, img_four_name, img_four_file) =\
    square_four(screen, file, def_rect)

    pygame.event.set_allowed(MOUSEMOTION)
    while 1:
        flag = 0
        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()
        if hit_key(event, K_ESCAPE):
            file = old_file
            break
        check_quit(event)
        if hit_key(event, K_SPACE):
            paint_screen(screen)
            flag = 1
        if hit_key(event, K_BACKSPACE):
            paint_screen(screen)
            file = file - 8
            flag = 1
        if flag == 1:
            (file, img_one_rect, img_one_name, img_one_file) =\
            square_one(screen, file, def_rect)
        if flag == 1:
            (file, img_two_rect, img_two_name, img_two_file) =\
            square_two(screen, file, def_rect)
        if flag == 1:
            (file, img_three_rect, img_three_name, img_three_file) =\
            square_three(screen, file, def_rect)
        if flag == 1:
            (file, img_four_rect, img_four_name, img_four_file) =\
            square_four(screen, file, def_rect)
        (show_img_one, show_img_two, show_img_three, show_img_four, rect) =\
        hover_square(screen, show_img_one, show_img_two, show_img_three,\
        show_img_four, img_one_rect, img_two_rect, img_three_rect,\
        img_four_rect, img_one_name, img_two_name, img_three_name,\
        img_four_name, img_one_file, img_two_file, img_three_file,\
        img_four_file, rect)
        if left_click(event):
            if img_one_rect.collidepoint(cursor):
                wait_cursor()
                new_img = load_img(files[img_one_file])
                return (img_one_file, new_img)
            if img_two_rect.collidepoint(cursor):
                wait_cursor()
                new_img = load_img(files[img_two_file])
                return (img_two_file, new_img)
            if img_three_rect.collidepoint(cursor):
                wait_cursor()
                new_img = load_img(files[img_three_file])
                return (img_three_file, new_img)
            if img_four_rect.collidepoint(cursor):
                wait_cursor()
                new_img = load_img(files[img_four_file])
                return (img_four_file, new_img)
    return (file, new_img)


def square_one(screen, file, def_rect):
    wait_cursor()
    draw_lines(screen)
    if file >= len(files) or file <= 0:
        file = 0
    img_one_name = files[file]
    img_one_file = file
    pygame.display.set_caption("%s %s" % (TITLE, img_one_name))
    img_one = load_img(img_one_name)
    file = file + 1
    img_one = adust_img_size(img_one, screen.get_width(), \
    screen.get_height())
    img_one_rect = img_one.get_rect()
    screen.blit(img_one, img_one_rect)
    pygame.display.update(img_one_rect)
    draw_lines(screen)
    normal_cursor()
    return (file, img_one_rect, img_one_name, img_one_file)


def square_two(screen, file, def_rect):
    wait_cursor()
    draw_lines(screen)
    if file >= len(files) or file <= 0:
        file = 0
    img_two_name = files[file]
    img_two_file = file
    pygame.display.set_caption("%s %s" % (TITLE, img_two_name))
    img_two = load_img(img_two_name)
    file = file + 1
    img_two = adust_img_size(img_two, screen.get_width(), \
          screen.get_height())
    img_two_rect = img_two.get_rect()
    img_two_rect[0] = (screen.get_width() / 2)
    screen.blit(img_two, img_two_rect)
    pygame.display.update(img_two_rect)
    draw_lines(screen)
    normal_cursor()
    return (file, img_two_rect, img_two_name, img_two_file)


def square_three(screen, file, def_rect):
    wait_cursor()
    draw_lines(screen)
    if file >= len(files) or file <= 0:
        file = 0
    img_three_name = files[file]
    img_three_file = file
    pygame.display.set_caption("%s %s" % (TITLE, img_three_name))
    img_three = load_img(img_three_name)
    file = file + 1
    img_three = adust_img_size(img_three, screen.get_width(), \
          screen.get_height())
    img_three_rect = img_three.get_rect()
    img_three_rect[1] = (screen.get_height() / 2)
    screen.blit(img_three, img_three_rect)
    pygame.display.update(img_three_rect)
    draw_lines(screen)
    normal_cursor()
    return (file, img_three_rect, img_three_name, img_three_file)


def square_four(screen, file, def_rect):
    wait_cursor()
    draw_lines(screen)
    if file >= len(files) or file <= 0:
        file = 0
    img_four_name = files[file]
    img_four_file = file
    pygame.display.set_caption("%s %s" % (TITLE, img_four_name))
    img_four = load_img(img_four_name)
    file = file + 1
    img_four = adust_img_size(img_four, screen.get_width(), \
          screen.get_height())
    img_four_rect = img_four.get_rect()
    img_four_rect[0] = (screen.get_width() / 2)
    img_four_rect[1] = (screen.get_height() / 2)
    screen.blit(img_four, img_four_rect)
    pygame.display.update(img_four_rect)
    draw_lines(screen)
    normal_cursor()
    pygame.display.set_caption(TITLE)
    return (file, img_four_rect, img_four_name, img_four_file)


def draw_lines(screen):
    "draw the lines that split the screen into 4 squares"
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    line_color = 100, 100, 100
    vline = pygame.draw.line(screen, line_color, ((screen_width / 2),\
        screen_height), ((screen_width / 2), 0), 2)
    hline = pygame.draw.line(screen, line_color, (0, (screen_height / 2)),\
        (screen_width, (screen_height / 2)), 2)
    pygame.display.update(vline)
    pygame.display.update(hline)


def hover_square(screen, show_img_one, show_img_two, show_img_three,\
show_img_four, img_one_rect, img_two_rect, img_three_rect, img_four_rect,\
img_one_name, img_two_name, img_three_name, img_four_name, img_one_file,\
img_two_file, img_three_file, img_four_file, rect):
    "display image name in title bar on mouse over"
    nav_msg = "Space for next page, Backspace for last page. Click to enlarge"
    num_imgs = len(files)
    cursor = pygame.mouse.get_pos()
    if show_img_one == 0:
        if img_one_rect:
            if img_one_rect.collidepoint(cursor):
                paint_screen(screen, rect)
                rect = show_message(screen, "%s: %d/%d - %s" % (img_one_name,\
                img_one_file + 1, num_imgs, nav_msg), "top", 9)
                show_img_one = 1
                (show_img_two, show_img_three, show_img_four) = (0, 0, 0)
    if show_img_two == 0:
        if img_two_rect:
            if img_two_rect.collidepoint(cursor):
                paint_screen(screen, rect)
                rect = show_message(screen, "%s: %d/%d - %s" % (img_two_name,\
                img_two_file + 1, num_imgs, nav_msg), "top", 9)
                show_img_two = 1
                (show_img_one, show_img_three, show_img_four) = (0, 0, 0)
    if show_img_three == 0:
        if img_three_rect:
            if img_three_rect.collidepoint(cursor):
                paint_screen(screen, rect)
                rect = show_message(screen, "%s: %d/%d - %s" %\
                (img_three_name, img_three_file + 1, num_imgs, nav_msg),\
                "top", 9)
                show_img_three = 1
                (show_img_one, show_img_two, show_img_four) = (0, 0, 0)
    if show_img_four == 0:
        if img_four_rect:
            if img_four_rect.collidepoint(cursor):
                paint_screen(screen, rect)
                rect = show_message(screen, "%s: %d/%d - %s" % (img_four_name,\
                img_four_file + 1, num_imgs, nav_msg), "top", 9)
                show_img_four = 1
                (show_img_one, show_img_two, show_img_three) = (0, 0, 0)
    return (show_img_one, show_img_two, show_img_three, show_img_four, rect)


def adust_img_size(the_img, screen_width, screen_height):
    "scale the image down if necessary to fit in its square"
    (img_width, img_height) = the_img.get_size()
    small_img = the_img
    if img_width < img_height:
        if img_width > (screen_width / 2) or img_height > (screen_height / 2):
            small_img = pygame.transform.scale(the_img, ((screen_height / 2),\
                (screen_height / 2)))
    if img_width > img_height:
        if img_width > (screen_width / 2) or img_height > (screen_height / 2):
            small_img = pygame.transform.scale(the_img, ((screen_width / 2),\
                (screen_height / 2)))
    if img_width == img_height:
        "if the demensions are equal"
        if img_width > (screen_width / 2) or img_height > (screen_height / 2):
            small_img = pygame.transform.scale(the_img, ((screen_width / 2),\
                (screen_height / 2)))
    return small_img


class verbose:
    def __init__(self):
        self.font = pygame.font.Font(FONT_NAME, 12)
    def curdir(self, screen):
        curdir_details = "Directory:  %s" % os.getcwd()
        ren = self.font.render(curdir_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 15
        screen.blit(ren, ren_rect)
    def filename(self, screen, file):
        filename_details = "Filename:  %s" % files[file]
        ren = self.font.render(filename_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        screen.blit(ren, ren_rect)
    def filesize(self, screen, file):
        fsize = os.path.getsize(files[file])
        if fsize >= 1024:
            filesize_details = "Size: %d bytes (%.f kilobytes)" %\
                (fsize, (fsize / 1024.0))
        else:
            filesize_details = "Size:  %d bytes" % fsize
        ren = self.font.render(filesize_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 30
        screen.blit(ren, ren_rect)
    def type(self, screen, file):
        img_type = imghdr.what(files[file])
        type_details = "Type:  %s" % img_type
        ren = self.font.render(type_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 45
        screen.blit(ren, ren_rect)
    def original_demensions(self, screen, refresh_img):
        (img_width, img_height) = refresh_img.get_size()
        orig_demensions_details = "Original Demensions:  %sx%s" %\
            (img_width, img_height)
        ren = self.font.render(orig_demensions_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 60
        screen.blit(ren, ren_rect)
    def current_demensions(self, screen, new_img):
        (img_width, img_height) = new_img.get_size()
        current_demensions_details = "Current Demensions:  %sx%s" %\
            (img_width, img_height)
        ren = self.font.render(current_demensions_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 75
        screen.blit(ren, ren_rect)
    def current_placement(self, screen, file, num_imgs):
        current_img = str(file + 1)
        current_placement_details = "Current Placement:  %s/%s" %\
            (current_img, str(num_imgs))
        ren = self.font.render(current_placement_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 90
        screen.blit(ren, ren_rect)
    def last_modified(self, screen, file):
        last_modified_details = "Last Modified:  %s" %\
            str(ctime(os.stat(files[file])[ST_MTIME]))
        ren = self.font.render(last_modified_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 105
        screen.blit(ren, ren_rect)
    def last_accessed(self, screen, file):
        last_accessed_details = "Last Accessed:  %s" %\
            str(ctime(os.stat(files[file])[ST_ATIME]))
        ren = self.font.render(last_accessed_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 120
        screen.blit(ren, ren_rect)
    def status_last_changed(self, screen, file):
        last_changed_details = "Status Last Changed:  %s" %\
            str(ctime(os.stat(files[file])[ST_CTIME]))
        ren = self.font.render(last_changed_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 135
        screen.blit(ren, ren_rect)
    def owner(self, screen, file):
        uid = os.stat(files[file])[ST_UID]
        owner_details = "Owner: %s (uid: %s)" % (getpwuid(uid)[0], str(uid))
        ren = self.font.render(owner_details, 1, SILVER) 
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 150
        screen.blit(ren, ren_rect)
    def group(self, screen, file):
        gid = os.stat(files[file])[ST_GID]
        group_details = "Group:  %s (gid: %s)" % (getgrgid(gid)[0], str(gid))
        ren = self.font.render(group_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 165
        screen.blit(ren, ren_rect)
    def perms(self, screen, file):
        mode = os.stat(files[file])[ST_MODE]
        perms_details = "Permissions:  %o" % S_IMODE(mode)
        ren = self.font.render(perms_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 180
        screen.blit(ren, ren_rect)
    def date(self, screen):
        date_details = "Todays Date:  %s" % ctime(time())
        ren = self.font.render(date_details, 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 220
        ren_rect[1] = 195
        screen.blit(ren, ren_rect)
    def show_next_image(self, screen, file):
        if (file + 1) >= len(files):
            file = -1
        ren = self.font.render("next image, %s (%d/%d):" %\
        (files[file + 1], (file + 2), len(files)), 1, SILVER)
        ren_rect = ren.get_rect()
        ren_rect[0] = 240
        ren_rect[1] = 230
        screen.blit(ren, ren_rect)      
        next = pygame.image.load(files[file + 1])
        next = preview_img(screen, next)
        next_rect = next.get_rect()
        next_rect[0] = 240
        next_rect[1] = 245
        screen.blit(next, next_rect)
        pygame.display.update(next_rect)
    def show_prev_image(self, screen, file):
        if (file - 1) < 0:
            ren = self.font.render("previous image, %s (%d/%d):" %\
            (files[file-1], (file - 1), len(files)), 1, SILVER, BLACK)
        else:
            ren = self.font.render("previous image, %s (%d/%d):" %\
            (files[file-1], file, len(files)), 1, SILVER, BLACK)
        ren_rect = ren.get_rect()
        ren_rect[0] = 0
        ren_rect[1] = 210
        screen.blit(ren, ren_rect)
        prev = pygame.image.load(files[file - 1])
        prev = preview_img(screen, prev)
        prev_rect = prev.get_rect()
        prev_rect[0] = 0
        prev_rect[1] = 225
        screen.blit(prev, prev_rect)
        pygame.display.update(prev_rect)
    def show_current_image(self, screen, file):
        current = pygame.image.load(files[file])
        current = preview_img(screen, current)
        current_rect = current.get_rect()
        current_rect.topleft = screen.get_rect().topleft
        screen.blit(current, current_rect)
        pygame.display.update(current_rect)


def command_verbose_info(screen, new_img, img, refresh_img, rect, file,\
    num_imgs):
    paint_screen(screen)
    orig_resolution = screen.get_size()
    verbose_info(screen, new_img, img, refresh_img, file, num_imgs)
    pygame.display.set_mode(orig_resolution, RESIZABLE)
    pygame.display.set_caption(TITLE)
    rect = get_center(screen, new_img)
    my_update_screen(new_img, screen, rect, file, num_imgs)


def preview_img(screen, refresh_img):
    "make a preview image"
    (img_width, img_height) = refresh_img.get_size()
    # display image in demensions that won't distort it:
    if img_width == img_height:
        "if the demensions are equal"
        if img_width < 150 and img_height < 150:
            "don't change if smaller than 150x150"
            small_img = pygame.transform.scale(refresh_img, (img_width,\
                img_height))
        else:
            "shrink down to 150x150"
            small_img = pygame.transform.scale(refresh_img, (150, 150))
    if img_width < img_height:
        if img_width < 150 and img_height < 200:
            "don't change if smaller than 150x200"
            small_img = pygame.transform.scale(refresh_img, (img_width,\
                  img_height))
        else:
            small_img = pygame.transform.scale(refresh_img, (150, 200))
    if img_width > img_height:
        if img_width < 200 and img_height < 150:
            "don't change if smaller than 200x150"
            small_img = pygame.transform.scale(refresh_img, (img_width,\
                img_height))
        else:
            small_img = pygame.transform.scale(refresh_img, (200, 150))
    return small_img


def print_verbose_info(screen, new_img, refresh_img, file, num_imgs):
    verb = verbose()
    verb.show_current_image(screen, file)
    verb.filename(screen, file)
    verb.curdir(screen)
    verb.current_placement(screen, file, num_imgs)
    verb.filesize(screen, file)
    verb.type(screen, file)
    verb.original_demensions(screen, refresh_img)
    verb.current_demensions(screen, new_img)
    verb.last_modified(screen, file)
    verb.last_accessed(screen, file)
    verb.status_last_changed(screen, file)
    if platform != 'win32':
        verb.owner(screen, file)
        verb.group(screen, file)
    verb.perms(screen, file)
    verb.date(screen)
    verb.show_next_image(screen, file)
    verb.show_prev_image(screen, file)
    pygame.display.flip()


def verbose_info(screen, new_img, img, refresh_img, file, num_imgs):
    wait_cursor()
    paint_screen(screen)
    pygame.display.set_caption("F2 to enlarge screen")
    print_verbose_info(screen, new_img, refresh_img, file, num_imgs)
    normal_cursor()
    pygame.event.set_blocked(MOUSEMOTION)
    while 1:
        event = pygame.event.wait()
        if (event.type == KEYDOWN and not event.key in (K_q, K_F2)) or\
            event.type == MOUSEBUTTONDOWN:
            break
        check_quit(event)
        if hit_key(event, K_F2):
            "enlarge so all info becomes visible"
            screen = pygame.display.set_mode((800, 600), RESIZABLE)
            pygame.display.set_caption(TITLE)
            print_verbose_info(screen, new_img, refresh_img, file, num_imgs)


def command_hide(screen, new_img, rect, file, num_imgs):
    "hide the image by making the screen blank"
    hide(screen)
    rect = get_center(screen, new_img)
    my_update_screen(new_img, screen, rect, file, num_imgs)


def hide(screen):
    paint_screen(screen)
    normal_cursor()
    while 1:
        event = pygame.event.wait()
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            break


def command_show_dirs(new_img, img, screen, rect, file, num_imgs):
    global files
    paint_screen(screen)
    (num_imgs, file) = show_dirs(screen, num_imgs, file)
    wait_cursor()
    start = start_timer()
    if num_imgs < 1:
        files = [DATA_DIR + IMGV_LOGO]
        num_imgs = 1
        new_img = img = load_img(files[file])
    else:
        new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    pygame.display.set_caption(TITLE)
    normal_cursor()
    return (new_img, new_img, new_img, num_imgs, file, rect)


def show_dirs(screen, num_imgs, file):
    global files
    global PLAY_LIST_NAME
    wait_cursor()
    slash = os.sep
    # store all files in the current directory in 'dirs'
    dirs = os.listdir(os.getcwd()) 
    paint_screen(screen)
    screen_height = screen.get_height()
    fg_color = SILVER
    font = pygame.font.Font(FONT_NAME, 10)
    line = 55 
    show_message(screen, "%s: %d images" % (os.getcwd(), len(get_imgs())),\
    "top", 13)
    # take out everything but real directories from 'dirs'
    dirs = strip_dirs(dirs)
    dirs.sort()
    x = []
    ren_ok_rect = imgv_button(screen, "OK", 0, 18, "midtop")
    col = 10
    # go through all the directory names
    for d in dirs:
        if d == slash:
            ren = font.render(d, 1, fg_color)
        else:
            ren = font.render(d+slash, 1, fg_color)
        # print directory names on screen, wrapping if necessary
        font_height = font.size(d)[1]
        if (line + font_height) >= screen_height:
            longest_dir_name = get_longest(d, dirs, font)
            line = 55 # reset to beginning of screen
            col = col + (longest_dir_name + 15) # go to next column
        ren_rect = ren.get_rect()
        ren_rect[0] = col
        ren_rect[1] = line
        screen.blit(ren, (col, line))
        line = line + 15
        x.append((ren_rect, d))
        pygame.display.update(ren_rect)
    normal_cursor()
    pygame.event.set_blocked(MOUSEMOTION)
    # handle events
    while 1:
        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()
        if left_click(event):
            for item in x:
                if item[0].collidepoint(cursor):
                    wait_cursor()
                    # change to the clicked directory
                    os.chdir(item[1])
                    # store new sub-directories in 'dirs'
                    dirs = os.listdir(os.getcwd())
                    # adjust the variables for the new dir
                    file = adjust_files()
                    show_dirs(screen, num_imgs, file)
                    # get new num_imgs value here for recursion reasons
                    num_imgs = len(files)
                    normal_cursor()
                    return (num_imgs, file)
        if hit_key(event, K_RETURN) or hit_key(event, K_SPACE):
            wait_cursor()
            file = adjust_files()
            num_imgs = len(files)
            PLAY_LIST_NAME = " "
            break
        cursor = pygame.mouse.get_pos()
        if left_click(event):
            if ren_ok_rect.collidepoint(cursor):
                wait_cursor()
                file = adjust_files()
                num_imgs = len(files)
                PLAY_LIST_NAME = " "
                break
        check_quit(event)
    return (num_imgs, file)


def adjust_files():
    global files
    files = get_imgs()
    files.sort()
    file = 0
    return file


def strip_dirs(dirs):
    l = []
    for dir in dirs:
        if os.path.isdir(dir):
            l.append(dir)
    l[0:0] = ["..", os.sep]
    return l


def get_longest(d, dirs, font):
    longest_dir_name = 0
    b = dirs.index(d)
    i = 0
    for dir in dirs:
        if i >= b: 
            break 
        i = i + 1
        if len(dir) > longest_dir_name:
            longest_dir_name = len(dir)
            font_width = font.size(dir)[0]
    return font_width


def command_main_menu(refresh_img, screen, screen_midtop,\
    file, num_imgs, rect, new_img, img, new_img_width, new_img_height):
    global MENU_COLOR
    global MENU_COLOR_ITEM
    global MENU_POS
    wait_cursor()
    x = []
    i = 16 # how far down the top of menu starts
    cursor = pygame.mouse.get_pos()
    font = pygame.font.Font(FONT_NAME, 11) 
    if MENU_POS == -1:
        MENU_POS = cursor[0]
    main_menu_fg(screen, font, i, x)
    normal_cursor()

    last_rect = Rect(rect)
    screen_midtop = screen.get_rect().midtop
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    new_img_width = new_img.get_width()
    new_img_height = new_img.get_height()
    while 1:
        event = pygame.event.wait()
        check_quit(event)
        cursor2 = pygame.mouse.get_pos()
        if left_click(event):
            wait_cursor()
            for it in x:
                if it[0].collidepoint(cursor2):
                    if it[1] == " next image ": 
                        (new_img, img, refresh_img, file, rect) =\
                        command_next_img(new_img, img, refresh_img, screen,\
                        screen_midtop, file, num_imgs, rect)
                    elif it[1] == " previous image ":
                        (new_img, img, refresh_img, file, rect) =\
                        command_prev_img(new_img, img, refresh_img, screen,\
                        screen_midtop, file, num_imgs, rect)        
                    elif it[1] == " new directory ":
                        (new_img, img, refresh_img, num_imgs, file, rect) = \
                        command_show_dirs(new_img, img, screen, rect,\
                        file, num_imgs)
                    elif it[1] == " list images ":
                        (new_img, img, refresh_img, file, rect) =\
                        command_show_images(screen, new_img, img, file,\
                        num_imgs, rect)
                    elif it[1] == " thumbnails ":
                        (new_img, img, refresh_img, file, rect) =\
                        command_thumbs(screen, new_img, file)
                    elif it[1] == " details ":
                        if not REMOTE:
                            command_verbose_info(screen, new_img, img,\
                            refresh_img, rect, file, num_imgs)
                    elif it[1] == " zoom out ":
                        (new_img, img, rect) = command_zoom_out(new_img,\
                        new_img_width, new_img_height, img, screen,\
                        screen_midtop, file, num_imgs, rect)
                    elif it[1] == " zoom in ":
                        (new_img, img, rect) = command_zoom_in(new_img,\
                        new_img_width, new_img_height, img, screen,\
                        screen_midtop, file, num_imgs, rect)
                    elif it[1] == " remove ":
                        (new_img, img, refresh_img, file, num_imgs, rect) = \
                        command_remove_img(new_img, img, screen,\
                        screen_midtop, file, rect)
                    elif it[1] == " rotate right ":
                        (new_img, img, rect) = command_rotate_right(new_img,\
                        screen, screen_midtop, file, num_imgs, rect)
                    elif it[1] == " rotate left ":
                        (new_img, img, rect) = command_rotate_left(new_img,\
                        screen, screen_midtop, file, num_imgs, rect)
                    elif it[1] == " multi-view ":
                        (file, new_img, img, refresh_img, rect) = command_four(\
                        screen, file, new_img)
                        normal_cursor()
                    elif it[1] == " 640x480 ":
                        (screen_midtop, rect) =\
                        command_640x480(new_img, file, num_imgs, rect)
                    elif it[1] == " 800x600 ":
                        (screen_midtop, rect) =\
                        command_800x600(new_img, file, num_imgs, rect)
                    elif it[1] == " 1024x768 ":
                        (screen_midtop, rect) =\
                        command_1024x768(new_img, file, num_imgs, rect)
                    elif it[1] == " fullscreen ":
                        command_fullscreen(screen)
                    elif it[1] == " refresh ":
                        (new_img, img, rect) = command_refresh(refresh_img,\
                        screen, screen_midtop, file, num_imgs)
                    elif it[1] == " first image ":
                        (new_img, img, refresh_img, file, rect) =\
                        command_first_img(new_img, img, refresh_img,\
                        screen, screen_midtop, file, num_imgs, rect)
                    elif it[1] == " last image ":
                        (new_img, img, refresh_img, file, rect) =\
                        command_last_img(new_img, img, refresh_img,\
                        screen, screen_midtop, file, num_imgs, rect)
                    elif it[1] == " shuffle ":
                        (new_img, img, refresh_img, rect) = command_shuffle(\
                        new_img, img, screen, rect, file, num_imgs)
                    elif it[1] == " unshuffle ":
                        (new_img, img, refresh_img, rect) =\
                        command_unshuffle(new_img, img, screen, rect,\
                        file, num_imgs)
                    elif it[1] == " flip horizontal ":
                        (new_img, img, rect) = command_horiz(new_img, screen,\
                        file, num_imgs, rect)
                    elif it[1] == " flip vertical ":
                        (new_img, img, rect) = command_vert(new_img, screen,\
                        file, num_imgs, rect)
                    elif it[1] == " start slideshow ":
                        (new_img, img, refresh_img, file, rect) = my_slideshow(\
                        new_img, img, screen, screen_midtop, file, num_imgs,\
                        rect)
                    elif it[1] == " play list options ":
                        (new_img, new_img, new_img, file, rect, num_imgs)\
                        = command_play_list_options(screen, file)
                    elif it[1] == " add to play list ":
                        command_add_to_play_list(screen, files[file])
                    elif it[1] == " hide image ":
                        command_hide(screen, new_img, rect, file, num_imgs)
                    elif it[1] == " about ":
                        command_about(screen, new_img, rect, file, num_imgs)
                    elif it[1] == " help ":
                        command_help(screen, new_img, file)
                    elif it[1] == " menu color ":
                        if MENU_COLOR_ITEM >= (len(MENU_ADJUST) - 1):
                            MENU_COLOR_ITEM = 0
                        else:
                            MENU_COLOR_ITEM = MENU_COLOR_ITEM + 1
                        MENU_COLOR = MENU_ADJUST[MENU_COLOR_ITEM]
                        my_update_screen(new_img, screen, rect, file, num_imgs)
                        (refresh_img, screen, screen_midtop, file,\
                        num_imgs, new_img, img, new_img_width, new_img_height,\
                        rect) = command_main_menu(refresh_img, screen,\
                        screen_midtop, file, num_imgs, rect, new_img, img,\
                        new_img_width, new_img_height)
                        return (refresh_img, screen, screen_midtop, file,\
                        num_imgs, new_img, img, new_img_width, new_img_height,\
                        rect)
                    elif it[1] == " close menu ":
                        MENU_POS = -1
                        my_update_screen(new_img, screen, rect, file, num_imgs)
                        normal_cursor()
                        return (refresh_img, screen, screen_midtop, file,\
                        num_imgs, new_img, img, new_img_width,\
                        new_img_height, rect)
                    elif it[1] == " exit ":
                        clean_screen()
                        raise SystemExit
            break
        if event.type == KEYDOWN:
            my_update_screen(new_img, screen, rect, file, num_imgs)
            return (refresh_img, screen, screen_midtop, file,\
            num_imgs, new_img, img, new_img_width,\
            new_img_height, rect)
        if middle_click(event):
            "close the menu upon middle click"
            MENU_POS = -1
            my_update_screen(new_img, screen, rect, file, num_imgs)
            normal_cursor()
            return (refresh_img, screen, screen_midtop, file,\
                num_imgs, new_img, img, new_img_width,\
                new_img_height, rect)
        if right_click(event):
            wait_cursor()
            MENU_POS = -1
            my_update_screen(new_img, screen, rect, file, num_imgs)
            (refresh_img, screen, screen_midtop, file,\
            num_imgs, new_img, img, new_img_width, new_img_height, rect) =\
            command_main_menu(refresh_img, screen, screen_midtop,\
            file, num_imgs, rect, new_img, img, new_img_width, new_img_height)
            return (refresh_img, screen, screen_midtop, file, num_imgs,\
                    new_img, img, new_img_width, new_img_height, rect)
    if KEEP_MENU_OPEN == "1":
        my_update_screen(new_img, screen, rect, file, num_imgs)
        (refresh_img, screen, screen_midtop, file, num_imgs, new_img, img,\
        new_img_width, new_img_height, rect) =\
        command_main_menu(refresh_img, screen, screen_midtop,\
        file, num_imgs, rect, new_img, img, new_img_width, new_img_height)
        normal_cursor()
    MENU_POS = -1
    normal_cursor()
    return (refresh_img, screen, screen_midtop, file,\
            num_imgs, new_img, img, new_img_width,\
            new_img_height, rect)


def main_menu_fg(screen, font, i, x):
    for item in MENU_ITEMS:
        ren = font.render(item, 1, MENU_COLOR, BLACK)
        ren_rect = ren.get_rect()
        ren_rect[0] = MENU_POS
        ren_rect[1] = i
        x.append((ren_rect, item))
        screen.blit(ren, (MENU_POS, i))
        i = i + 14 # space between each menu item in menu
        pygame.display.update(ren_rect)


def command_help(screen, new_img, file):
    paint_screen(screen)
    help(screen)
    rect = get_center(screen, new_img)
    my_update_screen(new_img, screen, rect, file, len(files))


def help(screen):
    "Display keyboard shortcuts"
    key_list = ["Space, n = next image","Backspace, b = previous image",
    "d = new directory", "i = list images", "t = thumbnails", "4 = multi-view",
    "w = slideshow","p = add to playlist","Ctrl+p = play list options",
    "f = first image","l = last image","+ = zoom in","- = zoom out",
    "r = rotate right","Ctrl+r = rotate left","o = refresh",
    "m = flip horizontal (mirror)","v = flip vertical","s = shuffle",
    "u = unshuffle","Del = remove","e = details","x = hide image","q = exit",
    "F1 = 640x480","F2 = 800x600","F3 = fullscreen","h = help (this screen)",
    "a = about","arrow keys = pan image (left, right, up, down)"]
    key_list.sort()
    font = pygame.font.Font(FONT_NAME, 12)
    i = 10
    for line in key_list:
        ren = font.render(line, 1, SILVER)
        screen.blit(ren, (10, i))
        i = i + 10
    pygame.display.flip()
    normal_cursor()
    while 1:
        event = pygame.event.wait()
        check_quit(event)
        if event.type == KEYDOWN and event.key != K_q or event.type ==\
        MOUSEBUTTONDOWN:
            break


def command_show_images(screen, new_img, img, file, num_imgs, rect):
    "copy current screen, display file names, repaint screen"
    start = start_timer()
    paint_screen(screen)
    pygame.display.set_caption(TITLE + " Click image name to jump to image. Esc to abort.") 
    normal_cursor()
    (list_names, filename, x, my_string) = command_file_master(screen,\
    files, "There are %d Images.  (Left-click a name to jump to that image)"\
    % len(files), 25, 13, 0, 1, 0)
    wait_cursor()
    if not filename == None:
        if num_imgs > 1:
            file = files.index(filename)
        new_img = load_img(files[file])
        rect = get_center(screen, new_img)
        screen_midtop = screen.get_rect().midtop
        ns = check_timer(start)
        my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    pygame.display.set_caption(TITLE)
    rect = get_center(screen, new_img)
    num_imgs = len(files)
    my_update_screen(new_img, screen, rect, file, num_imgs)
    return (new_img, new_img, new_img, file, rect)


def command_640x480(new_img, file, num_imgs, rect):
    "switch to 640x480"
    global MAX_SCREEN_FILES
    MAX_SCREEN_FILES = 165
    wait_cursor()
    resolution = 640, 480
    screen = pygame.display.set_mode(resolution, RESIZABLE)
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    my_update_screen(new_img, screen, rect, file, num_imgs)
    normal_cursor()
    return (screen_midtop, rect)


def command_800x600(new_img, file, num_imgs, rect):
    "switch to 800x600"
    global MAX_SCREEN_FILES
    MAX_SCREEN_FILES = 215
    wait_cursor()
    resolution = 800, 600
    screen = pygame.display.set_mode(resolution, RESIZABLE)
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    my_update_screen(new_img, screen, rect, file, num_imgs)
    normal_cursor()
    return (screen_midtop, rect)

def command_1024x768(new_img, file, num_imgs, rect):
    "switch to 1024x768"
    global MAX_SCREEN_FILES
    MAX_SCREEN_FILES = 265 
    wait_cursor()
    resolution = 1024, 768 
    screen = pygame.display.set_mode(resolution, RESIZABLE)
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    my_update_screen(new_img, screen, rect, file, num_imgs)
    normal_cursor()
    return (screen_midtop, rect)


def command_fullscreen(screen):
    "toggle between full screen and last screen mode"
    wait_cursor()
    if not pygame.display.toggle_fullscreen():
        pygame.display.set_mode(screen.get_size(), screen.get_flags()\
                        ^FULLSCREEN, screen.get_bitsize())
    normal_cursor()


def command_remove_img(new_img, img, screen, screen_midtop, file, rect):
    "Don't display the image anymore during the session"
    wait_cursor()
    start = start_timer()
    num_imgs = len(files)
    # only remove file if its not the only one:
    if not num_imgs < 2:
        files.remove(files[file])
        # go to the next image if there is one
        if file < (num_imgs - 1):
            new_img = next_img(file, new_img)
        # if not go to the previous image
        else:
            if file > 0:
                file = file - 1
                new_img = previous_img(file, new_img)
        num_imgs = len(files) # re-adjust
        rect = get_center(screen, new_img)
        screen_midtop = screen.get_rect().midtop
        ns = check_timer(start)
        my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, file, num_imgs, rect)
    

def command_rotate_left(new_img, screen, screen_midtop, file,\
     num_imgs, rect):
    "rotate counter clockwise"
    wait_cursor()
    start = start_timer()
    new_img = pygame.transform.rotozoom(new_img, 90, 1)
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, rect)


def command_rotate_right(new_img, screen, screen_midtop, file,\
    num_imgs, rect):
    "rotate clockwise"
    wait_cursor()
    start = start_timer()
    new_img = pygame.transform.rotozoom(new_img, -90, 1)
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, rect)


def command_zoom_out(new_img, new_img_width, new_img_height,\
        img, screen, screen_midtop, file, num_imgs, rect):
    "zoom out"
    wait_cursor()
    new_img_width = new_img.get_width()
    new_img_height = new_img.get_height()
    start = start_timer()
    if new_img_width >= MIN_WIDTH and new_img_height >= MIN_HEIGHT:
        new_img = pygame.transform.scale(img,\
            (new_img_width / 2, new_img_height / 2))
        rect = get_center(screen, new_img)
        ns = check_timer(start)
        my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, img, rect)


def command_zoom_in(new_img, new_img_width, new_img_height,\
        img, screen, screen_midtop, file, num_imgs, rect):
    "zoom in"
    wait_cursor()
    new_img_width = new_img.get_width()
    new_img_height = new_img.get_height()
    start = start_timer()
    if new_img_width < MAX_WIDTH and new_img_height < MAX_HEIGHT:
        new_img = pygame.transform.scale(img,\
                    (new_img_width * 2, new_img_height * 2))
        rect = get_center(screen, new_img)
        ns = check_timer(start)
        my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, img, rect)


def command_refresh(refresh_img, screen, screen_midtop,\
        file, num_imgs):
    "refresh image to its original state"
    wait_cursor()
    start = start_timer()
    new_img = refresh_img
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(refresh_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, rect)


def command_shuffle(new_img, img, screen, rect, file, num_imgs):
    "randomize the images"
    wait_cursor()
    start = start_timer()
    shuffle(files)
    new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, rect)


def command_unshuffle(new_img, img, screen, rect, file, num_imgs):
    "un-randomize the images"
    wait_cursor()
    start = start_timer()
    files.sort()
    new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, rect)


def command_down(rect, last_rect, new_img, screen, file, num_imgs,\
    screen_midtop):
    "scroll image to see more of the top"
    wait_cursor()
    if (rect.top + MOVE) < 0:
        rect.top = rect.top + MOVE
        screen.blit(new_img, rect)
        pygame.display.update(rect.union(last_rect))
        img_info(screen, screen_midtop, files[file], file, num_imgs, new_img,\
            NS_GLOBAL[0])
    normal_cursor()
    return rect


def command_up(rect, last_rect, new_img, screen, file, num_imgs,\
    screen_midtop, screen_height):
    "scroll image to see more of the bottom"
    wait_cursor()
    if (rect.bottom - MOVE) > screen_height:
        rect.bottom = rect.bottom - MOVE
        screen.blit(new_img, rect)
        pygame.display.update(rect.union(last_rect))
        img_info(screen, screen_midtop, files[file], file, num_imgs, new_img,\
            NS_GLOBAL[0])
    normal_cursor()
    return rect


def command_right(rect, last_rect, new_img, screen, file, num_imgs,\
    screen_midtop):
    "scroll image to see more of its left side"
    wait_cursor()
    if (rect.left + MOVE) < 0:
        rect.left = rect.left + MOVE
        screen.blit(new_img, rect)
        pygame.display.update(rect.union(last_rect))
        img_info(screen, screen_midtop, files[file], file, num_imgs, new_img,\
        NS_GLOBAL[0])
    normal_cursor()
    return rect 


def command_left(rect, last_rect, new_img, screen, file, num_imgs,\
    screen_midtop, screen_width):
    "scroll image to see more of its right side"
    wait_cursor()
    if (rect.right - MOVE) > screen_width:
        rect.right = rect.right - MOVE
        screen.blit(new_img, rect)
        pygame.display.update(rect.union(last_rect))
        img_info(screen, screen_midtop, files[file], file, num_imgs, new_img,\
        NS_GLOBAL[0])
    normal_cursor()
    return rect 


def command_horiz(new_img, screen, file, num_imgs, rect):
    "flip horizontally (mirror)"
    wait_cursor()
    start = start_timer()
    new_img = pygame.transform.flip(new_img, 90, 0)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, rect)


def command_vert(new_img, screen, file, num_imgs, rect):
    "flip vertically"
    wait_cursor()
    start = start_timer()
    new_img = pygame.transform.flip(new_img, 90, 90)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, rect)


def command_first_img(new_img, img, refresh_img, screen,\
    screen_midtop, file, num_imgs, rect):
    "jump to the first image"
    wait_cursor()
    start = start_timer()
    file = 0
    new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, file, rect)


def command_last_img(new_img, img, refresh_img, screen,\
            screen_midtop, file, num_imgs, rect):
    "jump to the last image"
    wait_cursor()
    start = start_timer()
    while file < (num_imgs - 1):
        file = file + 1
    new_img = load_img(files[file])
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, file, rect)
    

def command_next_img(new_img, img, refresh_img, screen, screen_midtop,\
    file, num_imgs, rect):
    "jump to next image"
    wait_cursor()
    start = start_timer()
    if WRAP == "0":
        if file < (num_imgs - 1):
            file = file + 1
            new_img = next_img(file, new_img)
            rect = get_center(screen, new_img)
            ns = check_timer(start)
            my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    if WRAP == "1":
        file = file + 1
        if file > (num_imgs - 1):
            file = 0
        if num_imgs > 1:
            new_img = next_img(file, new_img)
            rect = get_center(screen, new_img)
            ns = check_timer(start)
            my_update_screen(new_img, screen, rect, file, num_imgs, ns) 
    normal_cursor()
    return (new_img, new_img, new_img, file, rect)


def command_prev_img(new_img, img, refresh_img, screen, screen_midtop,\
    file, num_imgs, rect):
    "jump to previous image"
    wait_cursor()
    start = start_timer()
    if file > 0:
        file = file - 1
        new_img = previous_img(file, new_img)
        rect = get_center(screen, new_img)
        ns = check_timer(start)
        my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    return (new_img, new_img, new_img, file, rect)


def command_about(screen, new_img, rect, file, num_imgs):
    normal_cursor()
    about(screen)
    rect = get_center(screen, new_img)
    num_imgs = len(files)
    my_update_screen(new_img, screen, rect, file, num_imgs)


def about(screen):
    screen.fill(BLUE)
    msg = "imgv 1.2 by Ryan (gt3) Kulla. 2001"
    msg_font = pygame.font.Font(FONT_NAME, 23)
    char = 0
    i = 0
    show_message(screen, "Press a key or Click to return", "bottom", 13)
    pygame.event.set_blocked(MOUSEMOTION)
    while 1:
        event = pygame.event.poll()
        check_quit(event)
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            break
        if char < len(msg):
            if msg[char] != ' ': # don't delay on spaces
                pygame.time.delay(100)
            ren = msg_font.render(msg[char], 1, WHITE) # one char at a time
            ren_rect = ren.get_rect()
            ren_rect[0] = ren_rect[0] + (i + 10)
            ren_rect[1] = 10
            screen.blit(ren, ren_rect)
            i = i + ren.get_width() # make letters space evenly
            char = char + 1
            pygame.display.update(ren_rect)


def clean_screen():
    pygame.display.quit()
    pygame.font.quit()


def init_screen():
    pygame.display.init()
    pygame.font.init()


def errorbox(title, msg):
    "display a pygame error box"
    clean_screen()
    init_screen()
    errorbox_resolution = 450, 150
    err_screen = pygame.display.set_mode(errorbox_resolution)
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    pygame.display.set_caption(title)
    errorbox_color = IMGV_COLOR
    msg_color = WHITE 
    ok_fg_color = SILVER 
    ok_bg_color = BLUE 
    font = pygame.font.Font(FONT_NAME, 13)
    msg_ren = font.render(msg, 1, msg_color)
    err_screen.fill(errorbox_color)
    err_screen.blit(msg_ren, (10, 10))
    ok = font.render('OK', 1, ok_fg_color)
    ok_rect = ok.get_rect().inflate(20, 10)
    ok_rect.centerx = err_screen.get_rect().centerx
    ok_rect.bottom = err_screen.get_rect().bottom - 10
    err_screen.fill(ok_bg_color, ok_rect)
    err_screen.blit(ok, ok_rect.inflate(-20, -10))
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()
        if left_click(event):
            if ok_rect.collidepoint(cursor):
                clean_screen()
                raise SystemExit


def load_img(img_file):
    global REMOTE
    try:
        if img_file[:4] == "http":
            REMOTE = 1
            pic = urllib.urlopen(img_file).read()
            img = pygame.image.load(StringIO(pic))
            return img
        else:
            img = pygame.image.load(img_file).convert()
    except pygame.error:
        errorbox('pygame.error', '%s' % pygame.get_error())
    return img


def next_img(file, old_img):
    img = old_img
    if file < len(files):
        img = load_img(files[file])
    return img


def previous_img(file, old_img):
    img = old_img
    img = load_img(files[file])
    return img  


def my_update_screen(new_img, screen, rect, file, num_imgs, *ns):
    global NS_GLOBAL
    screen.fill(IMGV_COLOR)
    screen.blit(new_img, rect)
    pygame.display.flip()
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    if not ns:
        "ns wasn't passed, store last ns value in ns"
        ns = NS_GLOBAL
    else:
        "ns was passed update NS_GLOBAL"
        NS_GLOBAL = ns
    img_info(screen, screen_midtop, files[file], file, num_imgs, new_img, ns[0])


def get_center(screen, new_img):
    "fint out where the center of the screen is"
    screen_center = screen.get_rect().center
    rect = new_img.get_rect()
    rect.center = screen_center
    return rect


def resize_it(event, screen, new_img, file, num_imgs):
    resolution = event.size
    screen = pygame.display.set_mode(resolution, RESIZABLE)
    rect = get_center(screen, new_img)
    screen_midtop = screen.get_rect().midtop
    my_update_screen(new_img, screen, rect, file, num_imgs)
    return (screen_midtop, rect)


def wait_cursor():
    pygame.mouse.set_cursor(*pygame.cursors.diamond)


def normal_cursor():
    pygame.mouse.set_cursor(*pygame.cursors.arrow)


def img_info(screen, screen_midtop, filename, file, num_imgs, new_img, ns):
    "display info about the current image"
    current_img = str(file + 1)
    if REMOTE:
        fsize = 0
        filename = argv[1]
    else:
        fsize = os.path.getsize(filename)
        filename = os.path.basename(filename)
    if fsize >= 1024:
        file_size = "%.f Kilobytes" % (fsize / 1024.0)
    else:
        file_size = "%d bytes" % fsize

    if SLIDE_SHOW_RUNNING == 1:
        slide_show_running = "[slideshow]"
    else:
        slide_show_running = " "

    if PLAY_LIST_NAME != " ":
        img_status = "%s/%s, %s -- loaded in %s secs, %s [%s] %s" %\
        (current_img, str(num_imgs), filename, str(ns), str(file_size),\
        PLAY_LIST_NAME, slide_show_running)
    else:
        img_status = "%s/%s, %s -- loaded in %s secs, %s %s" % (current_img,\
        str(num_imgs), filename, str(ns), str(file_size), slide_show_running)

    show_message(screen, img_status, "top", 12)


def get_imgs():
    files = []
    for type in IMG_TYPES:
        files = files + glob("*.%s" % type)
    return files
    

def started_msg(screen):
    global SLIDE_SHOW_RUNNING
    SLIDE_SHOW_RUNNING = 1
    show_message(screen, "Hit any key to start (p = pause, Esc = stop, Space = skip forward, Backspace = skip backward)", 30, 11)
    while 1:
        event = pygame.event.wait()
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            break


def stopped_msg(screen):
    global SLIDE_SHOW_RUNNING
    SLIDE_SHOW_RUNNING = 0
    show_message(screen, "Slideshow Stopped", 30, 13)


def pause(screen):
    while 1:
        ren_rect = show_message(screen, "Slideshow Paused", 30, 13)
        event = pygame.event.wait()
        check_quit(event)
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            paint_screen(screen, ren_rect)
            break


def my_slideshow(new_img, img, screen, screen_midtop, file, num_imgs, rect):
    "image slideshow"
    speed = get_speed(screen, new_img, rect, screen_midtop,\
        files[file], file, num_imgs)
    if not speed == -1:  # didn't hit Esc from get_speed:
        started_msg(screen)
        dont_call = 0
        while 1:
            event = pygame.event.poll()
            pygame.event.set_blocked(MOUSEMOTION)
            check_quit(event)
            if event.type == KEYDOWN and event.key != K_p or \
            event.type == MOUSEBUTTONDOWN:
                stopped_msg(screen)
                file = file - 1
                break
            if hit_key(event, K_p):
                pause(screen)
                my_update_screen(new_img, screen, rect, file, len(files))
            if dont_call == 1:
                break
            if WRAP_SLIDESHOW == "0":
                if file < num_imgs:
                    (new_img, file, rect, dont_call) = show_slideshow_img(\
                    screen, new_img, file, num_imgs, speed)
            if WRAP_SLIDESHOW == "1":
                if file >= num_imgs:
                    file = 0
                (new_img, file, rect, dont_call) = show_slideshow_img(screen,\
                new_img, file, num_imgs, speed)
            pygame.time.delay(5) # don't hog cpu
    return (new_img, new_img, new_img, file, rect)


def show_slideshow_img(screen, new_img, file, num_imgs, speed):
    start = start_timer()
    wait_cursor()
    new_img = next_img(file, new_img)
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    if speed > 0:
        for i in range(speed):
            "trick delay into letting you escape anytime"
            event = pygame.event.poll()
            if event.type == KEYDOWN and event.key not in (K_p, K_SPACE,\
            K_BACKSPACE) or event.type == MOUSEBUTTONDOWN:
                stopped_msg(screen)
                return (new_img, file, rect, 1)
            if hit_key(event, K_p):
                pause(screen)
                my_update_screen(new_img, screen, rect, file, len(files))
            if hit_key(event, K_SPACE):
                "skip forward an image immediately"
                file = file + 1
                return (new_img, file, rect, 0)
            if hit_key(event, K_BACKSPACE):
                "skip backward an image immediately"
                file = file - 1
                return (new_img, file, rect, 0)
            pygame.time.delay(1000) # check every second
    file = file + 1
    return (new_img, file, rect, 0)


def get_speed(screen, new_img, rect, screen_midtop, filename, file, num_imgs):
    "get speed user wants slideshow to go"
    normal_cursor()
    DEFAULT_SPEED = 5
    MAX_SPEED = 100000
    speed_msg = " Enter slideshow speed (0-%d secs): " % MAX_SPEED
    speed = ['0']
    char_space = 0
    font = pygame.font.Font(FONT_NAME, 13)
    ren_speed_msg = font.render(speed_msg, 1, WHITE, BLACK)
    ren_speed_msg_rect = ren_speed_msg.get_rect()
    ren_speed_msg_width = ren_speed_msg.get_width()
    ren_speed_msg_rect.midtop = screen_midtop
    under_speed_msg = 15 # how far to go under speed_msg
    ren_speed_msg_rect[1] = ren_speed_msg_rect[1] + under_speed_msg
    screen.blit(ren_speed_msg, ren_speed_msg_rect)
    pygame.display.update(ren_speed_msg_rect)
    my_digits = [] # keypad number list.
    dirty_rects = []
    for num in range(10):
        my_digits.append('[%d]' % num) # [0],[1],..[9]
    while 1:
        event = pygame.event.wait()
        if event.type == KEYDOWN and not event.key == K_RETURN:
            speed_input = pygame.key.name(event.key)
            try:
                if speed_input in my_digits or speed_input in digits:
                    "only echo digits (0-9)"
                    for i in speed_input:
                        "extract n from brackets, [n]"
                        if i in digits:
                            speed_input = i
                    speed.append(speed_input)
                    ren_speed = font.render(speed_input, 1, WHITE, BLACK)
                    ren_speed_rect = ren_speed.get_rect()
                    ren_speed_rect.midtop = screen_midtop
                    ren_speed_rect[0] = ren_speed_rect[0] +\
                    (char_space + (ren_speed_msg_width / 2) + 5)
                    ren_speed_rect[1] = ren_speed_rect[1] + under_speed_msg
                    dirty_rects.append(ren_speed_rect)
                    screen.blit(ren_speed, ren_speed_rect)
                    pygame.display.update(ren_speed_rect)
                    char_space = char_space + ren_speed.get_width()
            except TypeError:
                "don't crash if user hits Backspace, Esc, etc."
                pass
        if hit_key(event, K_RETURN) or hit_key(event, K_KP_ENTER):
            break
        if hit_key(event, K_ESCAPE):
            wait_cursor()
            my_update_screen(new_img, screen, rect, file, num_imgs)
            normal_cursor()
            return -1
            check_quit(event)
        if hit_key(event, K_BACKSPACE):
            "erase whatever text was inputed"
            speed = ['0']
            for rect in dirty_rects:
                paint_screen(screen, rect)
            char_space = ren_speed.get_width()
    # convert to a valid speed
    if not len(speed) > 1:
        speed.append(str(DEFAULT_SPEED))
    speed = int(join(speed, ''))
    if speed > MAX_SPEED:
        speed = DEFAULT_SPEED
    return speed


def start_timer():
    return pygame.time.get_ticks()


def check_timer(start):
    return (pygame.time.get_ticks() - start) / 1000.0


def read_config_file():
    global WRAP_VAL
    global WRAP_SLIDESHOW_VAL
    global THUMB_VAL
    global KEEP_MENU_OPEN
    f = open(CONF_FILE)
    for line in f.readlines():
        if line == "WRAP=1\n":
            WRAP_VAL = split(line, "=")[1]
        if line == "WRAP_SLIDESHOW=1\n":
            WRAP_SLIDESHOW_VAL = split(line, "=")[1] 
        if line == "KEEP_MENU_OPEN=1\n":
            KEEP_MENU_OPEN = split(line, "=")[1]
        if line.find("THUMB_SIZE=") != -1:
            THUMB_VAL = split(line, "=")[1]
    WRAP_VAL = replace(WRAP_VAL, "\n", "")
    WRAP_SLIDESHOW_VAL = replace(WRAP_SLIDESHOW_VAL, "\n", "")
    KEEP_MENU_OPEN = replace(KEEP_MENU_OPEN, "\n", "")
    THUMB_VAL = replace(THUMB_VAL, "\n", "")
    return (WRAP_VAL, WRAP_SLIDESHOW_VAL, THUMB_VAL, KEEP_MENU_OPEN)


def get_conf_name():
    try:
        for file in os.listdir(os.environ['HOME']):
            if file == ".imgv.conf":
                return (os.environ['HOME'] + os.sep + ".imgv.conf")
    except KeyError:
        return (DATA_DIR + "imgv.conf")
    return (DATA_DIR + "imgv.conf")


BASE_DIR = getcwd()
try:
    DATA_DIR = os.environ['IMGV_HOME'] + os.sep + 'data' + os.sep
except KeyError:
    DATA_DIR = os.path.join(BASE_DIR, 'data' + os.sep)
CONF_FILE = get_conf_name()
WRAP_VAL = "0"
WRAP_SLIDESHOW_VAL="0"
THUMB_VAL = "100x100"
KEEP_MENU_OPEN = "0"
(WRAP, WRAP_SLIDESHOW, THUMB_VAL, KEEP_MENU_OPEN) = read_config_file()
SLIDE_SHOW_RUNNING = 0
WHITE = 255, 255, 255
SILVER = 200, 200, 200
BLACK = 0, 0, 0
BLUE = 40, 40, 90
RED = 255, 000, 051
LIGHT_BLUE = 102, 000, 255
SKY_BLUE = 000, 255, 255
LIGHT_GREEN = 0, 255, 102
YELLOW = 255, 255, 51
ORANGE = 255, 102, 051
MENU_COLOR = WHITE
MENU_COLOR_ITEM = 0
MENU_ADJUST = [WHITE, RED, LIGHT_BLUE, SKY_BLUE, SILVER, LIGHT_GREEN, ORANGE, YELLOW]
NS_GLOBAL = 0 # number of seconds it took to load. used with check_timer()
START_RES = 640, 480
MAX_SCREEN_FILES = 165
IMGV_COLOR = 0, 0, 0
IMGV_FONT = "VIRTUE1.TTF" 
FONT_NAME = DATA_DIR + IMGV_FONT
IMGV_LOGO = "imgv-logo1.jpg"
TITLE = "IMGV"
IMGV_PLAYLISTS = DATA_DIR + "playlists"
PLAY_LIST_NAME = " "
REMOTE = 0 # true if its a remote url to the image
MIN_WIDTH = 31
MIN_HEIGHT = 35
MAX_WIDTH = 1024
MAX_HEIGHT = 768
MOVE = 21 # how much to move bigger-than-window images by
MENU_POS = -1 
if platform == 'win32':
    "don't include captials since it will only duplicate files in Windows"
    IMG_TYPES = ["gif","jpg","jpeg","png","bmp","ppm","pcx","tga","tif"]
else:
    IMG_TYPES = ["gif","GIF","jpg","JPG","jpeg","JPEG","png","PNG","bmp","BMP",
                 "ppm","PPM","pcx","PCX","tga","TGA","tif","TIF"]

MENU_ITEMS = [" next image "," previous image "," new directory ",
              " list images "," thumbnails "," multi-view ",
              " start slideshow "," play list options "," add to play list ",
              " first image "," last image "," shuffle "," unshuffle ",
              " hide image "," remove "," refresh "," details ",
              " --------------- "," zoom in "," zoom out ",
              " flip horizontal "," flip vertical "," rotate right ",
              " rotate left "," fullscreen "," 640x480 "," 800x600 ", " 1024x768 ",
              " --------------- "," help "," menu color ",
              " close menu "," about "," exit "]


if not pygame.version.ver >= "1.1":
    errorbox("Version Error", "You need pygame 1.1 or greater")

if len(argv) < 2:
    "use the current dir if none are supplied on command line"
    dir_or_file = '.'
else:
    dir_or_file = argv[1]

if os.path.isdir(dir_or_file):
    chdir(dir_or_file)
    # store only image files in 'files'
    files = get_imgs()
else:
    files = [dir_or_file]

files.sort() # put images in alphabetical order


def main():
    global files
    start = start_timer()
    num_imgs = len(files) # total number of images
    init_screen()
    wait_cursor()
    pygame.display.set_caption(TITLE + " Right click to bring up menu")
    screen = pygame.display.set_mode(START_RES, RESIZABLE)
    file = 0
    if num_imgs < 1:
        files = [DATA_DIR + IMGV_LOGO]
        num_imgs = 1 
        img = load_img(files[file])
    else:
        img = load_img(files[file])
    img_width = img.get_width()
    img_height = img.get_height()
    refresh_img = img
    new_img = img
    rect = get_center(screen, new_img)
    ns = check_timer(start)
    my_update_screen(new_img, screen, rect, file, num_imgs, ns)
    normal_cursor()
    pygame.event.set_blocked(MOUSEMOTION)
    # main loop
    while 1:
        event = pygame.event.wait()
        last_rect = Rect(rect)
        screen_midtop = screen.get_rect().midtop
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        new_img_width = new_img.get_width()
        new_img_height = new_img.get_height()

        if event.type == KEYDOWN:
            pygame.display.set_caption(TITLE)
            (screen, rect, new_img, img, refresh_img, file, num_imgs,\
            screen_midtop, screen_width, screen_height, new_img_width,\
            new_img_height, last_rect) = handle_keyboard(event, screen, rect,\
            new_img, img, refresh_img, file, num_imgs, screen_midtop,\
            screen_width, screen_height, new_img_width, new_img_height,\
            last_rect)

        check_quit(event)
        if event.type == MOUSEBUTTONDOWN:
            if right_click(event):
                pygame.display.set_caption(TITLE)
                (refresh_img, screen, screen_midtop, file, num_imgs, new_img,\
                img, new_img_width, new_img_height, rect) = command_main_menu(\
                refresh_img, screen, screen_midtop, file, num_imgs, rect,\
                new_img, img, new_img_width, new_img_height)
    clean_screen()


def handle_keyboard(event, screen, rect, new_img, img, refresh_img, file,\
num_imgs, screen_midtop, screen_width, screen_height, new_img_width,\
new_img_height, last_rect):
    if hit_key(event, K_a):
        command_about(screen, new_img, rect, file, num_imgs)
    if hit_key(event, K_d):
        (new_img, img, refresh_img, num_imgs, file, rect) =\
        command_show_dirs(new_img, img, screen, rect, file, num_imgs)
    if hit_key(event, K_i):
        (new_img, img, refresh_img, file, rect) = command_show_images(screen,\
        new_img, img, file, num_imgs, rect)
    if event.type == VIDEORESIZE:
        "let user resize window"
        (screen_midtop, rect) = resize_it(event, screen, new_img, file,\
        num_imgs)
    if hit_key(event, K_F1):
        (screen_midtop, rect) = command_640x480(new_img, file, num_imgs, rect)
    if hit_key(event, K_F2):
        (screen_midtop, rect) = command_800x600(new_img, file, num_imgs, rect)
    if hit_key(event, K_F3):
        command_fullscreen(screen)
    if hit_key(event, K_DELETE):
        (new_img, img, refresh_img, file, num_imgs, rect) =\
        command_remove_img(new_img, img, screen, screen_midtop, file, rect)
    if hit_key(event, K_s):
        (new_img, img, refresh_img, rect) = command_shuffle(new_img, img,\
        screen, rect, file, num_imgs)
    if hit_key(event, K_u):
        (new_img, img, refresh_img, rect) = command_unshuffle(new_img,\
        img, screen, rect, file, num_imgs)
    if event.type == KEYDOWN:
        mods = pygame.key.get_mods()
        if event.key == K_r and mods & KMOD_CTRL == 0:
            (new_img, img, rect) = command_rotate_right(new_img, screen,\
            screen_midtop, file, num_imgs, rect)
    if event.type == KEYDOWN:
        mods = pygame.key.get_mods()
        if event.key == K_r and mods & KMOD_CTRL:   
            (new_img, img, rect) = command_rotate_left(new_img, screen,\
            screen_midtop, file, num_imgs, rect)
    if event.type == KEYDOWN:
        mods = pygame.key.get_mods()
        if event.key == K_p and mods & KMOD_CTRL == 0:
            command_add_to_play_list(screen, files[file])
            my_update_screen(new_img, screen, rect, file, num_imgs)
    if event.type == KEYDOWN:
        mods = pygame.key.get_mods()
        if event.key == K_p and mods & KMOD_CTRL:
            (new_img, new_img, new_img, file, rect, num_imgs)\
            = command_play_list_options(screen, file)
    if hit_key(event, K_MINUS) or hit_key(event, K_KP_MINUS):
        (new_img, img, rect) = command_zoom_out(new_img, new_img_width,\
        new_img_height, img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_EQUALS) or hit_key(event, K_KP_PLUS):
        (new_img, img, rect) = command_zoom_in(new_img, new_img_width,\
        new_img_height, img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_DOWN):
        rect = command_down(rect, last_rect, new_img, screen, file,\
        num_imgs, screen_midtop)
    if hit_key(event, K_UP):
        rect = command_up(rect, last_rect, new_img, screen, file,\
        num_imgs, screen_midtop, screen_height)
    if hit_key(event, K_RIGHT):
        rect = command_right(rect, last_rect, new_img, screen, file,\
        num_imgs, screen_midtop)
    if hit_key(event, K_LEFT):
        rect = command_left(rect, last_rect, new_img, screen, file,\
        num_imgs, screen_midtop, screen_width)  
    if hit_key(event, K_m):
        (new_img, img, rect) = command_horiz(new_img, screen, file,\
        num_imgs, rect)
    if hit_key(event, K_v):
        (new_img, img, rect) = command_vert(new_img, screen, file,\
        num_imgs, rect)
    if hit_key(event, K_SPACE) or hit_key(event, K_n):
        (new_img, img, refresh_img, file, rect) = command_next_img(new_img,\
        img, refresh_img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_BACKSPACE) or hit_key(event, K_b):
        (new_img, img, refresh_img, file, rect) = command_prev_img(new_img,\
        img, refresh_img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_o):
        (new_img, img, rect) = command_refresh(refresh_img, screen,\
        screen_midtop, file, num_imgs)
    if hit_key(event, K_f):
        (new_img, img, refresh_img, file, rect) = command_first_img(new_img,\
        img, refresh_img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_l):
        (new_img, img, refresh_img, file, rect) = command_last_img(new_img,\
        img, refresh_img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_w):
        (new_img, img, refresh_img, file, rect) = my_slideshow(new_img,\
        img, screen, screen_midtop, file, num_imgs, rect)
    if hit_key(event, K_x):
        command_hide(screen, new_img, rect, file, num_imgs)
    if hit_key(event, K_e):
        if not REMOTE:
            command_verbose_info(screen, new_img, img, refresh_img, rect,\
            file, num_imgs)
    if hit_key(event, K_4):
        (file, new_img, img, refresh_img, rect) = command_four(screen,\
        file, new_img)
        normal_cursor()
    if hit_key(event, K_t):
        (new_img, img, refresh_img, file, rect) = command_thumbs(screen,\
        new_img, file)
    if hit_key(event, K_h):
        command_help(screen, new_img, file)

    return (screen, rect, new_img, img, refresh_img, file, num_imgs,\
            screen_midtop, screen_width, screen_height, new_img_width,\
            new_img_height, last_rect)


if __name__=='__main__': main()
