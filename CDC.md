Corrida De Canudos
==================

Aqui fica uma direção de como atuar na Corrida de Canudos.

A dinâmica é que, **em sessões de 2h**, fique uma pessoa (ou duas, caso queiram
fazer _pair programming_) no Caravela trabalhando no projeto tentando alcançar
a meta e resolvendo as diferentes _issues_ abertas nas sessões anteriores. Os
últimos minutos (**sugestão: 20min**) devem ser utilizados para documentar tudo
que foi feito/dificuldades/o que falta fazer e explicar para a próxima pessoa a
"assumir o canudo".

Início da sessão
----------------

1. Se for a sua primeira vez trabalhando no projeto:
   1. Faça um _clone_ deste repositório:
      ```console
      $ git clone https://github.com/caravelahc/paratex
      ```
   2. Leia as **[metas do projeto](README.md#Metas)**;
   3. Se tiver dúvidas do que é cada conceito/termo/etc., **veja se tem o que
      procura na [Contextualização](README.md#Contextualização)**.
2. Se não for a sua primeira vez, atualize o seu repositório local:
   ```console
   $ cd pasta-local-do-paratex
   $ git pull
   ```
3. Leia o [CHANGELOG.md](CHANGELOG.md), vendo quais as conquistas e
   dificuldades da última pessoa que esteve com o canudo;
4. Veja e selecione as _[issues](https://github.com/caravelahc/paratex/issues)_
   que quiser trabalhar em cima.

Fim da sessão
-------------

1. Documente todas as funções que você criou (ou atualize a documentação das
   que alterou), a menos que o nome + parâmetros da função sejam
   autoexplicativos **e não tenha alguma peculiaridade no seu funcionamento**
   (restrições ou comportamento diferente conforme valores dos parâmetros, por
   exemplo);
2. Adicione suas mudanças no [CHANGELOG.md](CHANGELOG.md) seguindo o formato
   descrito no início do arquivo;
3. Se o próximo a assumir o canudo estiver presente, repasse a ele as
   informações e explique o que for necessário (_"estava fazendo X mas não deu
   certo, minha ideia era [...]"_).
