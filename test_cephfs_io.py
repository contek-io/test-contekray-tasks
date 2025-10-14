import os
import sys
import shutil


node = sys.argv[1]
working_dir = sys.argv[2]
print(f"{node=}, {working_dir=}")

output_dir = os.path.join(working_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# 文件读写
output_file = os.path.join(output_dir, node)
if os.path.isfile(output_file):
    os.remove(output_file)

with open(output_file, "w") as f:
    f.write(node)

with open(output_file, "r") as f:
    raw = f.read()

assert node == raw

# 目录创建
dir_test = os.path.join(output_dir, node+"_test_dir")
if os.path.isdir(dir_test):
    shutil.rmtree(dir_test)
os.makedirs(dir_test)
assert os.path.isdir(dir_test)

# max pid 配置
with open("/sys/fs/cgroup/pids.max", "r") as f:
    pid_max_config = f.read().strip()

with open(output_file, "a") as f:
    f.write(f"\n{pid_max_config}")

assert pid_max_config == "max" or int(pid_max_config) > 200000
