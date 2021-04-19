<p align='center'>
  <img width="50%" src="https://user-images.githubusercontent.com/39718972/115223293-98e72580-a146-11eb-8151-13e95127a42c.jpg"/>
</p>


# Human Pose Estimation Project
**Extracting 2D Joint positions and angles for pose estimation with PyTorch.**

## Installation
#### Prerequisites
* Install [PyTorch](https://pytorch.org/get-started/locally/) `>= 1.2` with [torchvision](https://pytorch.org/get-started/locally/) `>= 0.4`
#### Option 1: Install using pip
```
pip install git+https://github.com/prasunroy/rcnnpose-pytorch.git
```
#### Option 2: Install from source
```
git clone https://github.com/hci-mkim/rcnnpose-pytorch.git
cd pose_project
python setup.py install
```

## Running examples
### Option 1: only for pose
#### locate video in folder [1]vid2img
* images will be sliced and saved in folder [2]inputs
```
cd examples_onlypose
!python vid2img.py
```

#### [2]inputs -> [3]output_keypoints
```
!python custom_image_demo.py
```

### Option 2: background subtraction(yolact++) and then pose
#### [1]vid2img -> [2]inputs
* locate your video([1]vid2img) and then images will be sliced and saved in folder [2]inputs
```
cd examples
!python vid2img.py
```

#### [2]inputs -> [3]outputs_background_removed
```
!cd yolact
# run yolact
!python eval.py --trained_model=weights/yolact_resnet50_54_800000.pth --score_threshold=0.15 --top_k=1 --images="../[2]inputs":"../[3]outputs_background_removed"
!cd ..
```

#### [3]outputs_background_removed -> [4]outputs_keypoint
```
!python custom_image_demo.py
```

### Angle.csv results
<p align='center'>
  <img width="80%" src="https://user-images.githubusercontent.com/39718972/115226702-8373fa80-a14a-11eb-9539-e2ea55dccc48.jpg"/>
</p>

### joint coordinates.csv results
<p align='center'>
  <img width="100%" src="https://user-images.githubusercontent.com/39718972/115226848-aa323100-a14a-11eb-8505-a033d0659ff4.jpg"/>
</p>


