import cv2 as cv
import numpy as np
import sys
from time import time
from time import sleep
import pyautogui as gui
from threading import Thread
from window_capture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter
from edgefilter import EdgeFilter

# This script was written following the tutorial(s) here:
# https://www.youtube.com/watch?v=KecMlLUuiE4

is_bot_in_action = False
is_mining_bot_in_action = False
dump_bag_amt = 12

def mine_iron(rectangles):
    if len(rectangles):
        targets = iron_vision.get_click_points(rectangles)
        target = wincap.get_screen_position(targets[0])
        gui.moveTo(x=target[0]+np.random.uniform(-30, 30), y=target[1]+np.random.uniform(-50, 50))
        gui.click()
        sleep(np.random.uniform(2, 4))
    global is_mining_bot_in_action
    is_mining_bot_in_action = False

def dump_inventory(rectangles):
    if len(rectangles):
        targets = iron_vision.get_click_points(rectangles)
        for t in targets:
            target = wincap.get_screen_position(t)
            gui.moveTo(x=target[0]+np.random.uniform(-15, 15), y=target[1]+np.random.uniform(-15, 15))
            gui.keyDown('shift')
            gui.click()
            gui.keyUp('shift')
            sleep(np.random.uniform(0.5, 2))
        global dump_bag_amt
        dump_bag_amt = int(np.random.uniform(12,18))
    global is_bot_in_action
    is_bot_in_action=False

wincap = WindowCapture(sys.argv[1])
iron_vision = Vision('iron_ore_0_preprocessed.png')
bag_vision = Vision('iron_ore_bag_0_preprocessed.png', method=cv.TM_SQDIFF_NORMED)

# limestone HSV filter
iron_hsvfilter = HsvFilter(0, 255, 21, 13, 255, 255, 137, 0, 55, 0)
bag_hsvfilter = HsvFilter(6, 90, 67, 19, 133, 126, 0, 0, 143, 141)
iron_edgefilter = EdgeFilter(5, 1, 1, 200, 500)

loop_time = time()
while(True):
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # pre-process the image
    processed_image = iron_vision.apply_hsv_filter(screenshot, iron_hsvfilter)
    processed_image_bag = bag_vision.apply_hsv_filter(screenshot, bag_hsvfilter)

    # do object detection
    rectangles = iron_vision.find(processed_image, 0.41)
    rectangles_bag = bag_vision.find(processed_image_bag, 0.05, 20)

    # draw the detection results onto the original image
    output_image = iron_vision.draw_rectangles(screenshot, rectangles)
    output_image_bag = bag_vision.draw_rectangles(screenshot, rectangles_bag)

    # display the processed image
    #cv.imshow('Processed', processed_image_bag)
    cv.imshow('Matches', output_image_bag)

    if len(rectangles_bag) > dump_bag_amt:
        is_bot_in_action = True
        t = Thread(target=dump_inventory, args=(rectangles_bag,))
        t.start()

    if not is_mining_bot_in_action and not is_bot_in_action:
        is_mining_bot_in_action = True
        t = Thread(target=mine_iron, args=(rectangles,))
        t.start()

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')