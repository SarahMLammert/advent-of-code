'''
    2015 Advent of Code Problems
'''

def day1(file_name: str):
    '''
    Help Santa Follow Instructions to Deliver Presents

    Santa moves up and down floors:
    ( is up
    ) is down

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

def day2(file_name: str):
    '''
    Help the Elves with Ordering the Right Amount of Wrapping Paper

    Elves give gift sizes
    length x width x height

    Part 1: Find the total square feet of wrapping paper to order for the gifts

    Part 2: Find the total feet of ribbon
    '''
    try:
        wrapping_paper_area = 0
        ribbon_length = 0

        with open(file_name, encoding='utf-8') as file:
            for line in file:
                x, y, z = sorted(int(x) for x in line.strip().split("x"))

                wrapping_paper_area += 2 * (x*y + y*z + x*z) + (x * y)

                ribbon_length += x*y*z + 2 * (x + y)

        print("Final floor Santa goes to: ", wrapping_paper_area)
        print("The total feet of ribbon: ", ribbon_length)

    except FileNotFoundError:
        print('This file does not exist')

if __name__ == "__main__":
    day1('day1.txt')
    day2('day2.txt')
