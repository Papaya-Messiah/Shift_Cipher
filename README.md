# Shift Cipher
Program to transform texts using a shift/Caesar cipher in the Latin Alphabet (a-z).
- Has functionality to encrypt and decrypt files with a given key.
- Can forcibly decrypt files using this encryption scheme.

## Usage
1. clone this repository
2. navigate to this repository in terminal
3. run `python Shift_Cipher.py [OPTIONS]`
	- -e		encryption mode, followed by `<file_in> <key> <file_out>`
	- -d		decryption mode, followed by `<file_in> <key> <file_out>`
	- -c		cracking mode, followed by `<file_in> -t <threshold>`
4. profit

### Examples
- `python Shift_Cipher.py -e foo.txt 20 out.txt`
- `python Shift_Cipher.py -d foo.txt 7 out.txt`
- `python Shift_Cipher.py -c foo.txt -t .75`

### Notes
- Does not respect or maintain capitalization
- Will ignore non-alphabetic characters and leave them untouched
- Can take the same file as input and output, the file will be overwritten
- Key is expected to be an integer
- Threshold is expected to be a decimal between 0 and 1
