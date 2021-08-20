# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    sec_l= numbers[1]
    fir_l= numbers[0]

    def check_swap(fir_l, sec_l):
        if sec_l > fir_l:
            sec_l, fir_l = fir_l, sec_l
        
        return (fir_l, sec_l)
    
    fir_l, sec_l = check_swap(fir_l, sec_l)

    for number in numbers[2:]:
        if number > sec_l :
            sec_l = number
            fir_l, sec_l = check_swap(fir_l, sec_l)

    

    return fir_l * sec_l


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
