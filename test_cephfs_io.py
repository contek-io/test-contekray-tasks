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

# test cephfs
with open(output_file, "w") as f:
    f.write(node)
with open(output_file, "r") as f:
    raw = f.read()
assert node == raw

# test pid config
with open("/sys/fs/cgroup/pids.max", "r") as f:
    pid_max_config = f.read().strip()
print(f"pid_max_config = {pid_max_config}")
with open(output_file, "a") as f:
    f.write(f"\n{pid_max_config}")
assert pid_max_config == "max" or int(pid_max_config) > 200000
