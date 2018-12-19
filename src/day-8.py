import argparse
import collections
import functools

class Node:
        def __init__(self):
                self.children = []
                self.metadata = []

class Visitor:
        def __init__(self):
                self.root = Node()
                self.total_metadata = 0

        def visit_node(self, data, index = 0, node = None):
                if node is None:
                        node = self.root
                num_child_nodes = data[index]
                index += 1
                num_metadata_entries = data[index]
                index += 1
                for _ in range(num_child_nodes):
                        child = Node()
                        index = self.visit_node(data, index, child)
                        node.children.append(child)
                for _ in range(num_metadata_entries):
                        self.total_metadata += data[index]
                        node.metadata.append(data[index])
                        index += 1
                return index

def part_one(node):
        total = 0
        for child in node.children:
                total += part_one(child)
        for value in node.metadata:
                total += value
        return total

def part_two(node):
        if len(node.children) == 0:
                return functools.reduce(lambda x, y: x + y, node.metadata)
        value = 0
        for index in node.metadata:
                if index == 0 or index > len(node.children):
                        continue
                value += part_two(node.children[index - 1])
        return value
                
def main(args):
        with open(args.path, 'r') as f:
                for line in f:
                        data = [int(x) for x in line.strip().split()]

        visitor = Visitor()
        visitor.visit_node(data)
        root = visitor.root

        print('Part one:', part_one(root))
        print('Part two:', part_two(root))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
