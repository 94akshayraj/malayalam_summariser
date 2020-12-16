import transformers


DEVICE = "cpu"
EPOCHS = 3
TRAIN_BATCH_SIZE = 64
VALID_BATCH_SIZE = 8
ACCUMULATION_STEPS = 4
MAX_LEN = 256


TRAINING_DATASET = "../input/train.json"
TEST_DATASET = "../input/test.json"
BERT_PATH = "../input/bert-base-multilingual-cased"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
