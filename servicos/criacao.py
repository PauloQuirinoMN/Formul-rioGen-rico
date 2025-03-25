import flet as ft

class CriadorFormulario:
    """ Cria o formulário, definodo pelo usuário o nome e as campos """

    def __init__(self, page:ft.Page):
        self.page = page
        self.nome_formulario = ""
        self.campos = [] # Lista com os nomes dos campos

    def mostra_tela_criacao(self, e):
        """ Exibe a tela para criar um formulário """
        self.page.clean()

        # Nome formulário
        self.campo_nome = ft.TextField(
            label="Nome do Formulário",
            on_change=self._atualizar_nome_formulario
        )
        
        # Botão para adicionar campos

        botao_add = ft.ElevatedButton(
            text="adicionar Campo",
            icon=ft.Icon(name=ft.Icons.ADD, size=30),
            on_click=self._mostrar_dialogo_campo
        )

        # Botão para finalizar
        botao_finalizar = ft.ElevatedButton(
            text="Finalizar",
            on_click=self._finalizar_formulario
        )

        self.page.add(
            ft.Column(
                [
                    self.campo_nome,
                    botao_add,
                    botao_finalizar
                ]
            )
        )
        self.page.update()

    def _atualizar_nome_formulario(self, e):
        """ Recebe o nome do formulário fornecido pelo usuário
        e adiciona a pagina """
        self.nome_formulario = e.control.value


    def _mostrar_dialogo_campo(self, e):
        """ Abre um diálogo para definir um novo campo """
        dialogo = ft.AlertDialog(
            title=("Adicionar Campo"),
            content=ft.Column(
                [
                    ft.TextField(label="Nome do Campo"),

                ]
            ),
            actions=[
                ft.TextButton("Salvar", on_click=self._adicionar_campo),
                ft.TextButton(text="Cancelar", on_click=self._fechar_dialogo)
            ]
        )
        self.page.dialog = dialogo
        dialogo.open = True
        self.page.update()


    def _adicionar_campo(self, e):
        """ Salva o novo campo na lista """
        nome_campo = self.page.dialog.content.controls.value
        if nome_campo:
            self.campos.append({"nome": nome_campo})
            self.fecha_dialogo(e)

    def _fechar_dialogo(self, e):
        self.page.dialog.open = False
        self.page.update()

    def _finalizar_formulario(self, e):
        """ Fecha a tela e exibe o Formulário pronto """
        if not self.nome_formulario:
            self.page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos"))
            self.page.snack_bar.open = True
            return
        
        # Exibe o formulário pronto
        self.page.clean()
        self.page.add(
            ft.Text(value=f"Formulário: {self.nome_formulario}, size=20")
        )

        for campo in self.campos:
            self.page.add(ft.TextField(label=campo["nome"]))

        self.page.update()