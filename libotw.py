import argparse
import time
import pyperclip
import os
import re
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(prog="Track your overTheWire", description="enter and write the last challenge you made")
subparsers = parser.add_subparsers(dest="command")

def main(argv = sys.argv[1:]):
    args = parser.parse_args(argv)

    match args.command:
        case "connect": cmd_connect()

# connect option
argsp = subparsers.add_parser("connect", help="join the last challenge you registered")
def cmd_connect():
    with open("last_bandit", "r") as f:
        text = f.read()
    # get the level number and password
    regex = r"^bandit: (\d+)\s+password: (.+)$"
    re_obj = re.compile(regex)
    re_match = re_obj.search(text)

    level = re_match.group(1)
    password = re_match.group(2)

    pyperclip.copy(password)
    logger.info("password copied to your clipboard")
    logger.info(f"connecting to bandit{level}...\n")
    time.sleep(3)

    os.system(f"ssh bandit{level}@bandit.labs.overthewire.org -p 2220")
