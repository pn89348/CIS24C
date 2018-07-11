
import argparse
import helper

parser = argparse.ArgumentParser()

parser.add_argument("--num1", type = int, default = 0, help = "enter the first number")
parser.add_argument("--num2", type = int, default = 0, help = "enter the second number")

args = parser.parse_args()

num1 = args.num1
num2 = args.num2

print(helper.add(num1, num2))