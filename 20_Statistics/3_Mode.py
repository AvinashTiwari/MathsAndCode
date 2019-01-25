from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


if __name__ == '__main__':
    donation = [100, 60 , 70, 900 , 100 , 200, 500, 500, 503, 600 , 1000, 1200]
    mode = calculate_mode(donation)
    print('The mode of the list of number is : {0} '.format(mode))