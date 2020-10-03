import math

class Prime():
    def __init__(self, number = 1000):
        self.number = number
        print(self.number)
##        self.midpoint = self.__midpoint__(self.number)

    def __midpoint__(self, chk_number):
        return int(math.sqrt(chk_number))

    def is_prime(self, chk_number = number):
        """
        checks if a number is prime by looping through each possible
        divisor and moding with chk_number.  divisors range from 3 to
        the square root of chk_number.
        """  
        #first check the easy ones.
        if chk_number == 2:
            return True
        elif chk_number == 1 or chk_number %2 == 0:
            return False   #one or even is not prime

        midpoint = self.__midpoint__(chk_number)
        for num in range(3, midpoint +1, 2):
            if chk_number % num == 0:
                return False

        return True

    def closest_prime(self, chk_number, ignore_chk_num = False):

        if chk_number < 2:
            print('ERROR: Numbers below 2 are never prime.')
            return 0
        
        if not ignore_chk_num:
            if self.is_prime(chk_number):
                return(chk_number)
        
        for num in range(chk_number-1,0,-1):
            if self.is_prime(num):
                return num

        return 0 #something else is wrong

    def primes_list(self, max_num):
        p_list = []
        for num in range(2,max_num):
            if self.is_prime(num):
                p_list.append(num)

        return p_list

    def find_adjacent_primes(self, start_num, closeness = 3):
        i = start_num
        adj_list = []

        while True:
            p1 = self.closest_prime(i, ignore_chk_num = False)
            p2 = self.closest_prime(p1, ignore_chk_num = True )
            if (p1 - p2) <=closeness:
                adj_list.append((p1,p2))
            i = p2
            if i <= 2:
                break

        return adj_list

    
    


if __name__ == '__main__':

    chk_num = 100
    p = Prime(1000)

##    p_list = p.primes_list(chk_num)
##    for i in range(len(p_list)):
##        print(p_list[i])
    

##    for i in range(20):
##        print(i, p.is_prime(i))

     
    print(f'The prime closest to {chk_num} is {p.closest_prime(chk_num, ignore_chk_num=True)}')
##    print(f'The prime closest to {chk_num} is {p.closest_prime(chk_num)}')

    test_list = p.find_adjacent_primes(chk_num, closeness = 2)
##    for i in range(3):
##        print(test_list[i])

    print(test_list)
    
