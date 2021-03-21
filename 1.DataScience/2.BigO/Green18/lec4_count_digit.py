n = int(input())
def count_num(n):
  i = 0
  while n > 0:
    i += 1
    n = n // 10
  return i

print(count_num(n))