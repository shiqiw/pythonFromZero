# Usage Guide

```sh
# Starts Program, select mode
$ python code_tracker.py
=> Select mode.
   P)ractice
   R)eal
   Default: Practice
   Input your choice or ENTER to default: 
```

```sh
# Select operation to perform
=> Select operation.
   A)dd
   D)elete
   E)xit
   F)ind   
   S)elect mode
   U)pdate
   Default: Add
   Input your choice or ENTER to default: 
```

```sh
# Create a new entry
=> Question ID:
xxx
=> Question title:
yyy
=> Question company:
zzz
=> Add more?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
=> Solutions:
www
=> Add more?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
Add a new entry xxx, total count vvv.
```

```sh
# Delete an exisiting entry
=> Question ID:
xxx
=> Delete?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
```

```sh
# Find entry or entry info
=> Search direction?
   A)ll
   C)ompany
   E)xit
   I)D
   K)ey word
   R)andom
   S)ummary
   T)ags
   Default: Random
   Input your choice or ENTER to default: 
```

```sh
# Update exisiting entry
=> Question ID:
xxx
# entry will be downloaded as file.
=> Update description?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
=> Update company?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
=> Update tags?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
=> Update similar?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
=> Update solutions?
   N)o
   Y)es
   Default: Yes
   Input your choice or ENTER to default: 
n
```

# Design Choice
- Single responsibility principle. 
    * UI/UX layer (IO, styling), Process layer (main logic, data format), Database (db management).
    * **Or**, main (top level script), operation (connect, disconnect, create, read, update, delete), user IO,  online scrape, text styling, and db management (pymongo).
- Open closed principle.
    * No extension or modification? Theoretically, we can define standard IO, extend to console IO, file IO and web content IO. IInput-able, IOutput-able?
- Listcov substitution principle.
- Interface segregation principle.
- Dependency inversion principle.
    * Depend on abstraction. Should implement interfaces.

# TODO: 
> https://docs.python.org/2/distutils/builtdist.html
1. Evolve it into a CLI app that has download package, download page and versioning. 
2. Scrape web content that needs user sign-in.
3. Ask for confirmation for soft/hard delete. Soft deletion is lazy, only removal date value is added. Entry will be hard delete after 30 days.
4. Use similarity analysis to suggest potential duplicate and/or relevant questions.
5. Rank popularity and recommend trend (using time stamp?).