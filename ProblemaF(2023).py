coordenadas = input()

x1 = int(coordenadas.split()[0])
y1 = int(coordenadas.split()[1])
x2 = int(coordenadas.split()[2])
y2 = int(coordenadas.split()[3])

pts = []

if y1 == y2 :
    if x1 < x2  :
        for i in range(x1, x2+1) :
            add = str(i) + " " + str(y1)
            pts.append(add)

    elif x1 > x2 :
        for i in range(x1, x2-1, -1) :
            add = str(i) + " " + str(y1)
            pts.append(add)

elif x1 == x2 :
    if y1 < y2  :
        for i in range(y1, y2+1) :
            add = str(x1) + " " + str(i)
            pts.append(add)

    elif y1 > y2 :
        for i in range(y1, y2-1, -1) :
            add = str(x1) + " " + str(i)
            pts.append(add)

elif y1 != y2 and x1 != x2 :
    m = (y2 - y1) / (x2 - x1)

    #print(m)
    if x1 < x2 :
        for i in range(x1,x2+1) :
            y = (m * i) - (x1 * m) + y1
            add = str(i) + " " + str(y)
            pts.append(add)
    elif x1 > x2 :
        for i in range(x1,x2 - 1, -1) :
            y = (m * i) - (x1 * m) + y1
            add = str(i) + " " + str(y)
            pts.append(add)

#print(pts)

number_pts_to_validate = int(input())
pts_to_validate = []

for i in range(0,number_pts_to_validate) :
    pts_input = input()
    pts_to_validate.append(pts_input)

#print(pts_to_validate)

count = 0
for i in range(0, len(pts_to_validate)) :
    for j in range(0, len(pts)) :
        if float(pts_to_validate[i].split()[0]) == float(pts[j].split()[0]) and float(pts_to_validate[i].split()[1]) == float(pts[j].split()[1]):
            count = count + 1

print(count)