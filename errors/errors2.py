run_counter = 0
while run_counter < 3:
    try:
        age = int(input('What is your age? '))
        print(f'Your age is {age}')
        div = 10 / age  # dummy code to check 0
        run_counter += 1
    # except ValueError as e:
    #    print(f'Please enter correct age integer. Error: {e}')
    #    # + e - prints error in red if required to do so in your program
    # except ZeroDivisionError as e:
    #    print(f'Age cannot be a Zero! Please enter correct age integer. Error: {e}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Please enter correct age integer. Error: {e}')
    else:
        print(f'Done in else without exception')
        # break;
    finally:
        print('In finally block here.')
else:
    print(f'Finished running program after {run_counter} successful attempts.')
