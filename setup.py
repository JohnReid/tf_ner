from setuptools import setup

setup(name='tfner',
      version='0.1',
      description='TensorFlow Named Entity Recognition',
      url='https://github.com/JohnReid/tf_ner',
      author='Guillaume Genthial and John Reid',
      author_email='johnbaronreid@netscape.net',
      license='MIT',
      packages=['tfner'],
      scripts=['scripts/build-glove', 'scripts/build-vocab', 'scripts/lstm-crf', 'scripts/split-data'],
      zip_safe=False)
