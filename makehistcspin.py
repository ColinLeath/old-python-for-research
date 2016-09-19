import string


#filebases=['last960_ctab_cdiffr','last960_ctab_cdifbin3r','last960_ctab_cdifbin6r']
filebases=['last960_ctab_cdifspinr','last960_ctab_cdifspin3r','last960_ctab_cdifspin6r']
#filebases=['difrag','bin3rag','bin6rag']

emptyline='name,xx,,,,,,,,,,,,'
emptylinedata = emptyline.split(',')

for filebase in filebases:
    fin = open(filebase + '.txt','r')
    fout = open(filebase + '.csv','w')
    if filebase == filebases[0]: rangelimit = [-45,135] 
    elif filebase == filebases[1]: rangelimit= [-15,45]
    elif filebase == filebases[2]: rangelimit= [-8,22]
    #myrange = range(-90,91)
    myrange = range(rangelimit[0],rangelimit[1]+1)
    myrange = myrange + myrange
    myline = fin.readline()
    for diff in myrange:
        mylinedata = myline.split(',')
        if int(float(mylinedata[2])) <> diff:
            emptylinedata[2]=str(diff)
            emptylinedata[0]=mylinedata[0]
            emptyline = string.join(emptylinedata,',')
            fout.write(emptyline+'\n')
        else:
            fout.write(myline)
            myline = fin.readline()
            if myline == "": 
                myline= "name,45,200"

            
#needs to fill in all values within range!!! -90-90, -30-30, -15-15
