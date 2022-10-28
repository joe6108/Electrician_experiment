# 電工實驗
## 10/28
##
- Hugging
- LLM 
- conda
```
1.創造一個環境 -->  conda create -n ENV_NAME(環境名稱) -y python=3.8  
2. 切換環境  -->  conda activate ENV_NAME(環境名稱) 
3. 下載需要的套件  -->  pip install {transformers torch gradio}
```
'''
###　使用Usage
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
