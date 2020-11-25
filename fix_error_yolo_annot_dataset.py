

import os

rep_im= r"/home/debian/BIG DATA/IA_AVANCEE/Projet/TRAIN/"
noms_im= os.listdir(rep_im)


for x in noms_im:
	if x[len(x)-4:]!='.txt':
		nm=x.split('.')[0]+'.txt'
		if nm not in noms_im:
			print(nm)
			os.remove(rep_im+x)


