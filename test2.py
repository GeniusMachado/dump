def main():
    a = [1,2,3,4,5]    
    caller(a)
    
    print(a)
    
def caller(a):
    a = a.append(90) 

main()

