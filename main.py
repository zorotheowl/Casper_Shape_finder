import math

def check_quadrilateral(coords):
    # Check that the set of coordinates has exactly 4 points
    if len(coords) != 4:
        raise ValueError("Set of coordinates must have exactly 4 points.")

    # Compute the length of each side of the quadrilateral
    sides = []
    for i in range(4):
        j = (i + 1) % 4
        dx = coords[j][0] - coords[i][0]
        dy = coords[j][1] - coords[i][1]
        sides.append(math.sqrt(dx*dx + dy*dy))

    # Compute the angle between adjacent sides of the quadrilateral
    angles = []
    for i in range(4):
        j = (i + 1) % 4
        k = (i + 2) % 4
        dx1 = coords[j][0] - coords[i][0]
        dy1 = coords[j][1] - coords[i][1]
        dx2 = coords[k][0] - coords[j][0]
        dy2 = coords[k][1] - coords[j][1]
        dot = dx1*dx2 + dy1*dy2
        det = dx1*dy2 - dx2*dy1
        angle = math.atan2(det, dot)
        angles.append(abs(angle))

    # Determine the type of quadrilateral based on the side lengths and angles
    if all(s == sides[0] for s in sides) and all(a == angles[0] for a in angles):
        return "Square"
    elif sides[0] == sides[2] and sides[1] == sides[3]:
        if angles[0] == angles[2] and angles[1] == angles[3]:
            return "Rectangle"
        else:
            return "Parallelogram"
    elif sides[0] == sides[2] or sides[1] == sides[3]:
        return "Trapezoid"
    else:
        return "Kite"

# Example usage

coords1 = [(0,0), (0,1), (1,0), (1,1)] # Square
coords2 = [(0,0), (0,1), (1,0), (2,1)] # Parallelogram
coords3 = [(0,0), (0,1), (1,0), (3,3)] # Quadrilateral
coords4 = [(0,0), (0,1), (1,1), (1,0)] # Rectangle
coords5 = [(0,0), (0,1), (1,1), (2,0)] # Quadrilateral

print(check_quadrilateral(coords1))
print(check_quadrilateral(coords2))
print(check_quadrilateral(coords3))
print(check_quadrilateral(coords4))
print(check_quadrilateral(coords5))
coords2 = [(0, 0), (3, 0), (3, 4), (0, 4)]
print(check_quadrilateral(coords2)) # Outputs "Rectangle"
