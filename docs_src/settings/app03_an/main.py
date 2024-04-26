from functools import lru_cache
### Summary of Changes:
1. Import the `lru_cache` decorator to cache the results of the `get_settings` function.
2. Ensure that the correct import for `lru_cache` is included to resolve any import errors.
3. Check the usage of `Annotated` from `typing` to correctly annotate the `settings` parameter dependency.
4. Verify the logic in the `info` endpoint to ensure it retrieves and returns the settings accurately.