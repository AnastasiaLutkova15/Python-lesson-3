# Task 16

N = int(input())
A = list(range(1, N + 1))
print(A)
X = int(input())
print(A.count(X))

# Task 18

# N = int(input())
# A = list(range(1, N + 1))
# print(A)
# X = int(input())
# num = 0
# for i in range(len(A)):
#     if (X-A[i]) < X - num and X - A[i] > 0:
#         num = i
# print(A[num])

# Task 20

# text = input()
# eng = {1:'A, E, I, O, U, L, N, S, T, R',
#        2:'D, G',
#        3:'B, C, M, P',
#        4:'F, H, V, W, Y',
#        5:'K',
#        8:'J, X',
#        10:'Q, Z'}
# rus = {1:'А, В, Е, И, Н, О, Р, С, Т',
#        2:'Д, К, Л, М, П, У',
#        3:'Б, Г, Ё, Ь, Я',
#        4:'Й, Ы',
#        5:'Ж, З, Х, Ц, Ч',
#        8:'Ш, Э, Ю',
#        10:'Ф, Щ, Ъ'}
# result = 0
# for i in text:
#     for key, value in rus.items():
#         if i.upper() in value:
#             result += key
# else:
#     for i in text:
#         for key, value in eng.items():
#             if i.upper() in value:
#                 result += key
# print(result)