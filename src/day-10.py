import argparse
import collections
import functools

FOUND_T = 0

def show_grid(data, t):
        points = []
        for entry in data:
                position_x, position_y, velocity_x, velocity_y = entry 
                x = position_x + t * velocity_x
                y = position_y + t * velocity_y
                points.append((x, y))
        x_min = min(points, key = lambda x: x[0])[0]
        x_max = max(points, key = lambda x: x[0])[0]
        y_min = min(points, key = lambda x: x[1])[1]
        y_max = max(points, key = lambda x: x[1])[1]
        y_range = y_max - y_min + 1

        if y_range > 10:
                return False


        grid = [['.' for x in range(x_max - x_min + 1)] for y in range(y_max - y_min + 1)]
        for x, y in points:
                grid[y - y_min][x - x_min] = '#'

        for row in grid:
                print(''.join(row))

        global FOUND_T
        FOUND_T = t

        return True

def part_one(data):
        t = 0
        while not show_grid(data, t):
                t += 1

def part_two(data):
        return FOUND_T

def main(args):
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        split = line.replace('<', ' ').replace('>', ' ').replace(',', ' ').split()
                        position_x = int(split[1])
                        position_y = int(split[2])
                        velocity_x = int(split[4])
                        velocity_y = int(split[5])
                        data.append((position_x, position_y, velocity_x, velocity_y))
        print('Part one:')
        part_one(data)
        print('Part two:', part_two(data))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
