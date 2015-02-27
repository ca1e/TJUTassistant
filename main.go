package main
import(
  "fmt"
  "net/http"
  "net/url"
  "io/ioutil"
 )
                                                                                                                     
func main(){
        get()
        post()
}
 func get(){
                                                                                                                     
  response,_:=http.Get("http://www.baidu.com/")
  defer response.Body.Close()
  body,_:=ioutil.ReadAll(response.Body)
                                                                                                                     
  if response.StatusCode == 200 {
          fmt.Println(string(body))
  }else{
          fmt.Println("error")
  }
 }
 func post(){
  //resp, err :=
  http.PostForm("http://www.baidu.com/",
          url.Values{"name": {"ruifengyun"}, "blog": {"xiaorui.cc"},
          "aihao":{"python golang"},"content":{"nima,fuck "}})
 }