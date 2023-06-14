Integrantes:
 - George Lucas Monção Zambonin

## Sistema de recomendação

 Sistema de recomendação com Docker.

#### Containers:

- **Container0**: API de recomendação - Api consumida pelo *Container1*, esta api receberá os conteudos utilizados por um usuario e retornará uma coleção de conteudos que possam estar relacionado com os mesmos.
- **container1**: React Framework - Interface utilizado pelos usuarios do sistema. Um site que mostrará os conteudos relacionados a aqueles que o usuario já possui. Este container também ficara responsavel por atualziar o *container2*.
- **container2**: Banco de dados - Conterá informações sobre os conteudos e usuarios.
- **container3**: API para Exportação de dataset - Esse container ira consumir o *container2* e exportar um dataset em *.csv* para atualização do sistema de recomendação contido no *container0*.

#### Conteudos:
- Jogos da Steam.