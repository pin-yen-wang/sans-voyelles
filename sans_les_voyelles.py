def remove_vowels_it(s):
    list_voyelles = ["a", "i" , "e", "o", "u", "y"]
    if s == "" : # cas de base, la liste est vide
        return s 
    if s[0] in list_voyelles :
        return remove_vowels_it(s[1:])
    else : 
        return s[0] + remove_vowels_it(s[1:])

def main():
    pass
    s = "phacochere"
    print(remove_vowels_it(s))

if __name__ == "__main__":
    main()
