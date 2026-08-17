c=input('')
n=input('')
l=list()
n=int(n)
while int(n)>0:
    t=input('')
    l.append(int(t))
    n=n-1
x=0
for weight in l:
    w=weight+x
    x=w
print('Total Shipment Weight:', x)

lenght=len(l)
a=x/lenght

print('Average Container Weight:',a)

maxi=max(l)

print('Heaviest Container:', maxi)
print('Lightest Container:', min(l))

if x>=200:
    print('Classification: Heavy')
else:
    print('Classification: Light')


if x<int(c):
    print('Status: Shipment can be unloaded')
else:
    print('Status: Shipment exceeds port capacity')
