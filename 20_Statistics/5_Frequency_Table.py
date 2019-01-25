from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\t Factory')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number[1]))



if __name__ == '__main__':
    scores = [5,5,5,4,4,4,9,1,3]
    frequency_table(scores)