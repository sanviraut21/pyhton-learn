def main():
    a=[1,3,5,6,7]
    n=int(input("Enter the number:"))
    for i in range(len(a)):
        if n==a[i]:
            print("found",i)
            break
if __name__=="__main__":
    main()