
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--text", default = "No text provided", help = "enter some text here in quotes")
parser.add_argument("--verbose", action = 'store_true', help = "enable verbose mode")

args = parser.parse_args()

if args.verbose == True:
    print(args.text, args.verbose)

print(args.text)