import argparse
import collections
import re

def part_one(path):
        data = [[set() for x in range(1000)] for x in range(1000)]
        pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        with open(path, 'r') as f:
                for line in f:
                        result = pattern.match(line.strip())
                        ident = int(result.group(1))
                        x = int(result.group(2))
                        y = int(result.group(3))
                        width = int(result.group(4))
                        height = int(result.group(5))
                        for i in range(width):
                                for j in range(height):
                                        data[x + i][y + j].add(ident)
        num = 0
        for i in range(1000):
                for j in range(1000):
                        if len(data[i][j]) > 1:
                                num += 1
        print('Part one:', num)
                                        

def part_two(path):
        pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        inputs = {}
        with open(path, 'r') as f:
                for line in f:
                        result = pattern.match(line.strip())
                        ident = int(result.group(1))
                        x = int(result.group(2))
                        y = int(result.group(3))
                        width = int(result.group(4))
                        height = int(result.group(5))
                        inputs[ident] = (x, y, width, height)

        data = [[set() for x in range(1000)] for x in range(1000)]
        could_be_only = set()
        for ident, tup in inputs.items():
                x, y, width, height = tup
                possible = True
                for i in range(width):
                        for j in range(height):
                                if len(data[x + i][y + j]) >= 1:
                                        possible = False
                                data[x + i][y + j].add(ident)
                if possible:
                        could_be_only.add(ident)

        for ident in could_be_only:
                x, y, width, height = inputs[ident]
                found = False
                for i in range(width):
                        for j in range(height):
                                if len(data[x + i][y + j]) > 1:
                                        found = True
                                        continue
                        if found:
                                continue
                if not found:
                        print('Part two:', ident)

def main(args):
        part_one(args.path)
        part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
