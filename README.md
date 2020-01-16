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
  misc 1421
  var-annotated 476
  attr-defined 449
  assignment 366
  arg-type 257
  name-defined 254
  syntax 237
  return-value 180
  union-attr 152
  valid-type 150
  no-redef 119
  return 101
  index 100
  operator 100
  call-arg 58
  str-format 56
  call-overload 50
  override 43
  has-type 33
  func-returns-value 19
  list-item 17
  str-bytes-safe 11
  type-var 8
  dict-item 7
  type-arg 2
  exit-return 2
  abstract 2
  valid-newtype 1


(misc) - Number of repo with these errors. One repo can have more than 1 type
714: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')
440: No parent module -- cannot perform relative import
49: Bracketed expression '[...]' is not valid as a type
43: Relative import climbs too many namespaces
5: Incompatible import of 'aaa' (imported name has type 'yyy', local name has type 'zzz'
 
251: Success: no issues found in #NUMBER source files
```

# Notes
- Duplicate module named (714) means there are 2 or more files with the same name in the repo.