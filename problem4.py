#Get the total count of number listed
#in the dictionary which is multiple of
#[1,2,3,4,5,6,7,8,9]
#(examples)
#input: [1,2,8,9,12,46,76,82,15,20,30]
# Output:
# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}


def count_mul(numbers,multiples):
    counts={}

    for num in multiples:
        counts[num]=0

    for number in numbers:
        for num in multiples:
            if number%num==0:
                counts[num]+=1
    return counts


numbers=[1,2,8,9,12,46,76,82,15,20,30]
multiples=[1,2,3,4,5,6,7,8,9]
counts=count_mul(numbers,multiples)
print(counts)
