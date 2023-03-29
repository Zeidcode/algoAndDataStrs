def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)

    freq_arr = [0] * (max_val - min_val +1)
    for val in arr:
        freq_arr[val - min_val] += 1


    cum_freq_arr = [0] * len(freq_arr)
    cum_freq_arr[0] = freq_arr[0]
    for i in range(1, len(freq_arr)):
        cum_freq_arr[i] = cum_freq_arr[i-1] + freq_arr[i]


    output_arr = [0] * len(arr)
    for val in arr:
        output_arr[cum_freq_arr[val - min_val] - 1] = val
        cum_freq_arr[val - min_val] -= 1
    

    return output_arr


print(counting_sort([888,3,23,4,23,54,25,23,7,7,7,88,888]))
