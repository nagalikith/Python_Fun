number_of_people = int(input("Number of people"))
people_amount = []
people_return = []
total = 0
amount = 10000
print("Please Do remeber the Chit fund amount is 10,000 ")
for i in range (0,number_of_people):
    name = input("Input Persons name")    
    people_amount.append([name,amount])

for i in people_amount:
    people_return.append(float(i[1]/(amount*number_of_people)))
    
def money_payout(number_of_people,total,people_amount,people_return):
    total = number_of_people*amount
    print("Pot Before the Loan ", total)
    loan = int(input("Enter the Loan amount "))
    total = total - loan
    print("Pot After the Loan ", total)
    for index,i in enumerate(people_amount): 
        print("User ",i[0]," gets",people_return[index]*total)

for i in range (0,number_of_people):
    money_payout(number_of_people,total,people_amount,people_return)
