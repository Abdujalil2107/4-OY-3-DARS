text = ['olma','nok','behi','limon','uzm']
txt = ''

for i in text:
    if len(i) > len(txt):
        txt = i
print(txt)
