import ipfshttpclient

client = ipfshttpclient.connect()
res = client.add('test.txt')
print(res)