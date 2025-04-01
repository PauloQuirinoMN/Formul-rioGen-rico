import flet as ft

class Display:
    """Inicializa o display com menus de acesso """
    def __init__(self, page: ft.Page):
        self.page = page
        self.componente = self._menu_display()

        
    def _menu_display(self):
        return ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    tab_content=ft.Image(src='resumo.png', fit=ft.ImageFit, color=ft.Colors.WHITE,),
                    content=ft.Text("This is Tab 1"),
                ),

                ft.Tab(
                    tab_content=ft.Image(src='analise.png', fit=ft.ImageFit, color=ft.Colors.WHITE),
                    content=ft.Text("This is Tab 2"),
                ),
                
                ft.Tab(
                    tab_content=ft.Image(src='dowload.png', fit=ft.ImageFit, color=ft.Colors.WHITE),
                    content=ft.Text("This is Tab 3"),
                ),
            ],
            expand=1,
        )

