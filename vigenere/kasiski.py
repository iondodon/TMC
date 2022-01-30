# kasiski
#


import argparse
import os
import re
import sys
import time
from collections import Counter
from itertools import chain
from typing import List, Tuple


def get_args() -> argparse.Namespace:
    """
    Get the command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Kasiski test",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--input",
        type=str,
        default="input.txt",
        help="Input file"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="output.txt",
        help="Output file"
    )

    return parser.parse_args()


def get_message(filename: str) -> str:
    """
    Get the message from the file
    """
    with open(filename, "r") as f:
        message = f.read()

    return message


def get_key_length(message: str) -> int:
    """
    Get the key length
    """
    key_length = 0
    for i in range(1, len(message)):
        for j in range(0, len(message) - i):
            if message[j:j + i] * (len(message) // i) == message:
                key_length = i
                break

    return key_length


def get_key(message: str, key_length: int) -> str:
    """
    Get the key
    """
    key = ""
    for i in range(key_length):
        key += chr(ord("A") + Counter(message[i::key_length]).most_common(1)[0][0])

    return key


def get_key_from_file(filename: str) -> str:
    """
    Get the key from the file
    """
    with open(filename, "r") as f:
        key = f.read()

    return key


def get_key_from_message(message: str) -> str:
    """
    Get the key from the message
    """
    key_length = get_key_length(message)
    key = get_key(message, key_length)

    return key
