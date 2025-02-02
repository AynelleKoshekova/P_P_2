from utilities import (
    grams_to_ounces, fahrenheit_to_celsius, solve, is_prime, filter_prime, 
    reverse_words, has_33, spy_game, sphere_volume, unique_list, is_palindrome, 
    print_permutations
)
print("Testing grams_to_ounces:")
print(grams_to_ounces(100)) 

print("\nTesting fahrenheit_to_celsius:")
print(fahrenheit_to_celsius(32))  
print(fahrenheit_to_celsius(212))  

print("\nTesting solve:")
print(solve(4, 10))  
print(solve(5, 14)) 
print(solve(3, 6)) 
print(solve(3, 7))  

print("\nTesting is_prime:")
print(is_prime(7)) 
print(is_prime(10))  

print("\nTesting filter_prime:")
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  

print("\nTesting reverse_words:")
print(reverse_words("Hello world this is Python"))  

print("\nTesting has_33:")
print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3])) 

print("\nTesting spy_game:")
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7])) 
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

print("\nTesting sphere_volume:")
print(sphere_volume(3))  

print("\nTesting unique_list:")
print(unique_list([1, 2, 2, 3, 4, 4, 5]))  

print("\nTesting is_palindrome:")
print(is_palindrome("madam")) 
print(is_palindrome("hello")) 
print(is_palindrome("A man, a plan, a canal, Panama"))  

print("\nTesting print_permutations:")
print_permutations("abc")  
