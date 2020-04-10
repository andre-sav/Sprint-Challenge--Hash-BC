#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loops through range of route list
    for i in range(length):
        if tickets[i].source == "NONE":
        #  fills first index of route list with start point 
            route[0] = tickets[i].destination
        # inserts source as key, destination as value into hashtable from tickets list
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # loops through range of route list
    for i in range(length):
        # checks that index at iterable - 1 is not empty, this will bring the loop to the first empty index in the route list
        if route[i-1] != None:
            # assigns the value retrieved from the hashtable to the route list, based on the key
            # which is the previous element in the the route list and the source in the hashtable
            route[i] = hash_table_retrieve(hashtable, route[i-1])
    
    return route[:-1]
    
