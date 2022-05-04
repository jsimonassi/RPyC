import rpyc
import time


class MyService(rpyc.Service):

    start = end = 0
    exposed_the_real_answer_though = 43     # este é um atributo exposto

    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        print("Conectado!" + "\n")
        pass

    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        print("Desconectado!" + "\n")
        print("Tempo de execução: {}".format(self.end - self.start))
        pass

    def exposed_get_answer(self):  # este é um método exposto
        return 42

    def get_question(self):  # este método não é exposto
        return "Qual é  a cor do cavalo branco de Napoleão?"

    def exposed_sum(self, array):
        self.start = time.time()
        result = sum(array)
        self.end = time.time()
        return result


# Para iniciar o servidor
if __name__ == "__main__":
    print("Iniciando o servidor...")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
