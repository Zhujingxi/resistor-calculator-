import itertools

list = (open("List.txt", "r"))
target = float(input("target value: "))
num = int(input("number: "))

standard_resistor = []
while 1:
    value = list.readline().strip('\n')
    if value == 'end':
        break
    standard_resistor.append(float(value))

if target in standard_resistor:
    print(target)
    if input("Press N if you don't have: ") != "N":
        exit()


def cal_resistor(resistor_value):
    reciprocal_resistor_value = []
    for y in resistor_value:
        reciprocal_resistor_value.append(1 / y)
    v = 0
    for x in reciprocal_resistor_value:
        v += x
    v = round(1 / v, 6)
    error_persent = str(round((target - v) / target * 100, 2)) + "%"
    return [resistor_value, v, error_persent]


i = 0
for v in standard_resistor:
    if v > target:
        break
    i += 1

# reciprocal_standard_resistor = []
standard_resistor = standard_resistor[i:-1]

combined = []
for p in itertools.combinations_with_replacement(standard_resistor, num):
    combined.append(cal_resistor(p))

reciprocal_target = 1 / target

combined.sort(key=lambda x: abs(float(target - x[1])), reverse=True)

if len(combined) > 100:
    for x in combined[len(combined)-100 : -1]:
        print(x)
    input("Press any to exit")
    exit()
for x in combined:
    print(combined)
    input("Press any to exit")
    exit()