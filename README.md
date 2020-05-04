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
Below is a statistic from the "Good" repo. 

The first number is # of repo with atleast 1 of that error type.

The second number is the total # of error reported over all reepo.
```plain
  attr-defined 989 9732
  var-annotated 899 2761
  misc 789 5143
  assignment 697 3104
  name-defined 500 9319
  arg-type 490 1851
  return-value 339 1399
  syntax 331 515
  union-attr 297 1592
  valid-type 291 1564
  no-redef 283 810
  operator 207 674
  index 196 864
  return 180 292
  call-arg 127 528
  str-format 125 211
  call-overload 101 229
  override 81 201
  has-type 76 485
  func-returns-value 40 77
  list-item 27 72
  str-bytes-safe 25 31
  dict-item 20 50
  type-var 15 20
  abstract 8 10
  type-arg 7 69
  exit-return 3 3
  valid-newtype 1 1

318: Success: no issues found in #NUMBER source files
```

(misc) - Number of repo with these errors. One repo can have more than 1 type   
115: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')   
43: No parent module -- cannot perform relative import   
75: Bracketed expression '[...]' is not valid as a type     
225: Relative import climbs too many namespaces   
12: Incompatible import of 'aaa' (imported name has type 'yyy', local name has type 'zzz'

# misc

mypy 0.770

pytype 2020.04.01

pylint 2.4.4
astroid 2.3.3
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0]
