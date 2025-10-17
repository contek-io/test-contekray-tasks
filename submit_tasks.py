import subprocess
import os
import shutil

import fire
import jinja2


nodes = {
    "ceph-3.szidc",
    "ceph-4.szidc",
    "researchhub-1.szidc",
    "researchhub-2.szidc",
    "researchhub-3.szidc",
    "researchhub-4.szidc",
    "researchhub-5.szidc",
    "researchhub-6.szidc",
    "researchhub-7.szidc",
    "researchhub-8.szidc",
    "researchhub-9.szidc",
    "researchhub-10.szidc",
    "researchhub-11.szidc",
}

env = jinja2.Environment()
with open("task.yaml.j2", "r") as f:
    template = env.from_string(f.read())


def main(dry_run: bool = False, working_dir:str = "", retry:int=0, run_nodes:str = "", name_prefix:str = "test"):
    shutil.rmtree("configs", ignore_errors=True)
    os.makedirs("configs", exist_ok=True)
    shutil.rmtree("output", ignore_errors=True)
    os.makedirs("output", exist_ok=True)

    if not working_dir:
        working_dir = os.path.realpath(".")
    for node in nodes:
        exclude_nodes = nodes - {node}
        conf = template.render(
            node=node,
            exclude_nodes=exclude_nodes,
            working_dir=working_dir,
            retry=retry,
            name_prefix=name_prefix
        )
        with open(os.path.join("configs", f"task-{node}.yaml"), "w") as f:
            f.write(conf)

    if not dry_run:
        node_list = run_nodes.split(',')
        node_list = [i.strip() for i in node_list if i.strip()]
        if not node_list:
            node_list = list(nodes)
        for node in node_list:
            cmd = f"contekray task create configs/task-{node}.yaml"
            print("Runing", cmd)
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    fire.Fire(main)
