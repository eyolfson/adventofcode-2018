import argparse

def part_one(path):
        freq = 0
        with open(args.path, 'r') as f:
                for line in f:
                        data = line.strip()
                        num = int(data[1:])
                        if data[0] == '-':
                                freq -= num
                        elif data[0] == '+':
                                freq += num
        print('Part one:', freq)

def part_two(path):
        freq = 0
        seen = set()
        seen.add(freq)
        while True:
                with open(args.path, 'r') as f:
                        for line in f:
                                data = line.strip()
                                num = int(data[1:])
                                if data[0] == '-':
                                        freq -= num
                                elif data[0] == '+':
                                        freq += num
                                if freq in seen:
                                        print('Part two:', freq)
                                        return
                                seen.add(freq)

def main(args):
        freq = 0
        part_one(args.path)
        part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
