import json as js
import datetime as dt
import shutil as st
from colorama import *

init(autoreset=True)

width = st.get_terminal_size().columns

title = Fore.CYAN + Style.BRIGHT + " TODO LIST " + Style.RESET_ALL


# ------------------- FILE FUNCTIONS -------------------

def Add(file):

    with open("todo.json", "w") as y:
        js.dump(file, y, indent=4)


def load():

    with open("todo.json", "r") as y:
        return js.load(y)


# ---------------------- CLASS -------------------------

class Todo:

    def __init__(self):

        try:

            with open("todo.json", "x") as y:
                js.dump([[], [], [], []], y)

        except FileExistsError:

            data = load()
            n_data = data[0] + data[1] + data[2] + data[3]

            if len(n_data) != 0:

                for i in range(len(data)):

                    for a in range(len(data[i])):

                        try:

                            if data[i][a]["due"] != "none":

                                if data[i][a]["due"] != "OVERDUE⚠️":

                                    if dt.date.fromisoformat(
                                        data[i][a]["due"]
                                    ) < dt.date.today():

                                        data[i][a]["due"] = "OVERDUE⚠️"

                        except:
                            pass

                Add(data)

    # ---------------- PRIORITY SORT ----------------

    def sort_priority(self, n_data):

        a_data = [x for x in n_data if x["priority"] == "HIGH"]
        b_data = [x for x in n_data if x["priority"] == "MID "]
        c_data = [x for x in n_data if x["priority"] == "LOW "]
        d_data = [x for x in n_data if x["priority"] == "none"]

        return [a_data, b_data, c_data, d_data]

    # -------------------- ADD ----------------------

    def add(self, task, prio, due):

        data = load()

        if prio == "1":
            priority = "HIGH"

        elif prio == "2":
            priority = "MID "

        elif prio == "3":
            priority = "LOW "

        else:
            priority = "none"

        if due != "none":
            due = due.isoformat()

        data[int(prio)-1].append({

            "task": task,
            "is done": "❌",
            "priority": priority,
            "due": due
        })

        Add(data)

    # -------------------- SHOW ---------------------

    def show(self):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        if len(n_data) == 0:
            return "none"

        print(f'{"":=^{width}}')

        for i, task in enumerate(n_data, start=1):

            if task["is done"] == "❌":

                stt = width - len(task['task']) - 5
                du = width - 18

                print(

                    f"{i}.{task['task']}"
                    f"{f'status:{task['is done']}':>{stt}}\n\n"
                    f" priority:{task['priority']}"
                    f"{f'(due:{task['due']})':>{du}}"
                )

            else:

                print(

                    f"{i}.{task['task']}"
                    f"{f'status:{task['is done']}':>{44-len(task['task'])}}:-\n\n"
                    f" 👏congratulations🎉"
                )

            print(f'{"":=^{width}}')

    # -------------------- DELETE -------------------

    def delete(self, task):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        if len(n_data) == 0:
            return "none"

        elif task > len(n_data) or task < 1:
            return "vn"

        n_data.pop(task-1)

        Add(self.sort_priority(n_data))

        return "done"

    # --------------------- MARK --------------------

    def mark(self, task):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        if len(n_data) == 0:
            return "none"

        elif task > len(n_data) or task < 1:
            return "vn"

        if n_data[task-1]["is done"] == "✅":
            return "added"

        n_data[task-1]["is done"] = "✅"

        Add(self.sort_priority(n_data))

        return "done"

    # ------------------- UNMARK --------------------

    def unmark(self, task):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        if len(n_data) == 0:
            return "none"

        elif task > len(n_data) or task < 1:
            return "vn"

        if n_data[task-1]["is done"] == "❌":
            return "added"

        n_data[task-1]["is done"] = "❌"

        Add(self.sort_priority(n_data))

        return "done"

    # -------------------- CLEAR --------------------

    def clear(self):

        Add([[], [], [], []])

    # ------------------- SEARCH --------------------

    def search(self, task):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        if len(n_data) == 0:
            return "none"

        a_list = [

            y for y in n_data
            if task.lower() in y["task"].lower()
        ]

        if len(a_list) == 0:
            return "s_none"

        print(f'{"":=^{width}}')

        for i, task in enumerate(a_list, start=1):

            if task["is done"] == "❌":

                print(

                    f"{i}.{task['task']}"
                    f"{f'status:{task['is done']}':>{55-len(task['task'])}}\n\n"
                    f" priority:{task['priority']}"
                    f"{f'(due:{task['due']})':>44}"
                )

            else:

                print(

                    f"{i}.{task['task']}"
                    f"{f'status:{task['is done']}':>{55-len(task['task'])}}:-\n\n"
                    f" 👏congratulations🎉"
                )

            print(f'{"":=^{width}}')

    # -------------------- IS IN --------------------

    def is_in(self, task):

        data = load()

        n_data = data[0] + data[1] + data[2] + data[3]

        a_data = [x["task"].lower() for x in n_data]

        if task.lower() in a_data:
            return True


# -------------------- OBJECT -------------------------

a = Todo()

# -------------------- HEADER -------------------------

print(f"{title:@^{width+10}}\n")

print(Fore.MAGENTA + f"{'':®^{width}}")

# --------------------- MENU --------------------------

menu = (

    Fore.YELLOW +

    "\n1.show"
    "\n2.add"
    "\n3.delete"
    "\n4.mark task"
    "\n5.unmark task"
    "\n6.search"
    "\n7.clear list"
    "\n8.exit"

    "\n\nans(1-8): "

    + Style.DIM
)

# --------------------- MENU --------------------------

while True:

    try:

        command = int(input(menu))

        if command < 1 or command > 8:
            raise ValueError

    except ValueError:

        print(
            Fore.RED +
            Style.BRIGHT +
            "\nENTER A VALID NUMBER\n"
        )

        continue

    print(Fore.MAGENTA + f"{'':÷^{width}}")

    # ---------------- MATCH CASE ----------------

    match command:

        # ---------------- SHOW ----------------

        case 1:

            print(f"{Fore.WHITE+'TASKS':^{width}}")

            reply = a.show()

            if reply == "none":

                print(
                    f'{Fore.RED+Style.BRIGHT+"NOTHING INSIDE THE LIST":^{width}}'
                )

        # ---------------- ADD ----------------

        case 2:

            task = input(
                Fore.YELLOW +
                Style.DIM +
                "\nenter your task: "
            )

            if a.is_in(task):

                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\nTASK ALREADY EXISTS\n"
                )

                continue

            try:

                prio = input(
                    Fore.YELLOW +
                    Style.DIM +
                    "\npriority (1,2,3,4): "
                )

                if int(prio) < 1 or int(prio) > 4:
                    raise ValueError

            except ValueError:

                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\nENTER VALID PRIORITY\n"
                )

                continue

            while True:

                rdue = input(

                    Fore.YELLOW +
                    Style.DIM +
                    "\ndo you want to add due date? (y/n): "
                )

                match rdue:

                    # ---------- YES ----------

                    case "y":

                        try:

                            ddue = int(input(

                                Fore.YELLOW +
                                Style.DIM +
                                "\nhow many days left?: "
                            ))

                        except ValueError:

                            print(

                                Fore.RED +
                                Style.BRIGHT +
                                "\nENTER VALID NUMBER\n"
                            )

                            continue

                        due = (
                            dt.date.today() +
                            dt.timedelta(days=ddue)
                        )

                        a.add(task, prio, due)

                        print(

                            Fore.GREEN +
                            "\nTASK ADDED SUCCESSFULLY 👍\n"
                        )

                        break

                    # ---------- NO ----------

                    case "n":

                        a.add(task, prio, "none")

                        print(

                            Fore.GREEN +
                            "\nTASK ADDED SUCCESSFULLY 👍\n"
                        )

                        break

                    # ---------- INVALID ----------

                    case _:

                        print(

                            Fore.RED +
                            Style.BRIGHT +
                            "\nENTER y/n ONLY\n"
                        )

        # ---------------- DELETE ----------------

        case 3:

            reply = a.show()

            if reply == "none":

                print(
                    Fore.RED +
                    "NOTHING INSIDE THE LIST"
                )

                continue

            try:

                task = int(input(

                    Fore.YELLOW +
                    Style.DIM +
                    "\nwhich task do you want to delete?: "
                ))

            except ValueError:

                print(
                    Fore.RED +
                    "ENTER A VALID NUMBER"
                )

                continue

            reply = a.delete(task)

            match reply:

                case "vn":

                    print(
                        Fore.RED +
                        "ENTER VALID TASK NUMBER"
                    )

                case "done":

                    print(
                        Fore.GREEN +
                        "TASK DELETED SUCCESSFULLY 👍"
                    )

        # ---------------- MARK ----------------

        case 4:

            reply = a.show()

            if reply == "none":

                print(
                    Fore.RED +
                    "NOTHING INSIDE THE LIST"
                )

                continue

            try:

                task = int(input(

                    Fore.YELLOW +
                    Style.DIM +
                    "\nwhich task do you want to mark?: "
                ))

            except ValueError:

                print(
                    Fore.RED +
                    "ENTER VALID NUMBER"
                )

                continue

            reply = a.mark(task)

            match reply:

                case "vn":

                    print(
                        Fore.RED +
                        "ENTER VALID TASK NUMBER"
                    )

                case "added":

                    print(
                        Fore.RED +
                        "TASK ALREADY MARKED"
                    )

                case "done":

                    print(
                        Fore.GREEN +
                        "TASK MARKED SUCCESSFULLY 👍"
                    )

        # ---------------- UNMARK ----------------

        case 5:

            reply = a.show()

            if reply == "none":

                print(
                    Fore.RED +
                    "NOTHING INSIDE THE LIST"
                )

                continue

            try:

                task = int(input(

                    Fore.YELLOW +
                    Style.DIM +
                    "\nwhich task do you want to unmark?: "
                ))

            except ValueError:

                print(
                    Fore.RED +
                    "ENTER VALID NUMBER"
                )

                continue

            reply = a.unmark(task)

            match reply:

                case "vn":

                    print(
                        Fore.RED +
                        "ENTER VALID TASK NUMBER"
                    )

                case "added":

                    print(
                        Fore.RED +
                        "TASK ALREADY UNMARKED"
                    )

                case "done":

                    print(
                        Fore.GREEN +
                        "TASK UNMARKED SUCCESSFULLY 👍"
                    )

        # ---------------- SEARCH ----------------

        case 6:

            task = input(

                Fore.YELLOW +
                Style.DIM +
                "\nsearch task: "
            )

            reply = a.search(task)

            match reply:

                case "none":

                    print(
                        Fore.RED +
                        "NOTHING INSIDE THE LIST"
                    )

                case "s_none":

                    print(
                        Fore.RED +
                        "NOTHING FOUND"
                    )

        # ---------------- CLEAR ----------------

        case 7:

            while True:

                inp = input(

                    Fore.YELLOW +
                    Style.DIM +
                    "\ndo you really want to clear? (y/n): "
                )

                match inp:

                    case "y":

                        a.clear()

                        print(

                            Fore.GREEN +
                            Style.BRIGHT +
                            "\nLIST CLEARED SUCCESSFULLY 👍"
                        )

                        break

                    case "n":

                        print(
                            Fore.GREEN +
                            "\nOK 👍"
                        )

                        break

                    case _:

                        print(

                            Fore.RED +
                            Style.BRIGHT +
                            "\nENTER y/n ONLY\n"
                        )

        # ---------------- EXIT ----------------

        case 8:

            print(

                Fore.GREEN +
                Style.BRIGHT +
                "\nGOODBYE 👋\n"
            )

            break

    print(Fore.MAGENTA + f"{'':÷^{width}}")