def hanoi(disc_count, rod_a, rod_b, rod_c):
    if disc_count == 1:
        print(f"Move a disk from rod {rod_a} to rod {rod_c}")
        return
    if disc_count == 2:
        print(f"Move a disk from rod {rod_a} to rod {rod_b}")
        print(f"Move a disk from rod {rod_a} to rod {rod_c}")
        print(f"Move a disk from rod {rod_b} to rod {rod_c}")
        return
    if disc_count % 2 == 0:
        rod_b, rod_c = rod_c, rod_b
        hanoi(disc_count-1, rod_a, rod_b, rod_c)
    else:
        hanoi(disc_count-1, rod_a, rod_b, rod_c)


if __name__ == '__main__':
    hanoi(4, "A", "B", "C") # A being the starting rod, B the middle rod and C the ending one


"""
The Tower of Hanoi is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters,
which can slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size,
the smallest at the top, thus approximating a conical shape. 
The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
    Only one disk may be moved at a time.
    Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    No disk may be placed on top of a disk that is smaller than it.
"""