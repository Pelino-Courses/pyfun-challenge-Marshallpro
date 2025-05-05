def calculate(*number,**kwargs) :
     '''This is function to perform calculations on a set of numerical inputs based on specified opertion.
     *args :each must be a number (int or float).
     **kwargs: Keyword arguments specifying operations:
                 
                  - add=True
                  - subtract=True
                  - multiply=True
                  - divide=True
     '''
     if not number:
          raise ValueError("Insert at least a number")
     numbers =[]
     for num in number :
          if not isinstance(num,(int,float)):
               return "Error: inputs must be numbers."
          numbers.append(num)

     result =numbers[0]
     operations_applied =False     
          
     if  kwargs.get('add'):
        return sum(numbers)
     
     elif kwargs.get("subtract"):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

     elif kwargs.get("multiply"):
        result = 1
        for num in number:
            result *= num
        return result

     elif kwargs.get("divide"):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

     else:
        return "Error: No valid operation specified. Use add, subtract, multiply, or divide."


'''main method'''
     
if __name__ == "__main__" :
    print(calculate(1, 2, 3, add=True))       
    print(calculate(10, 5, subtract=True))   
    print(calculate(2, 3, 4, multiply=True)) 
    print(calculate(20, 2, divide=True)) 
    print(calculate("a", 2, add=True)) 


