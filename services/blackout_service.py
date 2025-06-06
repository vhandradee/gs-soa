import random

bairros_afetados = ["centro", "vila mariana", "santana", "tucuruvi", "mooca"]

def get_blackout_response(bairro: str):
    bairro = bairro.lower()
    
    if bairro in bairros_afetados:
        tempo_estimado = random.choice([30, 60, 90, 120])
        return {
            "bairro": bairro,
            "status": "queda de energia confirmada",
            "tempo_estimado_para_retorno": f"{tempo_estimado} minutos"
        }
    else:
        return {
            "bairro": bairro,
            "status": "sem registros de queda",
            "mensagem": "Tudo normal por aqui!"
        }
