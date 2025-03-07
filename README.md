# LocalDataStoragePython-0.1
***
This Python package creates a file locally in the user's device more easily.

## Requirments for All OS (Operating System)
***
* Python should be Installed
*  PIP should also be Installed

## What is PIP?
***
Pip is a package manager for Python that allows you to install additional libraries and packages that are not part of the standard Python library, such as the ones found in the Python Package Index.

## How do I Install LocalDataStorePython 0.1?
***
Type this code in the terminal to install this package `pip install LocalDataStoragePython`.

## Examples
***
Here is an example of this Python package:
``` python
import LocalDataStorage

content = 'If laziness was an Olympic sport, I’d come in second just so I wouldn’t have to stand up for the gold medal.'  # just random text

storage_txt = LocalDataStorage.LocalDataStore(
    '.txt')  # initiate the LocalDataStore class and pass 'file_type' as the perimeter.
file = storage_txt.update_data('text file', content)  # creates and adds content to the file.

print(storage_txt.value)  # prints the content


```
Output:
```
If laziness was an Olympic sport, I’d come in second just so I wouldn’t have to stand up for the gold medal.
```
As shown in the above code, `py` is used as **filetype**, and `example` is used as **filename**.

## Documentation
***
there are four methods in this package:

1) **save_data:** It creates a new file but cannot upload the data inside that file and throws an error when the file already exists. There is a single attribute for this method `filename`.
   
2) **load_data:** It opens a pre-made file; if the file doesn't exist, it throws an error and returns the data written in that file if everything is fine. There is a single attribute for this method `filename`.

3) **update_data:** It creates a new file file and updates the text in that file and if the file doesn't exist, it throws an error. There are two attributes for this method: `filename` and `value`.
   
4) **delete_data:** It opens a pre-made file and deletes it and if the file doesn't exist, it throws an error. There is a single attribute for this method `filename`.

## More Examples
***
there is another example in front of you that shows the workings of the whole package:
``` python
import LocalDataStorage

storage_txt = LocalDataStorage.LocalDataStore(
    '.txt')  # initiate the LocalDataStore class and pass 'file_type' as perimeter.

value = input("Enter something:")
file = storage_txt.update_data('text file', value)  # creates and adds content to the file.

print("You Wrote:", storage_txt.load_data('text file'))  # fetch data from file and prints it

```
Output:

```
Enter something:hello world
You Wrote: hello world
```
As we can see the `update_data()` method can also be used to create a file if it doesn't exist and give values.

## Be a Member
***
you can become a member by reporting bugs or faults you find in this package, we will do our best to solve that bug and make this package comfortable for you.

## License
***
there is **MIT LICENCE** for this package
