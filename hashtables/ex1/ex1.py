def get_indices_of_item_weights(weights, length, limit):
    # Create a cache
    cache = {}

    # check list of w, to find index
    for i in range(length):
        cache[weights[i]] = i
    
    # get the w that matches
    for index, weight in enumerate(weights):
        wgt = limit - weight
        if wgt in cache:
            i = cache[wgt]
            return (index, i) if index > i else (i, index)
    
    return None
