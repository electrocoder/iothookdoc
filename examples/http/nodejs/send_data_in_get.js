
// 04 Eylul 2017
// Guncelleme: 19 Agustos 2019
// Sahin MERSIN
// iothook.com
// postman kullanilarak olusturulmustur

var http = require("http");

var options = {
  "method": "GET",
  "hostname": "iothook.com",
  "port": null,
  "path": "/api/update?api_key=58088bb005633bb39cdf3b7d&field_1=10&field_2=2&field_3=3",
  "headers": {
    "cache-control": "no-cache",
    "postman-token": "033da3c8-6196-cd49-f72d-1850a7d18500"
  }
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.end();