ch = input("Enter a lowercase letter (a-z): ")

if ch in "abcdefghijklmnopqrstuvwxyz":
    pos = ord(ch) - ord('a') + 1
    print("letter-" + str(pos) + " = " + ch)
else:
    print("This is not a lowercase letter (a-z).")
