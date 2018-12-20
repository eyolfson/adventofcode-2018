import argparse
import collections
import functools

def get_grid(serial_number):
        grid = [[0 for _ in range(300)] for _ in range(300)]
        for j in range(300):
                for i in range(300):
                        x = i + 1
                        y = j + 1
                        rack_id = x + 10
                        power_level = rack_id * y + serial_number
                        power_level *= rack_id
                        hundreds_digit = (power_level // 100) % 10
                        power_level = hundreds_digit - 5
                        grid[j][i] = power_level
        return grid

def part_one(grid):
        powers = {}
        for j in range(298):
                for i in range(298):
                        total_power = 0
                        for l in range(3):
                                for k in range(3):
                                        total_power += grid[j + l][i + k]
                        x = i + 1
                        y = j + 1
                        powers[(x, y)] = total_power
        s = sorted(powers.items(), key = lambda x: x[1], reverse = True)
        return '{},{}'.format(s[0][0][0], s[0][0][1])

def part_two(grid):
        powers = {}
        best = 0
        best_answer = ''
        for k in range(1, 301):
                for j in range(300 - k + 1):
                        for i in range(300 - k + 1):
                                total_power = 0
                                for dj in range(k):
                                        for di in range(k):
                                                total_power += grid[j + dj][i + di]
                                x = i + 1
                                y = j + 1
                                if total_power > best:
                                        best = total_power
                                        best_answer = '{},{},{}'.format(x, y, k)
        return best_answer

def main(args):
        with open(args.path, 'r') as f:
                for line in f:
                        serial_number = int(line.strip())
        grid = get_grid(serial_number)
        print('Part one:', part_one(grid))
        print('Part two:', part_two(grid))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
