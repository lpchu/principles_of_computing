"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    result_line = []

    # create a new line with no '0' in between numbers
    for num in line:
        if num != 0:
            new_line.append(num)

    # check if 2 neighbouring numbers are the same -> merge
    while len(new_line) > 1:
        if new_line[1] == new_line[0]:
            result_line.append(new_line.pop(0) + new_line.pop(0))
        else:
            result_line.append(new_line.pop(0))
    if len(new_line) == 1:
        result_line.append(new_line.pop(0))

    # append '0' to the result_line to make its length the same as the original line
    if len(result_line) != len(line):
        result_line.extend([0] * (len(line) - len(result_line)))

    return result_line


a_line = [8, 8, 2, 2, 4, 8, 8]
print merge(a_line)

