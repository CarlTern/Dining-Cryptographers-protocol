if __name__ == "__main__":
    secretAice = 'D75C'
    dataAlice = 'C568'
    secretBob = 'EE87'
    dataBob = 'FCB3'
    userMessage = '4674'
    b = 1

    # This is our data to broadcast.
    if(b == 0):
        dataUser = hex(int('0000', 16) ^ int(secretBob, 16) ^ int(secretAice, 16))
        message = hex(int(dataAlice, 16) ^ int(dataBob, 16) ^ int(dataUser, 16))
        print('b=0:\t', dataUser[2:] + message[2:])

    elif(b == 1):
        dataUser = hex(int(userMessage, 16) ^ int(secretAice, 16) ^ int(secretBob, 16))
        message = hex(int(dataAlice, 16) ^ int(dataBob, 16) ^ int(dataUser, 16))
        print('b=1:\t', dataUser)
