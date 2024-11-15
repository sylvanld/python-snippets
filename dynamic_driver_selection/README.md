## Description

Demonstrates how to create arbitrary abstract types, and whose implementation might be loaded from defined entry points without direct dependencies.

## Pros

- Dynamically switch selected implementation of a type without modifying source code using it.
- No need to reference implementation dependencies in code using type => avoid unnecessary requirements.
- Implementations of a type may be provided by package defining the type, third-party packages, or directly in application using it (if it is packaged).

## Cons

- Implementations may only be provided through entry points, meaning that they must belong to a package.
