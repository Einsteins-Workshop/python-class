# See https://usaco.org/index.php?page=viewproble2m&cpid=94

# Problem 1: Hay Bales [Brian Dean, 2011]
#
# The cows are at it again!  Farmer John has carefully arranged N (1 <= N <=
# 10,000) piles of hay bales, each of the same height.  When he isn't
# looking, however, the cows move some of the hay bales between piles, so
# their heights are no longer necessarily the same.  Given the new heights of
# all the piles, please help Farmer John determine the minimum number of hay
# bales he needs to move in order to restore all the piles to their original,
# equal heights.
#
# PROBLEM NAME: haybales
#
# INPUT FORMAT:
#
# * Line 1: The number of piles, N (1 <= N <= 10,000).
#
# * Lines 2..1+N: Each line contains the number of hay bales in a single
#         pile (an integer in the range 1...10,000).
#
# SAMPLE INPUT (file haybales.in):
#
# 4
# 2
# 10
# 7
# 1
#
# INPUT DETAILS:
#
# There are 4 piles, of heights 2, 10, 7, and 1.
#
# OUTPUT FORMAT:
#
# * Line 1: An integer giving the minimum number of hay bales that need
#        to be moved to restore the piles to having equal heights.
#
# SAMPLE OUTPUT (file haybales.out):
#
# 7

# Fill out the following function, which should return the correct answer for a file with
# the correct input file format.
def determine_solution(file_name):

    input_list = [4, 2, 10, 7, 1]
    active_pile = 0

    while True:
        print(input_list)
        for i in range(len(input_list) - 1):

            if input_list[i] < input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

            for j in range(len(input_list) - 1):

                if input_list[j] == input_list[j+1]:
                    active_pile = j+1
                    print(active_pile)
                    break

        input_list[active_pile] = input_list[active_pile] - 1
        input_list[len(input_list) - 1] = input_list[len(input_list) - 1] + 1

        if active_pile == len(input_list):
            return input_list

def better_solution(file_name):

    input_list = [4, 2, 10, 7, 1]



# Proper format to be evaluated by USACO
# with open("haybales.out", "w") as f:
#    f.write(str(determine_solution("haybales.in")))
#    exit()

# Checking against all local files
for case in range(1, 11):
    input_file_name = f"data_files/I.{case}"
    with open(f"data_solutions/O.{case}", 'r') as input_file:
        correct_answer = input_file.readline().rstrip()
        print(f"For file {input_file_name} the correct answer is {correct_answer}")
        your_answer = str(determine_solution(input_file_name))
        if correct_answer != your_answer:
            print(f"Your answer of {your_answer} is not correct, try again.")
            exit()
