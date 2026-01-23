def main():
    a = [2,3,3,5,7,8,9]
    for i in range(len(a)):
        for j in range(i+1, len(a)):   
            if a[i] + a[j] == 12:
                print("Indexes:", i, j)

if __name__ == "__main__":
    main()
