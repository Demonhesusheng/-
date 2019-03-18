from sys import argv
from decimal import *


def delBlank(str):
    """
    Delete all blanks in the str
    :param str:
    :return:
    """
    ans = ""
    for e in str:
        if e != ' ':
            ans += e
    return ans


def precede(a, b):
    """
    Compare the prior of operator a and b
    :param a:
    :param b:
    :return:
    """
    # the prior of operator
    prior = (
        ('>', '>', '<', '<', '<', '>', '<', '>'),  # '+'
        ('>', '>', '<', '<', '<', '>', '<', '>'),  # '-'
        ('>', '>', '>', '>', '<', '>', '<', '>'),  # '*'
        ('>', '>', '>', '>', '<', '>', '<', '>'),  # '/'
        ('<', '<', '<', '<', '<', '=', '<', ' '),  # '('
        ('>', '>', '>', '>', ' ', '>', '>', '>'),  # ')'
        ('>', '>', '>', '>', '<', '>', '>', '>'),  # '^'
        ('<', '<', '<', '<', '<', ' ', '<', '=')  # '#'

    )
    char2num = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '(': 4,
        ')': 5,
        '^': 6,
        '#': 7
    }
    return prior[char2num[a]][char2num[b]]


def operate(a, b, operator):
    """
    operate [ a operator b]
    :param a:
    :param b:
    :param operator:
    :return:
    """
    if operator == '+':
        ans = a + b
    elif operator == '-':
        ans = a - b
    elif operator == '*':
        ans = a * b
    elif operator == '/':
        if b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a/b
    elif operator == '^':
        if a == 0 and b == 0:
            ans = "VALUE ERROR"
        else:
            ans = a ** b
    return ans

def calc(exp):
    """Calculate the ans of exp"""
    exp += '#'
    operSet = "+-*/^()#"
    stackOfOperator, stackOfNum = ['#'], []
    pos, ans, index, length = 0, 0, 0, len(exp)
    while index < length:
        e = exp[index]
        if e in operSet:
            topOperator = stackOfOperator.pop()
            compare = precede(topOperator, e)
            if compare == '>':
                try:
                    b = stackOfNum.pop()
                    a = stackOfNum.pop()
                except:
                    return "FORMAT ERROR"
                ans = operate(a, b, topOperator)
                if ans == "VALUE ERROR":
                    return ans
                else:
                    stackOfNum.append(ans)
            elif compare == '<':
                stackOfOperator.append(topOperator)
                stackOfOperator.append(e)
                index += 1
            elif compare == '=':
                index += 1
            elif compare == ' ':
                return "FORMAT ERROR"
        else:
            pos = index
            while not exp[index] in operSet:
                index += 1
            temp = exp[pos:index]

            last = index - 1
            if '.' in temp:
                while exp[last] == '0':
                    last -= 1
                    temp = exp[pos:last + 1]
            try:
                temp = Decimal(temp)
            except:
                return "INPUT ERROR"
            stackOfNum.append(temp)

    if len(stackOfNum) == 1 and stackOfOperator == []:
        return stackOfNum.pop()
    else:
        return "INPUT ERROR"


if __name__ == "__main__":
    exp = argv[1]
    getcontext().prec = 10
    exp = delBlank(exp)
    ans = calc(exp)
    print(ans)