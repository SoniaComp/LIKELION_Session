# AJAX
Ajax는 JavaScript 라이브러리 중 하나이며, Asynchronous Javacript And XML(비동기식 자바스트립트와 xml)의 약자입니다.<br>
Ajax는 Javascript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술<br>

* 비동기(Async): 웹페이지를 리로드하지 않고, 데이터를 불러오는 방식입니다. 이 방식의 장점은 페이지 리로드의 경우, 전체 리소스를 다시 불러와야 하는데, 이미지, 스크립트, 기타 코드 등을 모두 재요청할 경우 불필요한 리소스 낭비가 발생하게 되지만, 비동기 방식을 이용할 경우, **필요한 부분만** 불러와 사용할 수 있으므로 매우 큰 장점이 있습니다.

* jQuery와 Ajax의 시너지: jQuery를 이용하면 더 적은 코딩량과 동일한 코딩방법으로 대부분의 브라우저에서 같은 동작을 할 수 있게 됩니다.

### 사용기술
`XHTML` `Cascading Style Sheets` `Javascript` `XmlHttpRequest(웹서버와 통신을 담당` ` XML&JSON` `DOM`

### JQuery.AJAX 기본 공식
```javascript
$.ajax({옵션속성: 값};
```
예시
```javascript
$(document).ready(function(){
  $.ajax({
    type: "POST", // Http 요청방식
    // timeout: Http 요청에 대한 제한 시간을 지정합니다.
    url: "/someController", // 요청이 전송되는 URL이 포함된 문자열
    data: {name:"John", location:"Boston"}, // Http요청 후 return하는 값
    // 서버에 있는 내용을 가져오고 싶다면!!
    // 프론트에 있는 값을 가져오고 싶다면-> jQuery: $("#id").val();
    success: function(html){ // Http요청 성공시 이벤트 핸들러 + error, complete
      $("#results").append(html);
    }
    // async: 요청시 동기 유무를 선택할 수 있습니다.(True/false)
    // dataType: return된 데이터의 Type입니다.
    // cache: 브라우저에 의해 요청되는 페이지를 캐시할 수 있습니다.
    // beforeSend: Http 요청 전에 발생하는 이벤트 핸들러 입니다.
    // global: 전역함수 활성 여부를 설정합니다.
  };
})
```