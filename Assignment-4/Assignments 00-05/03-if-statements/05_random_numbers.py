import random  

def main():
    print(*[random.randint(1, 100) for _ in range(10)])

if __name__ == '__main__':
    main()