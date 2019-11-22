import sys
import binascii

def b1(SA,SB,M):
    result = hex(~(~(SA ^ SB ^ M)))[2:]
    if (len(str(result)) < 4):
        numberOfAdded = 4 - len(str(result))
        for i in range(0, numberOfAdded):
            result = '0' + result
        return result
        
if __name__ == "__main__":
    try:
        SA = sys.argv[1]
        DA = sys.argv[2]
        SB = sys.argv[3]
        DB = sys.argv[4]
        M = sys.argv[5]
        b = sys.argv[6]
    except:
        print("Invalid parameters")
        print("Usage:", '"DiningCryptoProtocol SA DA SB DB M b"')
        print("For example:", '"python3 DiningCryptoProtocol.py 27C2 35F6 0879 1A4D 27BC 1"')
        exit()
    output = b1(int(SA,16),int(SB,16),int(M,16))
    print(output)