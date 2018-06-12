
## Số nguyên tố:
Số nguyên tố là số chỉ chia hết cho 1 và chính nó.

Cách đơn giản nhất để kiểm tra number có phải là số nguyên tố không là tạo một nhóm các số từ 2 đến number // 2 + 1 (chia lấy phần nguyên).
Nếu number không chia hết cho 1 số nào đó trong nhóm đó --> number là số nguyên tố.

Cách này chưa phải hiệu quả nhất trong việc kiểm tra một số có phải là số nguyên tố không. Ta có thể thu gọn tập số kiểm tra bằng cách tạo ra một nhóm từ 2 đến (căn bậc hai của number) + 1.


Ví dụ:
Kiểm tra số nguyên tố của 36.
36 có các ước số là 2, 3, 6, 9, 18.
căn bậc hai của 36 là 6. --> Chỉ cần kiểm tra từ 2 --> 6 là đủ.


```Python

import math


def is_prime_normal_solution(number):
    if number <= 1:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(2, max_range):
        if not number % counter:
            return False
    return True


```


Việc kiểm tra này có vẻ như khá ổn nhưng liệu có cách nào khác để kiểm tra tốt hơn không ?


Để ý danh sách các số nguyên tố: 2, 3, 5, 7, 11, 13...

Ngoại trừ số 2 đầu tiên, các số tiếp theo đều là số lẻ.

--> Nếu đặt counter = 3 và tăng dần thêm 2 chúng ta sẽ giảm được 1/2 số lần trong vòng lặp.

Ngoài ra chúng ta có thể giảm số lượng so sánh bằng cách đặt bước kiểm tra chia hết cho 2 ngay từ đầu.



```Python

def is_prime_advance_solution(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif not number % 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(3, max_range, 2):
        if not number % counter:
            return False
    return True


```



Đưa 2 function trên vào code hoàn thiện:
```Python

"""
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""
import math

def is_prime_normal_solution(number):
    if number <= 1:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(2, max_range):
        if not number % counter:
            return False
    return True


def is_prime_advance_solution(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif not number % 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(3, max_range, 2):
        if not number % counter:
            return False
    return True



if __name__ == "__main__":
    import time
    number = 3
    print("is_prime_normal_solution: {} ".format(number), end=' ')
    start = time.time()
    print(is_prime_normal_solution(number), end=' ')
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

    print("is_prime_advance_solution: {} ".format(number), end=' ')
    start = time.time()
    print(is_prime_advance_solution(number), end=' ')
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))


```


Kết quả chạy chương trình:
```
Nguyens-MacBook-Pro:prime vinh.nguyenquang$ python3 prime.py 
is_prime_normal_solution: 999999911111111  True elapsed time: 3.7082290649414062s
is_prime_advance_solution: 999999911111111  True elapsed time: 1.875870943069458s
Nguyens-MacBook-Pro:prime vinh.nguyenquang$ python3 prime.py 
is_prime_normal_solution: 9999999111111112  False elapsed time: 2.8133392333984375e-05s
is_prime_advance_solution: 9999999111111112  False elapsed time: 2.1457672119140625e-06s


```


Với khoảng cách thời gian như này, thật đáng để chúng ta suy nghĩ và áp dụng vào thực tế.


