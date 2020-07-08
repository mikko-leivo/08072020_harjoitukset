import argparse
from harjoitus3 import filereaderapp as toteutus

parser = argparse.ArgumentParser()
parser.add_argument("luettava_tiedosto", help = "anna luettavan tiedoston polku tähän", type=str)
parser.add_argument("luotava_tiedosto", help = "anna luettavan tiedoston nimi tähän", type=str)
args = parser.parse_args()

toteutus(args.luettava_tiedosto, args.luotava_tiedosto)
print(f"Olet luonut super mahtavan uuden tiedoston{args.luotava_tiedosto}. Break you' self")
