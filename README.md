<h1 align="center"> Bharat Scene Text Dataset</h1>

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Bhashini-IITJ/BharatSceneTextDataset.svg?style=social&label=Star&maxAge=2592000)](https://github.com/Bhashini-IITJ/BharatSceneTextDataset/stargazers/)
![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/Bhashini-IITJ/BharatSceneTextDataset&title=Repo%20Views)

</div>


Bharat Scene Text Dataset (BSTD) is large scene-text dataset with coverage across **13 Indian languages** and English. It consists of 6,582 scene-text images, with polygon bounding box annotations of 1,20,560 words and ground truth text annotations of 1,00,495 cropped words. This dataset is an effort towards scaling scene-text detection and recognition systems to work on Indian languages. The current version of this dataset can be used for studying scene text detection and cropped scene text word recognition.

[comment]: <> (Add a table with 13 languages and links to its files)

# Release updates:

[comment]: <> (checkbox style release updates with cross ticks for the ones present)

- [8/8/24] First Public Release.

# Data Statistics:

### Scene Text Detection

| Total images | #Total detection annotations | #Train | #Test |
| :---: | :---: | :---: | :---: |
| 6,582 | 1,20,560 | 94,128 | 26,432 |

### Cropped Word Recogntion
| Language | #Total recognition annotations | #Train | #Test|
| :---: | :---: | :---: | :---: |
| Assamese | 3966 | 2623 | 1343 |
| Bengali | 6129 | 4968 | 1161 |
| English | 36891 | 28778 | 8113 |
| Gujarati | 2649 | 1956 | 693 |
| Hindi | 18889 | 14855 | 4034 |
| Kannada | 2934 | 2241 | 693 |
| Malayalam | 2975 | 2408 | 567 |
| Marathi | 4977 | 3932 | 1045 |
| Meitei | 494 | 381 | 113 |
| Odia | 4198 | 3176 | 1022 |
| Punjabi | 11104 | 8544 | 2560 |
| Tamil | 2548 | 2041 | 507 |
| Telugu | 2709 | 2227 | 482 |
| Urdu | 32 | 29 | 3 |
|Total| 100495 | 78159 | 22336 |


## Task 1: Scene text detection

### Data Download:
Download the detection.zip from the [link](https://drive.google.com/file/d/16irnMGdT8ohhvfMMG3qbBKWKxcPLNF0y/view?usp=share_link) (zip file ~17 GB).

Annotations are in BSTD_release_v1.json

### File structure

    Detection/
    │
    ├── A/
    │   ├── image_xx.jpg
    │   ├── ...
    │   └── image_xx.jpg
    ├── B/
    ├── C/
    ├── ...
    ├── M/
    └── BSTD_release_v1.json

### Annotation Format (BSTD_release_v1.json):
Words in the image are annotated in the polygon format. The annotation file is a json file with the following format:
```
"folderName_image_id": {
    "annotations": 
    {
        "polygon_0":
        {
            "coordinates":
                [
                    [x1, y1],
                    [x2, y2],
                    ...,
                    [xn, yn]
                ],
            "text": "text in the current polygon",
            "script_language" : "language of the word present in the polygon."
        },
        ...,
        "polygon_n":
        {
            "coordinates":
                [
                    [x1, y1],
                    [x2, y2],
                    ...,
                    [xn, yn]
                ],
            "text": "text in the current polygon",
            "script_language" : "language of the word present in the polygon."
        }
    },
    "url": "url of the image",
    "image_name": "path to the image",
    "split" : "train/test split"
    "folderName": "folder of the image"
}
```

## Task 2: Cropped word recognition

### Data Download:
Download the recognition.zip from the [link](https://drive.google.com/file/d/1wvlTbGnpnSRspM5MbjDgfSMH3BwM6qI0/view?usp=sharing) (zip file ~19GB).

### File structure

    Recognition/
    │
    ├── train/
    │   ├── assamese/
    │   │   ├── X_image_name_xx_xx.jpg
        │   ├── X_image_name_xx_xx.jpg
        │   ├── X_image_name_xx_xx.jpg
    │   ├── bengali/
    │   │   ├── ...
    │   ├── ...
    │   └── urdu/
    ├── test/
    │   ├── assamese/
    │   ├── bengali/
    │   ├── ...
    │   └── urdu/
    ├── train.csv
    └── test.csv

### Annotation Format (BSTD_release_v1.json):
Files: ```recognition/train.csv``` and  ```recognition/test.csv```

Each file contains rows (each row has comma seperated values as follows)
```
path_to_the_cropped_word_image, recogntion_annotation, script_language
```

## Data Visualisation of Detection Annotations:
To visualise detection annotations, run the following command:
```
python3 visualise.py <image_path> <path_to_BSTD_release_v1.json>
```
for e.g.
```
python3 visualise.py D/image_141.jpg path_to_BSTD_release_v1.json
```

Some examples are below:
<!-- Add an example image next to this line -->
![image info](visualised_images/image.jpg)
![image info](visualised_images/image2.jpg)


## Data Annotation
- All the images are collected from Wikimedia commons (under Creative Commons Licence, cc-by-sa-4.0)
- Further detection and recognition annotations are manually annotated.

## Acknowledgement
This work was partly supported by MeitY, Government of India (Project Number: S/MeitY/AM/20210114) under NLTM-Bhashini.

## Contact
For any queries, please contact us at:
- [Abhirama Subramanyam](mailto:penamakuri.1@iitj.ac.in)
- [Anik De](mailto:anikde@iitj.ac.in)

## Citation

```
@software{BharatSceneTextDataset,
  author = {Abhirama Subramanyam Penamakuri, Anik De, Anand Mishra},
  month = {8},
  title = {{BharatSceneTextDataset}},
  url = {https://github.com/Abhiram4572/BharatSceneTextDataset},
  version = {1.0},
  year = {2024}
}
```
