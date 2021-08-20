# python3


def max_pairwise_product(numbers):
    if len(numbers) < 2:
        return(o)
    n = max(numbers)
    numbers.remove(n)
    m= max(numbers)


    return n*m


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
