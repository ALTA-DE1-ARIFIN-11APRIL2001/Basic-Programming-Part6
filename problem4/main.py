def find_max_sum_sub_array(k, arr):
    jumlah_maksimal = jumlah_jendela = sum(arr[:k]) 

    for i in range(k, len(arr)):
        jumlah_jendela += arr[i] - arr[i - k]  

        if jumlah_jendela > jumlah_maksimal:
            jumlah_maksimal = jumlah_jendela

    return jumlah_maksimal

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8
