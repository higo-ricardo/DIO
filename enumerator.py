# Dicionário de portas associdas a serviços
ports_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   
}

# Gera a lista de saida conforme a entrada  
def enumerar_servicos(ports):
    services = []
    for port in ports:
       
          if port in ports_services:
             services.append(ports_services[port])
          else:
              services.append("Desconhecido")
    return services

def main():
   while True:
      try:
        ports_input = input()
        ports = [int(port.strip()) for port in ports_input.split(',')]
        break
      except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros separados por vírgulas.")
    # Chamada da função e exibição dos resultados
   services = enumerar_servicos(ports)
   print(services)



if __name__ == "__main__":
    main()