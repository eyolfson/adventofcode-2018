import argparse
import collections

def part_one(path):
        twos = 0
        threes = 0
        with open(path, 'r') as f:
                for line in f:
                        data = collections.defaultdict(int)
                        for c in line.strip():
                                data[c] += 1
                        twos_counted = False
                        threes_counted = False
                        for k, v in data.items():
                                if v == 2 and not twos_counted:
                                        twos += 1
                                        twos_counted = True
                                elif v == 3 and not threes_counted:
                                        threes += 1
                                        threes_counted = True
        print('Part one:', twos * threes)

def part_two(path):
        data = []
        with open(path, 'r') as f:
                for line in f:
                        data.append(line.strip())
        for i, str1 in enumerate(data):
                for j, str2 in enumerate(data):
                        if i >= j:
                                continue
                        first_different_index = None
                        at_least_one_different = False
                        at_least_two_different = False
                        for k in range(len(str1)):
                                if str1[k] != str2[k]:
                                        if at_least_one_different:
                                                at_least_two_different = True
                                        if first_different_index is None:
                                                first_different_index = k
                                        at_least_one_different = True
                        if not at_least_two_different and at_least_one_different:
                                print('Part two:', end=' ')
                                for k, c in enumerate(str1):
                                        if first_different_index == k:
                                                continue
                                        print(c, end='')
                                print('')

def main(args):
        part_one(args.path)
        part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
