
 //  хз             var testerjs = document.getElementsByTagName("a")[0].getAttribute("href");


function myFunction(test) {
    alert("Hello from a static file!",test, testerjs);
    if (test == 1){
    alert("You are right!",test);}
  }


  function getRectArea(width, height) {
    if (width > 0 && height > 0) {
      return width * height;
    }
    return 0;
  }

  function getValue (id) {
    text = document.getElementById(id).value; //value of the text input
    alert(text);
    return false;
}


