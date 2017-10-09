#!/home/chml/tools/Python-2.7.6

def cmpstr(str1, str2):
    col = 0
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            col += 1
            continue
        else :
            break

    if c1 != c2 or len(str1) != len(str2):
        return col+1
    else :
        return 0
    
file1 = open("a.txt",'r')
file2 = open("b.txt",'r')

fa = file1.readlines()
fb = file2.readlines()
file1.close()
file2.close()

#fa = [ str.decode("gbk") for str in fa]
#fb = [ str.decode("gbk") for str in fb]

row = 0
col = 0


for str1, str2 in zip(fa, fb):
    col = cmpstr(str1,str2)
# col=0 means two line same
    if col == 0 :
        row += 1
        continue
    else:
        break

#if one line not same or file length not same
if str1 != str2 or len(fa) != len(fb):
    print "row:", row+1, "col:", col
    print "file a is:\n", fa[row-1],fa[row], "\n"
#    print "file b is:\n", fb[row-1],fb[row][:col+1], "\n"
    print "file b is:\n", fb[row-1],fb[row], "\n"
else :
    print "All are same!"
    
raw_input("Press Enter to exit.")  
