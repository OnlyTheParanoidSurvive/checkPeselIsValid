# https://obywatel.gov.pl/pl/dokumenty-i-dane-osobowe/czym-jest-numer-pesel
# pesel is polish social security number

def checkPeselIsValid(pesel):
    weight = '1379137913'
    a1 = tuple(pesel)[0:10]
    a2 = tuple(weight)

    zipped = zip(a1, a2)
    result=0
    for (a,b) in zipped:
        result_tmp = int(a)*int(b)
        if len(str(result_tmp)) > 1:
            result_tmp = str(result_tmp)[-1]
        result = int(result_tmp) + int(result)
        
    if len(str(result)) > 1:
        result = str(result)[-1]

    new_result = 10 - int(result)

    if int(pesel[-1]) == int(new_result):
        return True
    else:
        return False
    
print(checkPeselIsValid('02070803628'))
