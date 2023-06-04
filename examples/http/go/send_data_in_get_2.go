// 04 Eylul 2017
// Guncelleme: 19 Agustos 2019
// Sahin MERSIN
// iothook.com
// postman kullanilarak olusturulmustur

package main

    import (
        "fmt"
        "net/http"
        "io/ioutil"
    )

    func main() {

        url := "http://iothook.com/api/update?api_key=58088bb005633bb39cdf3b7d&field_1=10&field_2=2&field_3=3"

        req, _ := http.NewRequest("GET", url, nil)

        req.Header.Add("cache-control", "no-cache")

        res, _ := http.DefaultClient.Do(req)

        defer res.Body.Close()
        body, _ := ioutil.ReadAll(res.Body)

        fmt.Println(res)
        fmt.Println(string(body))

    }
