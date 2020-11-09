def has_negatives(int_list):
    cache = {}
    result = []
    for i in int_list:
        if -i in cache:
            result.append(abs(i))
        else:
            cache[i] = True 
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
