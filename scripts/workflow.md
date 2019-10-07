This document describes a workflow to process invoices with a BiLSTM-CRF.

- Change into data directory. For example: `cd tf_ner/data/tgmy-synthetic`
- Extract the words from the document using OCR: `doc-extract-training-text ../../../../data/tgmy-synthetic/`
- Take the resulting `train.{docs|tags|words}.txt` and split them into `train`, `testa` and `testb` data
  sets, for example: `split-data ../../../../data/tgmy-synthetic/text`
- Build the vocabulary from GloVe:
  - `build-vocab` : build the words, characters and tags vocabularies.
  - `build-glove` : build GloVe representations of the words.
- Fit the BiLSTM-CRF: `lstm-crf`
