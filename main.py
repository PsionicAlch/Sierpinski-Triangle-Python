import turtle
import random
import sys

class Triangle:
    def __init__(self, width, height):
        turtle.setup(width, height)

        win = turtle.Screen()
        win.bgcolor("black")
        win.title("Sierpinski Triangle")

        triangle = turtle.Turtle()
        triangle.hideturtle()
        triangle.speed(0)
        triangle.color("white")
        triangle.penup()

        self.origin_1 = (0, (height / 2) - 20)                      # Top.
        self.origin_2 = (-(width / 2) + 20, -(height / 2) + 20)     # Bottom left.
        self.origin_3 = ((width / 2) - 20, -(height / 2) + 20)      # Bottom right.

        self.width = width
        self.height = height
        self.triangle = triangle
        self.win = win


    def draw(self, iterations: int):
        # Draw the three points of the triangle.
        self.triangle.goto(self.origin_1)
        self.triangle.dot(2)

        self.triangle.goto(self.origin_2)
        self.triangle.dot(2)

        self.triangle.goto(self.origin_3)
        self.triangle.dot(2)

        original_points = [self.origin_1, self.origin_2, self.origin_3]

        # Generate a random point that's somewhere inside the triangle.
        x = random.randint(int(self.origin_2[0]), int(self.origin_3[0]))
        y = random.randint(int(self.origin_2[1]), int(self.origin_1[1]))    # randint expects the start value to be less than the stop value.
        random_point_inside_triangle = (x, y)

        while not inside_triangle(self.origin_1, self.origin_2, self.origin_3, random_point_inside_triangle):
            x = random.randint(int(self.origin_2[0]), int(self.origin_3[0]))
            y = random.randint(int(self.origin_2[1]), int(self.origin_1[1]))
            random_point_inside_triangle = (x, y)

        # Draw the random point.
        self.triangle.goto(random_point_inside_triangle)
        self.triangle.dot(2)

        for _ in range(iterations):
            # Step 2:
            chosen_point = random.choice(original_points)

            midpoint = (int((chosen_point[0] + random_point_inside_triangle[0]) / 2), int((chosen_point[1] + random_point_inside_triangle[1]) / 2))

            self.triangle.goto(midpoint)
            self.triangle.dot(2)

            random_point_inside_triangle = midpoint


    def finish(self):
        self.win.mainloop()


# This code is not my own. It was taken from:
# https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
def area(p1, p2, p3):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)


def inside_triangle(p1, p2, p3, point):
    A = area(p1, p2, p3)

    A1 = area(point, p2, p3)

    A2 = area(p1, point, p3)

    A3 = area(p1, p2, point)

    if (A == A1 + A2 + A3):
        return True
    else:
        return False


if __name__ == "__main__":
    iterations = 1_000_000_000

    if len(sys.argv) > 0:
        iterations = int(sys.argv[1])

    triangle = Triangle(700, 700)

    print(f'Generating Sierpinski triangle with {iterations} iterations.')

    triangle.draw(iterations)
    triangle.finish()