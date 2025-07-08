from func import load_save,save_files, add_task, removing_tasks

# -----------------------------
# Main menu loop
# -----------------------------
def menu():
    removed_tasks = []
    tasks = load_save(save_files)

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. ➕ Add new task")
        print("2. ❌✅ Remove or complete task")
        print("3. 📋 View all tasks")
        print("4. 🚪 Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks, save_files)
        elif choice == "2":
            removed_tasks = removing_tasks(removed_tasks, tasks, save_files)
        elif choice == "3":
            if not tasks:
                print("📭 No tasks available.")
            else:
                print("\n📋 All Tasks:")
                for k, v in tasks.items():
                    print(f"{k}: {v['task']} {'✅' if v['state'] else '❌'}")
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("⚠️ Invalid input. Please try again.")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    menu()
