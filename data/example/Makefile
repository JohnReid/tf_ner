download-glove:
	wget -P . "http://nlp.stanford.edu/data/glove.840B.300d.zip"
	unzip glove.840B.300d.zip -d glove.840B.300d.txt
	rm glove.840B.300d.zip

build:
	python ../../scripts/build-vocab
	python ../../scripts/build-glove
