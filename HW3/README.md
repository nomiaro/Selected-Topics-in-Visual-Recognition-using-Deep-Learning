# Selected-Topics-in-Visual-Recognition-using-Deep-Learning-HW1
基於深度學習之視覺辨識專論HW1的code，詳細情形可參考[HW3](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/blob/main/HW3/HW3.pdf)

# 環境
 - linux
 - CUDA 10.1
 - pytorch(torch==1.4.0 torchvision==0.5.0)

# 重現方法
跟著以下步驟可以重現同樣成果：
1. [環境下載](#環境下載)
2. [下載網路參數](#下載網路參數)
3. [準備資料](#準備資料)
4. [訓練model](#訓練model)
5. [提示](#提示)

# 環境下載
 - 下載指定版本的pytorch避免錯誤:
   ```Shell
   pip install torch==1.4.0 torchvision==0.5.0
   ```
 - 下載yolact並進入資料夾:
   ```Shell
   git clone https://github.com/dbolya/yolact.git
   cd yolact
   ```
 - 下載其他需要的package:
   ```Shell
   # Cython needs to be installed before pycocotools
   pip install cython
   pip install opencv-python pillow pycocotools matplotlib 
   ```
 - 建立yolact++所需環境:
   ```Shell
   cd external/DCNv2
   python setup.py build develop
   ```

# 下載網路參數
將config.py下載下來。

# 準備資料
前往[Kaggle](https://www.kaggle.com/c/cs-t0828-2020-hw1/data)
csv => 將training_labels.csv下載下來
image => 將training_data和testing_data下載下來解壓縮
完成後擺放成以下結構:
```
HW3
  +- HW1.ipynb
  +- data
  |  +- training_data
  |  |  +- ...jpg
  |  +- testing_data
  |  |  +- ...jpg
  |  +- training_labels.csv
```

### 訓練model
1. 按照上面結構擺好後，上傳到google drive
2. 點擊HW1.ipynb，透過google colab開啟它
3. 點開左上角編輯 => 筆記本設定 => 選擇gpu => 儲存
4. 修改Parameters中的dir_path為你HW1.ipynb的路徑
5. 點開上方執行階段 => 全部執行，就可以得到預測結果的result.csv

## 提示
1. 如果在執行train的時候，遇到Error:Input/output error，不要驚慌，過幾分鐘再執行就會正確了，這是還沒完全連接google drive造成的錯誤
2. 如果是連接google drive的第一次訓練，執行train的第一個epoch會特別久(大約1小時)，之後的epoch就會正常了(大約6分鐘)
