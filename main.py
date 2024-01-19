#ub1
from functools import reduce
def is_palindrom(string):
    if len(string) <=1:
        return True
    if string[0].lower() != string[-1]:
        return False
    return is_palindrom(string[1:len(string)-1])

def count_palindromes(underage,filename):
    with open(filename, 'r') as f:
        personal_data=list(map(lambda line: line.split('\n')[0].split(','),f))

    if underage:
        result=list(filter(lambda person: is_palindrom(person[0])and int(person[1])<18,personal_data))
    else:
        result=list(filter(lambda person: is_palindrom(person[0]),personal_data))

    result_count = len(result)
    return result_count

result_underage = count_palindromes(True,'people.txt')
print(f"underage + palindrom :{result_underage}")

result_all = count_palindromes(False,'people.txt')
print(f"all names that are palindromes:{result_all}")

def test_underage_true():
    assert count_palindromes(True,people.txt) == 2
def test_underage_false():
    assert count_palindromes(False,people.txt) == 6

 #test_underage_true()
 #test_underage_false()

#ub2

class BinaryNumber():
    def __init__(self, number_string: str):
        self.number_string = number_string
        self.numberList = [int(digit) for digit in self.number_string]

    def _str_(self):
        return f'BinaryNumber {self.number_string}'

    def sum(self, number, return_list: bool):
        number1 = list(reversed(self.numberList))
        number2 = list(reversed(number.numberList))
        if return_list:
            cf = 0
            new_number = []
            if len(number1) > len(number2):
                maxim = number1
            else:
                maxim = number2
            for index in range(len(maxim)):
                if index < min(len(number1), len(number2)):
                    digit_on_pos = number1[index] + number2[index] + cf
                else:
                    digit_on_pos = maxim[index] + cf

                if digit_on_pos > 1:
                    cf = 1
                    digit_on_pos = 0
                else:
                    cf = 0

                new_number.append(digit_on_pos)

            if cf == 1:
                new_number.append(1)

            return new_number[::-1]
        else:
            cf = 0
            new_number = []
            if len(number1) > len(number2):
                maxim = number1
            else:
                maxim = number2
            for index in range(len(maxim)):
                if index < min(len(number1), len(number2)):
                    digit_on_pos = number1[index] + number2[index] + cf
                else:
                    digit_on_pos = maxim[index] + cf

                if digit_on_pos > 1:
                    cf = 1
                    digit_on_pos = 0
                else:
                    cf = 0

                new_number.append(digit_on_pos)

            if cf == 1:
                new_number.append(1)

            numberString = ''.join(map(str, reversed(new_number)))
            return numberString


binary_number1 = BinaryNumber("101")
binary_number2 = BinaryNumber("1110")
binary_number3 = BinaryNumber('1001')
res_sum = binary_number1.sum(binary_number2, True)
res_sum2 = binary_number1.sum(binary_number2, False)
print('sum as list:', res_sum)
print('sum as string:', res_sum2)


class RepoBinaryNumber:
    def __init__(self):
        self.binarynumbers = []

    def sum_all(self):
        if len(self.binarynumbers) == 1:
            number1 = self.binarynumbers[0]
            return BinaryNumber.sum(BinaryNumber('0'), number1, False)
        elif len(self.binarynumbers) == 2:
            number1 = self.binarynumbers[0]
            number2 = self.binarynumbers[1]
            return BinaryNumber.sum(number1, number2, False)

    def add(self, number: BinaryNumber):
        if number.numberList[-1] == 1:
            self.binarynumbers.append(number)


repo_binary_number = RepoBinaryNumber()
repo_binary_number.add(binary_number1)
repo_binary_number.add(binary_number2)
repo_binary_number.add(binary_number3)
print('sum from odd numbers: ', repo_binary_number.sum_all())

