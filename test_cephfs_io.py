import os
import sys


node = sys.argv[1]
working_dir = sys.argv[2]
print(f"{node=}, {working_dir=}")
with open(os.path.join(working_dir, "output", node), "w") as f:
    f.write(node)

with open(os.path.join(working_dir, "output", node), "r") as f:
    raw = f.read()

assert node == raw
