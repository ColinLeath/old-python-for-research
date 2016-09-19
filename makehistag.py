import string

filebase='last960_ctab_cdiffr'

#filebases=['last960_ctab_cdiffr','last960_ctab_cdifbin3r','last960_ctab_cdifbin6r']
filebases=['difrag','bin3rag','bin6rag']

emptyline='xx,,,,,,,,,,,,'
emptylinedata = emptyline.split(',')

for filebase in filebases:
    fin = open(filebase + '.txt','r')
    fout = open(filebase + '.csv','w')
    if filebase == filebases[0]: rangelimit = 90
    elif filebase == filebases[1]: rangelimit=30
    elif filebase == filebases[2]: rangelimit=15
    #myrange = range(-90,91)
    myrange = range(-1*rangelimit,rangelimit+1)
    myrange = myrange + myrange
    
    myline = fin.readline()
    for diff in myrange:
        mylinedata = myline.split(',')
        if int(float(mylinedata[1])) <> diff:
            emptylinedata[1]=str(diff)
            emptylinedata[0]=mylinedata[0]
            emptyline = string.join(emptylinedata,',')
            fout.write(emptyline+'\n')
        else:
            fout.write(myline)
            myline = fin.readline()
            if myline == "": myline= "45,100"
            
#needs to fill in all values within range!!! -90-90, -30-30, -15-15
