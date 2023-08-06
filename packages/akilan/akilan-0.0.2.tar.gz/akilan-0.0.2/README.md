# AKILAN : ***Image Classification Engine***

Akilan is a Python library for quick image classification using [TensorFlow](https://www.tensorflow.org/). It is a wrapper around [TensorFlow's `tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) library. It is designed to be easy to use and easy to understand. The library is currently in development and is not yet ready for use. The library uses `numpy`, `pandas`, `matplotlib`and `seaborn` for data manipulation and visualization. The library is written in Python 3.6. It is tested on windows and linux.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the library.

```bash
pip install akilan
```

## Usage

```python
import ICE

# Convert directory into dataframe
df = ICE.dir_to_df(path)

# Create train and test dataframes
train_df, test_df = ICE.split_df(df, test_size=0.2)
```
