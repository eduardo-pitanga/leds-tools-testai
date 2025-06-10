using ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Request;
using ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response;
using ConectaFapes.Test.Shared;
using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using Xunit;
using Xunit.Gherkin.Quick;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ConectaFapes.Test.Steps
{
    [FeatureFile("../../../Features/ModalidadeBolsaFeature.feature")]
    [Collection(WebApplicationFactoryParameters.CollectionName)]
    public class ModalidadeBolsaStep : Xunit.Gherkin.Quick.Feature
    {
        private const string BASE_URL = "https://localhost:3000/api/modalidadebolsa/";
        private readonly WebApplicationFactory _factory;
        private readonly HttpClient _client;
        private HttpResponseMessage? _response;
        private ApiDataProvider _provider;

        public ModalidadeBolsaStep(WebApplicationFactory factory)
        {
            _factory = factory;
            _client = _factory.CreateClient();
            _client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            _provider = new ApiDataProvider(_client);
        }

        [Given("o usuário está autenticado no sistema")]
        public void GivenUsuarioAutenticado()
        {
            // Implement your authentication logic here.  This might involve setting
            // an authentication token in the HttpClient's headers.  Example:
            // _client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "your_token");
        }

        [When("ele acessa o endpoint de modalidades de bolsa")]
        public async Task WhenAcessaEndpointModalidadesBolsa()
        {
            _response = await _client.GetAsync(BASE_URL);
        }

        [Then("o sistema retorna todas as modalidades de bolsa cadastradas")]
        public async Task ThenRetornaTodasModalidades()
        {
            _response.EnsureSuccessStatusCode();
            var responseBody = await _response.Content.ReadAsStringAsync();
            var modalidades = JsonSerializer.Deserialize<List<ModalidadeBolsaResponseDTO>>(responseBody);

            Assert.NotNull(modalidades);
            Assert.NotEmpty(modalidades);

            // Add more specific assertions here based on the expected data in the response.
            // Example: Assert.Contains(modalidades, m => m.Nome == "Expected Modality Name");

        }

        [When(@"I send a GET request to /modalidadebolsa/""(.+)""")]
        public async Task WhenISendAGetRequest(string modalidadeBolsaId)
        {
            _response = await _client.GetAsync(BASE_URL + modalidadeBolsaId);
        }

        [When(@"I send a POST request to /modalidadebolsa with the following ModalidadeBolsa details: ""(.+)"", ""(.+)""")]
        public async Task WhenISendAPostRequest(string sigla, string nome)
        {
            var modalidadeBolsa = new ModalidadeBolsaRequestDTO
            {
                Sigla = StringValidator.CheckEmptyString(sigla),
                Nome = StringValidator.CheckEmptyString(nome)
            };

            var content = new StringContent(JsonSerializer.Serialize(modalidadeBolsa), Encoding.UTF8, "application/json");
            _response = await _client.PostAsync(BASE_URL, content);
        }

        [When(@"I send a PUT request to /modalidadebolsa/""(.+)"" with the following ModalidadeBolsa details: ""(.+)"", ""(.+)""")]
        public async Task WhenISendAPutRequest(string modalidadeBolsaId, string sigla, string nome)
        {
            ModalidadeBolsaResponseDTO modalidadeBolsa = await _provider.GetEntityById<ModalidadeBolsaResponseDTO>("ModalidadeBolsa", modalidadeBolsaId);

            modalidadeBolsa.Sigla = StringValidator.CheckEmptyString(sigla);
            modalidadeBolsa.Nome = StringValidator.CheckEmptyString(nome);

            var content = new StringContent(JsonSerializer.Serialize(modalidadeBolsa), Encoding.UTF8, "application/json");
            _response = await _client.PutAsync(BASE_URL + modalidadeBolsaId, content);
        }

        [When(@"I send a DELETE request to /modalidadebolsa/""(.+)""")]
        public async Task WhenISendADeleteRequest(string modalidadeBolsaId)
        {
            _response = await _client.DeleteAsync(BASE_URL + modalidadeBolsaId);
        }

        [When(@"I send a PUT request to /modalidadebolsa/""(.+)""/ativar")]
        public async Task WhenISendAPutActiveRequest(string modalidadeBolsaId)
        {
            _response = await _client.PutAsync(BASE_URL + modalidadeBolsaId + "/ativar", null);
        }

        [When(@"I send a PUT request to /modalidadebolsa/""(.+)""/desativar")]
        public async Task WhenISendAPutDisableRequest(string modalidadeBolsaId)
        {
            _response = await _client.PutAsync(BASE_URL + modalidadeBolsaId + "/desativar", null);
        }

        [Then(@"the API response should be: ""(.+)""")]
        public void ThenApiResponse(string statusCode)
        {
            if (_response != null)
            {
                Assert.Equal(Convert.ToInt32(statusCode), (int)_response.StatusCode);
            }
        }


    }
}

namespace ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Request
{
    public class ModalidadeBolsaRequestDTO
    {
        public string Sigla { get; set; }
        public string Nome { get; set; }
    }
}

namespace ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response
{
    public class ModalidadeBolsaResponseDTO
    {
        public int Id { get; set; }
        public string Sigla { get; set; }
        public string Nome { get; set; }
        public bool Ativo { get; set; }
    }
}

namespace ConectaFapes.Test.Shared
{
    public static class StringValidator
    {
        public static string CheckEmptyString(string value)
        {
            if (string.IsNullOrEmpty(value))
            {
                throw new ArgumentException("String cannot be null or empty.");
            }
            return value;
        }
    }
    public class ApiDataProvider
    {
        private readonly HttpClient _client;

        public ApiDataProvider(HttpClient client)
        {
            _client = client;
        }

        public async Task<T> GetEntityById<T>(string entityName, string id)
        {
            var response = await _client.GetAsync($"https://localhost:3000/api/{entityName}/{id}");
            response.EnsureSuccessStatusCode();
            var content = await response.Content.ReadAsStringAsync();
            return JsonSerializer.Deserialize<T>(content);

        }

    }
}