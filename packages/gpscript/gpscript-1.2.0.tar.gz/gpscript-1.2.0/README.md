### Install General purpose scripts ([Check This](https://github.com/ujjwalkar0/General-Purpose-Scripts)) using gpscript command

First of all install gpscript. Write following command(s)
```
pip install gpscript
```
or,
```
git clone https://github.com/ujjwalkar0/gpscript

cd gpscript

python setup.py install

```

If `gpscript` command not work, then open `python` interpreter, and write following command

```python
>>> import gpscript
>>> gpscript.gpscript.setup()
```

List of all script (Only those packages are in packages.json will shown here.)

```
gpscript list
```
Install a script
```
gpscript install <package_name>
```

List all installed packages...
```
gpscript installed
```
Remove a package...
```
gpscript remove <package_name>
```
Update a package...
```
gpscript update <package_name>
```
