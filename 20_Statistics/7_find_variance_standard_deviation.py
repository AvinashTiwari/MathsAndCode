from collections import Counter

def calulate_mean(numbers):
    s= sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def find_differences(numbers):
    mean = calulate_mean(numbers)
    diff =[]
    for num in numbers:
        diff.append(num-mean)
    
    return diff

def calculate_variance(numbers):
    diff =find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    
    squared_sqaured_diff = sum(squared_diff)
    variance = squared_sqaured_diff / len(numbers)
    return variance

if __name__ == '__main__':
    donation = [100, 60 ,70, 900, 100, 200, 500, 500 ,503, 600, 1000, 1200]
    variance = calculate_variance(donation)
    print('The variance of the list pf number is {0} '.format(variance))
    std = variance**0.5
    print('The standard deviation of the list of the numbers is {0} '.format(std))