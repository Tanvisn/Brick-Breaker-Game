import colorama
import sys
import os
import math
import time
import copy
import numpy as np
import random
from colorama import Fore, Back, Style
from input import *

rows = 45
cols = 180
fps = 20
t = 1/fps
flag = 0
score = 0
game_over = 0

blank_arr = []
arr_brick = []
arr = []
rainbow_idx = [4,8,10,14,25,26,29,31,40,48,55,63,69,71]
bullet_arr = []

for i in range(rows):
    blank_arr.append(' '*cols + '\n')

