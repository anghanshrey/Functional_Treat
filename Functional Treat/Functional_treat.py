print("Welcome to the Data Analyzer and Transformer Program")

# Global variables to store our datasets
array_1d = []
array_2d = []

def input_data():
   
   """Inputs data for 1D and 2D arrays."""
   global array_1d, array_2d

   print("1. 1D array")
   print("2. 2D array")
   input_choice = int(input("Choice the number:"))

   if input_choice == 1:
      # 1D Array Input
      print("Enter data for a 1D array (separated by spaces) :", end=" ")
      array_1d = list(map(int, input().split(" ")))
      print("1D Array:", array_1d)
   elif input_choice == 2:
      # Simple 2D Array Input (2 Rows)
      print("\n--- 2D Matrix Setup (2 Rows) ---")
      row1 = list(map(int, input("Enter values for Row 1 (separated by spaces): ").split()))
      row2 = list(map(int, input("Enter values for Row 2 (separated by spaces): ").split()))
      array_2d = [row1, row2]
      print("2D Matrix successfully stored!")
      print("Row 1:", array_2d[0])
      print("Row 2:", array_2d[1])
   else:
      print("Enter only 1 ANd 2 Number.")                              

def display_data():
   """Displays data summary using built-in functions."""
   if not  array_1d:
      print("Dataset is empty. Please input data first.")
      return
        
   print("--- 1D Data Summary ---")
   print("- Total elements: ", len(array_1d))
   print("- Minimum value: ", min(array_1d))
   print("- Maximum value: ", max(array_1d))
   print("- Sum of all values: ", sum(array_1d))
   print("- Average value: ", sum(array_1d) / len(array_1d))
    
   if array_2d:
      print("\n--- 2D Data Summary ---")
      print("- Row 1  & 2 Total Elements: ", len(array_2d[0] + array_2d[1]))
      print("- Row 1  & 2 Minimum: ", min(array_2d[0] + array_2d[1]))
      print("- Row 1  & 2 Maximum: ", max(array_2d[0] + array_2d[1]))
      print("- Row 1  & 2 Sum: ", sum(array_2d[0] + array_2d[1]))
      print("- Row 1  & 2 Average: ", sum(array_2d[0] + array_2d[1])/len(array_2d[0] + array_2d[1]))
   else:
      print("First input 2D array.")

def find_factorial(factorial):
    """Calculates factorial using recursion."""
    if factorial == 0 or factorial == 1:
        return 1
    else:
        return factorial * find_factorial(factorial - 1)

def filter_data():
   print("Select Option:\n")
   print("1. 1D array")
   print("2. 2D array")
   filter_input = int(input("Select your Option : "))
   """Filters 1D data by threshold using a lambda function."""
   if filter_input == 1:
      if not array_1d:
         print("Dataset is empty!")
         return
        
      threshold = int(input("Enter a threshold value to filter out data above this value: "))
      filtered_data = list(filter(lambda x: x >= threshold, array_1d))
      print(f"Filtered Data (values >= {threshold}):\n{filtered_data}")
       
   elif filter_input == 2:
       """Filters 1D data by threshold using a lambda function."""
       if array_2d:
           threshold = int(input("Enter a threshold value to filter out data above (2d_array) value: "))
           array2 = (array_2d[0] + array_2d[1])
           filtered2d_data = list(filter(lambda x: x >= threshold, array2))
           print(f"Filtered Data (values >= {threshold}):\n{filtered2d_data}")
       else:
           print("2d Dataset is empty!")

   else:
      print("Enter only 1 And 2 number.")

def sort_data():
   print("Select Option:\n")
   print("1. 1D sort array")
   print("2. 2D sort array")
   filter_sort = int(input("Select your Option : "))
   match filter_sort:
      case 1:
         """Sorts the 1D dataset."""
         if not array_1d:
             print("Dataset is empty!")
             return
        
         print("Choose sorting option:")
         print("1. Ascending")
         print("2. Descending")

         sort_choice = int(input("Enter your choice: "))
         if sort_choice == 1:
             array_1d.sort()
             print("Sorted Data:", array_1d)
         elif sort_choice == 2:
             array_1d.sort(reverse=True)
             print("Sorted Data:", array_1d)
         else:
             print("Invalid choice.")
      case 2:
         """Sorts the 2D dataset."""
         if not array_2d:
             print("2d_Dataset is empty!")
             return
        
         print("Choose sorting option:")
         print("1. Ascending")
         print("2. Descending")

         sort_choice = int(input("Enter your choice: "))
         if sort_choice == 1:
             array_2 = [sorted(row) for row in array_2d]
             print("Sorted Data:", array_2)
         elif sort_choice == 2:
             array_2reverse = [sorted(row, reverse = True) for row in array_2d]
             print("Sorted Data:", array_2reverse)
         else:
             print("Invalid choice.")
      case _:
         print("Enter only 1 And 2 Number.")

def display_multipledata(*args):  
   print("Select Option:\n")
   print("1. 1D  display array")
   print("2. 2D display array")
   display_data = int(input("Select your Option : "))

   if display_data == 1:
      """Returns multiple statistics values."""
      if not array_1d:
          return 0, 0, 0, 0
      minimum = min(array_1d)
      maximum = max(array_1d)
      sum_all = sum(array_1d)
      average = sum_all / len(array_1d)
      return minimum, maximum, sum_all, average
   elif display_data == 2:
      if not array_2d:
         return 0,0,0,0
      minimum_2d = min(array_2d[0] + array_2d[1])
      maximum_2d = max(array_2d[0] + array_2d[1])
      sum_all_2d = sum(array_2d[0] + array_2d[1])
      average_2d = sum_all_2d / len(array_2d[0] + array_2d[1])
      return minimum_2d , maximum_2d , sum_all_2d , average_2d

def print_summary_kwargs(**kwargs):
    """Prints the statistics using **kwargs."""
    print("Dataset Statistics:")
    print("- Minimum value:", kwargs.get("min"))
    print("- Maximum value:", kwargs.get("max"))
    print("- Sum of all values:", kwargs.get("sum"))
    print("- Average value:", kwargs.get("avg"))

while True:
    print("""
Main Menu:
1. Input Data (1D & 2D)
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
""")

    menu_choice = int(input("Please enter your choice: "))

    match menu_choice:
        case 1:
           print("Documantation : ",input_data.__doc__)
           input_data()
        case 2:
           print("Documantation : ",display_data.__doc__)
           display_data()
        case 3:
           print("Documantation : ",find_factorial.__doc__)
           factorial_number = int(input("Enter a number to calculate its factorial: "))
           if factorial_number < 0:
              print("Factorial is not defined for negative numbers.")
           else:
               answer = find_factorial(factorial_number)
               print(f"Factorial of {factorial_number} is: {answer}")
        case 4:
           print("Documantation : ",filter_data.__doc__)
           filter_data()
        case 5:
           print("Documantation : ",sort_data.__doc__)
           sort_data()
        case 6:
           print("Documantation : ",display_multipledata.__doc__)
           v1, v2, v3, v4 = display_multipledata()
           print_summary_kwargs(min=v1, max=v2, sum=v3, avg=v4)
        case 7:
           print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
           break
        case _:
            print("Enter numbers 1 to 7.")
