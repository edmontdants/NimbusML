###############################################################################
# ColumnConcatenator
from nimbusml import FileDataStream
from nimbusml.datasets import get_dataset
from nimbusml.preprocessing.schema import TypeConverter

# data input (as a FileDataStream)
path = get_dataset('infert').as_filepath()

data = FileDataStream.read_csv(path, sep=',')
print(data.head())
#    age  case education  induced  parity ... row_num  spontaneous  ...
# 0   26     1    0-5yrs        1       6 ...       1            2  ...
# 1   42     1    0-5yrs        1       1 ...       2            0  ...
# 2   39     1    0-5yrs        2       6 ...       3            0  ...
# 3   34     1    0-5yrs        2       4 ...       4            0  ...
# 4   35     1   6-11yrs        1       3 ...       5            1  ...

# transform usage
xf = TypeConverter(columns=['age'], result_type='R4')

# fit and transform
features = xf.fit_transform(data)

# print features
print(features.head())
#    age  case education  induced  parity  pooled.stratum  row_num  ...
# 0  26.0     1    0-5yrs        1       6               3        1  ...
# 1  42.0     1    0-5yrs        1       1               1        2  ...
# 2  39.0     1    0-5yrs        2       6               4        3  ...
# 3  34.0     1    0-5yrs        2       4               2        4  ...
# 4  35.0     1   6-11yrs        1       3              32        5  ...
