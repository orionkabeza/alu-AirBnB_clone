# AirBnB Clone - The Console

## Description

This project is the first step towards building a full web application
clone of AirBnB. This first part implements a command interpreter to
manage the objects of the application (`User`, `State`, `City`,
`Amenity`, `Place`, `Review`) and a storage engine that saves those
objects to a JSON file so they persist between runs.

It puts in place:

- `BaseModel`, a parent class that handles the `id`, `created_at` and
  `updated_at` attributes, along with the serialization/deserialization
  logic (instance <-> dictionary <-> JSON string <-> file) shared by
  every other class.
- `FileStorage`, the storage engine that saves all objects to a single
  JSON file (`file.json`) and reloads them on startup.
- A command interpreter, `console.py`, built with Python's `cmd`
  module, used to create, show, update, list and destroy objects.

## How to start it

From the root of the repository, run:

```
$ ./console.py
```

or

```
$ python3 console.py
```

This opens an interactive prompt:

```
(hbnb)
```

The console also works in non-interactive mode, by piping commands
into it:

```
$ echo "help" | ./console.py
```

## How to use it

Type `help` to see the list of available commands, or `help <command>`
for details about one command. Type `quit`, or press `Ctrl+D` (EOF),
to exit.

| Command   | Usage                                              | Description                                    |
|-----------|-----------------------------------------------------|-------------------------------------------------|
| `create`  | `create <class name>`                              | Creates a new instance and prints its id       |
| `show`    | `show <class name> <id>`                           | Prints the string representation of an instance |
| `destroy` | `destroy <class name> <id>`                        | Deletes an instance                            |
| `all`     | `all [class name]`                                 | Prints all instances, optionally of one class  |
| `update`  | `update <class name> <id> <attribute> "<value>"`   | Adds or updates an attribute on an instance    |
| `quit`    | `quit`                                             | Exits the console                              |
| `EOF`     | `Ctrl+D`                                           | Exits the console                              |

Supported class names: `BaseModel`, `User`, `State`, `City`,
`Amenity`, `Place`, `Review`.

## Examples

```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
$
```

## Running the tests

```
$ python3 -m unittest discover tests
```
