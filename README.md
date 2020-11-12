# Selected-Topics-in-Visual-Recognition-using-Deep-Learning-HW1
基於深度學習之視覺辨識專論HW1的code，詳細情形可參考[HW1](https://www.kaggle.com/c/cs-t0828-2020-hw1/overview)

## 環境
- Google colab

## 重現方法
跟著以下步驟可以重現同樣成果：
1. [Installation](#installation)
2. [Dataset Preparation](#Dataset Preparation)
3. [Train models](#Train models)

## Installation
將HW1.ipynb下載下來。

## Dataset Preparation
前往[Kaggle](https://www.kaggle.com/c/cs-t0828-2020-hw1/data)
csv => 將training_labels.csv下載下來
image => 將training_data和testing_data下載下來解壓縮
完成後擺放成以下結構:
```
HW1
  +- HW1.ipynb
  +- data
  |  +- training_data
  |  |  +- ...jpg
  |  +- testing_data
  |  |  +- ...jpg
  |  +- training_labels.csv
```

### Train models
1. 按照上面結構擺好後，上傳到google drive
2. 點擊HW1.ipynb，透過google colab開啟它
3. 點開左上角編輯 => 筆記本設定 => 選擇gpu => 儲存
4. 修改Parameters中的dir_path為你HW1.ipynb的路徑，如果不知道可執行上方的!pwd取得路徑
5. 點開上方執行階段 => 全部執行，就可以得到預測結果的result.csv
