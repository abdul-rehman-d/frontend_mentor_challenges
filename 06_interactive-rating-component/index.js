const ratingBtns = document.getElementsByClassName("rating")
const submitBtn = document.getElementById("submit-btn")
const submittedRating = document.getElementById("rating")

for (let i = 0; i < ratingBtns.length; i++) {
    ratingBtns[i].addEventListener('click', () => {
        if (document.querySelector(".selected") !== null) {
            document.querySelector(".selected").classList.remove("selected")
        }
        ratingBtns[i].classList.add("selected")
    })
}

submitBtn.addEventListener('click', () => {
    submittedRating.textContent = document.querySelector(".selected").textContent
    document.getElementById("rating-component").style.display = "none"
    document.getElementById("thank-you-component").style.display = "flex"
})