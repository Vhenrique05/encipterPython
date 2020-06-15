def encriptBasic(data): # Numbers Basic
    return data.replace("0", "(zero)").replace("1", "(one)").replace("2", "(two)").replace("3", "(three)").replace("4", "(four)").replace("5", "(five)").replace("6", "(six)").replace("7", "(seven)").replace("8", "(eight)").replace("9", "(nine)").replace(" ", "_").replace("-", "_").replace("+", "_").replace(".", "(dot)").replace(",", "(colon)")

def decriptBasic(data):
    return data.replace("(zero)", "0").replace("(one)", "1").replace("(two)", "2").replace("(three)", "3").replace("(four)", "4").replace("(five)", "5").replace("(six)", "6").replace("(seven)", "7").replace("(eight)", "8").replace("(nine)", "9").replace("_", " ").replace("_", "-").replace("_", "+").replace("(dot)", ".").replace("(colon)", ",")



def encipter(data): # Advanced : Ramdom Symbols before Letter And words separeted by ()
    return data.lower().replace("a", "\26a").replace("b", "\29b").replace("c", "\18c").replace("d", "\14d").replace("e", "\56e").replace("f", "\8f").replace("g", "\7g").replace("h", "\11h").replace("i", "\14i").replace("j", "\18j").replace("k", "\81k").replace("l", "\83l").replace("m", "\19m").replace("n", "\63n").replace("o", "\45o").replace("p", "\35p").replace("q", "\52q").replace("r", "\82r").replace("s", "\28s").replace("t", "\43t").replace("u", "\23u").replace("v", "\29v").replace("w", "\80w").replace("x", "20x").replace("y", "\21y").replace("z", "\13z")

def decipter(data):
    return data.lower().replace("\26a", "a").replace("\29b", "b").replace("\18c", "c").replace("\14d", "d").replace("\56e", "e").replace("\8f", "f").replace("\7g", "g").replace("\11h", "h").replace("\14i", "i").replace("\18j", "j").replace("\81k", "k").replace("\83l", "l").replace("\19m", "m").replace("\63n", "n").replace("\45o", "o").replace("\35p", "p").replace("\52q", "q").replace("\82r", "r").replace("\28s", "s").replace("\43t", "t").replace("\23u", "u").replace("\29v", "v").replace("\80w", "w").replace("20x", "x").replace("\21y", "y").replace("\13z", "z")


def main():

    print("==================================================")
    print("=> 0.0.0.0")
    print("==> "+encriptBasic("0.0.0.0"))
    print("===> "+encipter(encriptBasic("0.0.0.0")))
    print("            =========================")
    print(">==> "+encipter(encriptBasic("0.0.0.0")))
    print(">=> "+decipter(encipter(encriptBasic("0.0.0.0"))))
    print(">> "+decriptBasic(decipter(encipter(encriptBasic("0.0.0.0")))))
    print("==================================================")


if __name__ == '__main__':
    main()




"""
    #==| To Encript/Decript : |==#

        * Use : *

        ``python
            encripted0 = encriptBasic(data) # for numbers First : 1a.34bc.12def.1d2 => (one)a(dot)bc(three)(four)(dot)(one)(two)def(dot)(one)d(two)
            encripted1 = encipter(encripted0) # for best encript : abc => (example) a!b#c$ ==> (%o3n.e)▬a(♀d%o#t)☻9b☺8c(#th\82r.e.e)(\8f%o‼u\82r)(♀d%o#t)(%o3n.e)(#t\80w%o)♀d.e\8f(♀d%o#t)(%o3n.e)♀d(#t\80w%o)
        ``

        or invert :

        ``python
        decripted0 = decipter("(%o3n.e)▬a(♀d%o#t)☻9b☺8c(#th\82r.e.e)(\8f%o‼u\82r)(♀d%o#t)(%o3n.e)(#t\80w%o)♀d.e\8f(♀d%o#t)(%o3n.e)♀d(#t\80w%o)")
        decripted1 = decriptBasic(decripted0) # (one)a(dot)bc(three)(four)(dot)(one)(two)def(dot)(one)d(two) => 1a.34bc.12def.1d2
        ``

        -- if all numbers decripted => (number) and (is not decimal) => (one)(two)
        -- if all numbers decripted => separeted by ()
        -- (\8f%o‼u\82r) = (four) [remove numbers and symbols] : remove '\8 %% !! \82' = 'f o u r' = 4


        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`@VHenrique05.-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`
        ´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`´-_-`

"""
