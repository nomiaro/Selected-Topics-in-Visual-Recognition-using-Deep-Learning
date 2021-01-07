# Selected-Topics-in-Visual-Recognition-using-Deep-Learning-HW3
 - 基於深度學習之視覺辨識專論HW3的code，使用[yolact](https://github.com/dbolya/yolact)實作
 - 任務要求可參考[HW3](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/blob/main/HW3/HW3.pdf)

# 環境
 - linux
 - CUDA 10.0

# 重現方法
跟著以下步驟可以重現同樣成果：
1. [準備資料](#準備資料)
2. [環境下載](#環境下載)
3. [下載網路參數](#下載網路參數)
4. [下載pretrained weights](#下載pretrained_weights)
5. [產生結果](#產生結果)

# 準備資料
1. 將[HW3.zip](https://drive.google.com/file/d/1D_B7Ns9Blh5wSahj-3BN07DryyuvjObJ/view?usp=sharing)下載下來並解壓縮<br>
2. 將HW3中的test_images.zip解壓縮

# 環境下載
 - 下載yolact:
   ```
   cd HW3
   git clone https://github.com/dbolya/yolact.git
   ```
 - 下載其他需要的package:
   ```
   # Cython needs to be installed before pycocotools
   pip install cython
   pip install opencv-python pillow pycocotools matplotlib 
   ```

# 下載網路參數
1. 將[config.py](https://drive.google.com/file/d/1cTDXjvRogcTQfkmgwVcsTLidsIV_0sTW/view?usp=sharing)下載下來<br>
2. 修改config.py中的路徑
```
# config.py:187
my_custom_test_dataset = dataset_base.copy({
    'name': 'my custom test dataset',

    'valid_images': 'path_to_test_images',
    'valid_info':   'path_to_test.json',

    'has_gt': False,
    'class_names': PASCAL_CLASSES
})
```
3. 取代yolact/data/ 中的 config.py

# 下載pretrained_weights
1. 將[weight.pth](https://drive.google.com/file/d/1x1BmaA_jgRfbUtoTRcP8CXHoYWk7kJ3_/view?usp=sharing)下載下來<br>
2. 在yolact/ 創建資料夾weights/，接著將下載的weight放入這個資料夾

# 修改模型錯誤
```
# yolact/eval.py:975
print('\rProcessing Images  %s %6d / %6d (%5.2f%%)    %5.2f fps        '
    % (repr(progress_bar), it+1, dataset_size, progress, fps), end='')
=>
'''
print('\rProcessing Images  %s %6d / %6d (%5.2f%%)    %5.2f fps        '
    % (repr(progress_bar), it+1, dataset_size, progress, fps), end='')
'''
```
```
# yolact/data/coco.py:172
if target.shape[0] == 0:
    print('Warning: Augmentation output an example with no ground truth. Resampling...')
    return self.pull_item(random.randint(0, len(self.ids)-1))
=>
'''
if target.shape[0] == 0:
    print('Warning: Augmentation output an example with no ground truth. Resampling...')
    return self.pull_item(random.randint(0, len(self.ids)-1))
'''
```
```
# yolact.py:490 
self.load_state_dict(state_dict)
=>
try:
    self.load_state_dict(state_dict)
except RuntimeError as e:
    print('Ignoring "' + str(e) + '"')
```

# 產生結果
1. 按照上面完成後結構:
```
HW3
  +- test.json
  +- test_images
  |  +- ...jpg
  +- yolact
  |  +- data
  |  |  +- config.py
  |  |  +- ...
  |  +- weights
  |  |  +- weight.pth
  |  +- ...
```
2. 進入yolact資料夾執行以下指令，產生在yolact/result/的mask_detections.json就是這次要的結果
```
python3 eval.py --trained_model=weights/weight.pth --config=my_custom_test_config --output_coco_json --dataset=my_custom_test_dataset
```
