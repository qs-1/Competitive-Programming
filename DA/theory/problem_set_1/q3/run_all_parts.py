import importlib
import sys
import os

# Test cases for each part (input and expected output)
TESTCASES = {
    "Part_A": {
        "input": "listen\nsilent",
        "output": "True"
    },
    "Part_B": {
        "input": "10 50 30 60 20 40",
        "output": "40"
    },
    "Part_C": {
        "input": "3\nabcdef",
        "output": "defabc"
    },
    "Part_D": {
        "input": "16",
        "output": "-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-\n-#-#-#-#-#-#-#-#\n#-#-#-#-#-#-#-#-"
    },
    "Part_E": {
        "input": "1 2 3 4 5\n4 3 2 5 1",
        "output": "True"
    },
    "Part_F": {
        "input": "1 2 3 4",
        "output": "2 1 4 3"
    },
    "Part_G": {
        "input": "RRRRRRRRRRSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTT",
        "output": "20"
    },
    "Part_H": {
        "input": "2 5 8 11 14 17 20 23 26 29 32 35 38 41 44 47 50 53 56 59",
        "output": "177"
    }
}

# Map part to approach function names (in order of appearance in the file)
PART_APPROACHES = {
    'Part_A': [
        ('Oneliner nlogn', 'solve_oneliner_nlogn'),
        ('Hashmap Linear', 'solve_hashmap_linear'),
        ('DivConq Hashmap Linear', 'solve_divconq_hashmap_linear'),
        ('Bad DivConq n2logn', 'solve_bad_divconq_n2logn'),
    ],
    'Part_B': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq', 'solve_divconq'),
    ],
    'Part_C': [
        ('Iterative', 'solve_iterative'),
        ('DivConq', 'solve_divconq'),
    ],
    'Part_D': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq', 'solve_divconq'),
    ],
    'Part_E': [
        ('Oneliner nlogn', 'solve_oneliner_nlogn'),
        ('Hashmap Linear', 'solve_hashmap_linear'),
        ('DivConq Hashmap Linear', 'solve_divconq_hashmap_linear'),
        ('Bad DivConq n2logn', 'solve_bad_divconq_n2logn'),
    ],
    'Part_F': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq', 'solve_divconq'),
    ],
    'Part_G': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq', 'solve_divconq'),
        ('BS Recursive', 'solve_bs_recursive'),
        ('BS Iterative', 'solve_bs_iterative'),
    ],
    'Part_H': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq', 'solve_divconq'),
    ],
}

PARTS = [
    ('Part_A', 'Part_A.py'),
    ('Part_B', 'Part_B.py'),
    ('Part_C', 'Part_C.py'),
    ('Part_D', 'Part_D.py'),
    ('Part_E', 'Part_E.py'),
    ('Part_F', 'Part_F.py'),
    ('Part_G', 'Part_G.py'),
    ('Part_H', 'Part_H.py'),
]

def parse_input(part, input_str):
    if part in ['Part_A', 'Part_E']:
        # anagram: string input, two lines
        lines = input_str.strip().split('\n')
        s = list(lines[0]) if part == 'Part_A' else lines[0].split()
        t = list(lines[1]) if part == 'Part_A' else lines[1].split()
        return [s, t]
    elif part in ['Part_B', 'Part_F', 'Part_H']:
        return [list(map(int, input_str.strip().split()))]
    elif part == 'Part_C':
        lines = input_str.strip().split('\n')
        k = int(lines[0])
        s = list(lines[1])
        return [k, s]
    elif part == 'Part_D':
        n = int(input_str.strip())
        return [n]
    elif part == 'Part_G':
        s = list(input_str.strip())
        return [s]
    else:
        raise ValueError('Unknown part')

def normalize_output(output):
    if isinstance(output, (list, tuple)):
        # For board outputs (Part_D), join with newlines
        if all(isinstance(x, str) for x in output):
            return '\n'.join(output)
        return ' '.join(map(str, output))
    return str(output)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)
    print('--- Running All Parts ---')
    for idx, (part, pyfile) in enumerate(PARTS):
        print(f'\n===== {part} =====\n')
        test_input = TESTCASES[part]['input']
        expected_output = TESTCASES[part]['output'].strip()
        mod_name = pyfile[:-3]
        mod = importlib.import_module(mod_name)
        for approach_name, func_name in PART_APPROACHES[part]:
            func = getattr(mod, func_name)
            args = parse_input(part, test_input)
            try:
                result = func(*args)
                result_str = normalize_output(result)
                correct = (result_str.strip() == expected_output)
            except Exception as e:
                result_str = f'Error: {e}'
                correct = False
            emoji = '✅' if correct else '❌'
            print(f'Approach: {approach_name}')
            print(f'Output:   {result_str}')
            print(f'Expected: {expected_output}')
            print(f'Correct:  {"YES" if correct else "NO"} {emoji}')
            print('-'*30)
        if idx != len(PARTS)-1:
            print()  # Extra space between parts

if __name__ == '__main__':
    main()
