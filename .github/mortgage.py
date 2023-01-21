def mortgage(years, interest_rate, money_borrowed):
    r = interest_rate / 100 / 12  
    n = years * 12
    return (r * money_borrowed) / (1 - (1 + r) **-n)

print(mortgage(20,6.5,200000)) 
