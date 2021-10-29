#created by Ivannikov Maksym, Sobol Oleg, Mendyk Sofiia
universum = [1, 2, 3, 4, 5, 6, 7, 8]
def unification(a, b):
    result_array = a.copy()
    for i, elemB in enumerate(b):
        if elemB not in result_array:
            result_array.append(elemB)
    return result_array
def intersection(a, b):
    new_array = []
    for x in a:
        for j in b:
            if x == j:
                new_array.append(x)
    return new_array
def difference(a, b):
    new_array = a.copy()
    for x in b:
        for j in new_array:
            if x == j:
                new_array.remove(j)
    return new_array
def supplementing(a):
    new_array = universum.copy()
    for x in a:
        for j in new_array:
            if x == j:
                new_array.remove(j)
    return new_array
def symetrical_difference(a, b):
    if is_equal(a,b) or subset(a, b):
        return []
    array_all = unification(a, b)
    array_dif = intersection(a, b)
    for x in array_dif:
        array_all.remove(x)
    return array_all
def decart(a, b):
    decart_array = []
    for index, i in enumerate(a):
        decart_array.append([])
        for j in b:
            decart_array[index].append((i, j))
    return decart_array
        
def subset(a, b):
    for _, elemA in enumerate(a):
        if elemA not in b:
            return False
    return True
def is_equal(a, b):
    if len(a) != len(b):
        return False
    for i in a:
        exist = False
        for j in b:
            if i == j:
                exist = True
                continue
        if not exist:
            return False
    return True
def translate_to_bit(a):
    bitarray_a = []
    for i in universum:
        if i in a:
            bitarray_a.append(1)
        else:
            bitarray_a.append(0)
    return bitarray_a
def unification_bit(a, b):
    bit_a = translate_to_bit(a)
    bit_b = translate_to_bit(b)
    uni_bit = []
    for i, _ in enumerate(bit_a):
        uni_bit.append(bit_a[i] | bit_b[i])
    return uni_bit


def intersection_bit(a, b):
    bit_a = translate_to_bit(a)
    bit_b = translate_to_bit(b)
    result_array = []
    for i, _ in enumerate(bit_a):
        result_array.append(bit_a[i] & bit_b[i])
    return result_array
def difference_bit(a, b):
    bit_a = translate_to_bit(a)
    bit_b = translate_to_bit(b)
    result_array = bit_a.copy()
    for i, elem in enumerate(bit_b):
        if elem == 1:
            result_array[i] = 0
    return result_array
def symetrical_bit_difference(a, b):
    result_array = []
    bit_a = translate_to_bit(a)
    bit_b = translate_to_bit(b)
    for i, _ in enumerate(bit_a):
        result_array.append(bit_a[i] ^ bit_b[i])
    return result_array
