class AppError(Exception):
    def __init__(self, codigo, mensagem, status=400):
        super().__init__(mensagem)
        self.codigo = codigo
        self.mensagem = mensagem
        self.status = status


class ValidationError(AppError):
    pass


class UnauthorizedError(AppError):
    def __init__(self, codigo, mensagem, status=401):
        super().__init__(codigo, mensagem, status)


class ConflictError(AppError):
    def __init__(self, codigo, mensagem, status=409):
        super().__init__(codigo, mensagem, status)
