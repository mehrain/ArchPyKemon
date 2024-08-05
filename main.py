from src.BDparse import BDParser
from src.Pokeapi import Pokedex
import csv

def main():
    BDParser.start()
    
    # Initialize the Pokedex
    pokedex = Pokedex()

    # Read the existing CSV file and add Pokémon to each row
    input_file = 'src/parses/BDparsed.csv'
    output_file = 'src/parses/BDparsed_with_pokemon.csv'

    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read the header
        header = next(reader)
        header.append('Pokemon')
        writer.writerow(header)
        
        # Process each row
        for row in reader:
            rank = int(row[0].split(': ')[1])
            pokemon = pokedex.get(rank).name
            row.append(pokemon)
            writer.writerow(row)

    print(f"Updated CSV file with Pokémon saved to {output_file}")
