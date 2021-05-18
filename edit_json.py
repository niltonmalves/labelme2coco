import json

"""
INDEX_TO_CLASS = {0: 'text',
                  1: 'image',
                  2: 'table',
                  3: 'equation',
                  4: 'title',
                  5: 'list',
                  6: 'legenda'}

"categories": [
        {
            "supercategory": "equation",
            "id": 0,
            "name": "equation"
        },
        {
            "supercategory": "image",
            "id": 1,
            "name": "image"
        },
        {
            "supercategory": "legenda",
            "id": 2,
            "name": "legenda"
        },
        {
            "supercategory": "list",
            "id": 3,
            "name": "list"
        },
        {
            "supercategory": "table",
            "id": 4,
            "name": "table"
        },
        {
            "supercategory": "text",
            "id": 5,
            "name": "text"
        },
        {
            "supercategory": "title",
            "id": 6,
            "name": "title"
        }


"""

with open('trainval.json') as json_file:
    data = json.load(json_file)

x=[0,0,0,0,0,0,0]
#data['categories']
for p in data['categories']:
    if p['name']=='text':
        x[0]=p['id']
        p['id']= 0
    if p['name']=='image':
        x[1]=p['id']
        p['id']= 1
    if p['name']=='table':
        x[2]=p['id']
        p['id']= 2
    if p['name']=='equation':
        x[3]=p['id']
        p['id']= 3
    if p['name']=='title':
        x[4]=p['id']
        p['id']= 4
    if p['name']=='list':
        x[5]=p['id']
        p['id']= 5
    if p['name']=='legenda':
        x[6]=p['id']
        p['id']= 6   
print(x) 
# print(data['images'])
# #lista 
# data['categories']
# #[{'supercategory': 'aaaaaatext', 'id': 0, 'name': 'aaaaaatext'}, {'supercategory': 'aatitle', 'id': 1, 'name': 'aatitle'}]
# ['supercategory']
# data['categories'][0]['supercategory']='aqui'
# data['categories'][0]['name']='aqui'
# data['categories'][0]['id']='aqui'
# data['categories'][0]['supercategory']='aqui'
#em annotations alterar o somente "category_id"
#per corre todo anotations
for p in data['annotations']:
    # print(p['category_id'])
    if p['category_id'] == x[0]:
        p['category_id'] = 0
    elif p['category_id'] == x[1]:
        p['category_id'] = 1
    elif p['category_id'] == x[2]:
        p['category_id'] = 2
    elif p['category_id'] == x[3]:
        p['category_id'] = 3
    elif p['category_id'] == x[4]:
        p['category_id'] = 4
    elif p['category_id'] == x[5]:
        p['category_id'] = 5
    elif p['category_id'] == x[6]:
        p['category_id'] = 6

with open('trainval_edited_with_legend.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

for index, p in enumerate(data['categories']):

    if p['name']=='legenda':
        x[6]=p['id']
        #nao consegui deletar o item abaixo
        # da lista "categorias" 
        """
        {
            "supercategory": "legenda",
            "id": 6,
            "name": "legenda"
        },
        """
        #p.pop(index)
        # print(index)
        # del p[index]  

for p in data['annotations']:
    # print(p['category_id'])
    if p['category_id'] == x[6]:
        p['category_id'] = 0  # legenda para texto

with open('trainval_edited_without_legend.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
# data['annotations'][0]['category_id']
# {'segmentation': [[...]], 'iscrowd': 0, 'area': 0.0, 'image_id': 0, 'bbox': [324.0, 340.0, 559.0, 82.0], 'category_id': 1, 'id': 1}
