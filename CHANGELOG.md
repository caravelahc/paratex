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
