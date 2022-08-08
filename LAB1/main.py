import web_serv
import client_serv

def main():
    entry=input("Bienvenido, seleccione cual módulo utilizara. \n1. Servidor. \n2. Cliente. \n")
    if(entry=="1"):
        server = web_serv.Web(8182, "127.0.0.1", 8193)
        server.web_start()
    elif(entry=="2"):
        print("Bienvenido al menu")
        user = client_serv.Client(8182,"127.0.0.1",8193)
        user.clientStart()


if __name__ == "__main__":
    main()
    