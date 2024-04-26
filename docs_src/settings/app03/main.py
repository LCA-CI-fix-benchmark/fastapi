from functools import lru_cache
### Summary of Changes:
1. Import the `lru_cache` decorator to cache the results of the `get_settings` function.
2. Ensure that the correct import for `lru_cache` is included to resolve any import errors.
3. Check the usage of `Depends` in the `info` endpoint to correctly inject the settings dependency.
4. Verify the structure and logic of the `info` endpoint to ensure it retrieves and returns the settings accurately.