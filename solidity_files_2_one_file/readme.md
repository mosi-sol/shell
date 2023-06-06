This pyton script merging all solidity in one folder, to the 1 file "00-clean.sol" for when need 1 file for deploy.
- this script clear all comments
- sort by name of file
- delete all "import ..."

usecase: when implement so many files and want be in same file.\
attention: in some cases solidity can not compile large siza files.

### requeirment
python

- shell
```sh
#!/bin/bash
python3 all2one.py
```
- bat
```bat
@echo off
py all2one.py
```
