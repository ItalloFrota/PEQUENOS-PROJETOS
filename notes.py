import tkinter as tk # <= Importa a biblioteca tkinter para criar a interface gráfica

#=============== janela principal ================#
janela = tk.Tk() # <= Cria a janela principal
janela.title("Notas") # <= Define o título da janela
janela.state('zoomed') # <= Maximiza a janela para ocupar toda a tela

#=============== Função para salvar o conteúdo do Text em um arquivo ================#
def salvar(): # <= Função para salvar o conteúdo do Text em um arquivo
    conteudo = notes.get("1.0", "end") # <= Obtém o conteúdo do Text, do início (1.0) até o final (end)
    with open("notas.txt", "w", encoding="utf-8") as arquivo:# <= Abre o arquivo "notas.txt" para escrita (w) com codificação UTF-8
        arquivo.write(conteudo)# <= Escreve o conteúdo no arquivo

#=============== Configuração da interface gráfica ================#
superior = tk.Frame(janela, bg='blue', height=100) # <= Cria um Frame para o topo da janela, com fundo azul e altura de 100 pixels
superior.pack(fill=tk.X)# <= Adiciona o Frame ao topo da janela, preenchendo horizontalmente (fill=tk.X)
botao_salvar = tk.Button(superior, text='Salvar', font='Arial 20', command=salvar) # <= Cria um botão "Salvar" no Frame superior, com fonte Arial tamanho 20, que chama a função salvar() quando clicado
botao_salvar.pack(side=tk.RIGHT, padx=10, pady=10) # <= Adiciona o botão "Salvar" ao lado direito do Frame superior, com padding de 10 pixels nas laterais e 10 pixels nas partes superior e inferior
texto = tk.Label(superior, text='Minhas notas', font='Arial 30', bg='blue', fg='white') # <= Cria um rótulo "Minhas notas" no Frame superior, com fonte Arial tamanho 30, fundo azul e texto branco
texto.pack(side=tk.LEFT, padx=10, pady=10) # <= Adiciona o rótulo "Minhas notas" ao lado esquerdo do Frame superior, com padding de 10 pixels nas laterais e 10 pixels nas partes superior e inferior

#=============== Widget Text para digitar as notas ================#
notes = tk.Text(janela, font='Arial 20')#  <= Cria um widget Text para digitar as notas, com fonte Arial tamanho 20
notes.pack(fill=tk.BOTH,padx=10, pady=10, expand=True)# <= Cria um widget Text para digitar as notas, com fonte Arial tamanho 20, e o adiciona à janela, preenchendo todo o espaço disponível (fill=tk.BOTH) e permitindo que ele expanda (expand=True)

#=============== Tenta carregar o conteúdo do arquivo "notas.txt" para o Text ================#
try:  # <= Tenta abrir o arquivo "notas.txt" para leitura (r) com codificação UTF-8
    with open("notas.txt", "r", encoding="utf-8") as arquivo: # <= Se o arquivo for encontrado, lê o conteúdo e insere no Text
        conteudo = arquivo.read() # <= Lê o conteúdo do arquivo
        notes.insert("1.0", conteudo)# <= Insere o conteúdo no Text, começando na posição 1.0 (início do Text)  
except FileNotFoundError: # <= Se o arquivo "notas.txt" não for encontrado, passa sem fazer nada 
    pass

janela.mainloop()# <= Inicia o loop principal da interface gráfica, permitindo que a janela seja exibida e interativa