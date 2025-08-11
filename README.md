# test-contekray-tasks

A script to submit a contekray task and write/read cephfs on each node.

NOTE: make sure you are on a path that you want to test. For example, if you want to test `/cephfs`, you should log on to a gate node (e.g. researchhub-1) and run the following commands under `/cephfs/<username>/`. This makes sure that you have the correct permissions.

```
python3.11 -m venv .venv
pip install -r requirements.txt
python submit_tasks.py
```

To generate configs for tasks only and do not submit:
```
python submit_tasks.py --dry-run
```
