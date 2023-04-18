let showDetail = document.getElementById("showDetail");
showDetail.addEventListener("click", function () {
    let detail = document.getElementById("detail");
    if (detail.style.display == "none") {
        detail.style.display = "block";
    } else {
        detail.style.display = "none";
    }
});
let buttontext = document.getElementById("showDetailButton");
buttontext.addEventListener("click", function () {
    if (buttontext.innerHTML == "Show details") {
        buttontext.innerHTML = "Hide details";
    } else {
        buttontext.innerHTML = "Show details";
    }
});