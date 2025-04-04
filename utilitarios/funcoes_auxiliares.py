import flet as ft


class Contador(ft.Container): 
    
    # herdando diretamente de Container
    def __init__(self):
        super().__init__()
        self.padding = 10
        self.margin = 5
        self.expand = True

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE, expand=True)

        
        self.content = ft.Row(
            controls=[
                self.txt_number,
                ft.Column([
                    ft.IconButton(
                        ft.Icons.ADD,
                        icon_size=10,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: self._plus_click(e)
                    ),
                    ft.IconButton(
                        ft.Icons.REMOVE,
                        icon_size=10,
                        icon_color=ft.Colors.WHITE,
                        on_click=lambda e: self._minus_click(e)
                ),
                ], 
                alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def _minus_click(self, e):
        """ Incremente o contador """
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.txt_number.update()

    def _plus_click(self, e):
        """ Incremente o contador """
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.txt_number.update()
       

class GeraTipo(ft.Container):
    def __init__(self, lista=None):
        super().__init__()


        self.bgcolor = ft.Colors.BLACK38
        self.border_radius = ft.border_radius.all(15)
        self.expand = True
        self.padding = 10

        self.lista = lista if lista is not None else []

        # Cria a linha responsiva
        self.responsive_row = ft.ResponsiveRow(controls=[], spacing=10)
        self.content = self.responsive_row

        # Gera os checkboxes
        self._gera_conj_check()

    
    def _gera_conj_check(self):
        """ Gera os checkboxes baseados na lista """

        self.responsive_row.controls.clear()
    
        for nome in self.lista:
            chk = ft.Container(
                alignment=ft.alignment.center,
                margin=0,
                padding=2,
                expand=True,
                col=4,
                content=ft.Checkbox(
                label=str(nome),
                value=False,
                label_style=ft.TextStyle(color="#2f2c79", size=12)
            )
            )
            self.responsive_row.controls.append(chk)

        