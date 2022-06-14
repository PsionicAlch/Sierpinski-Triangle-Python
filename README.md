# Sierpinski Triangle

This programming challenge was inpsired by this [TikTok video](https://vm.tiktok.com/ZMNNk5PW7/?k=1).

![GIF of Sierpinski Triangle being generated](https://github.com/Wolfman13/Sierpinski_Triangle/Sierpinski_Triangle.gif)

The idea is to draw a Sierpinski triangle using the following algorithm:
1. Start with three points. The points of a triangle.
2. Choose a random point inside the triangle and draw it.
3. Find the midpoint between the random point and a random point of the triangle and draw it.
4. Repeat step 3 by using the mid point as the new random point.

If done enough times a fractal triangle will begin to form.

## Running the application.

To run the application, you just need to have python 3 installed and then you can run the following command.

For unix based systems:

    python3 main.py [number of iterations]

For windows:

    python main.py [number of iterations]

The number of iterations can be left out and the default value will be used (The default being 1 000 000 000).