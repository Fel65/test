def number_negatives(seq):
    """Number of negative residues in a protein sequence"""
    # Count E's and D's, since these are the negative residues
    return 1


def test_seq_E_should_return_1():
    result = number_negatives('E')
    assert result == 1

# number_negatives('E') == 1
# False

# def number_negatives(seq):
#     """Number of negative residues a protein sequence"""
#     # Count E's and D's, since these are the negative residues
#     return seq.count('E') + seq.count('D')

# number_negatives('E') == 1
# True


# print(number_negatives('E') == 1)
# print(number_negatives('D') == 1)
# print(number_negatives('') == 0)
# print(number_negatives('ACKLWTTAE') == 1)
# print(number_negatives('DDDDEEEE') == 8)

# number_negatives('acklwttae')
# number_negatives('acklwttae') == 1
# True

# print(number_negatives('E') == 1)
# print(number_negatives('D') == 1)
# print(number_negatives('') == 0)
# print(number_negatives('ACKLWTTAE') == 1)
# print(number_negatives('DDDDEEEE') == 8)
# print(number_negatives('acklwttae') == 1)


# assert number_negatives('E') == 1


# "assert number_negatives('E') == 2"
