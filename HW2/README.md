# Selected-Topics-in-Visual-Recognition-using-Deep-Learning-HW2
基於深度學習之視覺辨識專論HW1的code，詳細情形可參考[HW2](https://github.com/nomiaro/Selected-Topics-in-Visual-Recognition-using-Deep-Learning/blob/main/HW2/HW2.pdf)

## 環境
- Google colab

## 重現方法
跟著以下步驟可以重現同樣成果：
1. [下載作業檔案](#下載作業檔案)
2. [準備資料](#準備資料)
3. [model測試](#model測試)

## 下載作業檔案
將HW2.ipynb下載下來。

## 準備資料
前往[google連結](https://drive.google.com/drive/folders/1P5rlaMDkdeJ8crg3TSnLs_IWgryoyv_N?usp=sharing)
將test.zip和checkpoint.pth下載下來，將test.zip解壓縮後擺成下面的結構
```
HW2
  +- HW2.ipynb
  +- checkpoint.pth
  +- test
  |  +- ...png
```

### model測試
1. 按照上面結構擺好後，上傳到google drive
2. 點擊HW2.ipynb，透過google colab開啟它
3. 點開左上角編輯 => 筆記本設定 => 選擇gpu => 儲存
4. 修改Parameters中的dir_path為你HW2.ipynb的路徑
5. 點開上方執行階段 => 全部執行，就可以得到預測結果的result.json
