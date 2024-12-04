from re import finditer


text="fatcatrunsveryfasttocaththecat"

pattern="at"

output=finditer(pattern,text)
for m in output:
    print(m.start(),m.group())


    