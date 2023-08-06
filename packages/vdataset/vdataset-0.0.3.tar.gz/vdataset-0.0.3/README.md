# VDataset

## Description

Load video datasets to PyTorch DataLoader. (Custom Video Data set for PyTorch DataLoader)
</br>
**VDataset can be use to load 20BN-Jester dataset to the PyTorch DataLoader**

## Required Libraries

* torch
* Pillow
* pandas

## Arguments for constructor

| Argument | Type | Required | Description|
|----------|------|----------|------------|
| csv_file  | str  | True     | Path to .csv file|
| root_dir | str  | True     | Root Directory of the video dataset|
| file_format| str | False    | File type of the frame images (ex: .jpg, .jpeg, .png)|
| id_col_name | str | False   | Column name, where id/name of the video on the .csv file|
| label_col_name | str | False | Column name, where label is on the .csv file |
| frames_limit_mode | str/None | False | Mode of the frame count detection ("manual", "csv" or else it auto detects all the frames available) |
| frames_limit | int | False | Number of frames in a video (required if frames_count_mode set to "manual") |
| frames_limit_col_name | str | False |Column name, where label is on the .csv file (required if frames_count_mode set to "csv") |
| video_transforms | tuple/None | False |        Video Transforms (Refere: <https://github.com/hassony2/torch_videovision>) |

## Usage

```python
from vdataset import VDataset 

from torch.utils.data import DataLoader

from torchvideotransforms.volume_transforms import ClipToTensor # https://github.com/hassony2/torch_videovision
from torchvideotransforms import video_transforms, volume_transforms # https://github.com/hassony2/torch_videovision

video_transform_list = [video_transforms.RandomRotation(30),
            video_transforms.Resize((100, 100)),
            volume_transforms.ClipToTensor()]
video_transforms = video_transforms.Compose(video_transform_list)

dataset = VDataset(csv_file='/path-to-csv/csv_file.csv', root_dir='/path-to-root/', video_transforms=video_transforms)

dataloader = DataLoader(dataset, batch_size=64, shuffle=True, num_workers=2, pin_memory=True)
print(dataloader)

for image, label in dataloader: # Do what do you want in dataset
    print(image, label)
    break

```
