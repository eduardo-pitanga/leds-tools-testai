using ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Request;
using ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response;
using ConectaFapes.Test.Shared;
using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using Xunit;
using Xunit.Gherkin.Quick;

namespace ConectaFapes.Test.Steps
{
    [FeatureFile("../../../Features/modalidadebolsaFeature.feature")]
    [Collection(WebApplicationFactoryParameters.CollectionName)]
    public class ModalidadeBolsaStep : Feature
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
            _provider = new ApiDataProvider(_client);
            // Add authentication if needed.  Example:
            //_client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", "your_token"); 
        }

        [Given("I have access to the ModalidadeBolsa API")]
        public async Task IHaveAccessAPI()
        {
            var response = await _client.GetAsync(BASE_URL);
            response.EnsureSuccessStatusCode(); // Throw exception if not successful
        }


        [When(@"I send a GET request to /modalidadebolsa/")]
        public async Task WhenISendAGetAllRequest()
        {
            _response = await _client.GetAsync(BASE_URL);
        }

        [When(@"I send a GET request to /modalidadebolsa/""(.+)""")]
        public async Task WhenISendAGetRequestById(string modalidadeBolsaId)
        {
            _response = await _client.GetAsync($"{BASE_URL}{modalidadeBolsaId}");
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
            var modalidadeBolsa = new ModalidadeBolsaRequestDTO
            {
                Sigla = StringValidator.CheckEmptyString(sigla),
                Nome = StringValidator.CheckEmptyString(nome)
            };

            var content = new StringContent(JsonSerializer.Serialize(modalidadeBolsa), Encoding.UTF8, "application/json");
            _response = await _client.PutAsync($"{BASE_URL}{modalidadeBolsaId}", content);
        }

        [When(@"I send a DELETE request to /modalidadebolsa/""(.+)""")]
        public async Task WhenISendADeleteRequest(string modalidadeBolsaId)
        {
            _response = await _client.DeleteAsync($"{BASE_URL}{modalidadeBolsaId}");
        }

        [When(@"I send a PUT request to /modalidadebolsa/""(.+)""/ativar")]
        public async Task WhenISendAPutActiveRequest(string modalidadeBolsaId)
        {
            _response = await _client.PutAsync($"{BASE_URL}{modalidadeBolsaId}/ativar", null);
        }

        [When(@"I send a PUT request to /modalidadebolsa/""(.+)""/desativar")]
        public async Task WhenISendAPutDisableRequest(string modalidadeBolsaId)
        {
            _response = await _client.PutAsync($"{BASE_URL}{modalidadeBolsaId}/desativar", null);
        }

        [Then(@"the API response should be: ""(.+)""")]
        public void ThenApiResponse(string expectedStatusCode)
        {
            HttpStatusCode statusCode = (HttpStatusCode)int.Parse(expectedStatusCode);
            Assert.Equal(statusCode, _response?.StatusCode);
        }

        [Then("the API returns all Modalidades de Bolsa")]
        public async Task ThenApiReturnsAllModalidades()
        {
            _response.EnsureSuccessStatusCode();
            var content = await _response.Content.ReadAsStringAsync();
            var modalidades = JsonSerializer.Deserialize<List<ModalidadeBolsaResponseDTO>>(content);
            Assert.NotEmpty(modalidades);
        }

        [Then("the API returns Modalidade de Bolsa with Id")]
        public async Task ThenApiReturnsModalidadeById()
        {
            _response.EnsureSuccessStatusCode();
            var content = await _response.Content.ReadAsStringAsync();
            var modalidade = JsonSerializer.Deserialize<ModalidadeBolsaResponseDTO>(content);
            Assert.NotNull(modalidade);
        }

    }
}