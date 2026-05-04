---
title: "Boas práticas em Unit Tests com .Net: A Prática"
date: 2025-06-19
draft: false
tags: ["testes", "dotnet", "unit-tests", "xunit"]
categories: ["testes"]
summary: "Parte prática sobre boas práticas em Unit Tests com .Net — criando testes com xUnit, Moq e NSubstitute aplicando os fundamentos na prática."
cover:
  image: image1.png
  alt: "Pirâmide de testes com destaque para a camada de unit tests"
  relative: true
---

### Boas práticas em Unit Tests com .Net: A prática

Essa é a **parte dois do artigo sobre Boas práticas em Unit Tests com .Net** contendo a parte prática da teoria apresentada na primeira parte.

*Caso não tenha lido, recomendo ler a* *[Primeira Parte do artigo](https://medium.com/@luan.dev.mello/boas-pr%C3%A1ticas-em-unit-tests-com-net-a-teoria-b01ee8b8ed78) com a teoria.*

### Criando testes de unidade em .Net

Começamos com o framework [**xUnit .Net**](https://xunit.net/), voltado para simplificar o desenvolvimento de testes de unidade em .Net em diversas linguagens como C#, F# e demais linguagens .Net. É open source e mantido pela .Net Foundation.

O **xUnit** utiliza uso de [Decorators](https://en.wikipedia.org/wiki/Decorator_pattern) indicando, assim, quais métodos ou funções dentro de um arquivo serão parte do conjunto de testes ao executá-los.

#### Mock e Fixtures

Para agilizar a geração de Mocks e instâncias de objetos necessários para a realização de um teste, temos as libraries **Moq** e **AutoFixture**.

O Moq, cria objetos “fakes” como Mocks e Stubs, que **auxiliam bastante** o processo de instanciar e gerenciar dependências do teste.

Já o AutoFixture ( [Quick Start](https://autofixture.github.io/docs/quick-start/) ) , cria um objeto ou um Array de objetos através do padrão Builder para qualquer classe que é necessária uma instância, estando um estado específico ou não, colocando um valor aleatório em cada uma propriedade sua de acordo com a tipagem.

### Exemplos práticos

O contexto para os exemplos está nesse [repositório no Github](https://github.com/luanmds/best-practices-unit-tests-csharp).

#### Usando o \[Fact\]

Nesse primeiro exemplo, temos testes unitários para o método Create da classe CustomerService.

Usamos o Decorator *\[Fact\]* do xUnit para indicar ao SDK do .Net que tal método é um teste de unidade e executá-lo. Além disso, nosso “Stub” é gerado pela classe Fixture da lib AutoFixture.

```csharp
public class BasicTestsWithFactDecorator
{
private readonly Mock<ICustomerRepository> _repositoryMock;
private readonly Mock<ILogger<CustomerService>> _loggerMock;
private readonly Fixture _fixture;
private readonly CustomerService _service;
public BasicTestsWithFactDecorator()
{
_repositoryMock = new Mock<ICustomerRepository>();
_loggerMock = new Mock<ILogger<CustomerService>>();
_fixture = new Fixture();
_service = new CustomerService(_repositoryMock.Object,
_loggerMock.Object);
}
[Fact]
public async Task Save_customer_successfully_when_Dto_is_valid()
{
var dto = new Mock<CustomerDto>();
await _service.Create(dto.Object);
dto.Verify(x => x.ToCustomer(), Times.Once);
_repositoryMock.Verify(x => x.SaveAsync(It.IsAny<Customer>()),
Times.Once);
_loggerMock.Verify(l =>
l.Log(LogLevel.Information,
It.IsAny<EventId>(),
It.Is<It.IsAnyType>((v, _) => v.ToString().Contains("Customer save
successfully")),
It.IsAny<Exception>(),
It.IsAny<Func<It.IsAnyType, Exception, string>>()), Times.Once);
}
[Fact]
public void Save_customer_fails_when_repository_throws_exception()
{
var dto = new Mock<CustomerDto>();
_repositoryMock.Setup(x =>
x.SaveAsync(It.IsAny<Customer>())).Throws<Exception>();
Func<Task> result = async () => await _service.Create(dto.Object);
result.Should().ThrowAsync<Exception>();
dto.Verify(x => x.ToCustomer(), Times.Once);
}
[Fact]
public async Task
GetById_returns_customer_successfully_when_id_is_valid()
{
string id = _fixture.Create<string>();
var customer = _fixture.Build<Customer>().With(x => x.Id,
id).Create();
_repositoryMock.Setup(x => x.GetAsync(It.IsAny<string>()))
.ReturnsAsync(customer);
var result = await _service.GetById(id);
result.Should().BeOfType<Customer>();
_repositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
}
[Fact]
public void GetById_throws_ArgumentNullException_when_id_is_not_found()
{
string id = _fixture.Create<string>();
Func<Task> result = async () => await _service.GetById(id);
result.Should().ThrowAsync<ArgumentNullException>();
_repositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
}
}
```

Aqui usa-se a classe Mock (da lib Moq) para abstrair o acesso ao *ICustomerRepository* e *Logger*. O método *Setup* de Mock é usado para selecionar qual será o valor ou retorno ao chamar uma propriedade ou método da classe "mockada".

Também é possível fazer em N vezes para uma mesma chamada com o método *Setups*.

#### Usando o Theory

Nesse segundo exemplo temos o uso do Decorator *\[Theory\]* juntamente com o *\[InlineData()\]* que geram diversos tipos de entradas como parâmetros e, assim, conseguirmos realizar o teste em diversos cenários.

```csharp
public class UsingTheoryWithInlineData
{
private readonly Mock<ICustomerRepository> _repositoryMock;
private readonly Mock<ILogger<CustomerService>> _loggerMock;
private readonly Fixture _fixture;
private readonly CustomerService _service;
public UsingTheoryWithInlineData()
{
_repositoryMock = new Mock<ICustomerRepository>();
_loggerMock = new Mock<ILogger<CustomerService>>();
_fixture = new Fixture();
_service = new CustomerService(_repositoryMock.Object,
_loggerMock.Object);
}
[Theory]
[InlineData(ProcessStatus.Pending, "123")]
[InlineData(ProcessStatus.Blocked, "456")]
[InlineData(ProcessStatus.Processed, "789")]
public async Task
UpdateStatusScore_a_customer_successfully_when_parameters_are_valid(ProcessStatus
status, string customerId)
{
var customer = _fixture.Build<Customer>().With(x => x.Id,
customerId).Create();
_repositoryMock.Setup(x => x.GetAsync(It.IsAny<string>())).
ReturnsAsync(customer);
_repositoryMock.Setup(x => x.UpdateAsync(It.IsAny<Customer>())).
ReturnsAsync(customerId);
await _service.UpdateStatusScore(status, customerId);
_repositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
_repositoryMock.Verify(x => x.UpdateAsync(It.IsAny<Customer>()),
Times.Once);
_loggerMock.Verify(l =>
l.Log(LogLevel.Information,
It.IsAny<EventId>(),
It.Is<It.IsAnyType>((v, _) => v.ToString().Contains($"Customer with
ID: {customerId} update successfully")),
It.IsAny<Exception>(),
It.IsAny<Func<It.IsAnyType, Exception, string>>()), Times.Once);
}
[Theory]
[InlineData(ProcessStatus.Pending, "123")]
public void
UpdateStatusScore_throws_ArgumentNullException_when_id_is_not_found(ProcessStatus
status, string customerId)
{
Func<Task> result = async () => await
_service.UpdateStatusScore(status, customerId);
result.Should().ThrowAsync<ArgumentNullException>();
_repositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
}
}
```

Aqui temos dois cenários de teste onde o valor do enum *ProcessStatus* varia e gera um valor de resposta específico. Onde cada *InlineData* se torna um cenário a ser testado.

Esse tipo de abordagem nos ajuda demais já que economiza boas linhas de código para fazer um teste de unidade para cada cenário existente daquele comportamento.

#### MemberData e ClassData para reúso de código

O próximo exemplo utiliza o *\[MemberData\]* com o intuito de termos como passar objetos via parâmetro de forma dinâmica.

Para utilizá-lo corretamente é obrigatório utilizar a interface *IEnumerable\<object\[\]\>* e fornecer uma lista de objetos utilizados como inputs necessários para o teste funcionar. Segue o exemplo:

```csharp
public class UsingTheoryWIthMemberData
{
private readonly Mock<ICustomerRepository> _customerRepositoryMock;
private readonly Mock<IScoreRepository> _repositoryMock;
private readonly Mock<ILogger<ScoreService>> _loggerMock;
private readonly Fixture _fixture;
private readonly ScoreService _service;
public UsingTheoryWIthMemberData()
{
_repositoryMock = new Mock<IScoreRepository>();
_customerRepositoryMock = new Mock<ICustomerRepository>();
_loggerMock = new Mock<ILogger<ScoreService>>();
_fixture = new Fixture();
_service = new ScoreService(_repositoryMock.Object,
_customerRepositoryMock.Object, _loggerMock.Object);
}
[Fact]
public async void CreateScore_successfully_when_customer_exists()
{
var customer = _fixture.Create<Customer>();
_customerRepositoryMock.Setup(x => x.GetAsync(customer.Id))
.ReturnsAsync(customer);
await _service.CreateScore(customer.Id);
_customerRepositoryMock.Verify(x => x.GetAsync(customer.Id),
Times.Once);
_repositoryMock.Verify(x => x.SaveAsync(It.IsAny<Score>()),
Times.Once);
_loggerMock.Verify(l =>
l.Log(LogLevel.Information,
It.IsAny<EventId>(),
It.Is<It.IsAnyType>((v, _) => v.ToString().Contains("Score with
ID:")),
It.IsAny<Exception>(),
It.IsAny<Func<It.IsAnyType, Exception, string>>()), Times.Once);
}
[Fact]
public void
CreateScore_throws_ArgumentNullException_when_customer_not_found()
{
var id = _fixture.Create<string>();
Func<Task> result = async () => await _service.CreateScore(id);
result.Should().ThrowAsync<ArgumentNullException>();
_customerRepositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
_repositoryMock.Verify(x => x.SaveAsync(It.IsAny<Score>()),
Times.Never);
}
[Theory]
[MemberData(nameof(CalculateScoreData))]
public void
CalculateScore_should_return_correct_value_to_the_debits_amount(decimal
debits, int expectedScore)
{
int score = ScoreService.CalculateScore(debits);
score.Should().Be(expectedScore);
}
public static IEnumerable<object[]> CalculateScoreData()
{
yield return new object[] { 2000f, 0 };
yield return new object[] { 1000.0f, 0 };
yield return new object[] { 500.3f, 50 };
yield return new object[] { 450f, 55 };
yield return new object[] { 250.9f, 75 };
yield return new object[] { 0f, 100 };
}
}
```

Nele vemos que podemos ter diversos cenários para cálculo do Score de um Customer de acordo com os débitos do mesmo.

No último exemplo temos o *\[ClassData\]* sendo bem parecido com o anterior, mas fornece os dados via uma classe implementando a interface *IEnumerable\<object\[\]\>.* Veja mais:

```csharp
public class UsingTheoryWithClassData
{
private readonly Mock<ILoanRepository> _repositoryMock;
private readonly Mock<IScoreRepository> _scoreRepositoryMock;
private readonly Fixture _fixture;
private readonly LoanService _service;
public UsingTheoryWithClassData()
{
_repositoryMock = new Mock<ILoanRepository>();
_scoreRepositoryMock = new Mock<IScoreRepository>();
_fixture = new Fixture();
_service = new LoanService(_repositoryMock.Object,
_scoreRepositoryMock.Object);
}
[Fact]
public async void CreateLoan_successfully_when_score_exists()
{
var score = _fixture.Create<Score>();
var dt = DateTime.UtcNow;
_scoreRepositoryMock.Setup(x => x.GetAsync(score.Id))
.ReturnsAsync(score);
await _service.CreateLoan(score.Id, dt);
_scoreRepositoryMock.Verify(x => x.GetAsync(score.Id), Times.Once);
_repositoryMock.Verify(x => x.SaveAsync(It.IsAny<Loan>()),
Times.Once);
}
[Fact]
public void
CreateLoan_throws_ArgumentNullException_when_score_not_found()
{
var id = _fixture.Create<string>();
var dt = DateTime.UtcNow;
Func<Task> result = async () => await _service.CreateLoan(id, dt);
result.Should().ThrowAsync<ArgumentNullException>();
_scoreRepositoryMock.Verify(x => x.GetAsync(It.IsAny<string>()),
Times.Once);
_repositoryMock.Verify(x => x.SaveAsync(It.IsAny<Loan>()),
Times.Never);
}
[Theory]
[ClassData(typeof(CalculateLoanValueData))]
public void CalculateLoanValue_should_return_correct_value(decimal
debits, int score, decimal expectedLoan)
{
decimal result = _service.CalculateLoanValue(debits, score);
result.Should().Be(expectedLoan);
}
}
public class CalculateLoanValueData : IEnumerable<object[]>
{
public IEnumerator<object[]> GetEnumerator()
{
yield return new object[] { 2000f, 0, 0M };
yield return new object[] { 450f, -55, 0 };
yield return new object[] { 500.3f, 50, 4499.7 };
yield return new object[] { 250.9f, 75, 7249.1 };
yield return new object[] { 0f, 100, 10000 };
}
IEnumerator IEnumerable.GetEnumerator()
{
return GetEnumerator();
}
}
}
```

Mesmo que os Decorators sejam parecidos, temos uma clara diferença entre eles. E isso justamente ajuda no tipo de abordagem utilizado para reaproveitar o código.

Nesse caso, podemos reaproveitar os dados gerados pela classe *CalculateLoanValueData*, propagando entre outras classes de testes de unidade.

### Deixando mais claro o resultado esperado com Fluent Assertions

Podemos substituir o conhecido Assert.{method} de nossos testes em .Net pela library [Fluent Assertions](https://fluentassertions.com/).

Esse conjunto de extensions é utilizado para validar asserções de forma intuita e legível nos métodos de testes de unidade.

No exemplo abaixo, é testado cada campo retornado na variável *result* do método *ToCustomer*:

```csharp
public class CustomerDtoTests
{
private readonly Fixture _fixture;
public CustomerDtoTests()
{
_fixture = new Fixture();
}
[Fact]
public void ToCustomer_Should_Returns_Customer_With_DTO_Data()
{
var sut = _fixture.Create<CustomerDto>();
var result = sut.ToCustomer();
result.Address.Street.Should().Be(sut.Street);
result.Address.City.Should().Be(sut.City);
result.Address.StreetNumber.Should().Be(sut.StreetNumber);
result.Name.Should().Be(sut.Name);
result.Age.Should().Be(sut.Age);
result.Document.Should().Be(sut.Document);
result.DebitsAmount.Should().Be(sut.DebitsAmount);
}
}
```

### Referências

- [Mocking em testes unitários com o framework Moq](https://www.devmedia.com.br/mocking-em-testes-unitarios-com-o-framework-moq/36724)
- [GitHub — moq/moq4: Repo for managing Moq 4.x](https://github.com/moq/moq4)
- [Introduction](https://fluentassertions.com/introduction)
- [Quick Start — AutoFixture](https://autofixture.github.io/docs/quick-start/)
