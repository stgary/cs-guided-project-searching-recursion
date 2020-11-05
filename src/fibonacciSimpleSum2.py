
def fibonacciSimpleSum2(n: int) -> bool:
  if (n <= 0) : 
    return 0
   
  fibo =[0] * (n+1) 
  fibo[1] = 1
   
    # Initialize result 
  sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
  for i in range(2,n+1) : 
    fibo[i] = fibo[i-1] + fibo[i-2] 
    sm = sm + fibo[i] 
          
  return sm 
  

# def createHash(hash, max):
  
#   prev, current = 0, 1
#   hash.add(prev)
#   hash.add(current)
  
#   while current < max:
#     temp = current + prev
#     hash.add(temp)
#     prev = current
#     current = temp

# def fibonacciSimpleSum2(n: int) -> bool:

#   hash = set()
#   createHash(hash, n)
  
#   for i in range(n):
    
#     if i in hash and (n - i) in hash:
      
#       return True
  
#   return False



print(fibonacciSimpleSum2(1))
print(fibonacciSimpleSum2(11))
print(fibonacciSimpleSum2(66))