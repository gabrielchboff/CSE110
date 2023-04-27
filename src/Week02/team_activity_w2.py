from math import pi

square_length = float(input('What is the length of a side of the square? '))
square_area = square_length*square_length
print(f'The area of the square is: {square_area}')
retangle_len = float(input('What is the length of rectangle? '))
retangle_width = float(input('What is the width of the rectangle? '))
retangle_area = retangle_len*retangle_width
print(f'The area of the rectangle is: {retangle_area}')
circle_rad = float(input('What is the radius of the circle? '))
circle_area = pi*circle_rad**2
print(f'The area of the circle is: {circle_area}\n')

single_len = float(input('Put a single length: '))
square_area = single_len**2
circle_area = pi*single_len**2
cube_volume = single_len**3
sphere_volume = 4/3*pi*single_len**3
print(f"""
-------------------------------------
square area: {square_area}
circle area: {circle_area}
cube volume: {cube_volume}
sphere volume: {sphere_volume}
-------------------------------------
""")

side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"""
The area of the square is: {area} cm²")
The area of the square is: {area / 10000} m²
\n""")

length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"""
The area of the rectangle is: {area} cm²"
The area of the rectangle is: {area / 10000} m²
\n""")

radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)

print(f"""
The area of the circle is: {area} cm²"
The area of the circle is: {area / 10000} m²
\n""")
