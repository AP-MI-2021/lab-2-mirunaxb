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

