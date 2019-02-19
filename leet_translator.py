

user = str(input('Please enter phrase to be translated: '))
string_example = user

counter =0

while counter < len(string_example):
    # print(len(string_example))
    if  string_example[counter]=='a':
        string_example=string_example.replace("a", "4")
        print(string_example[counter],end='')
        counter=counter+1
        continue
    if  string_example[counter]=='A':
        string_example=string_example.replace("A", "4")
        print(string_example[counter],end='')
        counter=counter+1        
        continue
    if  string_example[counter]=='e':
        string_example=string_example.replace("e", "3")
        print(string_example[counter],end='')
        counter=counter+1  
        continue
    if  string_example[counter]=='E':
        string_example=string_example.replace("E", "3")
        print(string_example[counter],end='')
        counter=counter+1  
        continue
    if  string_example[counter]=='g':
        string_example=string_example.replace("g", "6")
        print(string_example[counter],end='')
        counter=counter+1
        continue
    if  string_example[counter]=='G':
        string_example=string_example.replace("G", "6")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='i':
        string_example=string_example.replace("i", "1")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='I':
        string_example=string_example.replace("I", "1")
        print(string_example[counter],end='')
        counter=counter+1
        continue
    if  string_example[counter]=='o':
        string_example=string_example.replace("o", "0")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='O':
        string_example=string_example.replace("O", "0")
        print(string_example[counter],end='')
        counter=counter+1
        continue
    if  string_example[counter]=='s':
        string_example=string_example.replace("s", "5")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='S':
        string_example=string_example.replace("S", "5")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='t':
        string_example=string_example.replace("t", "7")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    if  string_example[counter]=='T':
        string_example=string_example.replace("7", "7")
        print(string_example[counter],end='')
        counter=counter+1
        continue

    print(string_example[counter],end='')
    
    counter=counter+1
    
    if counter == len(string_example)+1:
        break
print()
