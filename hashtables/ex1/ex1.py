#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        # attempts to retrieve the index containing the weight which added to weight at loop iterable index will yield the limit
        value = hash_table_retrieve(ht, limit - weights[i])
        # if this doesn't exist, performs insertion
        if value == None:
            hash_table_insert(ht, weights[i], i)
        # if the value does exist, returns the expected response tuple 
        else:
            return (i, value)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
