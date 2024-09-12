#!/bin/bash

archivo="EUBGT-Examen1-CriptoYSeguridadRedes.pdf" 
hash_esperado="44e020231a398a439c3939936be07ca742bbe132f7fdd8d092717db4d16a04c3" 

hash_generado=$(shasum -a 256 "$archivo" | awk '{print $1}')

if [ "$hash_generado" = "$hash_esperado" ]; then
    echo "El archivo es válido. Los hashes coinciden."
else
    echo "El archivo NO es válido. Los hashes NO coinciden."
fi
