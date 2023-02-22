# Calculate volume of sphere
import math
from area import area_formula

# Volume of sphere = 4/3*pi*r*r*r

def volume_of_sphere(radius):
    volume_sphere = (4 * radius * radius * radius * math.pi) / 3
    return volume_sphere


# volume of cylinder = π*r*r*h

def volume_of_cylinder(radius, height):
    volume_cylinder = math.pi * radius * radius * height
    return volume_cylinder


# volume of triangular pyramid = 1/3 x Area of triangular base x Height of pyramid

def volume_of_pyramid(triangle_base, triangle_height, pyramid_height):
    triangle_area = area_formula.area_of_triangle(triangle_base,triangle_height)
    pyrmaid_volume = (triangle_area * pyramid_height) / 3
    return pyrmaid_volume


# volume of a cone = (1/3) π*r*r*h cubic units

def volume_of_cone(cone_radius, cone_height):
    cone_volume = (math.pi * cone_radius * cone_radius * cone_height) / 3
    return cone_volume
