# 1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,2,2,3,3,1,1,2,2,5,5,6,6,3,3,5,5,5,6,7,8,999
#Find frequency off numbers

number_lists = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 2, 2, 3, 3, 1, 1, 2, 2, 
        5, 5, 6, 6, 3, 3, 5, 5, 5, 6, 7, 8, 999]


frequency_of_numbers = {}
'''
for number in number_lists:
    if number in frequency_of_numbers:
        frequency_of_numbers[number] += 1
    else:
        frequency_of_numbers[number] = 1

print(frequency_of_numbers)

'''

def frequency(num):
 for num in number_lists:
    if num in frequency_of_numbers:
        frequency_of_numbers[num] +=1
    else:
        frequency_of_numbers[num] = 1

num = int(input("Pease enter number to find frequency: "))
frequency(num)

if num in frequency_of_numbers:
    print(f"The frequency of {num} is {frequency_of_numbers[num]}")
else:
    print(f"The number {num} is not in the list.")


    
'''
https://drive.google.com/file/d/1o7HoCQUCl01YMj1dIsH3dVp8pPgfz4yU/view?usp=sharing
https://drive.google.com/file/d/1o7HoCQUCl01YMj1dIsH3dVp8pPgfz4yU/view?usp=sharing
https://drive.google.com/file/d/1JHEOmgEsLOWlpGkOnEBQHNZ6Dop8NIz_/view?usp=sharing
https://drive.google.com/file/d/1JHEOmgEsLOWlpGkOnEBQHNZ6Dop8NIz_/view?usp=sharing
'''
