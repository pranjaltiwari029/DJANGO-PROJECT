from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def ans(request):
    text = request.GET.get('textarea')
    length=len(text)
    wordlist=text.split()
    noofwords=len(wordlist)
    symbols=list(''' !@#$%^&*()_?><:" ''')
    countuppercase=0
    countlowercase=0
    countnumber=0
    countsymbol=0

    for i in wordlist:
        if i.isupper():
            countuppercase+=1
        if i.islower():
            countlowercase+=1
        if i.isnumeric():
            countnumber+=1
        if i in symbols:
            countsymbol+=1  
    
    data={ 
        'length': length,
        'noofwords':noofwords,
        'upper':countuppercase,
        'lower':countlowercase,
        'numbers':countnumber,
        'symbols':countsymbol,
    }
     
    return render(request,'ans.html',data)

