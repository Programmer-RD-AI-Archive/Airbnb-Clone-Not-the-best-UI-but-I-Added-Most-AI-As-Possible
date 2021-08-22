import pandas as pd
from tqdm import tqdm

classes = [
    "Toilet",
    "Swimming pool",
    "Bed",
    "Billiard table",
    "Sink",
    "Fountain",
    "Oven",
    "Ceiling fan",
    "Television",
    "Microwave oven",
    "Gas stove",
    "Refrigerator",
    "Kitchen & dining room table",
    "Washing machine",
    "Bathtub",
    "Stairs",
    "Fireplace",
    "Pillow",
    "Mirror",
    "Shower",
    "Couch",
    "Countertop",
    "Coffeemaker",
    "Dishwasher",
    "Sofa bed",
    "Tree house",
    "Towel",
    "Porch",
    "Wine rack",
    "Jacuzzi",
]
bounding_boxes_train = pd.read_csv("./data/bounding-boxes-train.csv")
# bounding_boxes_test = pd.read_csv("./bounding-boxes-test.csv")
# bounding_boxes_valid = pd.read_csv("./bounding-boxes-valid.csv")
download_data = pd.read_csv("./data/ids.csv")
class_names = pd.read_csv("./data/classnames.csv")
class_names.rename(columns={"/m/011k07": "Id", "Tortoise": "name"}, inplace=True)
ids = class_names["Id"]
names = class_names["name"]
name_and_label_names = {}
label_names = []
idx = -1

for _id, name in tqdm(zip(ids, names)):
    if name in classes:
        idx += 1
        name_and_label_names[name] = [_id, idx]
        label_names.append(_id)

img_ids = bounding_boxes_train["ImageID"]
label_names_labels_pd_df = bounding_boxes_train["LabelName"]
img_id_and_label_names = {}

for img_id, label_name_labels_pd_df in tqdm(zip(img_ids, label_names_labels_pd_df)):
    if label_name_labels_pd_df in label_names:
        img_id_and_label_names[label_name_labels_pd_df] = img_id
image_ids = bounding_boxes_train.to_dict()["ImageID"].values()
x_mins = bounding_boxes_train.to_dict()["XMin"].values()
y_mins = bounding_boxes_train.to_dict()["YMin"].values()
x_maxs = bounding_boxes_train.to_dict()["XMax"].values()
y_maxs = bounding_boxes_train.to_dict()["YMax"].values()
urls = []
for url in download_data.to_dict():
    pass
image_ids_and_urls_dict = {}
for image_id, x_min, x_max, y_min, y_max in zip(
    image_ids, x_mins, x_maxs, y_mins, y_maxs
):
    image_ids_and_urls_dict[image_id] = [x_min, x_max, y_min, y_max]


for image_id, url in tqdm(
    zip(
        list(download_data.to_dict()["ImageID"].values()),
        list(download_data.to_dict()["OriginalURL"].values()),
    )
):
    if image_id in list(image_ids_and_urls_dict.keys()):
        image_ids_and_urls_dict[image_id] = image_ids_and_urls_dict[image_id].append(
            url
        )
print(image_ids_and_urls_dict)
