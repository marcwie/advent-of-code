import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11
import day12
import time


if __name__ == '__main__':
    
    t0 = time.time()

    days = [
        day1, 
        day2, 
        day3, 
        day4, 
        day5, 
        day6, 
        day7, 
        day8, 
        day9, 
        day10,
        day11, 
        day12
        ]

    for i, day in enumerate(days):
        print('----------- Day {0} -----------'.format(str(i+1).zfill(2)))
        day.run()
        print()

    print('Total runtime:', round(time.time() - t0, 2), 'sec.')
