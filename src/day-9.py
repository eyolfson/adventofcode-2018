import argparse
import collections
import functools

def part_one(players, last_marble_points):
        marbles = collections.deque([0])
        scores = collections.defaultdict(int)
        current_player = 1
        for num in range(1, last_marble_points + 1):
                if num % 23 == 0:
                        marbles.rotate(7)
                        scores[current_player] += num + marbles.pop()
                        marbles.rotate(-1)
                else:
                        marbles.rotate(-1)
                        marbles.append(num)

                current_player += 1
                if current_player > players:
                        current_player = 1
        return max(scores.values())

def part_two(players, last_marble_points):
        return part_one(players, last_marble_points * 100)

def main(args):
        with open(args.path, 'r') as f:
                for line in f:
                        s = line.strip().split()
                        players = int(s[0])
                        last_marble_points = int(s[6])
        print('Part one:', part_one(players, last_marble_points))
        print('Part two:', part_two(players, last_marble_points))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
