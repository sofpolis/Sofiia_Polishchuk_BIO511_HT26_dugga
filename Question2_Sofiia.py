my_list = [1, 5, "4", "six", 3.14]
#a)
print("a)")
new_list = []
for el in my_list:
    try:
        new_list.append(int(el))
    except ValueError:
            print(f"The element {el} cannot be converted to int")
            pass
print(new_list)

#b)
print("\nb)")

def clean_list(input_list, output_list):
    output_list = []
    for el in input_list:
        try:
            output_list.append(int(el))
        except ValueError:
            print(f"The element {el} cannot be converted to int")
            pass
    print(output_list)

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
    except IndexError:
        break

     