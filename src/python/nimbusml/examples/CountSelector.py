###############################################################################
# OneHotHashVectorizer
from nimbusml import FileDataStream, Pipeline
from nimbusml.datasets import get_dataset
from nimbusml.feature_extraction.categorical import OneHotHashVectorizer
from nimbusml.feature_selection import CountSelector

# data input (as a FileDataStream)
path = get_dataset('infert').as_filepath()
data = FileDataStream.read_csv(path, sep=',')
print(data.head())
#   age  case education  induced  parity  ... row_num  spontaneous  ...
# 0   26     1    0-5yrs        1       6 ...       1            2  ...
# 1   42     1    0-5yrs        1       1 ...       2            0  ...
# 2   39     1    0-5yrs        2       6 ...       3            0  ...
# 3   34     1    0-5yrs        2       4 ...       4            0  ...
# 4   35     1   6-11yrs        1       3 ...       5            1  ...


pip = Pipeline([
    OneHotHashVectorizer(columns={'edu': 'education'}, hash_bits=2),
    CountSelector(count=5, columns=['edu'])
])
features_selection = pip.fit_transform(data)
print(features_selection.head())
#   age  case  edu.0  edu.1 education  induced  parity  pooled.stratum  ...
# 0   26     1    0.0    1.0    0-5yrs        1       6               3  ...
# 1   42     1    0.0    1.0    0-5yrs        1       1               1  ...
# 2   39     1    0.0    1.0    0-5yrs        2       6               4  ...
# 3   34     1    0.0    1.0    0-5yrs        2       4               2  ...
# 4   35     1    1.0    0.0   6-11yrs        1       3              32  ...