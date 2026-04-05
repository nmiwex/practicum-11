numbers = list(map(int, input().split()))
n = len(numbers)
command = input()
direction = command[0].lower()
steps = int(command[1:]) % n

try:
    if direction == 'r':
        new_numbers = numbers[n - steps:] + numbers[:n - steps]
    elif direction == 'l':
        new_numbers = numbers[steps:] + numbers[:steps]
    print(new_numbers)
except NameError:
    print('неизвестная команда')