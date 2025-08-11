import subprocess
import os
import shutil

import fire
import jinja2


nodes = {
    "researchhub-1.szidc",
    "researchhub-2.szidc",
    "researchhub-3.szidc",
    "researchhub-4.szidc",
    "researchhub-5.szidc",
    "researchhub-6.szidc",
    "researchhub-7.szidc",
    "researchhub-8.szidc",
    "ceph-3.szidc",
    "ceph-4.szidc",
}
env = jinja2.Environment()
with open("task.yaml.j2", "r") as f:
    template = env.from_string(f.read())


def main(dry_run: bool = False):
    shutil.rmtree("configs", ignore_errors=True)
    os.makedirs("configs", exist_ok=True)
    shutil.rmtree("output", ignore_errors=True)
    os.makedirs("output", exist_ok=True)
    for node in nodes:
        exclude_nodes = nodes.copy()
        exclude_nodes.remove(node)
        working_dir = os.path.realpath(".")
        conf = template.render(node=node, exclude_nodes=exclude_nodes, working_dir=working_dir)
        with open(os.path.join("configs", f"task-{node}.yaml"), "w") as f:
            f.write(conf)
    if not dry_run:
        for node in nodes:
            subprocess.run(f"contekray task create configs/task-{node}.yaml", shell=True)


if __name__ == "__main__":
    fire.Fire(main)
