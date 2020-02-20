# Mypy config
Currently, every file in the repo is passed to Mypy to check together, along with 3 flags.
```
mypy --show-error-codes --namespace-packages --ignore-missing-imports PATH/file1.py PATH/file2.py PATH/file3.py ...
```

--namespace-packages = "this allows discovery of imported packages that don’t have an __init__.py file"

--show-error-codes = Add an error code which we use to categorize error types.

--ignore-missing-imports = Ignore all missing imports.

# Stats
```
GLOBAL SUMMARY: Total repo = 2678
- subtract:
  714: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')
  440: No parent module -- cannot perform relative import

Remaining repo = 1524 repo. 
  Following is the number of repo that have at least 1 type of a given error, and the number of total errors.
  misc 267 (= 1421 - 714 - 440)

                    #repo   #total errors
  var-annotated       476    1467
  attr-defined        449    2509
  assignment          366    1459
  arg-type            257     843
  name-defined        254    3785
  syntax              237     332
  return-value        180     543
  union-attr          152    1007
  valid-type          150     805
  no-redef            119     312
  return              101     156
  index               100     420
  operator            100     311
  call-arg             58     202
  str-format           56      86
  call-overload        50     114
  override             43      88
  has-type             33     222
  func-returns-value   19      28
  list-item            17      33
  str-bytes-safe       11      16
  type-var              8      12
  dict-item             7      25
  type-arg              2      10
  exit-return           2       2
  abstract              2       2
  valid-newtype         1       1
                            14790

  Success             251 out of 1524 (16.47%)



(misc 1421) - Number of repo with these errors. One repo can have more than 1 type
714: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')
440: No parent module -- cannot perform relative import
49: Bracketed expression '[...]' is not valid as a type
43: Relative import climbs too many namespaces
5: Incompatible import of 'aaa' (imported name has type 'yyy', local name has type 'zzz'
 
251: Success: no issues found in #NUMBER source files
```

# Notes
- Duplicate module named (714) means there are 2 or more files with the same name in the repo.