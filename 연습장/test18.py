directory = {
    1 : 1,
    2 : 1,
}

def fibonacci(n):
    if n in directory:
        return directory[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2 )
        directory[n] = output
        return output

print("fibonacci(1) : " , fibonacci(1))
print("fibonacci(2) : " , fibonacci(2))
print("fibonacci(3) : " , fibonacci(3))
print("fibonacci(4) : " , fibonacci(4))
print("fibonacci(1002) : " , fibonacci(1002))


