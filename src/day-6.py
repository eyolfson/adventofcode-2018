import argparse
import collections

def part_one(data):
        x_sorted = sorted(data, key = lambda x: x[0])
        y_sorted = sorted(data, key = lambda x: x[1])
        x_min = x_sorted[0][0]
        x_max = x_sorted[-1][0]
        y_min = y_sorted[0][1]
        y_max = y_sorted[-1][1]

        next_index = 1
        indicies = {}
        for x, y in data:
                indicies[next_index] = (x, y)
                next_index += 1

        num_indicies = collections.defaultdict(int)
        infinite_indicies = set()
        for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                        distances = {}
                        for index, (origin_x, origin_y) in indicies.items():
                                distances[index] = abs(x - origin_x) + abs(y - origin_y)
                        min_distances = sorted(distances.items(), key = lambda x: x[1])
                        if not min_distances[0][1] == min_distances[1][1]:
                                min_index = min_distances[0][0]
                                num_indicies[min_index] += 1
                                if x == x_min or x == x_max:
                                        infinite_indicies.add(min_index)
                                if y == y_min or y == y_max:
                                        infinite_indicies.add(min_index)

        for index, count in sorted(num_indicies.items(), key = lambda x: x[1], reverse = True):
                if index in infinite_indicies:
                        continue
                return count
        return None

def part_two(data):
        x_sorted = sorted(data, key = lambda x: x[0])
        y_sorted = sorted(data, key = lambda x: x[1])
        x_min = x_sorted[0][0]
        x_max = x_sorted[-1][0]
        y_min = y_sorted[0][1]
        y_max = y_sorted[-1][1]

        next_index = 1
        indicies = {}
        for x, y in data:
                indicies[next_index] = (x, y)
                next_index += 1

        LIMIT = 10000
        count = 0

        num_indicies = collections.defaultdict(int)
        infinite_indicies = set()
        for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                        total_distance = 0
                        for index, (origin_x, origin_y) in indicies.items():
                                total_distance += abs(x - origin_x) + abs(y - origin_y)
                        if total_distance < LIMIT:
                                count += 1
        return count

def main(args):
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        data.append(tuple([int(x) for x in line.strip().split(', ')]))
        print('Part one:', part_one(data))
        print('Part two:', part_two(data))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
