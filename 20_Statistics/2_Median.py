def calculate_meadian(numbers):
    N = len(numbers)
    numbers.sort()
    if N % 2 == 0:
        m1 = N /2
        m2 = (N/2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) /2
    else:
        m = int(m) -1
        median = numbers[m]
  
    return median

if __name__ == '__main__':
    donation = [100, 60 , 70, 900 , 100 , 200, 500, 500, 503, 600 , 1000, 1200]
    median = calculate_meadian(donation)
    N = len (donation)
    print('Mean donation over the last {0} days is {1}'.format(N , median))