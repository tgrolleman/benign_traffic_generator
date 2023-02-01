#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
import time

def main():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--file', '-f')
    params = parser.parse_args()

    file1 = open(params.file, 'r')

    for i in file1:
        try:
            result = subprocess.run(
                ["lynx", "-accept_all_cookies", "-dump", i.replace("\n", "")],
                timeout=3,
            )
        except subprocess.TimeoutExpired as err:
            print("[Error] ", err)
        except subprocess.CalledProcessError as err:
            print("[Error] ", err.stderr)
        except Exception as err:
            print(err)
        time.sleep(1)

if __name__ == '__main__':
    main()