"""
Jaki będzie wynik poniższego kodu i dlaczego? """


X = "qwerty"

def func():
    print(X)

func()
# po wywołaniu funkcji func() zostanie wyświetlony napis "qwerty",
# ponieważ zmienna X jest globalna i dostępna dla całego kodu znajdującego
# się po jej definicji (więc też dla funkcji func())


X = "qwerty"

def func():
    X = "abc"

func()
print(X)
# zostanie wyświetlnone "qwerty", ponieważ chociaż funkcja modyfikuje
# wartość zmiennej X, to jest to tylko zmiana lokalnej kopii, 
# która po wyjściu z funkcji jest niszczona


X = "qwerty"

def func():
    global X
    X = "abc"

func()
print(X)
# wyświetlonh zostanie napis "abc"; funckcja deklaruje zmienną X
# w swoim ciele jako zmienną globalną i w ten sposób przesłania
# zmienną X zdefiniowaną wcześniej
