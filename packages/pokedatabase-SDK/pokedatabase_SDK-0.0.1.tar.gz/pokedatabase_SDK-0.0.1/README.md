# pokedatabase_sdk


Acquisition of data from Pokemon games through asynchronous requests to [PokeAPI](https://pokeapi.co/).

Library with three options:
- Request for pokemon names: shows all the pokemon names and store them in a list
- Request for pokemon games names: shows all the pokemon game names and store them in a list
- Check requests lists: checks if there is data in the two different lists

Can be used as follows:

```py
import pokeDatabaseSDK as pdb
```

Being able to access its functions in the following way:

```py
pdb.pokemonNames()
```

```py
pdb.gameNames()
```

```py
pdb.requestsList()
```