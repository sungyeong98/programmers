def solution(brown, yellow):
    x = ((2 + brown/2) + ((-2-brown/2)**2 - 4*(brown + yellow))**0.5) // 2
    y = brown/2 - x + 2
    return [x, y]

# 가로 x, 세로 y
# 둘레 갯수 = 2x + 2(y-2) = 2x + 2y - 4 = brown
# 내부 갯수 = (x-2) * (y-2) = xy - 2x - 2y + 4 = yellow

# 2y = brown - 2x + 4
# y = brown/2 - x + 2
# x(brown/2 -x + 2) - 2x - 2(brown/2 - x + 2) + 4 = yellow
# x(brown/2 -x + 2) - 2x - brown + 2x - 4 + 4 = yellow
# - x^2 + 2x + x*brown/2 - brown = yellow
# x^2 + (- 2 - brown/2)x + yellow + brown = 0

# 근의 공식 -> x = ((2 + brown/2) + ((-2 -brown/2)^2 - 4(yellow + brown))^0.5) / 2