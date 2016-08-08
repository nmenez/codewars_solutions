def get_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def get_lcm(x, y):
   lcm = (x*y)//get_gcd(x,y)
   return lcm

def nbr_of_laps(x, y):
    lcm = get_lcm(x,y)
    return [lcm/x, lcm/y]


print(nbr_of_laps(3,5))
print(nbr_of_laps(4,6))
print(nbr_of_laps(5,5))