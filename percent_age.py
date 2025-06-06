# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
urdu = int(input("urdu :"))

# Let's calculate the percentage of marks
sum = math + english + science + urdu
print("sum of math, english, science and urdu")

perc = (sum / 400) * 100

print(end="Percentage Mark = ")
print(perc)
