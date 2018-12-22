import argparse
import collections
import functools

def print_state(state, leftmost_pot, rightmost_pot):
        print('Leftmost pot:', leftmost_pot)
        for i in range(leftmost_pot, rightmost_pot + 1):
                if state[i]:
                        print('#', end='')
                else:
                        print('.', end='')
        print()

def get_num_from_generations(initial_state, data, generations):
        leftmost_pot = -2
        rightmost_pot = len(initial_state) + 1
        state = initial_state.copy()
        for _ in range(generations):
                next_state = state.copy()
                for i in range(leftmost_pot, rightmost_pot + 1):
                        entry = (state[i - 2], state[i - 1], state[i],
                                 state[i + 1], state[i + 2])
                        match = False
                        for before, after in data:
                                if entry == before:
                                        next_state[i] = after
                                        if i == leftmost_pot:
                                                leftmost_pot -= 2
                                        elif i == (leftmost_pot - 1):
                                                leftmost_pot -= 1
                                        elif i == rightmost_pot - 1:
                                                rightmost_pot += 1
                                        elif i == rightmost_pot:
                                                rightmost_pot += 2
                                        match = True
                                        break
                        if not match:
                                next_state[i] = False
                state = next_state
        num = 0
        for i in range(leftmost_pot, rightmost_pot + 1):
                if state[i]:
                        num += i
        return num

def part_one(initial_state, data):
        return get_num_from_generations(initial_state, data, 20)

def part_two(initial_state, data):
        num_150 = get_num_from_generations(initial_state, data, 150)
        diff = num_150 - get_num_from_generations(initial_state, data, 149)
        return (50000000000 - 150) * diff + num_150

def plant_char_to_bool(c):
        if c == '.':
                return False
        elif c == '#':
                return True
        else:
                assert False

def main(args):
        initial_state = collections.defaultdict(bool)
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        if line.startswith('initial state:'):
                                s = line[15:-1]
                                for i, c in enumerate(s):
                                        initial_state[i] = plant_char_to_bool(c)
                        elif line.startswith('.') or line.startswith('#'):
                                before, after = line.strip().split(' => ')
                                if not after:
                                        continue
                                data.append(
                                        (tuple(map(plant_char_to_bool, before)),
                                         plant_char_to_bool(after))
                                )
        print('Part one:', part_one(initial_state, data))
        print('Part two:', part_two(initial_state, data))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
