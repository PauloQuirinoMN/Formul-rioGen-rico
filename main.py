import flet as ft
from interface.paginas import GerenciadorPaginas

def main(page: ft.Page):
    page.title = "FormuláriosDinâmicos"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.BLACK12
    page.padding = ft.padding.all(20)
    GerenciadorPaginas(page) 




ft.app(target=main)
