document.addEventListener("DOMContentLoaded", () => {
    let submit_button = document.getElementById("submit");
    let submit_about_button = document.getElementById("saydark");
    let dark_says = document.getElementById("dark-says");
    if (submit_button != null) {
        submit_button.addEventListener("click", function () {
            let quark_times = Math.floor(Math.random() * 5) + 1;
            let ans = "";
            for (let index = 0; index < quark_times; index++) {
                ans = ans.concat("quark ");
            }
            ans = ans.concat("!");
            alert(ans);
        });
    }
    if (submit_about_button != null) {
        submit_about_button.addEventListener("click", function () {
            let quark_times = Math.floor(Math.random() * 5) + 1;
            let ans = "";
            for (let index = 0; index < quark_times; index++) {
                ans = ans.concat("quark ");
            }
            ans = ans.concat("!");
            dark_says.innerHTML = ans;
        });
    }
});
