grades = [["Math", 80], ["ELA", 90], ["Art", 88], ["Social, 95"]]
print(grades[1][1])

grade = {"Math":80,
         "ELA":90,
         "Art":88,
         "Social":95}

print(grade["Math"])
grade["Math"] = 95
grade["Science"] = 90

print(grade)
del grade["Math"]
print(grade)