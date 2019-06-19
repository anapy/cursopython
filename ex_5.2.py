small = None
large = None

while True:
    try:
        num = input("Enter a number: ")

        if num == "done":
            break
        num = int(num)
        if small is None:
            small = num

        if large is None:
            large = num

        if num > large:
            large = num

        if num < small:
            small = num

    except:
        print("Invalid input")
        continue

print("Maximum is", large)
print("Minimum is", small)
