# So here we will create a project to randamly ganerate math questions 

import random

OPERATORS = ["+","-","/","*"]
MIN_OPRAND = 3
MAX_OPERAND = 12


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

