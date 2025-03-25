import flet as ft

class CriadorFormulario:
    """ Cria o formulário, definindo pelo usuário o nome e as campos """

    def __init__(self, page:ft.Page):
        self.page = page
        self.nome_formulario = ""
        self.campos = []
        self._definir_inteface_criacao()

    def _definir_inteface_criacao(self):
        """ Gera uma interface para serem definidas os nomes
         do formulário e dos campos """

        self.page.clean()

        # Elementos da UI

        self.nome_formulario = ft.TextField(
            label="Nome do formulário",
            on_change=self._atualizar_nome_formulario
        )

        self._lista_campos = ft.Column([])

        botao_add = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_size=30,
            icon_color=ft.Colors.WHITE,
            on_click=self._adicionar_campo
        )

        botao_finalizar = ft.ElevatedButton(
            text="OK",
            on_click=self._renderizar_formulario_final
        )

        self.page.add(
            ft.Column(
                [
                    self.nome_formulario,
                    ft.Row([
                        ft.Text("Campos do Formulário:"),
                        botao_add
                    ]),
                    self._lista_campos,
                    botao_finalizar, 
                ]
            )
        )
        
    def _adicionar_campo(self, e):
        """ Adiciona um novo campo á lista """
        novo_campo = ft.TextField(
            label=f"Campo {len(self.campos) + 1}",
            hint_text="Digite o nome do novo campo",
            on_change=lambda e, idx=len(self.campos): self._atualizar_campo(e, idx)
        )
        
        self.campos.append(""), # Inicia com nome vazio
        self._lista_campos.campos.controls.append(novo_campo)
        self.page.update()

    # Atualizar valores

    def _atualizar_nome_formulario(self, e):
        self.nome_formulario = e.control.value
    def _atualizar_campo(self, e, index):
        self.campos[index] = e.control.value


    def _renderizar_formulario_final(self, e):
        """Exibe o formulário pronto para preenchimento."""
    
        if not self.nome_formulario or not any(self.campos):
            self.page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            self.page.snack_bar.open = True
            return
    
    def renderizar_formulario_existente(self):
        """Renderiza o formulário completo (MÉTODO QUE VOCÊ PERGUNTOU)"""
        self.page.clean()
        
        # Cabeçalho
        cabecalho = ft.Text(f"Formulário: {self.nome_formulario}", size=24)
        
        # Campos para preenchimento
        campos_preenchimento = [
            ft.TextField(label=nome_campo)
            for nome_campo in self.campos if nome_campo
        ]
        
        self.page.add(ft.Column([cabecalho, *campos_preenchimento]))
        self.page.update()
        
        self.page.clean()
        
        # Cabeçalho
        cabecalho = ft.Text(f"Formulário: {self.nome_formulario}", size=24)
        
        # Campos para preenchimento
        campos_ui = []
        for nome_campo in self.campos:
            if nome_campo:  # Ignora campos vazios
                campos_ui.append(ft.TextField(label=nome_campo))
        
        self.page.add(
            ft.Column([cabecalho, *campos_ui])
        )