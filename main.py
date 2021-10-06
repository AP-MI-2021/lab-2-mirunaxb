'''
Găsește ultimul număr prim mai mic decât un număr dat.
'''

def get_largest_prime_below(n):
    for i in range(2 , n):
        prime = 1
        for d in range(2 , n//2):
            if(i % d == 0):
                prime = 0
        if (prime == 1):
            largest = i
    return largest

def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(50) == 47

test_get_largest_prime_below()

'''
Afișează toate pătratele perfecte dintr-un interval închis dat.
'''

def is_perfect_square(n):
    if(int(n ** 0.5) == n **0.5) :
        return True
    return False

def get_perfect_squares(list):
    rez = []
    for i in range(len(list)):
        if is_perfect_square(list[i]):
            rez.append(list[i])
    return rez

def test_get_perfect_squares():
    assert get_perfect_squares([]) == []
    assert get_perfect_squares([3,9,49]) == [9, 49]
    assert get_perfect_squares([7,16,25]) == [16, 25]
    assert get_perfect_squares([14, 28]) == []

test_get_perfect_squares()

'''
Determinare numar superprim.
'''

def is_superprime(n):
    ok = 1
    while n:
        d = 0
        for i in range(1 , int(n)):
            if n % i == 0:
                d = d + 1
        if d > 2:
            ok = 0
        n = n / 10
    if ok == 1:
        return True
    return False

def test_is_superprime():
    assert is_superprime(233) == 1
    assert is_superprime(237) == 0

test_is_superprime()


def main():
    print('''
	    (1.) Largest prime below
	    (6.) Superprime
	    (12.) Perfect squares
	''')
    while True:
        x = int(input("Comanda:"))
        if (x == 1):
            # Largest prime below
            n = int(input("Introduceti n="))
            print(get_largest_prime_below(n))
        if (x == 2):
            # Perfect squares
            n = int(input("Introduceti n="))
            list = []
            for i in range(0, n):
                el = int(input())
                list.append(el)
            print(list)
            print(get_perfect_squares(list))
        if (x == 3):
            # Superprime
            n = int(input("Introduceti n="))
            print(is_superprime(n))
if __name__ == '__main__':
    main()