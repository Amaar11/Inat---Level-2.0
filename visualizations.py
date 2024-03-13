import matplotlib.pyplot as plt
from portfolio import total_values

def create_portfolio_visualizations(total_values):
    tokens = list(tokens.keys())
    values = [0] * len(tokens)

  
    for address_type, address_values in total_values.items():
        for i, token_value in enumerate(address_values):
            values[i] += token_value


    plt.figure(figsize=(10, 6))
    plt.bar(tokens, values, color='skyblue')
    plt.title('Total Portfolio Values by Token')
    plt.xlabel('Token')
    plt.ylabel('Portfolio Value (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    
    plt.show()

create_portfolio_visualizations(total_values)
