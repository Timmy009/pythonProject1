for side1 in range(1, 501):
    for side2 in range(1, 501):
        for side3 in range(1, 501):
            if (side1 * side1) + (side2 * side2) == (side3 * side3):
                print(f"{side1} {side2} {side3}")

