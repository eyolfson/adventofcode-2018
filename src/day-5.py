import argparse
import collections
import functools

def part_one(polymer):
        polymer = polymer[:]
        length = len(polymer)
        for i in range(1, len(polymer)):
                j = i - 1
                while j >= 0 and polymer[j] == ' ':
                        j -= 1
                if j >= 0 and polymer[i].lower() == polymer[j].lower() and polymer[i].islower() ^ polymer[j].islower():
                        polymer[j] = ' '
                        polymer[i] = ' '
                        length -= 2
        return length

def remove_letter(letter, polymer):
        new_polymer = []
        for c in polymer:
                if c.lower() != letter:
                        new_polymer.append(c)
        return new_polymer

def part_two(polymer):
        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        min_length = None
        for letter in letters:
                smaller_polymer = remove_letter(letter, polymer)
                length = part_one(smaller_polymer)
                if min_length is None:
                        min_length = length
                elif length < min_length:
                        min_length = length
        return min_length

def main(args):
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        polymer = list(line.strip())
                        break

        print('Part one:', part_one(polymer))
        print('Part two:', part_two(polymer))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
