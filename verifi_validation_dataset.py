
import os

rep_im= r"/home/debian/BIG DATA/IA_AVANCEE/Projet/VALIDATION"
noms_im= os.listdir(rep_im)

cnt=0
for x in noms_im:
	if x[len(x)-4:]=='.png':
		cnt=cnt+1
	elif x[len(x)-4:]!='.xml':
		print(x)

print(len(noms_im)//2)
print(cnt)
