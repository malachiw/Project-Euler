def countPrimes (n):
    x = collections.Counter(n)
    return x.values()

def divisors(n):
    a=1
    for x in n:
        x += 1
        a *= x
    return a

def getNthTriangle(n):
    k = n*(n+1)/2
    return k

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return sieve

def getPrimes(n):
    primes = [2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(n)) if v and i>0]
    return primes

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 
    
def fib(self, number):
  if number==1:
      return 1
  if number==2:
      return 2
  return self.fib(number-2) + self.fib(number-1)

def fibSeq(n):
    index = 1
    fibNumbers = []
    while():
        value = fib(index)
        if value < n:
            fibNumbers.append(fib(index))
            index+=1
        else:
            break
    return fibNumbers   
