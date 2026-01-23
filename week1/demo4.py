def main():
    a=[2,3,3,5,7,8,9,5,6,3,2,3,2,1,4,1,2,2]
    count=0
    max=0
    n=0
    for i in range(len(a)):
        if a[0]==a[i]:
            count=count+1
            continue
        elif(count>max):
            max=count
            n=a[i] 
            count=0
    print("The max count=",max)
    print("count",n)
    
if __name__=="__main__":
    main()