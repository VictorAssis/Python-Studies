from math import radians, cos, sin, tan

angle = float(input('Type a angle: '))
angleRadians = radians(angle)
print(f'- Sine: {sin(angleRadians):.2f}º')
print(f'- Cosine: {cos(angleRadians):.2f}º')
print(f'- Tangent: {tan(angleRadians):.2f}º')
