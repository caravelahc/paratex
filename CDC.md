Corrida De Canudos
==================

A dinâmica da Corrida de Canudos é:
- Cada contribuidor¹ irá ter uma **sessão de 2h** no Caravela trabalhando no
  projeto;
- Cada sessão será para:
  - Tentar alcançar a meta;
  - Ir resolvendo as diferentes _issues_ abertas nas sessões anteriores.
- Os últimos minutos (**sugestão: 20min**) deverão ser para:
  - Documentar tudo que foi feito/dificuldades/o que falta fazer;
  - Explicar para a próxima pessoa a "assumir o canudo".

_**¹:** Se preferir, você pode combinar com alguém de fazer _pair programming_,
ou seja: um programa e o outro vai observando, comentando, corrigindo, e assim
os dois vão trocando ideias e erros são percebidos mais facilmente._

Se for sua primeira contribuição
--------------------------------

1. Peça para ser adicionado como Contribuidor no [Chat do
   Caravela](https://t.me/caravelahc);

   > Dica: Marque @jptiz em sua mensagem.

2. Faça um **Fork** deste repositório:

   ![Localização do botão de Fork](https://i.imgur.com/pMY4odP.png)

3. **Clone o _seu_ fork**:

   ```console
   $ cd onde-vai-ficar-o-projeto
   $ git clone https://github.com/seuusuario/paratex
   ```

4. Leia as **[metas do projeto](README.md#metas)**;
5. Se tiver dúvidas do que é cada conceito/termo/etc., **veja se tem o que
   procura na [Contextualização](README.md#contextualização)**;
6. Se ainda tiver dúvidas, [abra uma issue de
   Esclarecimento](https://github.com/caravelahc/paratex/issues/new?assignees=&labels=question&template=esclarecimento.md&title=).

Dicas gerais
------------

1. **Use `Fix` ou `Resolve` quando resolver uma issue**

   > Quando seu commit resolver uma issue, deixe a mensagem dele como `Fix #<nº da
   > issue>: <mensagem>` (ou `Resolve` no lugar de `Fix`, caso não seja bem uma
   > correção). Por exemplo, se ele resolve a Issue #1, você pode fazer seu commit
   > como:
   >
   > ```console
   > $ git commit -m "Resolve #1: Fetch page content via URL."
   > ```


2. **Faça 1 commit/alteração (quando ela funciona)**

   > Pequenas alterações por vez ajudam tanto a dar melhores mensagens de commit
   > quanto a pensar melhor nos passos do projeto, além de que estamos em uma
   > Corrida de Canudos e as sessões são curtas.


3. **Faça perguntas nos canais do Telegram**

   > Otimize seu tempo: pergunte no [@caravelahc](t.me/caravelahc) ou
   > [@pythonfloripa](t.me/pythonfloripa) quando tiver dúvidas.

4. **Chegue no Caravela 20min antes da sua sessão**

   > Assim você pode ver o que estão fazendo na corrida atual, e assim podem te
   > explicar onde pararam.

5. **Revise os passos abaixo em cada sessão**

   > Assim você consegue saber se não esqueceu de algo importante.

Início da sessão
----------------

#### 1. Atualize-se

1. Veja o [último Pull Request
   aberto](https://github.com/caravelahc/paratex/pulls) (é sempre o primeiro da
   lista) para saber o que a última pessoa (ou dupla) fez;

   > _Dica: se a pessoa não escreveu as alterações, os títulos dos commits
   > podem ajudar, ou vá em "Files Changed" e tente decifrar o que foi feito._
2. Clique em **"Merge Pull Request"**;
3. Tenha as últimas alterações em seu computador:
   ```console
   $ cd pasta-do-seu-fork
   $ git remote add upstream https://github.com/caravelahc/paratex # Necessário apenas uma vez
   $ git checkout master # Se tiver trocado de branch
   $ git pull upstream master
   $ git checkout sua-branch # Se já tiver feito alguma contribuição
   $ git rebase master # De novo: só se já tiver feito alguma contribuição
   ```

#### 2. Organize-se

1. Vá no [GitHub Projects deste
   repositório](https://github.com/caravelahc/paratex/projects/1);
2. A coluna **"Última corrida"** tem um resumo das conquistas, dificuldades e
   tarefas novas da última corrida;
3. Arraste:
   1. As issues **fechadas** (estão em vermelho) para a coluna **Concluídas**;
   2. As issues que você **vai trabalhar nesta sessão** para a coluna **Corrida
      atual**;
   3. As demais issues para a coluna **Afazeres**.
4. Vá para o seu terminal;
5. Crie uma _branch_ para seu trabalho com o nome `run-<seuusuario>`, por
   exemplo:
   ```console
   $ git checkout -b run-jptiz
   ```
6. Pode começar a trabalhar. ;)

Fim da sessão
-------------

1. Documente todas as funções que você criou (ou atualize a documentação das
   que alterou);
   > Dica 1: Funções em Python podem ser documentadas com uma _string_ na
   > primeira linha, por exemplo:
   > ```python
   > def insert(words: List[str], word: str) -> bool:
   >     '''Add word into words list ordering by length. Returns False if word
   >     was already on list, True otherwise.'''
   >     if ...
   > ```

   > Dica 2: Se o nome + parâmetros de uma função forem autoexplicativos **e
   > não tenha alguma peculiaridade no seu funcionamento** (restrições ou
   > comportamento diferente conforme valores dos parâmetros, por exemplo), não
   > precisa criar uma documentação para ela.
2. Certifique-se de que todos os devidos _commits_ foram feitos;
3. Envie suas alterações para o seu novo branch no repositório usando `git push
   -u origin <sua-branch>`, por exemplo:
   ```console
   $ git push -u origin run-jptiz
   ```
4. Vá no [Repositório do Caravela](https://github.com/caravelahc/paratex);
5. Crie um **Pull Request**:
   1. Clique em **New Pull Request**:

      ![Localização do botão Pull Request](https://i.imgur.com/qFp0r3h.png)

   2. Certifique-se de que:
      - **base repository** seja `caravelahc/paratex`;
      - **base** seja `master`;
      - **head repository** seja `seuusuario/paratex`;
      - **compare** seja `sua-branch`.

      ![Configuração correta do PR](https://i.imgur.com/ZF8SLU2.png)

   3. Clique em **Create Pull Request** (em **verde**);
   4. Dê um nome para suas alterações (pode ser "Canudo: (hora inicial) às
      (hora final)");
   5. Dê uma última verificada nas informações:

      ![Exemplo de PR completo](https://i.imgur.com/GTxv0BM.png)
   6. Clique em **Create Pull Request** uma última vez.

4. [Crie issues](https://github.com/caravelahc/paratex/issues/new/choose) para
   os próximos contribuidores:
   1. Crie elas clicando no **Get Started** da categoria correta;
   2. Adicione elas ao projeto:
      1. Visite o [GitHub Projects deste
         repositório](https://github.com/caravelahc/paratex/projects/1)
      2. Clique em **"Add cards"** à direita:

         ![Localização do botão Add Cards](https://i.imgur.com/lU4NAXA.png)

      3. Arraste suas issues em **Última corrida**.
5. Se o próximo contribuidor estiver presente, repasse a ele as informações e
   explique o que for necessário (_"estava fazendo X mas não deu certo, minha
   ideia era [...]"_).
