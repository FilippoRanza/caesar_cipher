# caesar_cipher
[![Build Status](https://travis-ci.org/FilippoRanza/caesar_cipher.svg?branch=master)](https://travis-ci.org/FilippoRanza/caesar_cipher)
encrypt, decrypt and crack text file using Caesar Cipher

## Description
**caesar_cipher** encrypt *pure text* files usign [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). 
**caesar_cipher** is also able to recover the key of an encrypted message using [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis). By now only *Italian* and *English* are supported.

#### ATTENTION
input must be made only of white spaces, new lines and letters, both upper and lower case. 

## Installation
This software requires *Python3*
Change directory to **caesar_cipher** repository and
```
[sudo] python[3] setup.py install
```

root access is needed to preform an install.

## Usage

**caesar_cipher** has four commands. Only one can be used at a time. Each argument
has its specific options. 

```
caesar_cipher crypt | decrypt | crack | help [command_options...]
```

### crypt
```
caesar_cipher crypt [ [-i INPUT_FILE] [-o OUTPUT_FILE] [-k KEY]| -h]
```
Encrypt INPUT_FILE, using KEY as key, writing output to OUTPUT_FILE.
If OUTPUT_FILE is omitted, output is wrote to INPUT_FILE.out.
If INPUT_FILE is omitted, *stdin* is read and the output is **always** *stdout* (OUTPUT_FILE is ignored).
if KEY is omitted **caesar_cipher**  uses a key = 3.

### decrypt
```
caesar_cipher decrypt [ [-i INPUT_FILE] [-o OUTPUT_FILE] [-k KEY]| -h]
```
Decrypt INPUT_FILE, using KEY as key, writing output to OUTPUT_FILE.
If OUTPUT_FILE is omitted, output is wrote to INPUT_FILE.out.
If INPUT_FILE is omitted, *stdin* is read and the output is **always** *stdout* (OUTPUT_FILE is ignored).
if KEY is omitted **caesar_cipher**  uses a key = 3.

### crack
```
caesar_cipher crack [ [-i INPUT_FILE] [-o OUTPUT_FILE] [-l LANG] | -a | -h]
```

Recover the *key* used to encrypt INPUT_FILE, writing recovered message to OUTPUT_FILE. This command also write key and a *key ranking* to *stdout*. The
analysis is done using distribution for the given language LANG.

If OUTPUT_FILE is omitted, output is wrote to INPUT_FILE.out.
If INPUT_FILE is omitted, *stdin* is read and the output is **always** *stdout* (OUTPUT_FILE is ignored).

If LANG is omitted by default is used *English*.

If this command is run with *a* flag it will print all'available languages without trying to 
recover anything.

### help

```
caesar_cipher help
```

Display an help message and exit.













