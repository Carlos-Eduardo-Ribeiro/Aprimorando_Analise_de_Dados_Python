import tkinter as tk
import orm
from tkinter import messagebox


# Interface grafica
root = tk.Tk() # Criando um objeto do tipo TK
root.title("Gerenciador de Filmes")
icone = tk.PhotoImage(file="bd/claquete.png")
root.iconphoto(True, icone)

# CRIANDO ID

# Crinado label para o id
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)

# Criando campo para o id
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, pady=5)

# CRIANDO NOME

# Criando label nome
label_nome = tk.Label(root, text="NOME:")
label_nome.grid(row=1, column=0)

# Criando campo para nome
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row = 1, column=1, pady=5)

# CRIANDO ANO

# Criando label de ano
label_ano = tk.Label(root, text= "ANO")
label_ano.grid(row=2, column=0)

# Criando comapo de ano
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, pady=5) 

# CRIANDO NOTA

# Criando label para nota
label_nota = tk.Label(root, text="NOTA:")
label_nota.grid(row=3, column=0)

# Criando campo para nota
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, pady=5)


# CRIANDO FUNÇÕES COM TKINTER E ORM

# Inerindo filmes
def inserir_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()

    if all([nome.strip(), ano.strip(), nota.strip()]):
        orm.inserir_filme(nome, ano, nota)
        messagebox.showinfo("Sucesso", f"filme {nome} cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Informações invalidas e/ou inexistentes")

# Atualizando filmes
def atualizar_filme():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()

    if all([id.strip(), nome.strip(), ano.strip(), nota.strip()]):
        filme = orm.listar_filme(id)

        if filme:
            orm.atualizar_filme(id, nome, ano, nota)
            messagebox.showinfo("Sucesso", f"filme {nome} atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Id informado não existe!")
    else:
        messagebox.showerror("Erro", "Informações invalidas e/ou inexistentes")

# Deletando filme
def deletar_filme():
    id = entry_id.get()
    nome =  entry_nome.get()

    if id.strip():
        filme = orm.listar_filme(id)

        if filme:
            orm.excluir_filme(id)
            messagebox.showinfo("Sucesso", f"filme {filme.nome} deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Id informado não existe!")
    else:
        messagebox.showerror("Erro", "Informações invalidas e/ou inexistentes")

# CRIANDO BOTÕES

# Botão cadastro
botao_cadastrar =  tk.Button(root, text="Cadastrar", command=inserir_filme, width=10)
botao_cadastrar.grid(row=4, column=1, columnspan=2, pady=5)

# Criando botão de deletar
botao_deletar = tk.Button(root, text="Deletar", command=deletar_filme, width=10)
botao_deletar.grid(row=5, column=1, columnspan=2, pady=5)

botao_atualizar = tk.Button(root, text="Atualizar", command=atualizar_filme, width=10)
botao_atualizar.grid(row=6, column=1, columnspan=2, pady=5)

# Execultando aplaicação desktop
root.mainloop()