import json
import os

save_files = "save.json"

# -----------------------------
# Load tasks from JSON file
# -----------------------------
def load_save(save_files):
    if os.path.exists(save_files) and os.path.getsize(save_files) > 0:
        with open(save_files, "r") as file:
            tasks = json.load(file)
            return {int(k): v for k, v in tasks.items()}
    return {}

# -----------------------------
# Save tasks to JSON file
# -----------------------------
def saving_file(save_files, tasks):
    with open(save_files, "w") as file:
        json.dump(tasks, file, indent=4)

# -----------------------------
# Add task to list
# -----------------------------
def add_task(tasks, save_files):
    next_id = max(tasks.keys(), default=0) + 1

    while True:
        task = input("📝 Enter a new task (or 'x' to quit): ").strip()

        if task.lower() == "x":
            break

        tasks[next_id] = {"task": task, "state": False}
        saving_file(save_files, tasks)
        print(f"✅ Task added with ID {next_id}")
        next_id += 1

    return tasks

# -----------------------------
# Remove or complete tasks
# -----------------------------
def removing_tasks(removed_tasks, tasks, save_files):
    while True:
        if not tasks:
            print("⚠️ NO TASKS LEFT")
            break

        print("\n-- REMOVE / COMPLETE MENU --")
        print("1. Remove a task ❌")
        print("2. Mark task as completed ✅")
        print("3. Exit to main menu 🔙")

        state = input("Choose an option: ")

        # ------------------- Remove Task -------------------
        if state == "1":
            while True:
                if not tasks:
                    print("⚠️ NO TASKS LEFT")
                    break

                print("\n📋 Current Tasks:")
                for k, v in tasks.items():
                    print(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")

                removing_task = input("\nEnter ID to remove (or 'x' to cancel): ")

                if removing_task.lower() == "x":
                    break
                elif removing_task.isdigit():
                    removing_task_id = int(removing_task)

                    if removing_task_id in tasks:
                        removed_tasks.append(tasks.pop(removing_task_id))
                        saving_file(save_files, tasks)
                        print(f"❌ Task {removing_task_id} removed")
                    else:
                        print("⚠️ Task ID not found")
                else:
                    print("⚠️ Invalid input. Please enter a number.")

        # ------------------- Complete Task -------------------
        elif state == "2":
            while True:
                if not tasks:
                    print("⚠️ NO TASKS LEFT")
                    break

                print("\n📋 Current Tasks:")
                for k, v in tasks.items():
                    print(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")

                complete_task = input("\nEnter ID to mark as complete (or 'x' to cancel): ")

                if complete_task.lower() == "x":
                    break
                elif complete_task.isdigit():
                    complete_task_id = int(complete_task)

                    if complete_task_id in tasks:
                        tasks[complete_task_id]["state"] = True
                        saving_file(save_files, tasks)
                        print(f"✅ Task {complete_task_id} marked as complete")
                    else:
                        print("⚠️ Task ID not found")
                else:
                    print("⚠️ Invalid input. Please enter a number.")

        elif state == "3":
            break
        else:
            print("⚠️ Invalid option. Please select 1, 2, or 3.")

    return removed_tasks
