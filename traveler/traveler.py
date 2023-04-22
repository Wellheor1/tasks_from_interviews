# u - up - вверх, d - down - вниз
traveler_path = 'uuddduuddu'


def count_depressions(path: str) -> int:
    count = 0
    start = 0
    for i in path:
        if i == "u":
            start += 1
        else:
            start -= 1
        if start == 0 and i == "u":
            count += 1
    return count


def count_elevations(path: str) -> int:
    count = 0
    start = 0
    for i in path:
        if i == "u":
            start += 1
        else:
            start -= 1
        if start == 0 and i == "d":
            count += 1
    return count


depressions = count_depressions(traveler_path)
elevations = count_elevations(traveler_path)
print("Кол-во впадин", depressions)
print("Кол-во холмов", elevations)
