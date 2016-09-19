from session import Session
global s  
s = Session()
s.initio()  #initialize i/o

def main():
    s._showcalibrationscreen(showtext=0)

if __name__ == '__main__': main()



