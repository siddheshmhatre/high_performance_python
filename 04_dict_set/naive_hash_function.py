from dict_probing import index_sequence, index_sequence_without_perturb

class City(str):

    def __hash__(self):
        return ord(self[0])

if __name__ == "__main__":
    print ("Adding Rome, San Francisco, New York and Barcelona to a set.  Rome and Barcenlona will collide!")
    data = {
        City("Rome"),
        City("San Francisco"),
        City("New York"),
        City("Barcelona"),
    }

    # Generating indices for n iterations
    iters = 10

    # Example of why we need to consider higher order bits along with 
    # linear probing

    # Print iters for Rome and Barcelona using index_sequence_without_perturb
    print ("No perturb")
    rome_gen = index_sequence_without_perturb(City("Rome"))
    barcelona_gen = index_sequence_without_perturb(City("Barcelona"))

    for i in range(iters):
        rome_idx = next(rome_gen)
        barcelona_idx = next(barcelona_gen)

        if (rome_idx != barcelona_idx):
            print (f"{rome_idx}, {barcelona_idx}")

    # Print iters for Rome and Barcelona using index_sequence
    print ("With perturb")
    rome_gen = index_sequence(City("Rome"), PERTURB_SHIFT=3)
    barcelona_gen = index_sequence(City("Barcelona"), PERTURB_SHIFT=3)

    for i in range(iters):
        rome_idx = next(rome_gen)
        barcelona_idx = next(barcelona_gen)

        if (rome_idx != barcelona_idx):
            print (f"{rome_idx}, {barcelona_idx}")

