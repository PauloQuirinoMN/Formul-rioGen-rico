import flet as ft
from interface.paginas import GerenciadorFormulario

def main(page: ft.Page):
    page.title = "FormuláriosDinâmicos"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.BLACK12
    page.padding = ft.padding.all(20)
    GerenciadorFormulario(page) # gerencia as telas e os seus widgts



ft.app(target=main)
