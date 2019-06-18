largest = None
smallest = None

def large(largest, num):
    if largest <= num:
        largest = num
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        entry = float(num)
        large(largest, entry)
    except:
        print("Invalid input")
    continue
    print(num)


print("Maximum", largest)
