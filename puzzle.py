#!/usr/bin/python3
# coding:utf-8
# date : 2019.11.23
# author : Hu
# email : ll104567i@163.com

import numpy as np
import random
import curses

def generate_np_puzzle(n=4):
    
    a = list(range(1,n*n))
    a.append(0)
    b = np.array(a).reshape((n,n))
    
    return b

def find_zero(np_puzzle):
        
    n = len(np_puzzle)
    for i in range(n):
        for j in range(n):
            if np_puzzle[i,j] == 0:
                return (i,j)

def move_up(np_puzzle):
    
    n = len(np_puzzle)
    zero_position = find_zero(np_puzzle)
    if zero_position[0] == n-1:
        return np_puzzle
    else:
        tmp = np_puzzle[zero_position]
        np_puzzle[zero_position] = np_puzzle[zero_position[0]+1,zero_position[1]]
        np_puzzle[zero_position[0]+1,zero_position[1]] = tmp

    return np_puzzle


def move_down(np_puzzle):
    
    n = len(np_puzzle)
    zero_position = find_zero(np_puzzle)
    if zero_position[0] == 0:
        return np_puzzle
    else:
        tmp = np_puzzle[zero_position]
        np_puzzle[zero_position] = np_puzzle[zero_position[0]-1,zero_position[1]]
        np_puzzle[zero_position[0]-1,zero_position[1]] = tmp

    return np_puzzle

def move_left(np_puzzle):
    
    n = len(np_puzzle)
    zero_position = find_zero(np_puzzle)
    if zero_position[1] == n-1:
        return np_puzzle
    else:
        tmp = np_puzzle[zero_position]
        np_puzzle[zero_position] = np_puzzle[zero_position[0],zero_position[1]+1]
        np_puzzle[zero_position[0],zero_position[1]+1] = tmp

    return np_puzzle

def move_right(np_puzzle):
    
    n = len(np_puzzle)
    zero_position = find_zero(np_puzzle)
    if zero_position[1] == 0:
        return np_puzzle
    else:
        tmp = np_puzzle[zero_position]
        np_puzzle[zero_position] = np_puzzle[zero_position[0],zero_position[1]-1]
        np_puzzle[zero_position[0],zero_position[1]-1] = tmp

    return np_puzzle

def generate_random_np(np_puzzle,default=500):

    random_np_puzzle = np.copy(np_puzzle)
    a = [move_left,move_right,move_up,move_down]
    for i in range(default):
        move = random.choice(a)
        random_np_puzzle = move(random_np_puzzle)
    
    return random_np_puzzle

def judge(a,b):
    
    flag = a == b
    if flag.all():
        return True
    else:
        return False


def display_info(str, x, y,):
    global stdscr
    stdscr.addstr(y,x,str)
    stdscr.refresh()

def get_key():
    global stdscr
    try:
        stdscr.nodelay(0)
        ch=stdscr.getch()
        stdscr.nodelay(1)
    except:
        exit(2)
    return ch

def set_win():
    global stdscr
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def unset_win():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

def gui(np_puzzle):
    
    n = len(np_puzzle)
    length = 4

    gui_str = ''
    init_str = '+' + ('-'*length + '+')*n
    gui_str += init_str + '\n'

    for i in np_puzzle:
        for j in i:
            if j == 0:
                j = ' '
            space = length - len(str(j))
            gui_str += '|' + ' '*space + str(j)
        gui_str += '|\n'
        gui_str += init_str + '\n'
    return gui_str



if __name__ ==  '__main__':
  
    stdscr = curses.initscr()
    UP,DOWN,LEFT,RIGHT=65,66,68,67
    std_np_puzzle = generate_np_puzzle()
    random_np_puzzle = generate_random_np(std_np_puzzle)
    banner0 = '//[q]uit/[r]estart'
    banner1 = '//[A]uthor:Hu'

    while 1:
        try:
            set_win()
            stdscr.clear()
            if judge(random_np_puzzle,std_np_puzzle): 
                display_info('Niu b1',0,1)
                display_info('Press any key continue...',0,2)
                display_info(gui(std_np_puzzle),0,3)
                a = get_key()
                if a in (ord('q'),ord('Q')):
                    exit()
                else:
                    random_np_puzzle = generate_random_np(std_np_puzzle)
                    continue
    
            display_info(banner0,0,1)
            display_info(banner1,0,2)
            display_info(gui(random_np_puzzle),0,3)
            display_info('>>>',0,15)
            key = get_key()
            if key in (ord('q'),ord('Q')):
                exit()
            if key in (ord('r'),ord('R')):
                random_np_puzzle = generate_random_np(std_np_puzzle)
                continue

            if key in (ord('w'),UP):
                random_np_puzzle = move_up(random_np_puzzle)
            if key in (ord('s'),DOWN):
                random_np_puzzle = move_down(random_np_puzzle)
            if key in (ord('a'),LEFT):
                random_np_puzzle = move_left(random_np_puzzle)
            if key in (ord('d'),RIGHT):
                random_np_puzzle = move_right(random_np_puzzle)
            if key in (ord('x'),ord('X')):
                random_np_puzzle = np.copy(std_np_puzzle)

        finally:
            unset_win()

