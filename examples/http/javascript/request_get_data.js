var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://iothook.com/api/device/?api_key=76d2628fd60903d3c1f7f8a0&results=1",
    "method": "GET",
    "headers": {
      "User-Agent": "PostmanRuntime/7.15.2",
      "Accept": "*/*",
      "Cache-Control": "no-cache",
      "Postman-Token": "ce2f06c2-817e-414a-8c7a-2c2fc59ad043,27a5bb35-4b13-48b2-8dbd-efe7188a68c6",
      "Host": "iothook.com",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "keep-alive",
      "cache-control": "no-cache"
    }
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
  