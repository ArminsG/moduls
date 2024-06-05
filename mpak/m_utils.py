import math

def sum_prod(seq_a, seq_b):
    return math.prod(seq_a) + math.prod(seq_b)

if __name__ == "__main__":
    print("Aprēķinātā divu sarakstu summa ir:")
    
    a = [2,3] # range(1,5)
    b = [5,10,2] # range(5,10)
    result = sum_prod(a,b)
    print(f"Result: {result}")
