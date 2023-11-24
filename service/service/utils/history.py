import os


def get_history() -> list[os.DirEntry]:
    res = []
    if not os.path.exists("reports"):
        return res
    with os.scandir("reports") as entries:
        for entry in entries:
            if entry.is_file():
                res.append(entry)
    return res


def get_history_item(filename) -> str | None:
    path = os.path.join("reports", filename)
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def delete_history_item(filename):
    path = os.path.join("reports", filename)
    if os.path.exists(path):
        os.remove(path)


def save_history_item(filename, content):
    if not os.path.exists("reports"):
        os.mkdir("reports")
    path = os.path.join("reports", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
