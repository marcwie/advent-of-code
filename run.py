import day01, day02, day03, day04, day05, day06, day07, day08
import day09, day10, day11, day12, day13, day14, day15, day16
import day17, day18, day19, day20, day21, day22
import time


if __name__ == '__main__':
    
    t0 = time.time()

    days = [
        day01, 
        day02, 
        day03, 
        day04, 
        day05, 
        day06, 
        day07, 
        day08, 
        day09, 
        day10,
        day11, 
        day12,
        day13,
        day14,
        day15,
        day16,
        day17,
        day18,
        day19,
        day20,
        day21,
        day22,
        ]

    for i, day in enumerate(days):
        print(20 * '-' + ' Day {0} '.format(str(i+1).zfill(2)) + 20 * '-')
        day.run()
        print()

    print('Total runtime:', round(time.time() - t0, 2), 'sec.')
