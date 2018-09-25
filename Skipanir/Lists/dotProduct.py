
# Input vector size: 3
# Element no 1: 1
# Element no 2: 3.0
# Element no 3: -5
# Element no 1: 4
# Element no 2: -2.0
# Element no 3: -1
# Dot product is:  3.0

def input_vector(size):
    input_vector = []
    element = 1
    for i in range(size):
        vector = float(input("Element no {}: ".format(element)))
        element += 1
        input_vector.append(vector)
    return input_vector

def dot_product(vector1, vector2):
    dot_product = 0
    for i in range(size):
        vector = vector1[i] * vector2[i]
        dot_product += vector

    return dot_product

    



# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))
