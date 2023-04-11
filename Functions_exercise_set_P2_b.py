W=input()
n=30
def word_count(W):
    word_list=W.split()[:n]
    output=" ".join(word_list)
    return(output)
print(word_count(W))
