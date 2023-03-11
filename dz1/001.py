# Найдите сумму цифр трехзначного числа.、
a = int(input('write your number'))
s = (a//100) + (a//10%10) +(a%10) 
print(round(s))