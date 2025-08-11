# test-contekray-tasks

A script to submit a contekray task and write/read cephfs on each node.

```
python3.11 -m venv .venv
pip install -r requirements.txt
python submit_tasks.py
```

To generate configs for tasks only and do not submit:
```
python submit_tasks.py --dry-run
```
