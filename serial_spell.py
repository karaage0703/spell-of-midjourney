#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import argparse
import pyautogui
import time

if __name__ == '__main__':
    quality_values = [1]
    stylize_values = [625, 1250, 2500, 20000, 60000]

    for quality in quality_values:
        for stylize in stylize_values:
            time.sleep(3)

            pyautogui.write('/imagine')
            pyautogui.press('tab')
            pyautogui.hotkey('command', 'v')
            option_words = str(' --quality ') + str(quality) + str(' --stylize ') + str(stylize)
            pyautogui.write(option_words)
            pyautogui.press('enter')
