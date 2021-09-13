from itertools import zip_longest


class Ipv4:
    def __init__(self, ipv4: str, mascara: int) -> None:
        self.__qtd_bits = 8

        self.ipv4 = ipv4
        self.mascara = mascara
        
        self.qtd_total_hosts = None
        self.ip_rede = None
        self.ip_broadcast = None
        self.ip_mascara = None
        self.num_ips = None      

    @property
    def ipv4(self):
        return self._ipv4
    
    @ipv4.setter
    def ipv4(self, value):
        val_maximo = sum(2**i for i in range(self.__qtd_bits))
        lista_valores = value.split(".")

        if len(lista_valores) != 4:
            raise TypeError("O ipv4 deve conter 4 grupos de números separados por um ponto")

        for numero in lista_valores:
            if not (0 <= int(numero) <= val_maximo):
                raise ValueError(f"Os numeros devem estar no intervalo de 0 a {val_maximo}, inclusos")
        
        self._ipv4 = value

    @property
    def mascara(self):
        return self._mascara
    
    @mascara.setter
    def mascara(self, value):
        if value > self.__qtd_bits * 4:
            raise ValueError(f"A mascara nao pode ser maior que {self.__qtd_bits * 4}")
        
        self._mascara = value

    
    @property
    def qtd_total_hosts(self):
        return self.__qtd_total_hosts
    
    @qtd_total_hosts.setter
    def qtd_total_hosts(self, value):
        value = 2**((self.__qtd_bits * 4) - self.mascara)

        self.__qtd_total_hosts = value

    @property
    def ip_rede(self):
        return self._ip_rede

    @ip_rede.setter
    def ip_rede(self, value):
        value = self._ipv4

        value = value.split(".")
        value[-1] = "0"

        value = ".".join(value)

        self._ip_rede = value

    @property
    def ip_broadcast(self):
        return self._ip_broadcast

    @ip_broadcast.setter
    def ip_broadcast(self, value):
        value = self._ipv4

        value = value.split(".")
        value[-1] = str(self.__qtd_total_hosts - 1)

        value = ".".join(value)

        self._ip_broadcast = value  

    @property
    def ip_mascara(self):
        return self._ip_mascara
    
    @ip_mascara.setter
    def ip_mascara(self, value):
        lista_calculo = [2**i for i in range(self.__qtd_bits - 1, -1, -1)] * 4
        val_maximo = sum(2**i for i in range(self.__qtd_bits))

        mascara_bin = []
        for _ in range(self.mascara):
            mascara_bin.append(1)
        else:
            for _ in range((4*self.__qtd_bits) - self.mascara):
                mascara_bin.append(0)

        teste = zip_longest(lista_calculo, mascara_bin)

        soma = 0
        mascara_ip = []
        for tupla in teste:
            if tupla[1] == 1:
                soma += tupla[0]
            
            if soma == val_maximo:
                mascara_ip.append(str(soma))
                soma = 0
        else:
            if soma != 0:
                mascara_ip.append(str(soma))
        
        mascara_ip = ".".join(mascara_ip)
        value = mascara_ip
        
        
        self._ip_mascara = value

    @property
    def num_ips(self):
        return self._num_ips

    @num_ips.setter
    def num_ips(self, value):

        value: int = (self.__qtd_total_hosts) - 2

        self._num_ips = value
    
    def __str__(self):
        lista_ip = self.ips_disponiveis()

        return f"""IP: {self.ipv4}
REDE: {self.ip_rede}
BROADCAST: {self.ip_broadcast}
MASCARA: {self.ip_mascara}
PRIMEIRO IP: {lista_ip[0]}
ULTIMO IP: {lista_ip[-1]}
N.IPs: {self.num_ips}"""

    def ips_disponiveis(self) -> list[str]:
        value = self._ipv4
        value = value.split(".")
        lista_ips = []

        for i in range(1, self.num_ips + 1):
            value[-1] = str(i)
            lista_ips.append(value.copy())

        lista_ips = [".".join(i) for i in lista_ips]
      
        return lista_ips


if __name__ == "__main__":
    ip = Ipv4("10.20.12.45", 26)

    print(ip)
    