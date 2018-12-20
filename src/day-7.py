import argparse
import collections
import functools

def find_roots(data):
        roots = set()
        for step, _ in data:
                roots.add(step)
        for step, depends_on in data:
                if step == depends_on:
                        continue
                if depends_on in roots:
                        roots.remove(depends_on)
        return sorted(list(roots))

def find_minimum_root(data):
        roots = set()
        for step, _ in data:
                roots.add(step)
        for step, depends_on in data:
                if step == depends_on:
                        continue
                if depends_on in roots:
                        roots.remove(depends_on)
        min_root = roots.pop()
        for root in roots:
                if root < min_root:
                        min_root = root
        return min_root

def part_one(data):
        solution = []
        while len(data) != 0:
                roots = find_roots(data)
                solution.append(roots[0])
                data = list(filter(lambda x: x[0] != roots[0], data))
        return ''.join(solution)

def get_time(char):
        return ord(char) - ord('A') + 1 + 60

def part_two(data):
        workers = [['', 0], ['', 0], ['', 0], ['', 0], ['', 0]]
        current_time = 0
        while len(data) != 0:
                for i, worker in enumerate(workers):
                        if worker[0] != '' and worker[1] == current_time:
                                data = list(filter(lambda x: x[0] != worker[0], data))
                                worker[0] = ''
                for i, worker in enumerate(workers):
                        if worker[0] == '':
                                roots = find_roots(data)
                                for j, coworker in enumerate(workers):
                                        if i == j:
                                                continue
                                        if coworker[0] != '':
                                                roots.remove(coworker[0])
                                if len(roots) == 0:
                                        continue
                                root = roots[0]
                                worker[0] = root
                                worker[1] = current_time + get_time(root)
                current_time += 1
        return current_time - 1

def main(args):
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        step = line[5]
                        depends_on = line[36]
                        data.append((step, depends_on))
                        data.append((depends_on, depends_on))
        print('Part one:', part_one(data))
        print('Part two:', part_two(data))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
