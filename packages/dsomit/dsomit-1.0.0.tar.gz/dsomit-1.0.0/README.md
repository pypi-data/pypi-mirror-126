# Description

A simple package that removes all *.DS_Store* files from a list.

# Usage

```python
import dsomit as ds

old_files_list = ["getJob.java", ".DS_Store", "root.xml"]
new_files_list = ds.omit(old_files_list) # Removes the .DS_Store 

print(old_files_list)
print(new_files_list)
```


