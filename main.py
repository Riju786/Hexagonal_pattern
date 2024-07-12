def print_hexagon_pattern(rows, cols):
    hexagon_top = "  __ "
    hexagon_middle_top = " /  \\"
    hexagon_middle_bottom = " \\__/"
    hexagon_middle_spacing = "_"  # middle    space between hexagons in the same row
    hexagon_spacing=" "
    for r in range(rows):
        # Print top part of hexagons
        for c in range(cols):
            print(hexagon_top, end=hexagon_spacing)
        print()

        # Print upper middle part of hexagons
        for c in range(cols):
            print(hexagon_middle_top, end=hexagon_middle_spacing)
        print()

        # Print lower middle part of hexagons
        for c in range(cols):
            print(hexagon_middle_bottom, end=hexagon_spacing)
        print()

# Input rows and column
rows=int(input("Enter no of rows: "))
cols=int(input("Enter no of cols: "))
print_hexagon_pattern(rows, cols) 