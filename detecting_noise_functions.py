
# Getting the distance between two values.
def find_distance(arg1,arg2):
    if arg1>arg2:
        avg = (arg1/arg2)*100
    else:
        avg = (arg2/arg1)*100
    if avg >0:
        return int(avg)
    else:
        return 0


# Adding the distance into a dictionary
def add_distance_dict(raw_data,area,column=1):
    
    head_history={}
    tail_history={}

    head=raw_data.head(n=area)[raw_data.columns[column]]
    tail=list(raw_data.tail(n=area)[raw_data.columns[column]])

    for idx in range(area):
        try:
            head_history[f"{(idx)},{(idx+1)}"] = find_distance(head[idx],head[idx+1])
        except:
           pass

    for idx in range(area):
        try:
            tail_history[f"{(idx)},{(idx+1)}"] = find_distance(tail[idx],tail[idx+1])
        except:
           pass

    return (head_history,tail_history,head,tail)
    


# This method will detect weather founded distance is noise or not(boundary is in the head of data set.)
def detect_noise_head(distances,boundary):
    head_history=distances[0]
    noise_data=list()
    for i in range(len(head_history)):
        if head_history[f"{i},{i+1}"]>boundary:
           noise_data.append(head_history[f"{i},{i+1}"])
    return noise_data


# This method will detect weather founded distance is noise or not(boundary is in the tail of data set.)
def detect_noise_tail(distances,boundary):
    tail_history=distances[1]
    noise_data=list()
    for i in range(len(tail_history)):
        if tail_history[f"{i},{i+1}"]>boundary:
            noise_data.append(tail_history[f"{i},{i+1}"])
    return noise_data
