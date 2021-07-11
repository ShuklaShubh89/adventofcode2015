import hashlib

input = 'yzbqklnj'
for x in range(99999999):
    hashinput = input+str(x)
    result = hashlib.md5(hashinput.encode())
    if(str(result.hexdigest()).startswith('00000')):
        print(x)
        break