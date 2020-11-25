
import os

 
rep_train= r"/home/debian/BIG DATA/IA_AVANCEE/Projet/TRAIN/"
noms_train= os.listdir(rep_train)

rep_val= r"/home/debian/BIG DATA/IA_AVANCEE/Projet/VALIDATION/"
noms_val= os.listdir(rep_val)

#Drop xml annotations : 
for x in noms_train:
	if x[len(x)-4:]=='.xml':
		os.remove(rep_train+x)

for x in noms_val:
	if x[len(x)-4:]=='.xml':
		os.remove(rep_val+x)