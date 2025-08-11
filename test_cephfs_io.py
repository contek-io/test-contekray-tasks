import os
import sys


node = sys.argv[1]
print(f"{node=}")
with open(f"output/{node}", "w") as f:
    f.write(node)

with open(f"output/{node}", "r") as f:
    raw = f.read()

assert node == raw
