def multiply_error_handling():
    user_input = input("Enter numbers: ")

    try:
        update_list = [int(num.strip()) for num in user_input.split(",")]

        print("List of numbers: ", update_list)

        user_index_input = int(input("Enter index of number: "))

        if user_index_input < 1 or user_index_input > len(update_list):
            raise IndexError

        print("Index: ", update_list[user_index_input - 1])
    except ValueError:
        print("Error: Invalid input. Try again")
    except IndexError:
        print("Error: Invalid index input. Try again")
    finally:
        print("Conversion is complete")


multiply_error_handling()
