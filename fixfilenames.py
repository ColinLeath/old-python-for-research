import os, shutil, string
DIR = 'x:\\noise1'
dirlist = os.listdir(DIR)
#print dirlist
for file in dirlist:
    if string.find(file,'16_sm')>0:
		#os.rename(DIR+'\\'+file,DIR + '\\'+string.replace(file,'dgtile_uv1','dgtile_uv1_',1))
		os.rename(DIR+'\\'+file,DIR + '\\' + 'dnoise_090-080t_090sp_045sl_sm_000' + file[-5:])
