# 電工實驗
## 10/28
##
- Hugging
- LLM 
- conda
  - 進入VSCODE or Anaconda Powershell Prompt (miniconda3)
  - 如果是VSCODE，則需按右下角的環境去進行切換
  - 接著往下執行
```
1.創造一個環境 -->  conda create -n ENV_NAME(環境名稱) -y python=3.8  
2. 切換環境  -->  conda activate ENV_NAME(環境名稱) 
3. 下載需要的套件  -->  pip install {transformers torch gradio}
4. pip list 查看下載套件
```
'''
### 快速開始
https://gradio.app/quickstart/
https://gradio.app/docs/#interface
### powershell無法使用時
https://israynotarray.com/other/20200510/1067127387/
### 使用Usage
```
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch

tokenizer=BertTokenizer.from_pretrained('IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment')
model=BertForSequenceClassification.from_pretrained('IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment')

text='今天心情不好'

output=model(torch.tensor([tokenizer.encode(text)]))
print(torch.nn.functional.softmax(output.logits,dim=-1))
```
