import numpy as np

with open('input_9.txt', 'r') as in_file:
    lines = in_file.readlines()

red_tiles = []
for line in lines:
    red_tiles.append(tuple(map(int, line.strip().split(','))))

vertical_edges = []
horizontal_edges = []
for ti, tj in zip(red_tiles, red_tiles[1:]+[red_tiles[0]]):
    if ti[0] == tj[0]:
        ylow, yhigh = sorted([ti[1], tj[1]])  # ensure direction
        vertical_edges.append((ti[0], ylow, yhigh))
    else:
        xlow, xhigh = sorted([ti[0], tj[0]])
        horizontal_edges.append((ti[1], xlow, xhigh))

def point_in_polygon(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    """ Check if a point is inside the polygon via the ray method: count the vertical polygon edges
        crossed by a horizontal ray from the point.
    Args:
        point (tuple[int, int]): The point to check.
        polygon (list[tuple[int, int]]): The polygon.
    Returns:
        bool: Is it inside?
    """
    x, y = point
    inside = False
    N = len(polygon)

    for i in range(N):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1)%N]

        if x1==x2:  # on edge == inside polygon
            if x==x1 and min(y1, y2)<=y<=max(y1, y2):
                return True
        else:
            if y==y1 and min(x1, x2)<=x<=max(x1, x2):
                return True

        if y1!=y2:  # count crossings
            if min(y1, y2) < y <= max(y1, y2):
                if x < x1:
                    inside = not inside

    return inside

def edges_ok(tx: list[int], ty: list[int]) -> bool:
    """ Test all polygon edges against the rectangle:
            1) edge endpoints on rectangle corners ok
            2) edge endpoints on rectangle sides only ok, if they go outwards
            3) edge endpoints inside the rectangle never ok
            4) edges crossing through the rectangle never ok
    Args:
        tx (list[int]): x-range for the rectangle.
        ty (list[int]): y-range for the rectangle.
    Returns:
        bool: Are all polygon edges ok?
    """
    xmin, xmax = sorted(tx)  # ensure direction
    ymin, ymax = sorted(ty)

    # vertical polygon edges
    for x, y1, y2 in vertical_edges:
        if xmin<x<xmax and (ymin<y1<ymax or ymin<y2<ymax):  # fully inside
            return False
        if xmin<x<xmax and y1<=ymin and ymax<=y2:  # crossing through center
            return False
        if xmin<x<xmax and ((ymin<y2 and y1<ymax)):  # side, not going out
            return False

    # horizontal polygon edges
    for y, x1, x2 in horizontal_edges:
        if ymin<y<ymax and (xmin<x1<xmax or xmin<x2<xmax):  # fully inside
            return False
        if ymin<y<ymax and x1<=xmin and xmax<=x2:  # crossing through center
            return False
        if ymin<y<ymax and (xmin<x2 and x1<xmax):  # side, not going out
            return False

    return True


areas = np.zeros((len(red_tiles), len(red_tiles)), dtype=int)
for i in range(len(red_tiles)-1):
    for j in range(i+1, len(red_tiles)):
        areas[i, j] = ((abs(red_tiles[i][0]-red_tiles[j][0])+1) *
                       (abs(red_tiles[i][1]-red_tiles[j][1])+1))

        # test if valid: 1) all corners inside
        if (not point_in_polygon((red_tiles[i][0], red_tiles[j][1]), red_tiles) or
            not point_in_polygon((red_tiles[j][0], red_tiles[i][1]), red_tiles)):
            areas[i, j] *= -1
            continue

        # 2) test middle point for good measure
        m = ((red_tiles[i][0]+red_tiles[j][0])//2, (red_tiles[i][1]+red_tiles[j][1])//2)
        if not point_in_polygon((red_tiles[j][0], red_tiles[i][1]), red_tiles):
            areas[i, j] *= -1
            continue

        # 3) test edges
        if not edges_ok([red_tiles[i][0], red_tiles[j][0]], [red_tiles[i][1], red_tiles[j][1]]):
            areas[i, j] *= -1
            continue

print(np.max(areas))
i, j = np.unravel_index(np.argmax(areas), areas.shape)
print(red_tiles[i], red_tiles[j])
