def norm(v, p=2):
    return sum(abs(x) ** p for x in v) ** (1 / p)

print(norm([4, 3]))        # Euclidean norm: √(4² + 3²) = 5
print(norm([4, 3], p=1))   # 1-norm: |4| + |3| = 7
print(norm([4, 3], p=3))   # 3-norm: (|4|³ + |3|³)^(1/3)