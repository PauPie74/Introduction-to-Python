try:
    d = input()
    key = d[3]+d[4]
    k = int(key)
    while k > 12:
        d = input()
        key = d[3]+d[4]
        k = int(key)
    m ={"01":"styczeń","02":"luty","03":"marzec","04":"kwiecień","05":"maj","06":"czerwiec","07":"lipiec","08":"sierpień","09":"wrzesień","10":"październik","12":"listopad","12":"grudzień"}
except ValueError:
    d = input()

if d[0] == "0":
    print(d[1],m[key],d[6]+d[7]+d[8]+d[9])
else:
    print(d[0]+d[1],m[key],d[6]+d[7]+d[8]+d[9])