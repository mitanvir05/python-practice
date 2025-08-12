# Write a program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

if x > 0 and y > 0:
    print("The point lies in Quadrant I")
elif x < 0 and y > 0:
    print("The point lies in Quadrant II")
elif x < 0 and y < 0:
    print("The point lies in Quadrant III")
elif x > 0 and y < 0:
    print("The point lies in Quadrant IV")
elif x == 0 and y != 0:
    print("The point lies on the Y-axis")
elif y == 0 and x != 0:
    print("The point lies on the X-axis")
else:
    print("The point is at the Origin")
