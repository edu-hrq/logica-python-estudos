#Criação de classe para clientes da Netflix (exemplo)
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos_disponíveis = ["padrão", "premium"] # lista de planos como atributo do Cliente
        if plano in self.planos_disponíveis:
            self.plano = plano
        else:
            raise ValueError("Plano inválido.")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos_disponíveis:
            self.plano = novo_plano
        else:
            return "Plano inválido."

    def ver_filme(self, filme, plano_filme):
        if self.plano == "premium" or self.plano == plano_filme:
            return f"Assistindo: {filme}"
        elif self.plano == "padrão" and plano_filme == "premium":
            return f"Faça upgrade para o plano Premium para ver esse filme."
        else:
            return "Plano inválido"
    
cliente = Cliente("Eduardo", "eduardo@teste.com", "premium")
print(cliente.plano)
cliente.ver_filme("Spider-Man", "padrão")