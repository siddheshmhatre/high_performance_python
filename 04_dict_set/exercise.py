from dict_probing import index_sequence
from naive_hash_function import City

if __name__ == "__main__":
    # Exercise 1 -
    print ("Printing the indices that would be checked for a lookup for Johannesburg")
    iters = 10
    john_gen = index_sequence(City("Johannesburg"))
    for _ in range(iters):
        print (next(john_gen))