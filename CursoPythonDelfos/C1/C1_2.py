# Conversion de tipo de datos (string)
## De entero a cadena de caracteres
print("--- De numero entero a cadena de carcteres ----")
varN = 3
print(varN, type(varN))

varSt = str(varN)
print(varSt, type(varSt))

## De cadena de caracteres a numero entero
print("--- De cadena de caracteres a numero entero ----")
varS = "19"
print("Variable string: ", varS, "\nEl tipo de dato de la variable: \n", type(varS))
varI = int(varS)
print("Variable Int: ", varI, "\nEl tipo de dato de la variable: \n", type(varI))

## De decimal a cadena de caracteres
print("--- De decimal a cadena de caracteres ----")
varF = 3.5
varCad = str(varF)
print("Las variables son: ", "Float", varF, type(varF),"Caracteres:\n", varCad, type(varCad))

## De cadena de caracteres a decimal
print("--- De cadena de caracteres a decimal ----")
varStr = "6.44"
varDec = float(varStr)
print("Las Variables son:\n","Cadena:",varStr, type(varStr), "\nCaracteres:",varDec, type(varDec))

## De numero entero a decimal
print(" --- De entero a decimal ---")
varEn = 8
varFlo = float(varEn)
print("Las variables son:\n","Entero:",varEn,type(varEn), "\n","Decimal:", varFlo, type(varFlo))

## De decimal a entero
print("--- De decimal a entero --- ")
varde=3.14
varint=int(varde)
print("Las variables son:\n","Decimal:",varde,type(varde),"\n","Entero:",varint,type(varint))

## Casos en los que no se puede hacer casteo
### palabra a numero entero
#palabrita = "Holis"
#enterito = int(palabrita)
#print(enterito)
### tampoco se puede de palabras a numero decimal
#word = "bye bye"
#dec = float(word)

# Operaciones matematicas basicas
## Valor absoluto
numero_neg = -1
valorAb = abs(numero_neg)
print("Value:",valorAb)
num_pos = 2
valAb = abs(num_pos)
print("Value:",valAb)

## Elevar a la potencia
bas = 3
pot = 2
resultado = pow(bas,pot)
print("Potencia",resultado)

## Redondear numeros
num_decimal = 5.22330096
numero_sin_dec = round(num_decimal, 2) #si no quiero decimales se quita el 2
print("Numero decimal", num_decimal,"\n Numero sin decimal",numero_sin_dec)

## Input
enter = input("Dime alguito: ")
print(enter)

