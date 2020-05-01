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


# MyPy statistic.

GLOBAL SUMMARY: Total repo = 2678

"Bad" repo = 195: If encountered, it prevents mypy from checking the repo.  
115: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')   
43: No parent module -- cannot perform relative import    
37: Other errors resulting in empty output. Eg. ____ is not a valid python package name

"Good" repo = 2678 - (115 + 43 + 37) = 2483   
Below is a statistic from the "Good" repo. The number means # of repo with atleast 1 of that error type. 
```plain
  attr-defined 989
  var-annotated 899
  misc 789
  assignment 697
  name-defined 500
  arg-type 490
  return-value 339
  syntax 331
  union-attr 297
  valid-type 291
  no-redef 283
  operator 207
  index 196
  return 180
  call-arg 127
  str-format 125
  call-overload 101
  override 81
  has-type 76
  func-returns-value 40
  list-item 27
  str-bytes-safe 25
  dict-item 20
  type-var 15
  abstract 8
  type-arg 7
  exit-return 3
  valid-newtype 1

318: Success: no issues found in #NUMBER source files
```

(misc) - Number of repo with these errors. One repo can have more than 1 type   
115: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')   
43: No parent module -- cannot perform relative import   
75: Bracketed expression '[...]' is not valid as a type     
225: Relative import climbs too many namespaces   
12: Incompatible import of 'aaa' (imported name has type 'yyy', local name has type 'zzz'

