from src.views.interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PessoaFisicaListerView(ViewInterface):
    def __init__(self, controller: PessoaFisicaListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()

        return HttpResponse(status_code=200, body=body_response)
