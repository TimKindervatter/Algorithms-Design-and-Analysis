def greedy_difference(jobs):
    """ Computes a greedy schedule based on the difference of a job's weight and its length. Ties broken by scheduling higher weighted jobs first."""
    schedule = sorted(jobs, key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    return schedule


def greedy_ratio(jobs):
    """ Computes a greedy schedule based on the ratio of a job's weight to its length."""
    return sorted(jobs, key=lambda x: x[0]/x[1], reverse=True)
    

def sum_weighted_completion_times(schedule):
    """ Computes the sum of the weighted completion times for the jobs in a given schedule."""
    sum = 0
    completion_time = 0
    for job in schedule:
        completion_time += job[1]
        sum += job[0]*completion_time

    return sum

if __name__ == '__main__':
    data = []
    with open('jobs.txt') as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip().split()])

    jobs = data[1:] #First line is number of jobs, not needed

    difference_schedule = greedy_difference(jobs)
    ratio_schedule = greedy_ratio(jobs)

    print(sum_weighted_completion_times(difference_schedule))
    print(sum_weighted_completion_times(ratio_schedule))
    