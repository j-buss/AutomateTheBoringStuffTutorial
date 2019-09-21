def list_to_string(input_list):
    try:
        output_string = input_list[0]
        if len(input_list) >= 3:
            for item in input_list[1:-1]:
                output_string = output_string + ', ' + item
        if len(input_list) >= 2:
            output_string = output_string + ' and ' + input_list[-1]
        return output_string
    except IndexError:
        print('Input list does not have a value. Potentially you are trying to pass an \"empty\" list?')

def main():
    print(list_to_string([]))
    print(list_to_string(['test 1']))
    print(list_to_string(['test 1', 'test 2']))
    print(list_to_string(['test 1', 'test 2', 'test 3']))
     
if __name__ == "__main__":
     main()
