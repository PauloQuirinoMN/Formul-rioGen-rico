import flet as ft

class Contador(ft.Container): 
    # herdando diretamente de Container
    def __init__(self):
        super().__init__()
        self.padding = 10
        self.margin = 5

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, color=ft.Colors.WHITE, width=35)

        
        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    ft.Icons.ADD,
                    icon_size=15,
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda e: self._plus_click(e)
                ),
                self.txt_number,
                ft.IconButton(
                    ft.Icons.REMOVE,
                    icon_size=15,
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda e: self._minus_click(e)
                ),  
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
       
        

