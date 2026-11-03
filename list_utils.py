def get_first_item(items):
    return items[0]


def get_last_item(items):
    return items[-1]


def is_empty(items):
    return len(items) == 0


def safe_get(items, index, default=None):
    if 0 <= index < len(items):
        return items[index]
    return default