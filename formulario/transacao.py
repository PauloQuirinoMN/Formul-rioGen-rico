import flet as ft

class FormularioTransacao:
    """
    Inicializa um formulário para registro de transação
    faz a validação dos dados e os empacota pra seram usados em 
    outras partes do código
    """
    def __init__(self, page: ft.Page):
        self.page = page
        self._formulario_ui()

        
    def mostrar(self, descricao="", qtd=0, valor=0, tipo="", categoria="", percepcaopreco=0, felicidade=0, importancia=0):  
       """ Renderiza com novos dados"""
       self._formulario_ui(descricao, qtd, valor, tipo, categoria, percepcaopreco, felicidade, importancia)
    
    
    def _formulario_ui(self):

        """ agrupas os controles e renderiza na tela """
        comp_descricao = ft.TextField(
            label="Descrição"
        )

        comp_qt = ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            padding=0,
            content=ft.Row(
                [
                    ft.Text(value='1', size=20, color=ft.Colors.WHITE),
                    ft.Column(
                        controls=[
                            ft.Icon(name=ft.Icons.EXPAND_LESS, size=30, color=ft.Colors.WHITE38),
                            ft.Icon(name=ft.Icons.EXPAND_MORE, size=30, color=ft.Colors.WHITE38),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                    )
                ],
                alignment=ft.alignment.center
            )
        )

        self.page.clean()

        self.page.add(
            ft.Column(
                expand=True,
                controls=[
                    ft.Row([comp_descricao, comp_qt], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ]
            )
        )               
        self.page.update()