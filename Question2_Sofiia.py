my_list = [1, 5, "4", "six", 3.14]
#a)
print("a)")
new_list = [] #create a new list to put integers in
#add a try-except block which prints an error message in case of ValueError
for el in my_list:
    try:
        new_list.append(int(el))
    except ValueError:
            print(f"The element {el} cannot be converted to int")
            pass
print(new_list)

#b)
print("\nb)")
#define a function with a loop within it
def clean_list(input_list, output_list):
    output_list = []
    for el in input_list:
        try:
            output_list.append(int(el))
        except ValueError:
            print(f"The element {el} cannot be converted to int")
            pass
    print(output_list)

#calling the function
clean_list(my_list, new_list)

#c)
print("\nc)")
i=0
for i in range(len(new_list)):
    try:
        for el in new_list:
            neighbour_sum = new_list[i] + new_list[i+1]
            print(neighbour_sum)
            i+=1
    except IndexError: #break the loop in case of IndexError
        break

