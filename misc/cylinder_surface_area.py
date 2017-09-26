def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius

    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return side_area + 2 * top_area
    else:
        return side_area


print(cylinder_surface_area(2, 4, True))
print(cylinder_surface_area(2, 4, False))
