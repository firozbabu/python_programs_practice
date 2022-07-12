n = input()
max = ''
for i in range(len(n)):
    t = n[i]


    if t[::-1]==t:
        if len(t) > len(max):
            max = t

    
    for j in range(i+1,len(n)):
        t+=n[j]
        if t[::-1] == t:
            if len(t) > len(max):
                max=t
print(max)


'''        
plyvmcthyommabcqtmqklpfkopccabybkneifgjdqhexoezlykccgpfidcqizmotounzpslphlpwghbubwthhpivqvwmvuirfhfnkjzpxyccwnuqodbdmsxybztgzvtonheaxcrpukdpgapfczulexugxghuzuvwqvgckpsgjqyzywlxtzmkqmzgavdmchnyaqzidzjfbizxgikjbsmhyikjvgveeifntxpmpgaoqbzwxyfsnexidvxdxxzzzykphrzprlzoyqqlbxbbgmyzplgqnzphbbdxitexvvjzhtpgkfpfazqiqeyczhkkooykaotkqwuuehbgfyznwjqutbltsamcmzyhzrdvvdrzhyzmcmastlbtuqjwnzyfgbheuuwqktoakyookkhzcyeqiqzafpfkgpthzjvvxetixdbbhpznqglpzymgbbxblqqyozlrpzrhpkyzzzxxdxvdixensfyxwzbqoagpmpxtnfieevgvjkiyhmsbjkigxzibfjzdizqaynhcmdvagzmqkmztxlwyzyqjgspkcgvqwvuzuhgxguxeluzcfpagpdkuprcxaehnotvzgtzbyxsmdbdoqunwccyxpzjknfhfriuvmwvqviphhtwbubhgwplhplspznuotomziqcdifpgcckylzeoxehqdjgfienkbybaccpokfplkqmtqcbammoyhtcmvylp

'''
