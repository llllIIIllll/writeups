# -*- coding: utf-8 -*-
#
# Hill Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import numpy as np

# 

def encrypt(matrix, words):
    check_param(matrix, words)
    cipher = ''
    length = len(matrix)
    matrix = np.array(matrix)
    words = words.lower()
    arr = [ord(i) - ord('a') for i in words]
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            cipher += chr(sum(matrix[count % length] * arr) % 26 + ord('a'))
            count += 1
    return cipher


# 

# 
def decrypt(matrix, words):
    cipher = ''
    length = len(matrix)
    matrix = (np.linalg.inv(matrix) + 26) % 26
    words = words.lower()
    arr = np.array([ord(i) - ord('a') for i in words], dtype=int)
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            number = sum(matrix[count % length] * arr) % 64;
            cipher += chr(int(str(number)[:-2]) + ord('a'))
            count += 1
    return cipher


# 
# 
def check_param(matrix, words):
    if len(matrix) * len(matrix) != \
       sum([len(matrix[i]) for i in range(len(matrix))]):
        print("Error: dimenstions must be the same m * m")
        quit()
    elif len(matrix) != len(words):
        print("Error:something broken")
        quit()
    try:
        np.linalg.inv(matrix)
    except Exception, e:
        print("Error: some exception: " + str(e))
        quit()


if __name__ == '__main__':
    secret = [[54, 53, 28, 20, 54, 15, 12, 7],
          [32, 14, 24, 5, 63, 12, 50, 52],
          [63, 59, 40, 18, 55, 33, 17, 3],
          [63, 34, 5, 4, 56, 10, 53, 16],
          [35, 43, 45, 53, 12, 42, 35, 37],
          [20, 59, 42, 10, 46, 56, 12, 61],
          [26, 39, 27, 59, 44, 54, 23, 56],
          [32, 31, 56, 47, 31, 2, 29, 41]]


#    text = "hill";
    text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"
    
    #ciphertext = encrypt(secret, text)
    ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"

    print(ciphertext)
    
    print(decrypt(secret, ciphertext))
