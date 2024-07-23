def evens_and_odds(int_number):
    count_evens = 0
    count_odds  = 0
    for i in range(int_number+1):
        if i%2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    print("The number of odds are ", count_odds)
    print("The number of evens are ", count_evens)
evens_and_odds(100)