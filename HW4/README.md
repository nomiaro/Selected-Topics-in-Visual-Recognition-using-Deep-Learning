# Selected-Topics-in-Visual-Recognition-using-Deep-Learning-HW4
 - 基於深度學習之視覺辨識專論HW4的code，使用[CARN](https://github.com/nmhkahn/CARN-pytorch)實作
 - 任務要求可參考[HW4](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/blob/main/HW4/HW4_and_FinalProject.pdf)

# 環境
 - linux
 - CUDA 10.0

# 重現方法
跟著以下步驟可以重現同樣成果：
1. [準備資料](#準備資料)
2. [環境下載](#環境下載)
3. [下載修改的code](#下載修改的code)
4. [下載pretrained weights](#下載pretrained_weights)
5. [產生結果](#產生結果)

# 準備資料
1. 將[HW3.zip](https://drive.google.com/file/d/1D_B7Ns9Blh5wSahj-3BN07DryyuvjObJ/view?usp=sharing)下載下來並解壓縮<br>
2. 將HW3中的test_images.zip解壓縮

# 環境下載
 - 下載CARN:
   ```
   git clone https://github.com/nmhkahn/CARN-pytorch
   ```

# 下載修改的code
1. 將我的github的[carn](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/tree/main/HW4/carn)資料夾下載下來<br>
2. 取代CARN-pytorch/carn/

# 下載pretrained_weights
1. 將[weight.pth](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/blob/main/HW4/carn_1000.pth)下載下來<br>
2. 將下載的weight放在CARN-pytorch/checkpoint/中

# 產生結果
1. 按照上面完成後結構:
```
CARN-pytorch
  +- carn
  |  +- ...
  +- testing_lr_images
  |  +- ...png
  +- checkpoint
  |  +- weight.pth
  | ...
```
2. 進入CARN-pytorch資料夾執行以下指令，產生在 CARN-pytorch/sample/testing_lr_images/x3/SR 裡的圖片就是這次要的結果
```
python3 carn/sample.py --model carn --test_data_dir ./testing_lr_images --scale 3 --ckpt_path ./checkpoint/carn/carn_1000.pth --sample_dir sample
```
