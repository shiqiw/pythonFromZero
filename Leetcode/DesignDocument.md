# Design document

### User interface

Starts Program, select mode
```sh
$ python PlayWithMongo
$ Which mode would you like to choose: P)ractive, R)eal
$ >> Real
$ Okay, let's go to real mode.
```

Select operation to perform
```sh
$ Which operation would you like to perform: A)dd, F)ind, S)et, D)elete
$ >> A
$ Okay, please follow the prompt to add an entry/entries.
```

Create a new entry
```sh
# Practice mode
$ Please input ID:
$ >> 1
$ Please input title:
$ >> Bulls and Cows
$ Please input thoughts and solutions: (optional)
$ Thought 1 >> "Need more practice"
$ Solution 1 >> """ your solution goes here """
$ Time to take 1 >> 5 min
$ Thought 2 >>
$ Solution 2 >>
$ Time to take 2 >>

# Real mode
$ Please input company name(s):
$ >> PWM
$ Please input title:
$ >> ...
$ Please input description:
$ >> ...
$ Please choose type: B)ehavior, C)oding, D)esign, O)ther
$ >> 
$ Please input thoughts and solutions: (optional)
$ Thought 1 >> "Need more practice"
$ Solution 1 >> """ your solution goes here """
$ Time to take 1 >> 5 min
$ Thought 2 >>
$ Solution 2 >>
$ Time to take 2 >>

# If key (_id) is not duplicate
$ You have added entry No.xxx. Total count xxxx.

# If key is duplicated
$ Entry with duplicate key exist, do you want to create new entry or update enisting entry: A)dd, S)et
$ Exisitng content: (Collision entry content go here)
$ Your input: (new entry content go here)
```

Find entry or entry info
```sh
$ What info are your looking for? S)ummary, I)D, K)eyword, R)andom
# Summary
$ Total count xxx, total tag/ company yyy
# ID and random
$ Specific entry: ...
$ Do you want to see its relevants? Y)es, N)o
# Key word
$ Do you want to match C)ontent, T)ag
$ Do you want to match C)ompany, T)ype
```

Update entry will show previous content for each column, then ask for update.
Delete entry will display content, ask for confirmation for soft/hard delete. Soft deletion is lazy, only removal date value is added. Entry will be hard delete after 30 days.

### Functionality
- Tool to track, search and summarize questions. 
- Running locally, expect running time during operation to be negeligible.
- Only work for certain website for scraping part, can manual input.
- No one-time execution is needed for first-time execution.
- Size limitation and other failing cases are to-be-discovered.

### Building blocks
- Query for user option
- Query for user input
- Scrape web content

### Milestone
- Install MongoDB
- CRUD to MonDB entries
- Prompt user input
- Serialization and deserialization
- Secondary functionalities

> TODO: 
> Evolve it into a CLI app that has download package, download page and versioning.
> Scrape web content that needs user sign-in.
> Use n-gram to analyze similar questions, suggest potential duplicate and/or relevant.
> Rank popularity and recommend trend.