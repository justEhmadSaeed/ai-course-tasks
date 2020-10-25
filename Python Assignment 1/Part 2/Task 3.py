# Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data: {'1': ['a', 'b'], '2': ['c', 'd']}
# Expected Output:
# ac
# ad
# bc
# bd

import itertools      

sample = {'1': ['a', 'b'], '2': ['c', 'd']}

for combine in itertools.product(*[sample[k] for k in sorted(sample.keys())]):
    print(''.join(combine))