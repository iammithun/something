import math

# Calculate sine, cosine, and tangent of an angle in radians
angle_radians = math.radians(30)  # Convert angle from degrees to radians
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print("Sine of 30 degrees:", sin_value)
print("Cosine of 30 degrees:", cos_value)
print("Tangent of 30 degrees:", tan_value)

# Calculate inverse trigonometric functions
angle_degrees = math.degrees(math.asin(0.5))  # arcsin(0.5)
print("Angle whose sine is 0.5 (in degrees):", angle_degrees)
