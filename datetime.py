from datetime import datetime
wait_until = datetime.now().second +2
while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')

['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)]
# for number in range(1, 9):
#     if number % 10 == 0:
#         break
# else:
#     print('Let\'s print something out!')

for number in range(1, 100):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')