def are_anagrams(s1, s2, s3):
    tmp1 = list(s1) #na początek ze stringu musimy zrobić obiekt typu iterowalnego, czyli listę; 
    tmp2 = list(s2)
    tmp3 = list(s3)

    if sorted(tmp1) == sorted(tmp2) == sorted(tmp3): #mając listę, sortujemy jej poszczególne elementy i porównujemy;
        return True
    else:
        return False


if __name__ == "__main__":
    print(are_anagrams("raz", "azr", "rza"))
    print(are_anagrams("dwa", "trzy", "raz"))