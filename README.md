# NBTaleBroadPhoneticClasses
Definition of broad phonetic classes for phone recognition on the NB Tale corpus

## Data preparation
the list of phonetic symbols was obtained with the following command (in the NB Tale rood directory)
```
cat Annotation/part_1.trans Annotation/part_2.trans | gawk '{print $3}' | sort -u
```
