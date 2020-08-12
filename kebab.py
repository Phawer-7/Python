from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())

what_u_want = input('?:')
print(kebab(what_u_want))

#print(kebab('some-mixed_string With spaces_underscores-and-hyphens'))
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
# kebab('AllThe-small Things') # "all-the-small-things"

