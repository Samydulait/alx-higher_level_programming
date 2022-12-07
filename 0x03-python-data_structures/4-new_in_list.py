#!/isr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    new = list(my_list)
    """Replace an element in a list at a specific position."""
    if idx < 0 or idx > len(my_list) - 1:
        return (new)
    else:
        new[idx] = element
        return (new)
