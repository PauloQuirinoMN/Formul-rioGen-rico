import flet as ft


class Contador(ft.Container): 
    
    # herdando diretamente de Container
    def __init__(self):
        super().__init__()
        self.padding = 10
        self.border_radius = 15
        self.margin = 0
        self.expand = True

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, text_size=20, color=ft.Colors.BLACK, expand=True, border=ft.InputBorder.NONE)

        
        self.content = ft.Row(
            spacing=0,
            controls=[
                self.txt_number,
                ft.Column([
                    ft.IconButton(
                        ft.Icons.ADD,
                        icon_size=15,
                        icon_color=ft.Colors.BLACK,
                        on_click=lambda e: self._plus_click(e)
                    ),
                    ft.IconButton(
                        ft.Icons.REMOVE,
                        icon_size=15,
                        icon_color=ft.Colors.BLACK,
                        on_click=lambda e: self._minus_click(e)
                    ),
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
                expand=True,
                )
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


        self.bgcolor = ft.Colors.TRANSPARENT
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


import flet as ft

class GeraProgresso(ft.Container):
    def __init__(self, titulo="Progresso"):  # Remova o conteudo=None se não for usar
        super().__init__()  # Chama o init do Container sem argumentos
        
        self.titulo = titulo
        self.valor = 0  # Valor inicial
        
        # Cria os componentes
        self._criar_componentes()
        
        # Configura o layout
        self._configurar_layout()
        
        # Estilização básica
        self.padding = 10
        self.border_radius = 8
    
    def _criar_componentes(self):
        """Cria todos os componentes UI"""
        self.label_titulo = ft.Text(value=self.titulo)
        self.label_valor = ft.Text(value=f"{self.valor}%")
        self.slider = ft.Slider(
            min=0,
            max=100,
            divisions=100,
            value=self.valor,
            label="{value}%",
            on_change=self._atualizar_valor
        )
    
    def _configurar_layout(self):
        """Configura o layout do container"""
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.label_titulo,
                        self.label_valor
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                self.slider
            ],
            spacing=10
        )
    
    def _atualizar_valor(self, e):
        """Atualiza o valor quando o slider é movido"""
        self.valor = int(e.control.value)
        self.label_valor.value = f"{self.valor}%"
        self.update()

class GerenciadorContainer:
        def __init__(self, container_receita, container_despesa):
            self.receita = container_receita
            self.despesa = container_despesa
            self.tam_padrao = 60
            self.tam_expandido = 80
        
        def alternar_tamanho(self, container_clicado):
            # Expande o clicado e reduz o outro
            if container_clicado == self.receita:
                self.receita.content.controls[0].height = self.tam_expandido
                self.despesa.content.controls[0].height = self.tam_padrao
            else:
                self.despesa.content.controls[0].height = self.tam_expandido
                self.receita.content.controls[0].height = self.tam_padrao
            
            self.receita.update()
            self.despesa.update()

