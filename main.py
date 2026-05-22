solutions_list = [('Hydrochloric Acid', 1), ('Water', 7), ('Bleach', 13), ('Vinegar', 3), ('Lemon juice', 2), ('Black coffee', 5), ('SodiumHydroxide', 14), ('Ammonia', 11) ]
min_ph = int(input('Enter a minimum pH: '))
max_ph = int(input('Enter a maximum pH: '))

def solutions(solutions_list, min_pH, max_pH):


    filtered = list(filter(lambda x: min_pH <= x[1] <= max_pH, solutions_list))
    if filtered == []:
        print('No compound found')
        exit(0)
    else:
        return filtered


result = solutions(solutions_list, min_ph, max_ph)
for solution in result:
    value, index = solution
    print(f"{value}: pH {index}")