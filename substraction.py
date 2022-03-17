

def multiply_two_numbers(number_a, number_b):
  mul = number_a * number_b
  print(mul)
multiply_two_numbers(1,5)


def count_digits(text):
    DIGITS = "0123456789"
    count = 0
    digit_count = []
    for i in text:
        if i in DIGITS:
            digit_count.append(i)
            count += 1
    print(len(digit_count))
count_digits()
