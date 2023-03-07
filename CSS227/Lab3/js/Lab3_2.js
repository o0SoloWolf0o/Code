function toggleMode(){
    var button = document.getElementsByTagName("button")[0];
    var div = document.getElementsByClassName("myDIV")[0];
    if (button.innerHTML == "Active the night mode") {
        nightMode();
        button.innerHTML = "Active the day mode";
        div.innerHTML = "Click the button below to activate the day mode";
    } else {
        dayMode();
        button.innerHTML = "Active the night mode";
        div.innerHTML = "Click the button below to activate the night mode";
    }
}
function nightMode() {
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
    document.getElementsByTagName("h1")[0].style.color = "white";
    document.getElementsByTagName("h2")[0].style.color = "white";
    document.getElementsByTagName("span")[0].style.color = "blue";
    document.getElementsByTagName("p")[0].style.color = "white";
}
function dayMode() {
    document.body.style.backgroundColor = "white";
    document.body.style.color = "black";
    document.getElementsByTagName("h1")[0].style.color = "black";
    document.getElementsByTagName("h2")[0].style.color = "black";
    document.getElementsByTagName("span")[0].style.color = "red";
    document.getElementsByTagName("p")[0].style.color = "black";
}