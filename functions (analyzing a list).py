numbers = [-5,12,-3,8,0,15,-2,20]

def analyze(numbers):
    
    positive_count = 0
    positive_sum = 0
    negative_count = 0

    for x in range(len(numbers)):

        if numbers[x] > 0:

            positive_count = positive_count + 1
            positive_sum = positive_sum +  numbers[x]

        elif numbers[x] < 0:
            negative_count = negative_count + 1

    return positive_count , positive_sum , negative_count
positive_count,positive_sum,negative_count=analyze(numbers)

result = analyze(numbers)
print("positive numbers :",positive_count)
print("positive sum :",positive_sum)
print("negative numbers :",negative_count)

            
        
