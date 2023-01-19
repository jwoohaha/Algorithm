a, b = map(int, input().split())

#  최대 공약수 구하기 (Euclidean algorithm)
def get_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return get_gcd(b, a % b)


#  최소 공배수 구하기
def get_lcm(a, b):
    gcd = get_gcd(a, b)
    lcm = a * b // gcd

    return lcm

print(get_gcd(a, b))
print(get_lcm(a, b))