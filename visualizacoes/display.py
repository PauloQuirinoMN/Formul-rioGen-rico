import flet as ft

class Display:
    """Inicializa o display com menus de acesso """
    def __init__(self, page: ft.Page):
        self.page = page
        self.componente = self._menu_display()

        
    def _menu_display(self):
        """Tab para gerenciamneto de conteúdo """
        return ft.Container(
            bgcolor = ft.Colors.WHITE38,
            border_radius=ft.border_radius.all(15),
            expand = True, 
            content=ft.Column(
                expand=True,
                spacing=5,
                controls=[
                    ft.Row(
                        [
                        ft.IconButton(icon=ft.Icons.DOWNLOAD, icon_size=15, icon_color=ft.Colors.BLACK38),
                        ft.IconButton(icon=ft.Icons.DELETE_FOREVER, icon_size=15, icon_color=ft.Colors.BLACK38),
                        ], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=10,
                    ),
                    ft.Divider(height=5, thickness=1, color=ft.Colors.WHITE38),
                    ft.Container(expand=True),    
                ]
            ),
        )
    
    