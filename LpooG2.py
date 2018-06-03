import random

class Pessoa:
    def __init__(self,nome):
        self.nome=nome
class Inscricao:
    def __init__(self):
        self.valor=0

class inscricaoAluno(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor=50
        self.universidade=universidade

class inscricaoProfessor(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor=80
        self.universidade=universidade

class inscricaoProfissional(Inscricao):
    def __init__(self,empresa):
        super().__init__()
        self.valor=120
        self.empresa=empresa

class Encoinfo:
    def __init__(self,atendentes):
        self.atendentes=atendentes
        self.inscritos=[]
        self.vagas=100
        
    def atender(self,atendente,pessoa,inscricao):
        self.inscricao=inscricao
        if len(self.inscritos) < self.vagas:
                self.inscritos.append(Inscrito(pessoa,inscricao,atendente))
        else:
            print('Desculpe, inscrição encerrada.')

    def atendimentosPorAtendente(self,atendente):
        cont = 0
        for inscrito in self.inscritos:
            if(atendente == inscrito.atendente):
                cont += 1
        return cont

    def tipoAtendimentosPorAtendente(self,atendente):
        alunos = 0
        professores = 0
        profissionais = 0
        for inscrito in self.inscritos:
            if atendente == inscrito.atendente:
                if type(inscrito.inscricao) == inscricaoAluno:
                    alunos += 1
                elif type(inscrito.inscricao) == inscricaoProfessor:
                    professores += 1
                else:
                    profissionais += 1
        return {'Alunos':alunos,
                'Professores':professores,
                'Profissionais':profissionais}
    
    def gerarRelatorio(self):
        ca=0      
        cprof=0
        cprofi=0       
        
        for i in self.inscritos:            
            if type(i.inscricao)==inscricaoAluno:
                ca+=1
            elif type(i.inscricao)==inscricaoProfessor:
                cprof+=1
            else:
                cprofi+=1
                
        print('Relatorio ')
        print('Atendimentos por atendente: ')
        for atendente in atendentes:
            print(atendente.nome, 'fez: ', self.atendimentosPorAtendente(atendente), 'Atendimentos')
            atendimentos = self.tipoAtendimentosPorAtendente(atendente)
            print(atendimentos)
        print('Numeros de inscricao de Alunos: ',ca,' = Valor total pago: ', ca*50)
        print('Numeros de inscricao de Professor(a): ', cprof,' = Valor total pago: ',cprof*80)
        print('Numeros de inscricao de Profissionais: ', cprofi,' = Valor total pago: ',cprofi*120)
        print('Valor total de todas as inscrição: ', ca*50+cprof*80+cprofi*120)

                   
class Inscrito:
    def __init__(self,pessoa,inscricao,atendente):
        self.pessoa=pessoa
        self.inscricao=inscricao
        self.atendente=atendente

class Atendente(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)


        

atendentes=[Atendente('Athos'),Atendente('Samuel'),Atendente('Cryslei')]
ulbra=Encoinfo(atendentes)
def inscricao():
    sorteado = random.randint(1, 10)
    if sorteado <=7:
        return inscricaoAluno('ULBRA')

    elif sorteado > 7 and sorteado <= 9:
        return inscricaoProfessor('ULBRA')

    else:
        return inscricaoProfissional('Google')


for i in range(101):
    atendente = random.sample(ulbra.atendentes, 1)
    
    ulbra.atender(
        atendente[0],
        Pessoa('Jose'+str(ulbra.inscritos)),
        inscricao())

    
ulbra.gerarRelatorio()

    


