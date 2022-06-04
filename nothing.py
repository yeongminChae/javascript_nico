def num():
    n = int(input(" 세 자리수 입력 :"))
    a = n // 100
    b = (n % 100)//10
    c = (n % 100) %10
    if n // 100 < 10 :
        print(f'100의 자리 = {a} ' ,
            f'10의 자리 = {b} ' ,
            f'1의 자리 = {c}')
    else :
        print(" 세 자리수가 입력되지 않음 ")
        return num
    


