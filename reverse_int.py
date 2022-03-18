def reverse(x: int) -> int:

    new_num = 0
    ten = 10 if x > 0 else -10

    while x != 0:
        new = x % ten
        x = x // ten

        if new_num*10 >= 2 ** 31 or new_num*10 <= -2 ** 31: return 0
        new_num = new_num * 10 + new

        if ten < 0: x *= -1  # keeps originally negative x from turning positive.

    return new_num

print(reverse(x= 1534236469))
