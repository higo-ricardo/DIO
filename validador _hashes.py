#def verificar_hashes(lista_hashes):
   

   # for pares in lista_hashes:
     
   #     hash_calculado, hash_esperado = pares.split(",")
    
   #     if hash_calculado == hash_esperado:
   #         print("Correto")
   #     else:
   #         print("Inválido")
        

hashes_usuario = [[abc123, abc123], [def456, def789]]
print(hashes_usuario)
print(type(hashes_usuario))
lista_hashes = hashes_usuario.split(",")
print(lista_hashes)
print(type(lista_hashes))
#verificar_hashes(lista_hashes)