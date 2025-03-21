# '''
# A sequence of k distinct positive integers between 1 and n is a (k, n)-tour 
# if the sequencebegins with n ends with n - 1, and every number in the sequence is 
# the difference of a pair of
# numbers that occur earlier in the sequence. 
# More precisely, (a1, a2, . . . , ak) is a (k, n)-tour if
# • 1 ≤ ai ≤ n for i = 1, . . . , k.
# • a1 = n, and ak = n - 1,
# • ai ̸= aj whenever i ̸= j,
# • For l ≥ 3, al = ai - aj for some i, j < l such that i ̸= j.

# For example, (10, 1, 9) is a (3, 10) tour, (10, 3, 7, 4, 1, 9) is a (6, 10)-tour, and 
# (10, 7, 3, 4, 6, 2, 8, 1, 5, 9)
# is a (10, 10)-tour. Notice that the last example is an (k, n)-tour where n = k, and 
# any (n, n)- tour must include all of the integers from 1 up to n.
# '''



# def find_kn_tours(k, n):
#     def is_valid(sequence):
#         if len(sequence) != len(set(sequence)):
#             return False  
#         if sequence[0] != n or sequence[-1] != n - 1:
#             return False  
#         for l in range(2, len(sequence)):
#             valid = False
#             for i in range(l):
#                 for j in range(i):
#                     if abs(sequence[i] - sequence[j]) == sequence[l]:
#                         valid = True
#                         break
#                 if valid:
#                     break
#             if not valid:
#                 return False

#         return True

#     def backtrack(sequence):
#         if len(sequence) == k:
#             if is_valid(sequence):
#                 tours.append(sequence[:])
#             return

#         for num in range(1, n + 1):
#             if num not in sequence:
#                 sequence.append(num)
#                 backtrack(sequence)
#                 sequence.pop()

#     tours = []
#     backtrack([n])
#     return tours


# k, n = 10, 10
# all_tours = find_kn_tours(k, n)

# print(f"Number of {k, n}-tours: {len(all_tours)}")
# for tour in all_tours:
#     print(tour)
def find_kn_tours(k, n):
    def is_valid_partial(sequence):
        # Validate the current sequence incrementally.
        if sequence[-1] == n - 1 and len(sequence) < k:
            return False
        if len(sequence) > 2:
            current = sequence[-1]
            valid = False
            for i in range(len(sequence) - 1):
                for j in range(i):
                    if abs(sequence[i] - sequence[j]) == current:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                return False
        return True

    def backtrack(sequence):
        if len(sequence) == k:
            if sequence[-1] == n - 1:
                tours.append(sequence[:])
            return

        for num in range(1, n + 1):
            if num not in sequence:
                sequence.append(num)
                if is_valid_partial(sequence):
                    backtrack(sequence)
                sequence.pop()

    tours = []
    backtrack([n])
    return tours

for i in range(1,17):
    all_tours = find_kn_tours(i, i)
    print(f"Number of {i, i}-tours: {len(all_tours)}")
    





