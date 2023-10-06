# 電工實驗
## 10/28
##
- Hugging
- LLM 
- conda
  - 進入VSCODE or Anaconda Powershell Prompt (miniconda3)
  - 如果是VSCODE，則需按右下角的環境去進行切換
  - 接著往下執行

## 設定環境變數

  1. C:\User\Continuum\Minionda3
  2. C:\User\Continuum\Minionda3\Scripts
  3. C:\User\Continuum\Minionda3\Library\bin
##

當遇到需要你使用`conda init <shell>`時，需要同時設定vscode裡面的默認設定，按終端機右上角(目前shell)旁邊的向下箭頭，然後按split terminal，然後選擇你能夠初始化的shell。
之後在vscode使用不想一直換的話，就要設定默認環境，也就是按住shift+ctrl+p，找到`Terminal: Select Default Profile`，然後設定默認環境，就能夠使用切換環境(conda activate)了。

```
1.創造一個環境 -->  conda create -n ENV_NAME(環境名稱) -y python=3.8  
2. 切換環境  -->  conda activate ENV_NAME(環境名稱) 
3. 下載需要的套件  -->  pip install {transformers torch gradio}
4. pip list 查看下載套件
5. 刪除虛擬環境 --> conda env remove --name myenv
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
