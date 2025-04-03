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
       
        

