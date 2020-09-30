# Python scripts.

**[This]**
- Contain all scripts used.
- Some of them are in python3_types/type_tools/ which contains a more "offficial" scripts. Those in that folder may be a bit outdated.
- Many of scripts are messy with weird naming and such (because of my bad habit).

**[This is probably what you are looking for]**
- genFilteredFiles.py
  - Filtered out some files in the directory. Those files are ones with duplicate names + files with "from . import xxx".
  - This is the final version used in the paper
- mypy4Filtered.py = Runun Mypy on filtered repositories mentioned above.
  - Result is an output of Mypy. It is the final version we used in the paper.
  - For each repo, similar to running: mypy --show-error-codes --namespace-packages --ignore-missing-imports --show-column-numbers PATH/file1.py PATH/file2.py PATH/file3.py ...
- processOutput.py = Process Mypy's result from mypy4Filtered.py
- pylintFiltered.py = Run Pylint on filtered repositories mentioned above.
  - Result is an output of Pylint. It is the final version we used in the paper.
  - For each repo, similar to running: pylint -d I,R,C,W,F PATH/file1.py PATH/file2.py PATH/file3.py ...
- pylintProcessOutput_all.py = Process Pylint's result from pylintFiltered.py
- pytype.py = Run Pytype on filtered repositories mentioned above.
  - Result is an output of Mypy. It is the final version we used in the paper.
  - For each **flie in each repo**, similar to running: pytype --keep-going PATH/file1.py
- pytypeProcessOutput.py = Process Pytype's result from pytype.py



**[Others]**
- **counter_scripts** 
  - Partly from Prof. Milanova.
  - Calculate stats of # of annotation per file/repo
- **import_statistic**
  - by files = # of files that import these packages
  - by repo = # of repo that import these packages in atleast 1 file
- **ManyFlags** = (outdated) Mypy stat catagorized by error code.
- **Note&Stats**
- **typed-repos-divided** = List of all repos divided into 27 files of 100 repo each. The ones with suffix (A,B,C,X) are for debugging. eg. list in 3X is a subset of 3.
- allowRedef-mypy.py = Run mypy with --allow-redefinition flag.
- collectImport.py = Get import stats of all repo.
- **those python files with "delete" in the names** = For debugging stuff. I can't name.
- ManyFlags-mypy.py = One veersion of mypy script that use many flags.
- mypy1/2/3/4.py, mypyPretty.py, mypy_byType_processOutput.py = Many versions of mypy script. The most recent one is mypy4Filtered.py
- pyiAllrepo.py/pyiExample.py/stugben.py/stubgen_no_semantic.py = getting pyi stats.
- Repo_Stats = For each repo: # of selected files, # of all files, percentage, repo name
- TypeVar_counter.py = Count TypeVar

