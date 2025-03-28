import flet as ft
from interface.paginas import GerenciadorPaginas

def main(page: ft.Page):
    page.title = "FormuláriosDinâmicos"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.BLACK12
    page.padding = ft.padding.all(20)



    # O gerenciador de páginas recebe 
    # a página e a instância do bando de dados
    GerenciadorPaginas(page) 




ft.app(target=main)
