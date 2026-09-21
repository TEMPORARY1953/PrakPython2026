x = int(input())
match x:
    case 1:
        print("один")
    case 2:
        print("два")
    case 3:
        print("три")
    case n if n % 2 == 0:
        print("чётное")
    case n:
        print(f"{n} -- это много")
