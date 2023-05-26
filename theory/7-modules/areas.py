PI = 3.141592

def square(large): return large ** 2
def triangle(base, height): return (base * height) / 2
def circle(ray): return PI * (ray ** 2)
def ellipse(a, b): return PI * a * b
def trapeze(minorBase, biggerBase, height): return ((biggerBase + minorBase) * height) / 2