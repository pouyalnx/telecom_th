import json

temp=[['a','b'],['l90','money'],['fabirc','linux'],['python','family'],['او عاشقی منه','ماشالله چه جوانه']]
temp_str1=json.dumps(temp)
temp_str2=json.dumps(temp,ensure_ascii=False)#.encode('ascii')

print(temp_str1)
print(temp_str2)

print(bytes(temp_str1.encode('utf8')))
print(bytes(temp_str2.encode('utf8')))

data=bytes(temp_str2.encode('utf8'))

print(data.decode('utf8'))
