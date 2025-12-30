def calculate_pyramidal_number(n):
    
    if n < 0:
        raise ValueError("Число n не може бути меншим за 0!")
    if n == 0:
        return 0
    pyramidal_sum = 0
    current_triangular = 0
  
    for i in range(1, n + 1):
        current_triangular += i
        pyramidal_sum += current_triangular    
    return pyramidal_sum

if __name__ == "__main__":
    try:
        user_input = int(input("Введіть значення n: "))
        
        result = calculate_pyramidal_number(user_input)
        print(f"Пірамідальне число для n={user_input} дорівнює: {result}")
        
    except ValueError as e:
        print(f"Помилка: {e}")