## 📚 Description

Define a new `ShortUUID` type of identifier that behaves both like an UUID and a string, and is more compact that native UUID.

## 🎯 Pros

- Copying identifier is easier (removal of spacing and hyphens allow double click to select an id in logs)
- Resulting URL are more compacts those easier to read

```
http://localhost:8000/recipes/49DzG8iHwugcGbYYHOlF5i/items/49DzG8iHwugcGbYYHOlF5i
```

vs

```
http://localhost:8000/recipes/08c9abc3-7ca5-4130-a656-8cbed59d14de/items/08c9abc3-7ca5-4130-a656-8cbed59d14de
```

## 🚫 Cons

- Need of an additional piece of code to define `ShortUUID` type
- Probably a bit slower compared to usage of native UUID.
