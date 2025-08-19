s= int(input("Enter the desired sum of digits: "))
div = int(input("Enter the divisor: "))

num =0
while True:
    temp=num
    digit_sum=0
    while(temp > 0):
        digit=temp%10
        digit_sum += digit
        temp//= 10

    if(digit_sum==s and num % div==0):
        smallest_int=num
        break
    num=num+1

print("Smallest number with given sum of digits and divisible by divisor is", smallest_int)
