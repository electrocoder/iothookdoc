// 04 Eylul 2017
// Guncelleme: 19 Agustos 2019
// Sahin MERSIN
// iothook.com
// postman kullanilarak olusturulmustur

HttpResponse<String> response = Unirest.get("http://iothook.com/api/update?api_key=58088bb005633bb39cdf3b7d&field_1=10&field_2=2&field_3=3")
  .header("cache-control", "no-cache")
  .asString();