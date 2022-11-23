# on this case I need to create a number converter than convert numbers to text and text to numbers, only with if, elif and else

def converter():
    print(f' {"=" * 10}\n CONVERTER \n {"=" * 10} ')
    print(f'Options menu: \n {"="* 15}')
    print("Convert numbers to text press: 1")
    print("Convert text to numbers press: 2\n")
    convert_type = int(input("Type your selection: "))
    if convert_type == 1:
       convert_num_to_text = input("Please insert the number: ")
       if convert_num_to_text == '1':
           print("\n The number is 'ONE' \n")
       elif convert_num_to_text == '2':
           print("\n The number is 'Two'\n")
       elif convert_num_to_text == '3':
           print("\n The number is 'Three'\n")
       else:
           print(f'{"*" * 15}\n OUT OF RANGE. \n {"*" * 15} ')
    elif convert_type == 2:
        convert_text_to_num = input("Please introduce the number in text: ")
        if convert_text_to_num == 'one':
            print("The number is '1'")
        elif convert_text_to_num == 'two':
            print("The number is '2'")
        elif convert_text_to_num == 'three':
            print("The number is '3'")
        else:
            print(f'{"*" * 15}\n OUT OF RANGE. \n {"*" * 15} ')
    else:
        print(f'{"*" * 15}\n OUT OF RANGE. \n {"*" * 15} ')
    print(f' {"*" * 4}\n END. \n {"*" * 4} ')
converter()