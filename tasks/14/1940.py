# Solved by Анастасия


d = (
    2 * 16**2020
    + 9 * 16**2021
    - 2 * 4**2022
    + 8**2023
    - 2 * 2**2024
    - 2 * 2**2024
    - 65536
)
d = hex(d)
print(d)
print(
    d.count("a")
    + d.count("b")
    + d.count("c")
    + d.count("d")
    + d.count("e")
    + d.count("f")
)
