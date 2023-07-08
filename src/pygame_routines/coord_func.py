def coordinates(m):

    coord_x1 = ((m + det - 1) % det)
    coord_y1 = (abs(m - 1) // det)
    coord_x2 = coord_x1 + 1
    coord_y2 = coord_y1 + 1

    print(coord_x2, coord_y2)