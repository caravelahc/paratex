Changelog
=========

Como utilizar
-------------

Cada "passagem de canudo" deve ser registrada aqui em 3 seções:
- Changes: mudanças realizadas no projeto;
- New Challenges: coisas que surgiram como questionamentos em sua sessão;
- Next Steps: melhores proximos passos da proxima dupla, em sua opinião

**Dica:** Vá editando este arquivo conforme for trabalhando no projeto.

Este formato é baseado em [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.0.6] - 29/09/2019

### Changes

- Adicionados testes unitários para garantir que as informações estão vindo
  como esperado;
- Refatorado o código separando apenas em `extractor.py` as questões
  relacionadas a extração de dados.

### Next Steps

- Transformar o `paratex` em uma aplicação CLI (além de ser uma lib), por exemplo:
  ```console
  $ paratex fetch-sessions 09-2019
  [('1786', datetime.date(2019, 9, 26)), ('1785', datetime.date(2019, 9, 25)), ('1784', datetime.date(2019, 9, 24)), ('1783', datetime.date(2019, 9, 19)), ('1781', datetime.date(2019, 9, 18)), ('1779', datetime.date(2019, 9, 17)), ('1778', datetime.date(2019, 9, 12)), ('1776', datetime.date(2019, 9, 11)), ('1775', datetime.date(2019, 9, 5)), ('1773', datetime.date(2019, 9, 4)), ('1772', datetime.date(2019, 9, 3))]
  $ paratex fetch-presence --id 1783
  Session(title='85ª Sessão Ordinária', date=datetime.date(2019, 9, 19), attendance={'Ada De Luca': ('Outras', 'Reunião do inventário referente ao falecimento de seu esposo.'), 'Altair Silva': ('Atividade Parlamentar Externa', 'Participar da Reunião Alianza Mercosur - Unión Europea, que acontecerá no dia 29 de setembro em La Plata - Província de Buenos Aires, Argentina.'), 'Ana Campagnolo': ('Presente', None), 'Bruno Souza': ('Presente', None), 'Doutor Vicente': ('Presente', None), 'Fabiano da Luz': ('Licença Médica', None), 'Felipe Estevão': ('Presente', None), 'Fernando Krelling': ('Presente', None), 'Ismael dos Santos': ('Presente', None), 'Ivan Naatz': ('Atividade Parlamentar Externa', None), 'Jair Miotto': ('Presente', None), 'Jerry Comper': ('Presente', None), 'Jesse Lopes': ('Presente', None), 'João Amin': ('Presente', None), 'José Milton Scheffer': ('Presente', None), 'Julio Garcia': ('Presente', None), 'Kennedy Nunes': ('Presente', None), 'Laércio Schuster': ('Presente', None), 'Luciane Carminatti': ('Presente', None), 'Luiz Fernando Vampiro': ('Atividade Parlamentar Externa', None), 'Marcius Machado': ('Presente', None), 'Marcos Vieira': ('Presente', None), 'Marlene Fengler': ('Presente', None), 'Mauricio Eskudlark': ('Presente', None), 'Mauro de Nadal': ('Presente', None), 'Milton Hobus': ('Outras', 'Motivo de saúde.'), 'Moacir Sopelsa': ('Presente', None), 'Nazareno Martins': ('Presente', None), 'Neodi Saretta': ('Presente', None), 'Nilso Berlanda': ('Presente', None), 'Padre Pedro Baldissera': ('Presente', None), 'Paulinha': ('Presente', None), 'Ricardo Alba': ('Presente', None), 'Rodrigo Minotto': ('Presente', None), 'Romildo Titon': ('Presente', None), 'Sargento Lima': ('Atividade Parlamentar Externa', 'Viagem  para Brasilia com o objetivo de apresentar sugestão de alteração do Pacote Anticrime do Governo Federal que tramita no Congresso Nacional e articulação junto aos Deputados Federais e Senadores.'), 'Sergio Motta': ('Presente', None), 'Valdir Cobalchini': ('Presente', None), 'Volnei Weber': ('Presente', None)})

  ```

## [0.0.5] - 28/09/2019

### Changes

- Adicionando repartição entre get_attendance e get_sessions_on_page
- Selenium descartado, continuamos usando bs4 e requests

### New Challenges

- Criar uma forma de navegar nos meses no botão da pagina
    ('http://transparencia.alesc.sc.gov.br/presenca_plenaria.php')

- Remover redundancia de código entre get_attendance e get_sessions_on_page

### Next Steps

- Usar get_sessions_on_month junto com get_attendance, pra gerar o pandas inteiro
- Usar algo emcima de get_sessions_on_month, pra pegar ao longo de varios meses


## [0.0.4] - 25/09/2019

### Changes

- Agora o Scraper percorre a pagina toda e cria um dataframe pandas

### New Challenges

- nenhum

### Next Steps

- Usar Selenium para Iterar sobre todas as paginas


## [0.0.3] - 21/09/2019

### Changes

- Scraper Iniciado

### New Challenges

- Tratar as ausências com justificativa, que possuem varios detalhes.
    (talvez seja possivel só pegar os presentes, e assumir o resto como ausente)

### Next Steps

- O mais imediato seria criar uma estrutura de dados pra receber as ausencias e presenças
    (algo como uma namedtuple deve servir)
    acho bem importante que a gente nao saia ja contando ausencia e presença com uma tabela de nome
    eh bom a gente manter essa estrutura pronta pra receber outros dados,
    eu faria um negocio tipo Parlamentar(nome, presente) e Assembleia( [Parlamentar] )

- Já dá pra ir vendo como que a gente vai pegar todas as seções,
    eu achei o selenium muito irado pra isso


## [0.0.2] - 18/09/2019

### Changes

- Reorganizadas as informações de uma maneira mais explicativa, com links,
  seções, etc;
- Criar um projeto Poetry básico.

### New Challenges

- Nenhum.

### Next Steps

- Fazer requisições a uma URL via Python;
- Navegar pelo HTML da página via Python.


## [0.0.1] - 18/09/2019

### Changes
- Adicionado CHANGELOG.md;
- Adicionado README.md;
- Adicionado ESCOPO.md;
- Adicionado CDC.md.

### New Challenges

- Definição de Regra de Negócio confusa: não faz sentido pegar a presença de
  uma comissao que o deputado não participa.

### Next Steps

- Definir qual presença queremos detectar;
- Continuar fazendo no braço até entender o problema como um todo;
- Definir bem o problema e _modus operandi_ braçal num documento para outros
  reproduzirem;
- Refinar CDC.md, coloquei só um cabeçalho nele.
