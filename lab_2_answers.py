# """Lab 2 Answers

# Usage:
#     cmd/bash - python/python3 ./lab_2_answers.py

# Note:
#     Some functions are used more than 1 time.
#     Do not comment functions, comment only # Program run 
#     part to avoid unnecessary task executions

# Author:
#     Shynggys Alshynov - 02.02.2022
# """



# # 1 Task - Frying shelpeks
from random import randint
from math import sqrt

# # This solution is by Aida Sapenova MT2001
# # I really liked this solution because it is truly elegant.
# def fry_shelpeks(shelpek:int):
#     time = 0
#     round = 0
#     side = 0
#     sh3lp3k = 0
#     if shelpek == 1:
#         time += 20
#         print("Total frying time: %s" % time)
#         shelpek -= 1
#         round += 1
#         print("Round %s: Shelpek %s Side %s; Shelpeks in the queue: %s" % (round, 1, 1, shelpek))
#         print("Round %s: Shelpek %s Side %s; Shelpeks in the queue: %s" % (round + 1, 1, 2, shelpek))
#     else:
#         time = shelpek * 10
#         print("Total frying time: %s" % time)
#         while shelpek >= 4:
#             shelpek -= 2
#             sh3lp3k += 2
#             time -= 20
#             while side != 2:
#                 side += 1
#                 round += 1
#                 print("Round %s: Shelpek %s Side %s, Shelpek %s Side %s; Shelpeks in the queue: %s" % (round, sh3lp3k - 1, side, sh3lp3k, side, shelpek))
#             side = 0
#         if shelpek % 2 == 0:
#             shelpek -= 2
#             sh3lp3k += 2
#             time -= 20
#             while side != 2:
#                 side += 1
#                 round += 1
#                 print("Round %s: Shelpek %s Side %s, Shelpek %s Side %s; Shelpeks in the queue: %s" % (round, sh3lp3k - 1, side, sh3lp3k, side, shelpek))
#         else:
#             shelpek -= 2
#             sh3lp3k += 2
#             round += 1
#             print("Round %s: Shelpek %s Side %s, Shelpek %s Side %s; Shelpeks in the queue: %s" % (round, sh3lp3k - 1, 1, sh3lp3k, 1, shelpek))
#             print("Round %s: Shelpek %s Side %s, Shelpek %s Side %s; Shelpeks in the queue: %s" % (round + 1, sh3lp3k - 1, 2, sh3lp3k + 1, 1, shelpek))
#             print("Round %s: Shelpek %s Side %s, Shelpek %s Side %s; Shelpeks in the queue: %s" % (round + 2, sh3lp3k, 2, sh3lp3k + 1, 2, 0))

# # Program run
# shelpek = int(input("Enter number of shelpeks to be fried:\t"))
# fry_shelpeks(shelpek)

# # Task 2 - Perfect number
# # if number is divided without any reminder
# # we are saving in generator the divisor
# def find_divisors(number):
#     for i in range(1, number):
#         if number % i != 0:
#             continue
#         else:
#             yield i

# # returning True if sum of divisors is equal to number itself


# def perfect_number(number):
#     return True if sum(find_divisors(number)) == number else False


# # Program run (un/comment this lines below to run the task)
# check_number = int(input("Number to check to be perfect:\t"))
# print(f"{perfect_number(check_number)} {list(find_divisors(check_number)) if perfect_number(check_number)==True else 'Not a perfect number'}")


# # Task 3 - Prime factors
# # getting sqrt of number will save us time
# # there is a mathematical reason to do so :)
# def is_prime(number):
#     div = int(sqrt(number))
#     for i in range(2, div+1):
#         if number % i == 0 and i != number:
#             return False
#     return True


# def prime_factors(number):
#     for i in range(2, number):
#         # conditions to be of prime factors, the divisor is prime and
#         # number is divided by divisor without any reminder
#         if is_prime(i) and number % i == 0:
#             yield i

# # Program run (un/comment this lines below to run the task)
# input_number = int(input("Input number to find its prime factors:\t"))
# print(f"Prime factors of number {input_number}:\t {list(prime_factors(input_number))}")


# # Task 4 - Matrix diagonals
# # generating matrix using list comprehension
def generate_matrix(row, col):
    return [[randint(1, 100) for c in range(col)] for r in range(row)]

# # printing matrix using list comprehension


def print_matrix(matrix):
    [[print(el, end="\t") if row.index(el) != len(row)-1 else print(el)
      for el in row] for row in matrix]
    print()
    # [print(*row) for row in matrix]


# def find_diagonals(matrix):
#     print_matrix(matrix)
#     main_diag = 0
#     counter_diag = 0
#     # main diagonal is row index == col index
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if row == col:
#                 main_diag += matrix[row][col]
#     # counter diagonal is row index + col index == len(matrix)-1
#     for row in range(len(matrix)-1, -1, -1):
#         for col in range(len(matrix[row])-1, -1, -1):
#             if row+col == len(matrix)-1:
#                 counter_diag += matrix[row][col]
#     return main_diag, counter_diag

# # Program run (uncomment this lines below to run the task)
# matrix = generate_matrix(int(input("Number of rows: ")), int(input("Number of columns: ")))
# main,counter=find_diagonals(matrix)
# print(f"Main diagonal is {main} and counter diagonal is {counter}.")


# # Task 5 - Shifting (easy solution, other option is to use deque from collections)
# def generate_list(number):
#     return [randint(-50, 50) for i in range(number)]


# def shift_elements(random_list):
#     print("Initial list is: ", *random_list)
#     direction = input("Choose direction to shift - right or left:\t")
#     max_el_index = random_list.index(max(random_list))
#     # just a list slicing :)
#     if direction.lower() == "right":
#         return random_list[max_el_index+1:]+random_list[:max_el_index+1]
#     elif direction.lower() == "left":
#         return random_list[max_el_index:]+random_list[:max_el_index]

# # Program run (uncomment this lines below to run the task)
# list_len = int(input("Input random list length:\t"))
# print(shift_elements(generate_list(list_len)))


# # Task 6 - Maximum possible value
# def max_pos_value(random_list):
#     print(f"Given random list: {random_list}")
#     # making values absolute and change them to be string
#     random_list = list(map(lambda x: str(abs(x)), random_list))
#     # joining all the elements into one big string
#     random_list_str_value = "".join(random_list)
#     # dividin each number
#     digits = [el for el in random_list_str_value]
#     # sorting in reverse (desc order e.g. ['9', '8', '7'])
#     digits.sort(reverse=True)
#     # joining all digits into one big string and cast it to int function
#     return int("".join(digits))


# # Program run (uncomment this lines below to run the task)
# random_list = generate_list(int(input("Set list length: \t")))
# print(f"Possible maximum value: {max_pos_value(random_list)}")


# Task 7 - Kind of "Bonus", but it is challenge task
# Sorting diagonals of matrix by from different angles: top left, right or bottom left, right

# This function is needed to replace the min value we need to a position we need
# for example we have row of matrix [1,2,3]
# we want 3 to be at the beginning and function will return [3,2,1]
def replace_vals(row, pos, val):
    val_index = row.index(val)
    row[pos], row[val_index] = row[val_index], row[pos]
    return row


# sorting and giving the result
def sorting(matrix, angle):
    # setting the borders of matrix to make it easier the sorting process
    # we are setting here initial positions of borders
    matrix_borders = {"tr": (0, len(matrix[0])-1), "tl": (0, 0), "bl": (
        len(matrix)-1, 0), "br": (len(matrix)-1, len(matrix[0])-1)}

    # condition to check whether user input is the right or not
    if angle in matrix_borders.keys():
        # getting starting positions
        start_row, start_col = matrix_borders.get(angle)

        # we have 4 available options:
        # when starting row is more than 0 and col is also more than 0
        # row more than 0 and col is 0
        # row is 0 col is more than 0
        # row is 0 col is 0
        # these angles actually gives us the access to the starting points(elements) of diagonals in the matrix
        if start_row > 0:
            if start_col > 0:  # this is BOTTOM RIGHT SORTING (br)
                # running over matrix row by row to check elements
                for r in range(len(matrix)):
                    # very first running of the cycle gives us very first min value
                    if r == 0:
                        # getting min value of first row
                        current_row_min = min(matrix[start_row])
                        # replacing min value position to a position we need using function
                        replace_vals(matrix[start_row],
                                     start_row, current_row_min)

                    # other iterations gives us min values which are more than previous min values
                    else:
                        # searching for min values that are more than previous min value
                        # otherwise program returns Sorting is impossible
                        available_mins = [
                            val for val in matrix[start_row] if val > old_min]
                        if len(available_mins) == 0:
                            return "Sorting is impossible"
                        available_mins.sort()
                        current_row_min = available_mins[0]
                        replace_vals(matrix[start_row],
                                     start_row, current_row_min)
                    # saving old min value to compare it on next iteration with a min of next row
                    old_min = current_row_min
                    # moving
                    start_row -= 1
                    start_col -= 1
                print_matrix(matrix)
            elif start_col == 0:  # this is BOTTOM LEFT SORTING (bl)
                for r in range(len(matrix)):
                    if r == 0:
                        current_row_min = min(matrix[start_row])
                        replace_vals(matrix[start_row],
                                     start_col, current_row_min)
                    else:
                        available_mins = [
                            val for val in matrix[start_row] if val > old_min]
                        if len(available_mins) == 0:
                            return "Sorting is impossible"
                        available_mins.sort()
                        current_row_min = available_mins[0]

                        # small notice here, as this is a counter diagonal, we will use column index to replace values, not row's
                        replace_vals(matrix[start_row],
                                     start_col, current_row_min)
                    old_min = current_row_min
                    start_row -= 1
                    start_col += 1
                print_matrix(matrix)
        elif start_row == 0:
            if start_col > 0:  # this is TOP RIGHT SORTING (tr)
                for r in range(len(matrix)):
                    print(matrix[start_row])
                    if r == 0:
                        current_row_min = min(matrix[start_row])
                        replace_vals(matrix[start_row],
                                     start_col, current_row_min)
                    else:
                        available_mins = [
                            val for val in matrix[start_row] if val > old_min]
                        if len(available_mins) == 0:
                            return "Sorting is impossible"
                        available_mins.sort()
                        current_row_min = available_mins[0]

                        # small notice here, as this is a counter diagonal, we will use column index to replace values, not row's
                        replace_vals(matrix[start_row],
                                     start_col, current_row_min)
                    old_min = current_row_min
                    start_row += 1
                    start_col -= 1
                print_matrix(matrix)
            elif start_col == 0:  # this is TOP LEFT SORTING (tl)
                for r in range(len(matrix)):
                    if r == 0:
                        current_row_min = min(matrix[start_row])
                        replace_vals(matrix[start_row],
                                     start_row, current_row_min)
                    else:
                        available_mins = [
                            val for val in matrix[start_row] if val > old_min]
                        if len(available_mins) == 0:
                            return "Sorting is impossible"
                        available_mins.sort()
                        current_row_min = available_mins[0]
                        replace_vals(matrix[start_row],
                                     start_row, current_row_min)
                    old_min = current_row_min
                    start_row += 1
                    start_col += 1
                print_matrix(matrix)

    return f"Sorting completed by angle {angle}"

# Running function


def sort_matrix_diagonals(matrix):
    print("Given matrix is:")
    print_matrix(matrix)
    angle_choice = input(
        "From which angle you would like to sort - tl, tr, bl, or br:\t")
    print(sorting(matrix, angle_choice.lower()))


# Running program (uncomment sort_matrix_diagonals and run the script)
# generate_matrix is from task 4
# I am using matrix 4x4 but you can provide different one, it might even 3x5
sort_matrix_diagonals(generate_matrix(3, 4))
