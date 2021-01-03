import sys
script, encoding, error = sys.argv #is it a typical names or args or we are stating our own here

def main(language_file, encoding, errors): #this is a start of the function called main
    line = language_file.readline() #readline is the name of function, method?

    if line: # what does it mean 'if line' here?
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() #what is strip?
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<====>", cooked_string) # why we need this <====>. ok, i got it

languages = open("languages.txt", encoding="utf-8") #why this encoding? do we need to know the names of other encoding?

main(languages, encoding, error)
