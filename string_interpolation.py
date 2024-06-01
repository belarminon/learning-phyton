name = "Belarmino"
age = 43
profission = "Developer"
language = "Phyton"

# Old style %
print("Old style %")
print("Hello, I'm %s, I'm %d years old, I work as %s and my hard skill is %s." %(name, age, profission, language))
print()

# Format method
print("Format method")
print("Hello, I'm {}, I'm {} years old, I work as {} and my hard skill is {}." .format(name, age, profission, language))
print("Hello, I'm {2}, I'm {0} years old, I work as {3} and my hard skill is {1}." .format(age, language, name, profission))
print("Hello, I'm {name}, I'm {age} years old, I work as {profission} and my hard skill is {language}." .format(age = age, language = language, name = name, profission = profission))
print()