import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get _pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    poke_info = get_pokemon_info(123)
    return

def get_pokemon_info(pokemon_name) :
    pokemon_name = str(pokemon_name).strip().lower()
    
    url = POKE_API_URL + pokemon_name
    
    print(f'Getting information for {pokemon_name}...', end='')
    resp_msg = requests.get(url)
    
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return

if __name__ == '__main__':
    main()