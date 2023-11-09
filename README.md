# Project information
[SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash implementation
# Description
 SHA-1 is a hash function which takes an input [(message of any length < 2^64 bits)](https://datatracker.ietf.org/doc/html/rfc3174#page-2) and produces a 160-bit (20-byte) hash value known as a message digest
 
The sha1.py file contains this algorithm, consisting of several functions.
* `padding` - purpose of message padding is to make the total length of a padded message a multiple of 512 (64 for a string of bytes)
* `split_into_chunks` - split the message string into chunks of a certain length
* `left_rotate` - [left circular shifts](https://en.wikipedia.org/wiki/Circular_shift)
* `get_digest` - runs hashing algorithm and returns a 20-byte string
* `get_hex` - runs `get_digest` and converts received 20-byte string to hex

# Usage
Import function file
```python
import sha1
```
Call the function for the string using `encode()` and get a 20-byte string
```python
message = "The quick brown fox jumps over the lazy dog"
my_hash = sha1.get_digest(message.encode())
```
Call the function for the byte string and get a hex string
```python
message = b"The quick brown fox jumps over the lazy dog"
my_hash = sha1.get_hex(message)
```
# Comparison
Python has a hashlib library that implements various types of hashes, including SHA-1.
Test.py file contains several tests to compare the output of these functions for different strings. You can make sure that the results match.
However, the results of time measurements for hashing strings of the same length show that the hashlib function is significantly faster than my implementation. The reason for this is that the library function uses a very C implementation, which will always be faster than the pure Python I use