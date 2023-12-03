user_input = input('Input a text: ')

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if is_palindrome(user_input):
    print('This is a palindrome')
else:
    print('This is not a palindrome')