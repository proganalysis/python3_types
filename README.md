# Folders and files
**[Data]**

Result from running following tools. Divided into 27 files of 100 repo each.
```bash
mypy --show-error-codes --namespace-packages --ignore-missing-imports --show-column-numbers PATH/file1.py PATH/file2.py PATH/file3.py ...
pylint -d I,R,C,W,F PATH/file1.py PATH/file2.py PATH/file3.py ...
pytype --keep-going PATH/file1.py
```
mypy and pylint were run on all selected files each repo.
pytype was run on each individual file in each repo.

Selected files from each repo are from filtering out duplicate names + files with "from . import xxx".
Resulting in 2673 repo with 142982 files. 


**[Result]**
- **Compare** = Comparison of errors that appear on the same line across 3 tools.
- **Error Code** = Small examples of each error type from Mypy. They are from older running version.
- **Images** = Weekely summary
- **Included_files_each_repo** = List of selected files in each repo.
- **import_Statistic**
  - by files = # of files that import these packages
  - by repo = # of repo that import these packages in atleast 1 file
- **pyi comparison** = 25 examples of type inference from pytype. More detail in its README.
- **Error_examples_comparison.txt** = Comparison between 4 tools (3 + PyCharm) across 41 examples. 
- **Repo_Stats** = For each repo: # of selected files, # of all files, percentage, repo name
- **Result.txt** = Detailed info of 41 examples from all mypy's error types. It's from an older version which is before filtering out some files.


**[OlderVer]Data**

Old result. Probably not needed now.
 

**[type_tools]**
- **Dan_tools** = modified Dan's pyi tools.
- **typed-repos-divided** = List of all repos divided into 27 files of 100 repo each.
- **others.py** = Several tools

