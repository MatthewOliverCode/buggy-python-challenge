# Find the bug and the antipattern
my_amazing_file = open("main.py","r")

for line_of_code in my_amazing_file:
  print(str(line_of_code))

my_amazing_file.close()
