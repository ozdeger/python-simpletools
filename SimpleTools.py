

def SaveToTxt(list_vars,path='',name='save_data'):
    print(name)
    txt_path = path + '/' + name + '.txt'
    text = open(txt_path, 'w+')
    for var in list_vars:

        text.write("%s\n" % str(var))

def LoadFromTxt(path,index,name='save_data'):
    txt_path=path+'/'+name+'.txt'
    text=open(txt_path,'r')
    lines=text.readlines()
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]

    if isinstance(lines[index],str) is True:
        return lines[index]
    return eval(lines[index])