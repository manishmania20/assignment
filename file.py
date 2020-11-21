#find all distinct characters in substrings and return length
def find_distinct_chars(string,n):
    k=set(string[0:n])
    k=str(k)
    length=len(k)
    return length

#smallest substring length and has to be less than original string length   
def small_substring_calculate(string):
    n=len(string)
    max_distinct_chars=find_distinct_chars(string,n)
    res=n
    for i in range(n):
        for j in range(n):
            substring=string[i:j]
            substring_length=len(substring)
            susbstring_distinct_chars=find_distinct_chars(substring,substring_length)
            
            if(substring_length<res and max_distinct_chars==susbstring_distinct_chars):
                res=substring_length
    return res

string = input()
ans=small_substring_calculate(string)
print(ans)