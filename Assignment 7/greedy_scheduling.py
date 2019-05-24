from pathlib import Path

def greedy_difference(jobs):
    """ Computes a greedy schedule based on the difference of a job's weight and its length. Ties broken by scheduling higher weighted jobs first."""
    schedule = sorted(jobs, key=lambda job: (weight(job) - length(job), weight(job)), reverse=True)
    return schedule


def greedy_ratio(jobs):
    """ Computes a greedy schedule based on the ratio of a job's weight to its length."""
    return sorted(jobs, key=lambda job: weight(job)/length(job), reverse=True)
    

def sum_weighted_completion_times(schedule):
    """ Computes the sum of the weighted completion times for the jobs in a given schedule."""
    sum = 0
    completion_time = 0
    for job in schedule:
        completion_time += length(job)
        sum += weight(job)*completion_time

    return sum


def weight(job):
    """ Jobs are represented as two-element lists. The first element of each job list is the job's weight."""
    return job[0]


def length(job):
    """ Jobs are represented as two-element lists. The second element of each job list is the job's length."""
    return job[1]

if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()
    
    data = []
    with open(Path(path, 'jobs.txt')) as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip().split()])

    jobs = data[1:] #First line is number of jobs, not needed

    difference_schedule = greedy_difference(jobs)
    ratio_schedule = greedy_ratio(jobs)

    print(sum_weighted_completion_times(difference_schedule))
    print(sum_weighted_completion_times(ratio_schedule))
    