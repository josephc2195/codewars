#https://www.codewars.com/kata/513e08acc600c94f01000001
def create_phone_number(n):
    return '(' + "".join(map(str, n[0:3])) + ') ' + "".join(map(str, n[3:6])) + '-' + "".join(map(str, n[6:10]))
