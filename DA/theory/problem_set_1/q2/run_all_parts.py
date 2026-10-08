import subprocess
import sys

def print_tree_ascii(part_name):
        if part_name == "Part_A":
                print("Tree used in Part_A:")
                print("""
              1
            / | \\
          2   3   4
        /
       5
                """)
        elif part_name == "Part_B":
                print("Tree(s) used in Part_B:")
                print("Balanced tree:")
                print("""
              1
            / | \\
          2   3   4
        /
       5
                """)
                print("Unbalanced tree:")
                print("""
              1
            / | \\
          2   3   4
        /
      5
    /
  6
                """)

PARTS = [
    {
        "name": "Part_A",
        "file": "Part_A.py",
        "approach": "Brute Force",
        "expected": "Maximum Depth of the Ternary Tree: 3"
    },
    {
        "name": "Part_B",
        "file": "Part_B.py",
        "approach": "Brute Force",
        "expected": "Is the ternary tree balanced? True Is the ternary tree balanced? False"
    },
]

def run_part(part):
    print(f"===== {part['name']} =====\n")
    print(f"Approach: {part['approach']}")
    print_tree_ascii(part['name'])
    try:
        result = subprocess.run([sys.executable, part["file"]], capture_output=True, text=True, check=True)
        output = result.stdout.strip().replace('\n', ' ')
    except subprocess.CalledProcessError as e:
        print(f"Error running {part['file']}: {e}")
        return
    print(f"Output:   {output}")
    print(f"Expected: {part['expected']}")
    correct = output == part['expected']
    print(f"Correct:  {'YES ✅' if correct else 'NO ❌'}")
    print("------------------------------\n\n")

def main():
    print("--- Running All Parts ---\n")
    for part in PARTS:
        run_part(part)

if __name__ == "__main__":
    main()
