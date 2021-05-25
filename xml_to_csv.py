import pandas as pd
import itertools
import os
from bs4 import BeautifulSoup as b
import glob

# \\ica-094\share\nilton\formatos

# all = glob.glob("\\\\ica-095\\tables\\manntis\\formatos\\*.xml")
all = glob.glob("\\\\ica-094\\share\\nilton\\formatos\\*.xml")
print("all is :",all)
for f in all:
    print(f)
#with open("f1.2-.xml", "r") as f: # opening xml file    
    with open(f, "r") as f: # opening xml file
        content = f.read()

    soup = b(content, "lxml")
    xmin =  [ values.text for values in soup.findAll("xmin")]
    ymin = [ values.text for values in soup.findAll("ymin")]
    xmax =  [ values.text for values in soup.findAll("xmax")]
    ymax =  [ values.text for values in soup.findAll("ymax")]
    label =  [ values.text for values in soup.findAll("name")]

    filename =  [ values.text for values in soup.findAll("filename")]
    filenames=[filename[0] for i in range(0, len(label))]
    # for i in range(0, len(name)):
    #     filenames.append(filename[0])


    path =  [ values.text for values in soup.findAll("path")]
    font = ["den" for i in range(0, len(label))]
    center_x = ["" for i in range(0, len(label))]
    center_y = center_x
    width =center_x
    height =center_x
    text = center_x
    
        

    #print(os.path.splitext(filename[0])[0])
    #fn=filename[0]
    #print(fn.split('.')[0])
    #print(len(name), len(filename))
    # For python-3.x use `zip_longest` method
    # For python-2.x use 'izip_longest method
    columns = ['center_x','center_y','width','height','xmin', 'ymin', 'xmax', 'ymax' ,'label','text','font','filename']
    data = [item for item in itertools.zip_longest(center_x,center_y,width,height,xmin, ymin, xmax, ymax ,label,text,font,filenames)] 
    df  = pd.DataFrame(data=data, columns=columns)
    # \\ica-094\share\nilton\formatos
    # print("save file on:",f'\\\\ica-09\\tables\\manntis\\formatos\\{os.path.splitext(filename[0])[0]}.csv')
    print("save file on:",f'\\\\ica-094\\share\\nilton\\formatos\\{os.path.splitext(filename[0])[0]}.csv')
    # df.to_csv(f'\\\\ica-095\\tables\\manntis\\formatos\\{os.path.splitext(filename[0])[0]}.csv',index=False, header=True)
    df.to_csv(f'\\\\ica-094\\share\\nilton\\formatos\\{os.path.splitext(filename[0])[0]}.csv',index=False, header=True)