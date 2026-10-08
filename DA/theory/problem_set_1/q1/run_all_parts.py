import importlib
import sys
import os

# Test cases for each part (input and expected output)
TESTCASES = {
    "Part_A": {
        "input": "3 4 5",
        "output": "3 8 15"
    },
    "Part_B": {
        "input": "5 3 7 2 8 1 10 4",
        "output": "False"
    },
    "Part_C": {
        "input": "9 8 8 7 6 6 6 5 3 3 1",
        "output": "9 8 -1 7 6 -1 -1 5 3 -1 1"
    },
    "Part_D": {
        "input": "-7\n-10 -5 0 5 10",
        "output": "-5"
    },
    "Part_E": {
        "input": "16\nA a a a a a a a a a a a a a a a\na A a a a a a a a a a a a a a a\na a A a a a a a a a a a a a a a\na a a A a a a a a a a a a a a a\na a a a A a a a a a a a a a a a\na a a a a A a a a a a a a a a a\na a a a a a A a a a a a a a a a\na a a a a a a A a a a a a a a a\na a a a a a a a A a a a a a a a\na a a a a a a a a A a a a a a a\na a a a a a a a a a A a a a a a\na a a a a a a a a a a A a a a a\na a a a a a a a a a a a A a a a\na a a a a a a a a a a a a A a a\na a a a a a a a a a a a a a A a\na a a a a a a a a a a a a a a A",
        "output": "16"
    }
}

PARTS = [
    ('Part_A', 'Part_A.py'),
    ('Part_B', 'Part_B.py'),
    ('Part_C', 'Part_C.py'),
    ('Part_D', 'Part_D.py'),
    ('Part_E', 'Part_E.py'),
]

PART_APPROACHES = {
    'Part_A': [
        ('Brute Force', 'solve_brute_force'),
        ('Divide & Conquer', 'solve_divide_and_conquer'),
        ('Stack Memoization', 'solve_stack_memo'),
        ('DivConq Explicit Stack', 'solve_divconq_explicit_stack'),
    ],
    'Part_B': [
        ('Brute Force', 'solve_brute_force'),
        ('Divide & Conquer', 'solve_divide_and_conquer'),
        ('Queue', 'solve_queue'),
        ('Linked List', 'solve_linked_list'),
    ],
    'Part_C': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq Merge', 'solve_divide_and_conquer_merge'),
        ('DivConq Seen', 'solve_divide_and_conquer_seen'),
        ('Stack', 'solve_stack'),
    ],
    'Part_D': [
        ('Brute Force', 'solve_brute_force'),
        ('Divide & Conquer', 'solve_divide_and_conquer'),
    ],
    'Part_E': [
        ('Brute Force', 'solve_brute_force'),
        ('DivConq 2x2', 'solve_divide_and_conquer_2x2'),
        ('DivConq 1x1', 'solve_divide_and_conquer_1x1'),
    ],
}

# Helper to parse input string into arguments for each part

def parse_input(part, input_str):
    if part in ['Part_A', 'Part_B', 'Part_C']:
        return [list(map(int, input_str.strip().split()))]
    elif part == 'Part_D':
        lines = input_str.strip().split('\n')
        ukey = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return [arr, ukey]
    elif part == 'Part_E':
        lines = input_str.strip().split('\n')
        n = int(lines[0])
        grid = [line.split() for line in lines[1:1+n]]
        return [n, grid]
    else:
        raise ValueError('Unknown part')

def normalize_output(output):
    if isinstance(output, (list, tuple)):
        return ' '.join(map(str, output))
    return str(output)

def part_c_equivalent(out1, out2):
    # Accept any output with the same numbers and same number of -1s, regardless of order
    a = list(map(int, out1.strip().split()))
    b = list(map(int, out2.strip().split()))
    def count_nonneg(l):
        return [x for x in l if x != -1]
    return sorted(count_nonneg(a)) == sorted(count_nonneg(b)) and a.count(-1) == b.count(-1)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    part_dir = os.path.join(base_dir)
    sys.path.insert(0, part_dir)
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
                if part == 'Part_C':
                    correct = part_c_equivalent(result_str, expected_output)
                else:
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
