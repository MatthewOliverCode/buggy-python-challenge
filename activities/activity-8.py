# Make the code output True; there is a hint given
my_dict = {
    1: "1",
    2: "2",
    3: "3"
}
print(1 in my_dict)
if my_dict.get(1) in my_dict:
    print(True)
else:
    print(False)
