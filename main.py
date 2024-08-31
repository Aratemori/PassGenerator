import random as r
import string as st

def main():
  max_symbols = int(input("Enter length: "))  
  multiple = st.ascii_letters + st.digits + st.punctuation
  
  for i in range(5):
    password = "".join(r.sample(multiple, max_symbols))
    print(password)
    
if __name__ == '__main__':
  main()