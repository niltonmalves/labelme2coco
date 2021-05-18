import glob
import os
import shutil

path = "\\\\139.82.152.10\\accounts\\niltonmonteiro\\ANP_Teses_Monografias_PRH\\folder_to_images_and_csv"
lista_json =glob.glob(path+"\\*.json")
lista_png = glob.glob(path+"\\*.png")

base =os.path.basename(lista_png[0])
filename = os.path.splitext(base)
print(filename[0])
print(len(lista_png))
new_path ="D:\\Arquivos_Nilton\\evaluator"
new_path2 =path + "\\test"
if not os.path.exists(new_path2):
    os.makedirs(new_path2)
for json in lista_json:
    basejson =os.path.basename(json)
    filenamejson = os.path.splitext(basejson)
    for png in lista_png:
       basepng = os.path.basename(png)
       filenamepng = os.path.splitext(basepng)
       if filenamejson[0] == filenamepng[0]:
           #move both
           shutil.copy(json, new_path2)
           shutil.copy(png, new_path2)
        