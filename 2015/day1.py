'''
    Day 1
'''

def day1(file_name):
    '''
    Help Santa Follow Instructions to Deliver Presents

    Santa moves up and down floors:
    ( means up
    ) means down

    Part 1: Find the floor that the instructions send Santa to

    Part 2: Find the first instruction that causes Santa to enter the basement
    '''

    try:
        floor_num = 0
        found_basement = False

        with open(file_name, encoding='utf-8') as file:
            for i, ch in enumerate(file.read()):
                if ch == "(":
                    floor_num += 1
                elif ch == ")":
                    floor_num -= 1

                if floor_num == -1 and not found_basement:
                    print("First instruction that sends Santa to the basement: ", i)
                    found_basement = True

        print("Final floor Santa goes to: ", floor_num)

    except FileNotFoundError:
        print('This file does not exist')

if __name__ == "__main__":
    day1('day1.txt')
