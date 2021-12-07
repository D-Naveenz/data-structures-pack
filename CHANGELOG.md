# Changelog


## v0.12

### Added or Changed
- Added DSA (base) Class
- Added feature to support generic type data structures
- Created Graph structure
- Created Stack(T) structure
- Restructured the package


## v0.18

### Added or Changed
- Various bugs fixed on Stack and Graph data structures
- Added `modal` and `store` properties to the base class
- Replaced `__dict__()` with `repr()` function in the base class
- Added the ability to initialize the stack using its constructor
- Optimized test cases

### Removed
- `Edge` Class. Now, can initialize data structures with basic data types.
- Unwanted dependencies


## v0.20

### Added or Changed
- Added `Queue` Data structure
- Renamed `DSAObj` base class to `DSObject`
- Created `DSGeneric` metaclass with referring `generic_class` decorator

### Removed
- `generic_class` decorator