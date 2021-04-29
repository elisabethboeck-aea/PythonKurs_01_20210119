def numbers_add(number_1,number_2):
    result = number_1 + number_2
    return result

def get_cube(number):
    return number * number * number

def get_square_cube(number): # 2 Ergebnisse in einer Funktion - guter Stil ist aber, dass eine Funktion nur eine bestimmte Aufgabe hat!
    square = number * number
    cube = number * number * number
    return square, cube

print(numbers_add(22, 5))
print(get_cube(5))
square, cube = get_square_cube(4) # wie in Array werden Ergebnisse auf variablen square und cube aufgeteilt. Es müssen alle Teile des Arrays hier erwähnt werden!
print(square)
print(cube)
