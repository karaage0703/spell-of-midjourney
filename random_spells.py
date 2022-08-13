#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import pyautogui
import time
import random


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--word_numb', type=int, default=3)
    parser.add_argument('-n', '--spell_numb', type=int, default=5)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()
    random.seed()

    with open('/usr/share/dict/words', 'r') as f:
        lines = f.readlines()

    input_words = [0] * args.word_numb

    for spell_numb in range(args.spell_numb):
        time.sleep(3)
        for i in range(args.word_numb):
            input_words[i] = lines[random.randint(1, len(lines)-1)].strip()

        spell = '/imagine'
        pyautogui.write(spell)
        pyautogui.press('tab')
        for word in input_words:
            pyautogui.write(word + ' ')

        pyautogui.press('enter')
