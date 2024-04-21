import time


def calculate_private_exponent(N, e):
   
    start_time = time.time()  
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            p = i
            q = N // i
            break
    phi_n = (p - 1) * (q - 1)

    
    d = 0
    for x in range(1, phi_n):
        if (x * e) % phi_n == 1:
            d = x
            break

    end_time = time.time()  
    print("Execution time:", end_time - start_time, "seconds")

    return p, q, d  



N = 1000  
e = 3  
p, q, d = calculate_private_exponent(N, e)
print("Prime factors:", p, q)
print("Private exponent:", d)