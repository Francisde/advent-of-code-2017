def generate_samples(seed, factor, size, multiply=0):
    result = []
    last = seed
    while len(result) < size:
        next = generate_next_value(last, factor)
        if multiply == 0:
            result.append(next)
        else:
            if next % multiply == 0:
                result.append(next)
        last = next
    return result

def generate_next_value(last, factor):
    next = last * factor
    return next % 2147483647

def solve_part_one(seed_a, seed_b, sample_size):
    last_a = seed_a
    last_b = seed_b
    matches = 0
    for i in range(sample_size):
        next_a = generate_next_value(last_a, 16807)
        next_b = generate_next_value(last_b, 48271)
        equals = True
        for i in range(16):
            if (iskthBitSet(last_a, i) and iskthBitSet(last_b, i)) or (not iskthBitSet(last_a, i) and not iskthBitSet(last_b, i)):
                continue
            else:
                equals = False
        if equals:
            matches += 1
        last_a = next_a
        last_b = next_b
    return matches

def solve_part_one_new(seed_a, seed_b, sample_size):
    list_a = generate_samples(seed_a, 16807, sample_size)
    print("generated a")
    list_b = generate_samples(seed_b, 48271, sample_size)
    print("generated b")
    matches = 0
    for i in range(sample_size):
        next_a = list_a[i]
        next_b = list_b[i]
        equals = True
        for i in range(16):
            if (iskthBitSet(next_a, i) and iskthBitSet(next_b, i)) or (not iskthBitSet(next_a, i) and not iskthBitSet(next_b, i)):
                continue
            else:
                equals = False
        if equals:
            matches += 1
    return matches

def solve_part_two(seed_a, seed_b, sample_size):
    list_a = generate_samples(seed_a, 16807, sample_size, 4)
    print("generated a")
    list_b = generate_samples(seed_b, 48271, sample_size, 8)
    print("generated b")
    matches = 0
    for i in range(sample_size):
        next_a = list_a[i]
        next_b = list_b[i]
        equals = True
        for i in range(16):
            if (iskthBitSet(next_a, i) and iskthBitSet(next_b, i)) or (not iskthBitSet(next_a, i) and not iskthBitSet(next_b, i)):
                continue
            else:
                equals = False
        if equals:
            matches += 1
    return matches

def iskthBitSet(n, k):
    if n & (1 << k):
        return True
    else:
        return False

# seed_a = 65
# seed_b = 8921
seed_a = 873
seed_b = 8921

sample_size_one = 40000000
sample_size_two = 5000000

print("TASK 1 - {}".format(solve_part_one_new(seed_a, seed_b, sample_size_one)))

print("TASK 2 - {}".format(solve_part_two(seed_a, seed_b, sample_size_two)))
