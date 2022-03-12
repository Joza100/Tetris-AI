from PIL import ImageGrab
import numpy as np
import cv2
from pynput.keyboard import Key, Controller

# Green Red Orange DarkBlue Yellow Magenta LightBlue
SHAPE_COLORS = [131, 79, 122, 71, 161, 92, 120]
# DROP_COLORS = [65, 32, 60, 35, 80, 46, 120]


class GameInteraction:
    def __init__(self):
        self.keyboard = Controller()
        self.state = np.empty(shape=([20, 10]))
        self.next_piece = 0
        self.max_height = 0

    def find_game_state(self):
        print("Finding game state")
        image = np.array(ImageGrab.grab(bbox=(225, 182, 465, 662)))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # cv2.imshow("dw", image)
        # cv2.waitKey(0)

        self.state.fill(0)
        for y in reversed(range(20)):
            has_block = False
            for x in range(10):
                pixel = image[y * 24 + 12, x * 24 + 12]
                for color in SHAPE_COLORS:
                    if pixel == color:
                        self.state[y, x] = 1
                        has_block = True
            if not has_block:
                self.max_height = 19 - y
                break
        self.state = np.flip(self.state, 0)
        # pixel = image[0 * 24 + 12, 5 * 24 + 12]
        # for i, shape_color in enumerate(SHAPE_COLORS):
        #    if pixel == shape_color:
        #        self.current_piece = i
    def find_next_piece(self):
        image = np.array(ImageGrab.grab(bbox=(480, 210, 580, 250)))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # cv2.imshow("dw", image)
        # cv2.waitKey(0)
        pixel = image[25, 50]
        for i, color in enumerate(SHAPE_COLORS):
            if pixel == color:
                self.next_piece = i
                return
        pixel = image[19, 50]
        for i, color in enumerate(SHAPE_COLORS):
            if pixel == color:
                self.next_piece = i
                return

    def play(self, position, rotation):
        print("Pressing move ", position, " ", rotation)
        # print(position)
        # print(rotation)
        move_x = position - 4
        for i in range(rotation):
            self.keyboard.press(Key.up)
            self.keyboard.release(Key.up)
        if move_x < 0:
            for i in range(move_x * -1):
                self.keyboard.press(Key.left)
                self.keyboard.release(Key.left)
        elif move_x > 0:
            for i in range(move_x):
                self.keyboard.press(Key.right)
                self.keyboard.release(Key.right)
        self.keyboard.press(Key.space)
        self.keyboard.release(Key.space)
