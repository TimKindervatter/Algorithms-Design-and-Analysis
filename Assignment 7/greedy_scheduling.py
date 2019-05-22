def greedy_difference(jobs):
    schedule = sorted(jobs, key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    return schedule


def greedy_ratio(jobs):
    return sorted(jobs, key=lambda x: x[0]/x[1], reverse=True)
    


def sum_weighted_completion_times(jobs):
    sum = 0
    completion_time = 0
    for job in jobs:
        completion_time += job[1]
        sum += job[0]*completion_time

    return sum

if __name__ == '__main__':
    data = []
    with open('jobs.txt') as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip().split()])

    