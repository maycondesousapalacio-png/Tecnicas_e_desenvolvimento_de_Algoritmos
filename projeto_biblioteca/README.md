# 📚 Sistema de Gerenciamento de Biblioteca



## 📖 Descrição
Um sistema completo desenvolvido em Python para gerenciamento de acervo bibliográfico, utilizando estruturas fundamentais da linguagem como listas, dicionários, estruturas condicionais e estruturas de repetição.

## 🎯 Objetivo do Projeto
Demonstrar na prática o uso de:

- Listas: Armazenamento e manipulação de coleções de livros
- Dicionários: Estruturação de dados complexos (livros e categorias)
- Estruturas Condicionais: Tomada de decisões e validações
- Estruturas de Repetição: Processamento de coleções e menus interativos

## 💡 Possíveis Aplicações
🏫 Uso Educacional
Escolas e Universidades: Para ensino de programação Python
Cursos de TI: Como exemplo de aplicação com estruturas de dados
Treinamentos: Prática de lógica de programação

## 📊 Uso Prático
Bibliotecas Pequenas: Gerenciamento de acervo básico
Coleções Pessoais: Controle de livros particulares
Sebo/Livrarias: Catálogo simples de produtos

## 🔧 Uso como Base
Protótipo: Para sistemas mais complexos
Template: Estrutura para outros CRUDs (Create, Read, Update, Delete)
Estudo: Base para implementação de novas funcionalidades

## 🚀 Funcionalidades
Funcionalidade	Descrição	Estruturas Utilizadas
📝 Adicionar Livros	Cadastro com validação de dados	Listas, Dicionários, Condicionais
📋 Listar Todos	Exibição completa do acervo	For, Listas, Enumerate
🔍 Buscar por Título	Busca parcial em títulos	For, Condicionais, Listas
🏷️ Filtrar por Categoria	Listagem por categorias	Dicionários, For, Condicionais
📊 Estatísticas	Métricas do acervo	Dicionários, For, Cálculos
🖥️ Exemplo de Execução
Menu Principal
text
==================================================
       SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
==================================================
1. Adicionar livro
2. Listar todos os livros
3. Buscar livro por título
4. Listar livros por categoria
5. Estatísticas da biblioteca
6. Sair
==================================================
📝 Exemplo: Adicionando um Livro
Entrada do usuário:

text
--- ADICIONAR NOVO LIVRO ---
Título do livro: Dom Casmurro
Autor: Machado de Assis

Categorias disponíveis:
1. Ficção
2. Não-Ficção
3. Técnico
4. Romance
5. Fantasia

Digite o número da categoria: 4
Ano de publicação: 1899
Saída do sistema:

text
✅ Livro 'Dom Casmurro' adicionado com sucesso!
📋 Exemplo: Listando Livros
Saída do sistema:

text
--- TODOS OS LIVROS ---
1. 'Dom Casmurro' - Machado de Assis (1899)
   Categoria: Romance | Status: ✅ Disponível

2. 'O Senhor dos Anéis' - J.R.R. Tolkien (1954)
   Categoria: Fantasia | Status: ✅ Disponível
🔍 Exemplo: Buscando Livro
Entrada do usuário:

text
--- BUSCAR LIVRO ---
Digite o título ou parte do título: casmurro
Saída do sistema:

text
📚 1 livro(s) encontrado(s):
1. 'Dom Casmurro' - Machado de Assis | ✅ Disponível
🏷️ Exemplo: Listando por Categoria
Entrada do usuário:

text
--- LIVROS POR CATEGORIA ---
1. Ficção
2. Não-Ficção
3. Técnico
4. Romance
5. Fantasia

Digite o número da categoria: 4
Saída do sistema:

text
📚 Livros na categoria 'Romance':
1. 'Dom Casmurro' - Machado de Assis (1899) | ✅ Disponível
📊 Exemplo: Estatísticas
Saída do sistema:

text
--- ESTATÍSTICAS DA BIBLIOTECA ---
📊 Total de livros: 5
✅ Livros disponíveis: 4
❌ Livros emprestados: 1

📚 Livros por categoria:
   Romance: 2 livro(s) (40.0%)
   Fantasia: 2 livro(s) (40.0%)
   Ficção: 1 livro(s) (20.0%)
🛠️ Estruturas de Dados Utilizadas
Lista Principal - biblioteca
python
biblioteca = [
    {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis", 
        "categoria": "Romance",
        "ano": 1899,
        "disponivel": True
    },
    # ... mais livros
]
Dicionário de Categorias
python
categorias = {
    "1": "Ficção",
    "2": "Não-Ficção", 
    "3": "Técnico",
    "4": "Romance",
    "5": "Fantasia"
}
📈 Possíveis Expansões
O sistema pode ser expandido com:

✅ Sistema de empréstimos com datas

✅ Persistência em arquivo (JSON, CSV)

✅ Interface gráfica (Tkinter, PyQt)

✅ Relatórios em PDF

✅ Sistema de usuários

✅ Busca avançada (autor, ano, múltiplos critérios)

🎓 Valor Educacional
Este projeto é ideal para:

Iniciantes em Python: Compreensão de sintaxe básica

Estudantes de Estruturas de Dados: Aplicação prática de listas e dicionários

Desenvolvedores Júnior: Padrões de validação e tratamento de entrada

Professores: Material didático para aulas práticas

📝 Como Executar
Salve o código em um arquivo .py

Execute com Python:

bash
python sistema_biblioteca.py