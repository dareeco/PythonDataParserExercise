# imports go here

def main():
   """Main entry"""


if __name__ == '__main__':
   with open('example.txt') as f:
      #lines = f.readlines() #vo lista gi vadi to ne ni treba
      lines=f.read()
      print(lines)
   
