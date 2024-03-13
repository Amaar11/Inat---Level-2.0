import matplotlib.pyplot as plt
from portfolio import total_values


def create_portfolio_visualizations(total_values):
    tokens = list(total_values.keys())  # Dobijamo listu svih tokena
    values = [0] * len(tokens)    # Inicijaliziramo listu vrijednosti za svaki token na 0

    
    for address_type, address_values in total_values.items():
        for i, token_value in enumerate(address_values):
            if i < len(tokens):
                # Dodajemo vrijednosti tokena na odgovarajućem indeksu
                values[i] += token_value
            else:
                # Ako je indeks veći od dužine liste tokens, dodajemo token i njegovu vrijednost na kraj liste
                tokens.append(f"Token {i+1}")
                values.append(token_value)

    # Kreiranje dijagrama
    plt.figure(figsize=(10, 6))
    plt.bar(tokens, values, color='skyblue')
    plt.title('Total Portfolio Values by Token')
    plt.xlabel('Token')
    plt.ylabel('Portfolio Value (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


create_portfolio_visualizations(total_values)
