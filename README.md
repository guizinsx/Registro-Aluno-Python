# Sistema de Registro de Alunos

Sistema desktop em **Python** com interface gráfica **Tkinter** para cadastro, atualização, exclusão e visualização de alunos, incluindo upload de fotos.

---

## Tecnologias

Este projeto utiliza as seguintes tecnologias:

- Python 3.x  
- Tkinter para interface gráfica  
- Pillow para manipulação de imagens  
- tkcalendar para seleção de datas  

---

## Funcionalidades

**Adicionar Aluno**  
Permite preencher campos obrigatórios: Nome, Email, Telefone, Sexo, Data de Nascimento, Endereço, Curso e Foto. Valida que todos os campos estejam preenchidos.

**Procurar Aluno**  
Busca por ID e preenche automaticamente os campos do formulário com os dados encontrados.

**Atualizar Aluno**  
Permite alterar todos os dados e a foto de um aluno já cadastrado.

**Deletar Aluno**  
Remove o aluno selecionado pelo ID.

**Tabela de Alunos**  
Exibe todos os alunos cadastrados em uma tabela, com barras de rolagem vertical e horizontal.

**Upload de Foto**  
Permite escolher imagens para cada aluno, redimensionando-as automaticamente para exibição.

---

## Estrutura do Projeto

A estrutura básica do projeto é a seguinte:
├── images/ # Ícones e logo
├── main.py # Lógica de dados (CRUD com SQLite)
├── tela.py # Interface Tkinter principal
├── README.md # Este arquivo
└── requirements.txt # Dependências opcionais


---

## Como Usar

1. Clone o repositório para sua máquina local.  
2. Instale as dependências necessárias: `tk`, `pillow` e `tkcalendar`.  
3. Execute a aplicação: abra o terminal ou prompt e rode `python app.py`.  
4. Use a interface para **Adicionar**, **Atualizar**, **Deletar** ou **Procurar** alunos.  
5. A tabela de alunos se atualiza automaticamente após cada operação.

---

## Observações

- O arquivo `main.py` gerencia a persistência dos dados.  
- Fotos devem ser arquivos válidos (`.png` ou `.jpg`).  
- A interface foi desenvolvida para resolução **810x535** e não é redimensionável.  

---

## Sobre o desenvolvimento

Este projeto foi criado como exercício de aprendizado em Python e Tkinter, baseado em referências de tutoriais e documentação oficial. Todo o código e adaptações foram feitos pelo desenvolvedor para consolidar o conhecimento.

---

## Contato

Desenvolvido por **Guilherme Orlandi**
Meu github: https://github.com/guizinsx


