# NBTaleBroadPhoneticClasses
Definition of broad phonetic classes for phone recognition on the NB Tale corpus. NOTE: the original Perl scripts by T. Svendsen are in `NTNUmods`.

## Example Usage:
```
from broad_classes import *
NBTaleSymbols
len(NBTaleSymbols)
simplifiedSymbols = list(set([broadClass(sym) for sym in NBTaleSymbols]))
len(simplifiedSymbols)
simplifiedSymbolsHTK = list(set([broadClass(sym, HTKsafe=True) for sym in NBTaleSymbols]))
len(simplifiedSymbolsHTK)
```

## Data preparation
the list of symbols in NBTale (NBTaleSymbols) was obtained from the transcriptions with the following command (in the NB Tale root directory)
```
cat Annotation/part_1.trans Annotation/part_2.trans | gawk '{print $3}' | sort -u | gawk '{printf("\x27%s\x27,\n", $1)}'
```
