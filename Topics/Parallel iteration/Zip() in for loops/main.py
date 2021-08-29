# please do not modify the following code
interest_rates = [float(x) for x in input().split(',')]
years = [int(x) for x in input().split(',')]
loan_principles = [int(x) for x in input().split(',')]

# your code here
for i in zip(interest_rates, years, loan_principles):
    print(int(i[0] * i[1] * i[2]))
