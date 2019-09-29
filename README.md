PARATEX
==================================

O PARATEX (**PAR**liamentary **AT**tendance **EX**tractor) visa extrair dados
como a frequência de presença dos deputados de Santa Catarina em diferentes
reuniões/assembleias.

O projeto foi iniciado através de uma ["Corrida de Canudos"](CDC.md), e
continuado com mais atividade através de pequenos _sprints_ promovidos pelo
Caravela HC em conjunto com projetos como o
[EnsineBot](https://github.com/caravelahc/ensinebot).

Contribuindo
------------

Ainda não foi produzido um CONTRIBUTING.md e portanto não há um padrão de
contribuição, mas sinta-se à vontade para contribuir:
- **Desenvolvendo código-fonte**: criando um Fork deste repositório e enviando
  um Pull Request com suas alterações em uma branch que não seja a `master`. Se
  tiver dúvidas de como fazer isso, apareça no Caravela ou mande uma mensagem
  para algum dos contribuidores e tentaremos lhe ajudar.
- **Dando ideias**: caso sinta que o projeto poderia ter alguma funcionalidade
  interessante, você pode [abrir uma
  issue](https://github.com/caravelahc/paratex/issues/new/choose) selecionando
  "Incremento/Funcionalidade" e descrevendo sua sugestão.
- **Reportando erros**: se encontrar algum erro no Paratex, sinta-se à vontade
  para [abrir uma
  issue](https://github.com/caravelahc/paratex/issues/new/choose) selecionando
  _"Bug"_ e descrevendo o erro que encontrou.


Instalação
----------

_TODO_ (#12).

Uso
---

```python
>>> import paratex
>>> from datetime import date
>>> paratex.fetch_sessions(date(2019, 9, 19))
[('1786', datetime.date(2019, 9, 26)), ('1785', datetime.date(2019, 9, 25)), ('1784', datetime.date(2019, 9, 24)), ('1783', datetime.date(2019, 9, 19)), ('1781', datetime.date(2019, 9, 18)), ('1779', datetime.date(2019, 9, 17)), ('1778', datetime.date(2019, 9, 12)), ('1776', datetime.date(2019, 9, 11)), ('1775', datetime.date(2019, 9, 5)), ('1773', datetime.date(2019, 9, 4)), ('1772', datetime.date(2019, 9, 3))]
>>> paratex.extract_attendance(1783)
Session(title='85ª Sessão Ordinária', date=datetime.date(2019, 9, 19), attendance={'Ada De Luca': ('Outras', 'Reunião do inventário referente ao falecimento de seu esposo.'), 'Altair Silva': ('Atividade Parlamentar Externa', 'Participar da Reunião Alianza Mercosur - Unión Europea, que acontecerá no dia 29 de setembro em La Plata - Província de Buenos Aires, Argentina.'), 'Ana Campagnolo': ('Presente', None), 'Bruno Souza': ('Presente', None), 'Doutor Vicente': ('Presente', None), 'Fabiano da Luz': ('Licença Médica', None), 'Felipe Estevão': ('Presente', None), 'Fernando Krelling': ('Presente', None), 'Ismael dos Santos': ('Presente', None), 'Ivan Naatz': ('Atividade Parlamentar Externa', None), 'Jair Miotto': ('Presente', None), 'Jerry Comper': ('Presente', None), 'Jesse Lopes': ('Presente', None), 'João Amin': ('Presente', None), 'José Milton Scheffer': ('Presente', None), 'Julio Garcia': ('Presente', None), 'Kennedy Nunes': ('Presente', None), 'Laércio Schuster': ('Presente', None), 'Luciane Carminatti': ('Presente', None), 'Luiz Fernando Vampiro': ('Atividade Parlamentar Externa', None), 'Marcius Machado': ('Presente', None), 'Marcos Vieira': ('Presente', None), 'Marlene Fengler': ('Presente', None), 'Mauricio Eskudlark': ('Presente', None), 'Mauro de Nadal': ('Presente', None), 'Milton Hobus': ('Outras', 'Motivo de saúde.'), 'Moacir Sopelsa': ('Presente', None), 'Nazareno Martins': ('Presente', None), 'Neodi Saretta': ('Presente', None), 'Nilso Berlanda': ('Presente', None), 'Padre Pedro Baldissera': ('Presente', None), 'Paulinha': ('Presente', None), 'Ricardo Alba': ('Presente', None), 'Rodrigo Minotto': ('Presente', None), 'Romildo Titon': ('Presente', None), 'Sargento Lima': ('Atividade Parlamentar Externa', 'Viagem  para Brasilia com o objetivo de apresentar sugestão de alteração do Pacote Anticrime do Governo Federal que tramita no Congresso Nacional e articulação junto aos Deputados Federais e Senadores.'), 'Sergio Motta': ('Presente', None), 'Valdir Cobalchini': ('Presente', None), 'Volnei Weber': ('Presente', None)})
```

Organização do projeto
----------------------

- [Projeto do GitHub](https://github.com/caravelahc/paratex/projects/1): Tem
  separado quais tarefas precisam ser feitas, quais foram concluídas, etc;
- [CHANGELOG.md](CHANGELOG.md): Detalhes de cada conjunto alterações do
  Paratex.

Metas
-----

- **Geral**: Encontrar a frequência de um político qualquer numa reunião
qualquer.
- **Específica**: Encontrar a frequencia de deputados de Santa Catarina nas
reuniões de frente pela educação.
- **Motivação**: Diminuir a credibilidade de opositores que tenham presença
baixa.

Contextualização
----------------

### O que são frentes parlamentares?

São associações de parlamentares de vários partidos para debater sobre
determinado tema de interesse da sociedade. Para que seja constituída, a frente
parlamentar deve registrar um requerimento, contendo:
- Composição de pelo menos um terço de membros do Poder Legislativo;
- Indicação do nome da Frente Parlamentar; e
- Representante responsável por prestar as informações.

### O que são grupos parlamentares?

São associações de parlamentares para fortalecer as relações entre o Congresso
brasileiro e o parlamento de um país estrangeiro. Para serem criados, é
necessário que o Deputado apresente um projeto de resolução (PRC), que deve ser
votado pelo Plenário da Câmara dos Deputados.

### Termos

| Termo | Significado                              |
| ----- | ---------------------------------------- |
| ALESC | Assembleia Legislativa de Santa Catarina |

Links
-----

- [Atas das comissões
  permanentes - ALESC](http://transparencia.alesc.sc.gov.br/comissoes_permanentes_presenca.php)
- [Diário da Assembleia - ALESC](http://www.alesc.sc.gov.br/diario-da-assembleia)
