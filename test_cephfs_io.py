import os
import sys


node = sys.argv[1]
working_dir = sys.argv[2]
print(f"{node=}, {working_dir=}")

output_dir = os.path.join(working_dir, "output")
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, node)
if os.path.isfile(output_file):
    os.remove(output_file)

with open(output_file, "w") as f:
    f.write(node)

with open(output_file, "r") as f:
    raw = f.read()

assert node == raw
