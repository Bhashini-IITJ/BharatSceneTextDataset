import sys
import os
import json
from tqdm import tqdm

# read BSTD.json
with open(os.path.join(os.getcwd(), "BSTD.json")) as f:
    data = json.load(f)

# get all folderNames
folderNames = []
for key, value in data.items():
    folderName = value["folderName"]
    if folderName not in folderNames:
        folderNames.append(folderName)


# create a data folder
dataFolder = os.path.join(os.getcwd(), "detection")
if not os.path.exists(dataFolder):
    os.makedirs(dataFolder)

# create a folder for each language inside data folder
for folderName in folderNames:
    Folder = os.path.join(dataFolder, folderName)
    if not os.path.exists(Folder):
        os.makedirs(Folder)
    

def downloadImg(image_url, image_name, folderName):

    path_to_save = os.path.join(dataFolder, folderName, image_name)
    if os.path.exists(path_to_save):
        print(f'{path_to_save} already exists')
        return
    
    try:
        # download the image using wget 
        os.system(f'wget {image_url} -O {path_to_save}')
    except:
        print(f'Error in downloading {image_url}')

    return


allUrls = [value['url'] for key, value in data.items()]
allImageNames = [value['image_name'].split("/")[-1] for key, value in data.items()]
allFolderNames = [value['folderName'] for key, value in data.items()]

for i in tqdm(range(len(allUrls))):
    downloadImg(allUrls[i], allImageNames[i], allFolderNames[i])
