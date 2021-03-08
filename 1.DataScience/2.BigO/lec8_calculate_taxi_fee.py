n = int(input())

def get_taxi_fee(n):
    if n <= 1:
        taxi_fee = n*15000
    elif n <= 5:
        taxi_fee = 15000 + (n-1)*13500
    elif n < 12:
        taxi_fee = 15000 + 4*13500 + (n-5)*11000
    else:
        taxi_fee = (15000 + 4*13500 + (n-5)*11000)*0.9
    return int(taxi_fee)
    
print(get_taxi_fee(n))