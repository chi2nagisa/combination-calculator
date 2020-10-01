import sys

def main():
    choose = int(sys.argv[1])
    all = int(sys.argv[2])
    f_c = factorial(choose)
    f_a = factorial(all)
    f_ac = factorial(all-choose)
    print(int(f_a/(f_c*f_ac)))


def factorial(num):
    sum = 1
    for i in range(1, num+1):
        sum *= i
    return sum


if __name__ == '__main__':
    main()




