rost=int(input())
ves=int(input())

rost_m=rost/100
imt=ves/(rost_m)**2

if imt<16:
    print('выраженный дефицит массы тела')
if imt>=16 and imt<=18.49:
    print('недостаточная масса тела')
if imt>=18.5 and imt<24.99:
    print('норма')
if imt>=25 and imt<=29.99:
    print('избыточная масса тела')
if imt>=30 and imt<=34.99:
    print('ожирение первой степени')
if imt>=35 and imt<=39.99:
    print('ожирение второй степени')
if imt>=40:
    print('ожирение третьей степени')

print(imt)
