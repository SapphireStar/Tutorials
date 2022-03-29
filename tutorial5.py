import re
def question1(str):
    return re.search(r'a(b{4})',str)

print(question1("abb29ABCLK%lCnrDBCabbbb")[0])
#I use the b{4} regex expression in the bracket to match the "bbbb" pattern, 
# and in front of it add an "a" to match the "abbbb" pattern. So that it only allow the pattern that 
# "a followed by 4 bs"


def question2(str):
    print(re.search(r'[A-Z][a-z]+',str)[0])

question2("abb29ABCLK%lCnrDBCabbbb")
#question2: It can search the string pattern that "the first character should be a Upper case character
#and then, it should be followed by at least 1 lowercase or more. "

#Because I used search, so that it will search the whole string, until find the first substring match the pattern.