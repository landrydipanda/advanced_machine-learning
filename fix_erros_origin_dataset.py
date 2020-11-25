
import os
import fnmatch
 
rep_im= r"/home/kotto/Downloads/TRAIN/IMAGES/"
noms_im= os.listdir(rep_im)
noms_im_t=[x.split('.')[0] for x in noms_im]


rep_anot=r"/home/kotto/Downloads/TRAIN/ANNOTATIONS/"
noms_anot=os.listdir(rep_anot)
noms_annot_t=[x.split('.')[0] for x in noms_anot]

print(len(noms_im))
print(len(noms_anot))

"""
for im in noms_im:
	x=im.split('.')[0]
	#print(x)
	if x not in noms_annot_t:
		try:
			os.remove(rep_im+im)
		except OSError as e:
			print(e)
		else:
			print("File is deleted successfully")
"""

"""
for anot in noms_anot:
	x=anot.split('.')[0]
	#print(x)
	if x not in noms_im_t:
		try:
			os.remove(rep_anot+anot)
		except OSError as e:
			print(e)
		else:
			print("File is deleted successfully")
"""
