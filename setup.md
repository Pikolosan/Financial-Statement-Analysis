# Setup Project Environment

1. Install conda by this [link](https://www.anaconda.com/download/)
2. Once conda is installed, ensure the conda is set in your machine environment variable. For window, the default path with be `C:\Users\username\anaconda3\Scripts`
3. Test your conda
```bash
conda --version
```
4. Install VSCode
5. Install VSCode extension: `Jupyter`
6. Setup your environment with provided `requirement.txt` file
```bash
conda env create -n ENVNAME --file requirement.txt
```
7. Activate your virual environment
```bash
conda activate ENVNAME

## or deactivate
conda deactivate ENVNAME
```
8. Or you can set your virtual environment in vscode. Press `CTRL+SHIFT+P` and `Python:Select Interpreter`. Over there, select your created env.

## Conda Cheet Sheet
```bash
# list all env
conda env list

# create environment with Python version
conda create -n ENVNAME python=3.10

# create environment and install packages
# create environment with Python version
conda create -n ENVNAME python=3.10 pandas matplotlib xxx xxx

# rename environment
conda rename -n ENVNAME NEWENVNAME

# delete environment by name
conda remove -n ENVNAME --all

# list all installed packages for current env
conda list

# install package for current env
conda install pandas xxx xxx

# remove package for current env
conda uninstall pandas xxx xxx

# export packages
conda export ENVNAME > requirements.yml
# or
conda list --export > requirements.txt
# or
conda list --explicit>requirements.txt

# import env
conda env create -n ENVNAME --file requirements.yml
```
For more commands, please look at [official website](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)