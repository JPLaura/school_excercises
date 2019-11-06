n=int(input("sisend: "))
squares = [k * k for k in range(0, n)]
print( "väljund: " + ", ".join( repr(e) for e in squares ) )