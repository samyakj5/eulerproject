import math

def permutations(elements):
    if len(elements) == 1:
        return [elements]
    
    result = []
    for i, current in enumerate(elements):
        remaining_elements = elements[:i] + elements[i + 1:]

        for p in permutations(remaining_elements):
            result.append([current] + p)

    return result

cubes = set()

for i in range(10_000):

    count = 1
    cube_set = {i**3}

    for p in permutations(list(str(i**3))):

        p_num = "".join(p)

        if p_num[0] == "0":
            continue

        p_num = int(p_num)

        if p_num > i**3:
            continue
        
        if p_num in cubes and p_num not in cube_set:
            count += 1
            cube_set.add(int(p_num))
    
    if count == 5:
        print(cube_set)
        print(min(cube_set))
        break

    cubes.add(i**3)