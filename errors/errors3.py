run_counter = 0
while run_counter < 3:
    try:
        age = int(input('What is your age? '))
        if age <= 0:
            raise ValueError('Age cannot be less than or equal to Zero.')
        print(f'Your age is {age}')
        run_counter += 1
    finally:
        print('In finally block here.')
else:
    print(f'Finished running program after {run_counter} successful attempts.')
