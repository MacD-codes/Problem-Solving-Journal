'''
In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?
'''
# Test Cases:
'''
test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)
'''
# SOLUTION:
def nb_year(p0, percent, aug, p):
    current_pop=p0
    year=0
    while current_pop<p:
        growth=current_pop*(percent/100)
        current_pop=int(current_pop+growth+aug)
        year+=1
    return year