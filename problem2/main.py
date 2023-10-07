def caesar(offset, input_str):
    result = ""
    for char in input_str:
        if char.isalpha():
            is_upper = char.isupper()
            
            char_index = ord(char.lower()) - ord('a')
            
            new_index = (char_index + offset) % 26
            
            new_char = chr(new_index + ord('a'))
            
            if is_upper:
                new_char = new_char.upper()
            
            result += new_char
        else:
            result += char
    
    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl
