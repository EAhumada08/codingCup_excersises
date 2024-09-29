coordenadas = input()

x1 = int(coordenadas.split()[0])
y1 = int(coordenadas.split()[1])
x2 = int(coordenadas.split()[2])
y2 = int(coordenadas.split()[3])

pts = []

if y1 == y2 :
    for i in range(x1,x2+1) :
        add = str(i) + " " + str(y1)
        pts.append(add)

print(pts)

number_pts_to_validate = int(input())
pts_to_validate = []

for i in range(0,number_pts_to_validate) :
    pts_input = input()
    pts_to_validate.append(pts_input)

print(pts_to_validate)

count = 0
for i in range(0, len(pts_to_validate)) :
    for j in range(0, len(pts)) :
        if pts_to_validate[i] == pts[j] :
            count = count + 1

print(count)