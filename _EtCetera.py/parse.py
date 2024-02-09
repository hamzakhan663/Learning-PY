import argparse

#create an argument parser object named parse
parser = argparse.ArgumentParser()
#define command line argument
parser.add_argument('-n', default=1, help='no of times to meow', type=int)
#call parse.args method on parser object to parse the command line arguments
args = parser.parse_args()

#print message according to the value of args.n
for _ in range(args.n):
    print ("meow")