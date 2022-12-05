#!/isr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position."""
    if not my_list:
        return None

    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (new_list)

    new_list[idx] = element
    return (new_list)
