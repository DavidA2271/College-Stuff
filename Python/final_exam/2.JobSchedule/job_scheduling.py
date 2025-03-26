import random


def generate_jobs(n, max_deadline, profit_range=(10, 100)):
    ''' This is the unmodified code you provided '''
    jobs = []
    for i in range(1, n + 1):
        job_id = f'Job_{i}'
        deadline = random.randint(1, max_deadline)
        profit = random.randint(*profit_range)
        jobs.append({'id': job_id, 'deadline': deadline, 'profit': profit})
    return jobs



def maximize_profit(jobs):
    ''' Algorithm focused on maximizing profit while adhering to the deadline of each job '''
    max_profit_jobs = []
    biggest_deadline = 0
    # iterate jobs once while adding most profitable jobs that fit timeline
    for i in range(len(jobs)):
        j = jobs[i]
        if j['deadline'] > biggest_deadline:
            biggest_deadline = j['deadline']
        # if jobs deadline is greater than amt of jobs in list, it can be added if the list has space for it
        if j['deadline'] > len(max_profit_jobs) and len(max_profit_jobs) < biggest_deadline:
            max_profit_jobs.append(j)
            continue
        # this is where I start comparing elements
        max_profit_jobs.sort(key=lambda x: x['profit'])
        # loops from least profitable to most
        for k in range(len(max_profit_jobs)):
            # a job cannot replace a job with a looser deadline
            if max_profit_jobs[k]['deadline'] > j['deadline']:
                continue
            # a job cannot replace a more profitable job
            if max_profit_jobs[k]['profit'] > j['profit']:
                continue
            else:
                max_profit_jobs[k] = j
                break
    return sorted(max_profit_jobs, key=lambda x: x['deadline'])


        


def main():
    j = generate_jobs(10, 5)
    m = maximize_profit(j)
    order = [x['id'] for x in m]
    total_profit = sum(x['profit'] for x in m)
    print("Jobs will be done in the order of:")
    print(', '.join(order))
    print(f"For a total profit of {total_profit}")
    print()
    print("All queued jobs are:")
    for job in m:
        print(job)
    print()
    print()


if __name__ == '__main__':
    main()