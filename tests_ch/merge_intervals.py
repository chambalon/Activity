def merge_intervals(intervals):

    intervals.sort(key=lambda a: a[0])
    #print(interval_list)
    merged_list = []

    for interval in intervals:
        if merged_list ==0 or merged_list[-1][1] < interval[0]:
            merged_list.append(interval)
        else:
            merged_list[-1][1] = max(merged_list[-1][1], interval[1])

    return merged_list


interval_list = [[1.3],
                 [2,5],
                 [6,7],
                 [9,10],
                 [8,12]
]

merge_intervals(interval_list)