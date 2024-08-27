import random
import time

MIN_OPERAND  = 3
MAX_OPERAND = 7

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    expr = f'{left} * {right}'
    answer = eval(expr)
    return expr, answer


total_problems = input('How many problems would you like to do?: ')
while True:
    if total_problems.isdigit():
        break
    else: total_problems = input('Please input the number of problems you would like to solve: ')
print('-------------------------')
start_time = time.time()


problems_correct = 0
for i in range(int(total_problems)):
    expr, answer = generate_problem()
    guess = input(f'problem # {i+1}: {expr} = ')
    if guess == str(answer):
        problems_correct += 1

end_time = time.time()
total_time = round(end_time - start_time,2)
average_time = total_time/int(total_problems)
print('--------------------------')
print(f'You got {problems_correct} problems out of {total_problems} correct!'
      f' You finished in {total_time} seconds!' )
print(f'The average time per problem is {average_time} seconds!')
