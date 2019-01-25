from collections import Counter

def find_range(numbers):
    lowests = min(numbers)
    highest = max(numbers)
    r = highest - lowests
    return lowests , highest , r

if __name__ == '__main__':
    donation = [100, 60 , 70, 900 , 100 , 200, 500, 500, 503, 600 , 1000, 1200]
    lowest , highest, r = find_range(donation)
    
    print('Lowest: {0} , Higest: {1} , Range:{2}'.format(lowest , highest, r))