def display_text(data_extenso, *args, **kwargs):
    context = "\n".join(args)
    metadata = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    msg = f"{data_extenso}\n\n{context}\n\n{metadata}"
    print(msg)


display_text(
    "12 de Junho de 2024",
    "qual quer rsrr", 
    "yyry uygu yd ytd y", 
    Author="Belarmino", Ano=2024
)