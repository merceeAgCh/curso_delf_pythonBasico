from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def obtener_texto(ruta):
    """
    Args: Recibe la ruta del archivo que será leído para obtener el texto a dar
    a nuestro programa ára crear la nube de palabras.
    """
    texto = ""
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    return texto

def obtener_stopWords(ruta):
    stop_words = []
    with open(ruta, encoding="utf-8") as f:
        stop_words_temp = f.readlines()
        for stop_word in stop_words_temp:
            stop_words.append(stop_word.replace("\n", ""))
    return stop_words

""" def principal():
    texto = obtener_texto("noticia.txt")
    stop_words = obtener_stopWords("spanish.txt")
    STOPWORDS.update(stop_words)
    wordcloud = WordCloud(background_color ='white').generate(texto)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
principal() """

def obtener_tabla_frecuencias(texto, stop_words):
    lista = texto.split(" ")
    lista_limpia = []
    for palabra in lista:
        palabra = palabra.replace("!", "")
        palabra = palabra.replace("¡", "")
        palabra = palabra.replace("¿", "")
        palabra = palabra.replace("?", "")
        palabra = palabra.replace(".", "")
        palabra = palabra.replace(",", "")
        palabra = palabra.replace("(", "")
        palabra = palabra.replace(")", "")

        if "\n" in palabra:
            palabras_resultantes = palabra.split("\n")
            lista_limpia.append(palabras_resultantes[0])
            lista_limpia.append(palabras_resultantes[1])
        else:
            lista_limpia.append(palabra)
    freciencias = {}
    for palabra in lista_limpia:
        if palabra not in stop_words:
            if palabra in freciencias:
                freciencias[palabra] += 1
            else:
                freciencias[palabra] = 1
