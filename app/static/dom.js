const navToggle = () => {
  const burger = document.querySelector(".burger");
  const target = document.querySelector(".left");
  const line1 = document.querySelector(".one");
  const line2 = document.querySelector(".two");
  const line3 = document.querySelector(".three");

  burger.addEventListener("click", (e) => {
    console.log("clicked")
    // target.style.transform = "translateX(10%)"
    target.classList.toggle("toView")
    line1.classList.toggle("first")
    line2.classList.toggle("second")
    line3.classList.toggle("third")
    // document.querySelector("body").style.backgroundColor = "white";
  });
};

(()=>{
    navToggle();
})()