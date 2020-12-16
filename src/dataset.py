import config
import torch
import json
import pandas as pd

class BERTDataset:
    def __init__(self, headline, news):
        self.headline = headline
        self.news = news
        self.tokenizer = config.TOKENIZER
        self.max_len = config.MAX_LEN
    
    json.loads
    def __len__(self):
        return len(self.headline)
    
    def __getitem__(self, item):
        headline = str(self.headline[item])
        news = str(self.news[item])
        
        headline = " ".join(headline.split())
        news = " ".join(news.split())

        inputs = self.tokenizer.encode_plus(
            headline,
            news,
            add_special_tokens=True,
            max_length=self.max_len,
            pad_to_max_length=True
        )

        ids = inputs["input_ids"]
        mask = inputs["attention_mask"]
        token_type_ids = inputs["token_type_ids"]

        return {
            'ids': torch.tensor(ids, dtype=torch.long),
            'mask': torch.tensor(mask, dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
            # 'targets': torch.tensor(self.target[item], dtype=torch.float)
        }

if __name__ == '__main__':
    with open(r'E:\work\bert\malayalam_summariser\input\test.json', encoding='utf-8') as f:
        data = json.load(f)
        hh = []
        pp = []
        for i in data[:10]:
            hh.append(str(i['headline']))
            pp.append(str(i['para']))
        data = pd.DataFrame(list(zip(hh,pp)))
        data.columns =['Headline', 'Para']
    dset = BERTDataset(
        headline=data.Headline,
        news=data.Para
    )
    print(dset[0])