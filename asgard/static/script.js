function btnFunction(element, id , object) {

    document.querySelector(".row2").style.display = "block"

    var id2 = document.querySelector(".description");
    id2.textContent = object;

}

function btnFunction2() {
    document.querySelector(".row2").style.display = "none";
}