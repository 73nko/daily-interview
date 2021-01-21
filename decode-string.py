###
# 20-01-2021
# Hi, here's your problem today. This problem was recently asked by Google:
#
# Given a string with a certain rule: k[string] should be expanded to string k times.
# So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen,
# so 2[a2[b]c] should be expanded to abbcabbc.
###
def decode_string(s):
    res = ""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            res += s[i]
            i += 1
            continue

        if s[i].isdigit():
            # get the number
            num = 0
            while s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            # parse string in bracket
            bracket = 1
            i += 1
            innerstr = ""
            while bracket > 0:
                if s[i] == '[':
                    bracket += 1
                if s[i] == ']':
                    bracket -= 1
                innerstr += s[i]
                i += 1
            res = res + num * decode_string(innerstr[:-1])

    return res


print(decode_string('2[a2[b]c]'))