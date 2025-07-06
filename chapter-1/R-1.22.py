import array

def product_array_elements(a, b):
    return [ a[i] * b[i] for i in range(len(a))]

try:
   a = eval(input("Enter array a: "))
   b = eval(input("Enter array b: "))
   print(product_array_elements(a, b))
except ValueError:
    print("Please check input")