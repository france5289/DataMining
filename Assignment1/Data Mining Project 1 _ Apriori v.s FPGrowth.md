# Data Mining Project 1 : Apriori v.s FPGrowth
## 作業要求
1. 實作 Apriori algorithm 和 FP Growth algorithm 並使用 IBM Quest Synthetic Data Generator 與 Kaggel Dataset 產生 frequent itemset
2. 使用 WEKA 驗證結果是否正確
3. 比較兩個演算法之間的效能差異

## 開發環境
- 作業系統: `Mac OS Mojave`, `Ubuntu 18.04 LTS`
- 程式語言: `Python 3.7`

## 程式使用說明
本次 project包含以下檔案:  
- `KaggleReader.py`
    負責讀取 Kaggle 資料集，將讀取結果以 dictionary object 回傳
- `IBMReader.py`
    負責讀取 IBM Quest Synthetic Data，將讀取結果以 dictionary object 回傳
- `apriori.py`
    定義且實作 Apriori object，該物件負責執行 apriori 演算法，生成並儲存 frequent itemsets
- `Node.py`
    定義 FP-Tree 中每個節點擁有的屬性。
- `FPTree.py`
    定義 FP-Tree 的屬性以及實作 Tree Mining 所需的 method
- `FPGrowth.py`
    定義且實作 FPGrowth object，該物件負責執行 FP-Growth 演算法，生成並儲存 frequent itemsets
- `AssociationRuleMining.py`
    輸出兩個演算法在相同資料集下產生的 frequent itemsets，並剖析兩個演算法的執行時間

我們透過以下指令執行 `AssociationRuleMining.py` 產生 frequent itemsets  
```bash
python3 AssociationRuleMining.py [DATA] [MIN_SUP] [MIN_CONF] [--p] [--a]
```
其中參數意義如下 :  
- [DATA]
    指定要使用哪種資料集，有以下選項
    - IBM1 : 具有828筆交易的 IBM dataset
    - IBM2 : 具有5萬筆交易的 IBM dataset
    - IBM3 : 具有10萬筆交易的 IBM dataset
    - IBM4 : 具有50萬筆交易的 IBM dataset
    - Kaggle : 具有20筆交易的 Kaggle dataset
- [MIN_SUP]
    minimum support 值設定，需輸入浮點數
- [MIN_CONF]
    minimum confidence 值設定，需輸入浮點數
- [ --p ]
    此 flag 為 optional，可以決定是否要進行 program profiling
- [ --a ]
    此 flag 為 optional，可以決定是否產生 association rule
## Association rule comparison
使用自行下載的 Kaggle Dataset 進行驗證，此 dataset 總共有 20 筆交易：


| TID        | Transaction |
| :--------: | :--------: | 
| 1          | MILK,BREAD,BISCUIT     |
| 2          | BREAD,MILK,BISCUIT,CORNFLAKES|
| 3          | BREAD,TEA,BOURNVITA |
| 4          | JAM,MAGGI,BREAD,MILK |
| 5          | MAGGI,TEA,BISCUIT |
| 6          | BREAD,TEA,BOURNVITA |
| 7          | MAGGI,TEA,CORNFLAKES |
| 8          | MAGGI,BREAD,TEA,BISCUIT |
| 9          | JAM,MAGGI,BREAD,TEA |
| 10         | BREAD,MILK          |
| 11         | COFFEE,COCK,BISCUIT,CORNFLAKES |
| 12         | COFFEE,COCK,BISCUIT,CORNFLAKES |
| 13         | COFFEE,SUGER,BOURNVITA |
| 14         | BREAD,COFFEE,COCK |
| 15         | BREAD,SUGER,BISCUIT |
| 16         | COFFEE,SUGER,CORNFLAKES |
| 17         | BREAD,SUGER,BOURNVITA |
| 18         | BREAD,COFFEE,SUGER |
| 19         | BREAD,COFFEE,SUGER |
| 20         | TEA,MILK,COFFEE,CORNFLAKES |

接著將 minimum support 及 minimum confidence 分別設為 0.2 及 0.6
 - WEKA 產生的 association rule 
    - Apriori 
    ![](https://i.imgur.com/4hd7CPw.png)
    - FPGrowth
    ![](https://i.imgur.com/2Hjkkll.png)
- 我的程式產生的 association rule
    - Apriori
    ![](https://i.imgur.com/BaINvVH.png)
    - FPGrowth
    ![](https://i.imgur.com/XTamQUa.png)

## Performance Comparison
以下分別對不同筆數的 IBM dataset 執行 Apriori algorithm 以及 FPGrowth algorithm，並透過 `CProfile` module 進行 profiling ，比較兩者執行效率上的差異。


| Dataset         | Apriori    | FP- Growth |
| :--------:      | :--------: | :--------: |
| IBM1(828筆)     | 0.029 sec   | 0.029 sec|
| IBM2(5 萬筆)    |  82.763 sec | 79.387 sec|
| IBM3(10 萬筆)   | 167.582 sec | 139.888 sec| 
