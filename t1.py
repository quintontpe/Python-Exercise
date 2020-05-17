import asn1


s='ABCDEFG'
print(s[1:3])

s1='1.2.3.4'

encoder = asn1.Encoder()
encoder.start()
encoder.write('1.2.3.4.5', asn1.Numbers.ObjectIdentifier)
encoded_bytes = encoder.output()
print('Step1', encoded_bytes)


encoder.write(s1, asn1.Numbers.ObjectIdentifier)
encoded_bytes = encoder.output()

print('Step2', s1, encoded_bytes)

encoder.write(s1, asn1.Numbers.ObjectIdentifier)
encoded_bytes = encoder.output()

print('Step3', s1, s1, encoded_bytes)


decoder = asn1.Decoder()
decoder.start(encoded_bytes)
tag, value = decoder.read()

print('tag', tag)
print('value', value)


a=1
b=a
print('a=',a, 'b=', b)

a=a+1
print('a=',a, 'b=', b)
