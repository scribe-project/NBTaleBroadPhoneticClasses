# NBTaleBroadPhoneticClasses
Definition of broad phonetic classes for phone recognition on the NB Tale corpus. NOTE: the original Perl scripts by T. Svendsen are in `NTNUmods`.

## Example Usage:
```
from broad_classes import *
NBTaleSymbols
len(NBTaleSymbols)
simplifiedSymbols = [broadClass(sym) for sym in NBTaleSymbols]
uniqueSimplifiedSymbols = list(set(simplifiedSymbols))
len(uniqueSimplifiedSymbols)
```

## Data preparation
the initial definition of the dictionary in `broad_classes.py` was obtained with the following command (in the NB Tale root directory)
```
cat Annotation/part_1.trans Annotation/part_2.trans | gawk '{print $3}' | sort -u | gawk '{printf("\x27%s\x27: \x27%s\x27,\n", $1, $1)}'
```

## Usage
copy the definition from `broad_classes.py` or import them into your code and then use, for example:
```
broadClasses['""eI']
```
