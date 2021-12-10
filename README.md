# NBTaleBroadPhoneticClasses
Definition of broad phonetic classes for phone recognition on the NB Tale corpus

## Data preparation
the initial definition of the dictionary in `broad_classes.py` was obtained with the following command (in the NB Tale root directory)
```
cat Annotation/part_1.trans Annotation/part_2.trans | gawk '{print $3}' | sort -u | gawk '{printf("\x27%s\x27: \x27%s\x27,\n", $1, $1)}'
```

## Usage
copy the definition from `broad_classes.py` or import them into your code and then use, for example:
```python
broadClasses['""eI']
```
## pip installation 
You can now access the convert.py functionality from other directories via pip installing this package locally. From the command line navigate to this directory and run 
```
pip install .
```

It can then be used like so 
```python
from broad_classes_converter.convert import convert

print(convert('}i'))
```



