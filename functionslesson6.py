def say_hello(name):
    return "Hello {0}".format(name)

def  main():
    hello_str1 = say_hello(name="Li") # Return in Variable gepackt
    print(hello_str1)
    print(say_hello(name="David")) # Return direkt in der Printfunktion

if __name__ == "__main__": # Variablen, die mit __ beginnen, sind vordefinierte Variablen. Das hat nichts mit der name-variable oben zu tun!
    # Das hier prüft, ob in DIESER datei main ausgeführt wird und führt es deswegen aus, sonst zeigt es das wenn ich funktion in einer anderen datei aufrufe dort auch an (also printet
    # auch Hallo Li, Hallo David und dann erst Hallo (Name).
    main()

