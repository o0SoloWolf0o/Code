// display none
let showDetail = document.getElementById("showDetail");
showDetail.addEventListener("click", function () {
    let detail = document.getElementById("detail");
    if (detail.style.display == "none") {
        detail.style.display = "block";
    } else {
        detail.style.display = "none";
    }
});