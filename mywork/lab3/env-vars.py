#!/c/msys64/ucrt64/bin/python3

import os

os.environ["MAJOR"] = input("What's your major?")
os.environ["MINOR"] = input("What's your minor?")
os.environ["IS_MINOR"] = input("Are you a minor?")

print(os.environ["MAJOR"], os.environ["MINOR"], os.environ["IS_MINOR"])