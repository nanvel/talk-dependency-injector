import sys
from pprint import pp
from datetime import datetime

import shelve


DB_PATH = "naive_tasks.db"


def main(args, shelf):
    cmd = args[0]
    tasks = shelf.get("tasks", [])
    sequence = shelf.get("sequence", 0)

    if cmd == "create":
        text = args[1]
        tasks.append(
            {
                "id": sequence,
                "text": text,
                "priority": 0,
                "created_ts": datetime.utcnow(),
            }
        )
        shelf["tasks"] = tasks
        shelf["sequence"] = sequence + 1
    elif cmd == "print":
        for task in sorted(tasks, key=lambda i: i["priority"], reverse=True):
            pp(task)
    elif cmd == "delete":
        task_id = int(args[1])
        shelf["tasks"] = [task for task in tasks if task["id"] != task_id]
    elif cmd == "edit":
        task_id = int(args[1])
        text = args[2]
        for task in tasks:
            if task["id"] == task_id:
                task["text"] = text
                break
        shelf["tasks"] = [dict(task) for task in tasks]
    elif cmd == "set-priority":
        task_id = int(args[1])
        priority = int(args[2])
        for task in tasks:
            if task["id"] == task_id:
                task["priority"] = priority
                break
        shelf["tasks"] = [dict(task) for task in tasks]


if __name__ == "__main__":
    with shelve.open(DB_PATH) as shelf:
        main(sys.argv[1:], shelf=shelf)
