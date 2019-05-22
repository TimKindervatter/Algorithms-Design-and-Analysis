def greedy_difference(jobs):
    return sorted(jobs, key=difference, reverse=True)


def difference(job):
    """ Returns the job's weight minus its length."""
    return job[0] - job[1] 


def greedy_ratio(jobs):
    return sorted(jobs, key=ratio, reverse=True)


def ratio(job):
    """Returns the job's weight divided by its length"""
    return job[0]/job[1]

if __name__ == '__main__':
    data = []
    with open('jobs.txt') as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip().split()])